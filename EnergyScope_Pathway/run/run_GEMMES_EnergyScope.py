# -*- coding: utf-8 -*-
"""
September 2024

@authors: Pierre Jacques, Xavier Rixhon, Stanislas Augier
"""

## Define which model you want to run: GEMMES, EnergyScope or the coupling of the two
# mode = 'GEMMES_only'
mode = 'EnergyScope_only'
# mode = 'GEMMES-EnergyScope'

## Define the country studied and the time granularity of EnergyScope
country = 'Turkey'                  # Choose between Colombia and Turkey
EnergyScope_granularity = 'MO'  # MO = Monthly resolution, TD = Typical Day (hourly resolution - takes much more time to run)
nbr_tds = 12

## Define which results to save and/or plot
plot_EnergyScope = True  
csv_EnergyScope  = True
plot_GEMMES = False
csv_GEMMES = True

def main():
    if mode=='GEMMES_only':
        variables_GEMMES = run_GEMMES()
    elif mode=='EnergyScope_only':
        output_EnergyScope = run_EnergyScope()
    else: # coupling between the two models
        variables_GEMMES = run_GEMMES()
        # The convergence criterion requires to look at all End-Use Demands
        El    = [variables_GEMMES['El_F'], variables_GEMMES['El_B'], variables_GEMMES['El_G'], variables_GEMMES['El_H']]
        HHT   = [variables_GEMMES['HHT_F']]
        HLTSH = [variables_GEMMES['HLTSH_F'], variables_GEMMES['HLTSH_B'], variables_GEMMES['HLTSH_G'], variables_GEMMES['HLTSH_H']]
        HLTHW = [variables_GEMMES['HLTHW_F'], variables_GEMMES['HLTHW_H']]
        PC    = [variables_GEMMES['PC_F']]
        SC    = [variables_GEMMES['SC_B'], variables_GEMMES['SC_G'], variables_GEMMES['SC_H']]
        MP    = [variables_GEMMES['MP_H']]
        MF    = [variables_GEMMES['MF_F']]
        NE    = [variables_GEMMES['NE_F']]
        EUD_current = [El, HHT, HLTSH, HLTHW, PC, SC, MP, MF, NE]
        diff = 1
        n_iter = 1
        diff_list = [0]
        while(diff > 0.03):
            EUD_previous = EUD_current
            n_iter += 1
            output_EnergyScope = run_EnergyScope()
            post_process_EnergyScope_outputs(output_EnergyScope[0], output_EnergyScope[1], variables_GEMMES)
            variables_GEMMES = run_GEMMES()
            El    = [variables_GEMMES['El_F'], variables_GEMMES['El_B'], variables_GEMMES['El_G'], variables_GEMMES['El_H']]
            HHT   = [variables_GEMMES['HHT_F']]
            HLTSH = [variables_GEMMES['HLTSH_F'], variables_GEMMES['HLTSH_B'], variables_GEMMES['HLTSH_G'], variables_GEMMES['HLTSH_H']]
            HLTHW = [variables_GEMMES['HLTHW_F'], variables_GEMMES['HLTHW_H']]
            PC    = [variables_GEMMES['PC_F']]
            SC    = [variables_GEMMES['SC_B'], variables_GEMMES['SC_G'], variables_GEMMES['SC_H']]
            MP    = [variables_GEMMES['MP_H']]
            MF    = [variables_GEMMES['MF_F']]
            NE    = [variables_GEMMES['NE_F']]
            EUD_current = [El, HHT, HLTSH, HLTHW, PC, SC, MP, MF, NE]
            diff = 0
            for i in range(len(EUD_current)):
                row = EUD_current[i]
                for j in range(len(row)):
                    diff = max(diff, ((EUD_current[i][j]-EUD_previous[i][j]).abs()/EUD_previous[i][j]).max())
            diff_list.append(diff)
    
    if plot_EnergyScope and mode!='GEMMES_only':
        plot_EnergyScope_outputs(output_EnergyScope[0], output_EnergyScope[1])
    if csv_EnergyScope and mode!='GEMMES_only':
        EnergyScope_output_csv(output_EnergyScope[0], output_EnergyScope[1])
    if plot_GEMMES and mode!='EnergyScope_only':
        plot_GEMMES_outputs(variables_GEMMES.iloc[20:,:])
    if csv_GEMMES and mode!='EnergyScope_only':
        variables_GEMMES_to_output = variables_GEMMES.copy()
        variables_GEMMES_to_output.to_csv(os.path.join(EnergyScope_case_study_path,'GEMMES_output_long.csv'))
        variables_GEMMES_to_output = variables_GEMMES_to_output[::10]
        variables_GEMMES_to_output.to_csv(os.path.join(EnergyScope_case_study_path,'GEMMES_output_short.csv'))
    
    if mode=='GEMMES-EnergyScope':
        print('Number of iterations before convergence between the two models: ', n_iter)
        print('Convergence values: ', diff_list)
    
    
def run_GEMMES():
    ## Change parameters values in GEMMES according to scenario definition
    # Build default parms vector in python importing data from C++
    parmsNames = solvePy.parmsNames()
    # Declare a structure that stores parameters values and their names
    namedParms = namedtuple("namedParms", parmsNames)
    # build named parms vector using the parmsNamed structure and loading parms values from C++
    newParms = namedParms(*solvePy.parms())
    newParms = newParms._replace(betaen=4.0) # to release tension on the exchange rate
    # newParms = newParms._replace(alphapO=0)      # Uncomment for the scenario with lower oil price
    # newParms = newParms._replace(alphapO=0.06)   # Uncomment for the scenario with higher oil price
    # newParms = newParms._replace(alphapwtr=0.04) # Uncomment for an alternative scenario with greenflation, not presented in the paper
    
    ## Fix the trajectories of exogenous variables
    Costs_ES_per_phase = pd.read_csv('Energy_system_costs.csv')
    Costs_ES_per_phase.drop(columns=['Phases'], inplace=True)
    Costs_ES_per_year = pd.DataFrame(np.repeat(Costs_ES_per_phase.values, 5, axis=0))
    Costs_ES_per_year = Costs_ES_per_year.loc[2:,:]
    index_list_mid  = [3,8,13,18,23,28]
    index_list_up_1   = [x - 1 for x in index_list_mid]
    index_list_down_1 = [x + 1 for x in index_list_mid]    
    index_list_up_2   = [x - 2 for x in index_list_mid]
    index_list_down_2 = [x + 2 for x in index_list_mid]  
    Costs_ES_per_year.iloc[index_list_mid,:-3] = (Costs_ES_per_year.iloc[index_list_up_2,:-3].values + Costs_ES_per_year.iloc[index_list_down_2,:-3].values) / 2
    Costs_ES_per_year.iloc[index_list_up_1,:-3] = (Costs_ES_per_year.iloc[index_list_up_2,:-3].values + Costs_ES_per_year.iloc[index_list_mid,:-3].values) / 2
    Costs_ES_per_year.iloc[index_list_down_1,:-3] = (Costs_ES_per_year.iloc[index_list_mid,:-3].values + Costs_ES_per_year.iloc[index_list_down_2,:-3].values) / 2
    Costs_ES_per_year.reset_index(drop=True, inplace=True)

    Thetas = pd.read_csv('Thetas.csv')
    Thetas.drop(columns=['Unnamed: 0'], inplace=True)
    samplesExogVar = pd.concat([Costs_ES_per_year,Thetas], axis=1)
    # samplesExogVar = pd.concat([Costs_ES_per_year.iloc[:,[26,30]],Thetas], axis=1) # for GEMMES without an energy sector
    samplesExogVar.columns = np.arange(len(samplesExogVar.columns))

    ## Run the GEMMES model
    variables_GEMMES = solveGEMMES(solvePy=solvePy, samplesExogVar=samplesExogVar, parms=newParms, solver="dopri", atol=1e-4, rtol=0, fac=0.85, facMin=0.1, facMax=4, nStepMax=300, hInit=0.025, hMin=0.025/100, hMax=0.2) # atol=1e-1, nStepMax=30000, hMin=0.025/10000
    variables_GEMMES.index = variables_GEMMES.index.round(1)

    ## Save the projection for EUDs for EnergyScope
    df_EUD = pd.read_csv('EUD_template.csv')
    share_elec_cst_H = 0.765
    share_elec_cst_S = 0.765
    share_elec_cst_F = 0.765
    list_years = [2021,2026,2031,2036,2041,2046,2051]
    list_EUDs = [df_EUD.copy()] * 7
    for i in range(7):
        list_EUDs[i] = df_EUD.copy()
        list_EUDs[i].set_index('parameter_name', inplace=True)
        variables_GEMMES_i = variables_GEMMES.loc[(variables_GEMMES.index>=list_years[i]) & (variables_GEMMES.index<list_years[i]+1)].mean()
        list_EUDs[i].loc[['ELECTRICITY', 'ELECTRICITY_VAR', 'HEAT_LOW_T_SH', 'HEAT_LOW_T_HW', 'SPACE_COOLING'], 'HOUSEHOLDS'] = [variables_GEMMES_i['El_H']*share_elec_cst_H, variables_GEMMES_i['El_H']*(1-share_elec_cst_H), variables_GEMMES_i['HLTSH_H'], variables_GEMMES_i['HLTHW_H'], variables_GEMMES_i['SC_H']]
        list_EUDs[i].loc[['ELECTRICITY', 'ELECTRICITY_VAR', 'HEAT_LOW_T_SH', 'SPACE_COOLING'], 'SERVICES'] = [(variables_GEMMES_i['El_B']+variables_GEMMES_i['El_G'])*share_elec_cst_S, (variables_GEMMES_i['El_B']+variables_GEMMES_i['El_G'])*(1-share_elec_cst_S), variables_GEMMES_i['HLTSH_B']+variables_GEMMES_i['HLTSH_G'], variables_GEMMES_i['SC_B']+variables_GEMMES_i['SC_G']]
        list_EUDs[i].loc[['ELECTRICITY', 'ELECTRICITY_VAR', 'HEAT_HIGH_T', 'HEAT_LOW_T_SH', 'HEAT_LOW_T_HW', 'PROCESS_COOLING', 'NON_ENERGY'], 'INDUSTRY']  = [variables_GEMMES_i['El_F']*share_elec_cst_F, variables_GEMMES_i['El_F']*(1-share_elec_cst_F), variables_GEMMES_i['HHT_F'], variables_GEMMES_i['HLTSH_F'], variables_GEMMES_i['HLTHW_F'], variables_GEMMES_i['PC_F'], variables_GEMMES_i['NE_F']]
        list_EUDs[i].loc[['MOBILITY_PASSENGER', 'MOBILITY_FREIGHT'], 'TRANSPORTATION'] = [variables_GEMMES_i['MP_H'], variables_GEMMES_i['MF_F']]
        list_EUDs[i] = list_EUDs[i].round(1)
        list_EUDs[i].reset_index(inplace=True)
        col_names = list_EUDs[i].columns
        list_EUDs[i] = list_EUDs[i][col_names[[1,2,0,3,4,5,6,7]]]
    list_EUDs[0].to_csv('EUD_2021.csv', index=False)
    list_EUDs[1].to_csv('EUD_2026.csv', index=False)
    list_EUDs[2].to_csv('EUD_2031.csv', index=False)
    list_EUDs[3].to_csv('EUD_2036.csv', index=False)
    list_EUDs[4].to_csv('EUD_2041.csv', index=False)
    list_EUDs[5].to_csv('EUD_2046.csv', index=False)
    list_EUDs[6].to_csv('EUD_2051.csv', index=False)
    
    ## Save the projections for space heating shares between sectors, space cooling shares between sectors and the discount rate
    variables_GEMMES['LTH_tot'] = variables_GEMMES['HLTHW_F'] + variables_GEMMES['HLTSH_F'] + variables_GEMMES['HLTSH_B'] + variables_GEMMES['HLTSH_G'] + variables_GEMMES['HLTHW_H'] + variables_GEMMES['HLTSH_H']
    variables_GEMMES['SC_tot'] = variables_GEMMES['SC_B'] + variables_GEMMES['SC_G'] + variables_GEMMES['SC_H']
    list_phases = ['2019_2021','2021_2026','2026_2031','2031_2036','2036_2041','2041_2046','2046_2051']
    list_variables_GEMMES = [variables_GEMMES.loc[variables_GEMMES.index<2021].mean()]
    for i in range(6):
        list_variables_GEMMES.append(variables_GEMMES.loc[(variables_GEMMES.index>=list_years[i]) & (variables_GEMMES.index<list_years[i+1])].mean())
    shares_LTH = pd.DataFrame(index=list_phases, columns=['F','B','G','H'])
    shares_cooling = pd.DataFrame(index=list_phases, columns=['B','G','H'])
    r_discount = pd.DataFrame(index=list_phases, columns=['r_discount'])
    for i in range(7):
        shares_LTH.loc[list_phases[i],'F'] = round((list_variables_GEMMES[i].loc['HLTSH_F'] + list_variables_GEMMES[i].loc['HLTHW_F']) / list_variables_GEMMES[i].loc['LTH_tot'], 3)
        shares_LTH.loc[list_phases[i],'B'] = round(list_variables_GEMMES[i].loc['HLTSH_B'] / list_variables_GEMMES[i].loc['LTH_tot'], 3)
        shares_LTH.loc[list_phases[i],'G'] = round(list_variables_GEMMES[i].loc['HLTSH_G'] / list_variables_GEMMES[i].loc['LTH_tot'], 3)
        shares_LTH.loc[list_phases[i],'H'] = round((list_variables_GEMMES[i].loc['HLTSH_H'] + list_variables_GEMMES[i].loc['HLTHW_H']) / list_variables_GEMMES[i].loc['LTH_tot'], 3)
        shares_cooling.loc[list_phases[i],'B'] = round(list_variables_GEMMES[i].loc['SC_B'] / list_variables_GEMMES[i].loc['SC_tot'], 3)
        shares_cooling.loc[list_phases[i],'G'] = round(list_variables_GEMMES[i].loc['SC_G'] / list_variables_GEMMES[i].loc['SC_tot'], 3)
        shares_cooling.loc[list_phases[i],'H'] = round(list_variables_GEMMES[i].loc['SC_H'] / list_variables_GEMMES[i].loc['SC_tot'], 3)
        r_discount.loc[list_phases[i],'r_discount'] = round(list_variables_GEMMES[i].loc['ip'], 3) #- list_variables_GEMMES[i].loc['pDot'] / list_variables_GEMMES[i].loc['p'], 3)   
    shares_LTH.reset_index(inplace=True)
    shares_LTH.rename(columns={'index':'Phase'}, inplace=True)
    shares_LTH.to_csv('shares_LTH.csv', index=False)
    shares_cooling.reset_index(inplace=True)
    shares_cooling.rename(columns={'index':'Phase'}, inplace=True)
    shares_cooling.to_csv('shares_cooling.csv', index=False)
    r_discount.reset_index(inplace=True)
    r_discount.rename(columns={'index':'Phase'}, inplace=True)
    r_discount.to_csv('r_discount.csv', index=False)
    en = variables_GEMMES['en'].round(3)
    en.to_csv('exchange_rate.csv')

    return variables_GEMMES
    
def run_EnergyScope():
    n_year_opti = 30 # We optimize over the entire transition period, from 2021 to 2051
    
    ## Define the AMPL optimization problem
    EnergyScope_output_file = os.path.join(EnergyScope_case_study_path,'_Results.pkl')
    ampl_0 = AmplObject(mod_1_path, mod_2_path, dat_path_0, ampl_options, type_model=EnergyScope_granularity)
    ampl_0.clean_history()
    ampl_pre = AmplPreProcessor(ampl_0, n_year_opti, n_years_overlap=0)
    ampl_collector = AmplCollector(ampl_pre, EnergyScope_output_file, expl_text)
    t = time.time()
    curr_years_wnd = ampl_pre.write_seq_opti(0).copy()
    ampl_pre.remaining_update(0)
    ampl = AmplObject(mod_1_path, mod_2_path, dat_path, ampl_options, type_model=EnergyScope_granularity)
    
    ## Read and integrate in EnergyScope the input data from GEMMES
    
    # Include the discount rate given by GEMMES
    r_discount = pd.read_csv('r_discount.csv')
    r_discount['r_discount'] = r_discount['r_discount'] * (r_discount['r_discount']>=0) # We cannot have a negative discount rate
    r_discount['r_discount'] += 1e-4  # We cannot have a zero discount rate
    r_discount.set_index('Phase', inplace=True)
    phases_ES = ['2015_2020', '2020_2025', '2025_2030', '2030_2035', '2035_2040', '2040_2045', '2045_2050']
    year_list = ['YEAR_2015', 'YEAR_2020', 'YEAR_2025', 'YEAR_2030', 'YEAR_2035', 'YEAR_2040', 'YEAR_2045', 'YEAR_2050'] 
    for j in range(len(phases_ES)):
        ampl.set_params('r_discount',{(phases_ES[j]):r_discount.iloc[j,0]})
        
    # Include the energy demand given by GEMMES
    if mode=='GEMMES-EnergyScope':
        EUD_2021 = pd.read_csv('EUD_2021.csv')
        EUD_2026 = pd.read_csv('EUD_2026.csv')
        EUD_2031 = pd.read_csv('EUD_2031.csv')
        EUD_2036 = pd.read_csv('EUD_2036.csv')
        EUD_2041 = pd.read_csv('EUD_2041.csv')
        EUD_2046 = pd.read_csv('EUD_2046.csv')
        EUD_2051 = pd.read_csv('EUD_2051.csv')
        EUD_2015 = EUD_2021.copy()
        EUD_dict = {0:EUD_2015, 1:EUD_2021, 2:EUD_2026, 3:EUD_2031, 4:EUD_2036, 5:EUD_2041, 6:EUD_2046, 7:EUD_2051}         
        series_list = []
        for j in np.arange(2,len(EUD_dict)):
            EUD_dict[j].set_index('parameter_name', inplace=True)
            EUD_dict[j].drop(columns=['Category','Subcategory','Units'], inplace=True) 
            m = EUD_dict[j].shape[0]
            n = EUD_dict[j].shape[1] 
            index0 = np.array([year_list[j]] * m * n)
            index1 = np.array(np.repeat(EUD_dict[j].index.to_list(), n))
            index2 = np.array(EUD_dict[j].columns.to_list() * m)
            series_list.append(pd.Series(EUD_dict[j].values.flatten(), index=[index0, index1, index2]))   
        eud_series_full = pd.concat(series_list)
        eud_ampl = apy.DataFrame.from_pandas(eud_series_full)
        ampl.set_params('end_uses_demand_year', eud_ampl)
    
    # Distinguish between imported and locally-produced content for each technology. Imported content is subject to exchange rate fluctuations.
    c_inv_ampl = ampl.get_param('c_inv').to_list()
    c_inv_ampl = pd.DataFrame(c_inv_ampl, columns=['Year', 'Technologies', 'Value'])
    # Read for reach technology, what fraction of it is locally produced in terms of added value
    if country=='Colombia':
        Technos_local_fraction = pd.read_csv('Technos_information_CO.csv')
        Technos_local_fraction.drop(columns=['Lifetime','Included_in_real_cost_2021'], inplace=True)
        en0 = 3.74424417 # Exchange rate value at the start year of 2021, given in k COP / USD
    elif country=='Turkey':
        Technos_local_fraction = pd.read_csv('Technos_information_TK.csv')
        en0 = 5.36731    # Exchange rate value at the start year of 2019, given in TL / USD
    c_inv_ampl = pd.merge(c_inv_ampl, Technos_local_fraction, on='Technologies', how='left')
    c_inv_ampl.fillna(0, inplace=True)
    # Include the evolution of the exchange rate given by GEMMES
    en = pd.read_csv('exchange_rate.csv')
    en.set_index('Unnamed: 0', inplace=True)
    en_yearly = pd.DataFrame(index=year_list, columns=['en'])
    list_years = [2019,2021,2026,2031,2036,2041,2046,2051]
    for i in range(8):
        en_yearly.iloc[i,0] = en.loc[(en.index>=list_years[i]) & (en.index<list_years[i]+1), 'en'].mean()
    # Only the evolution of the exchange rate, not its initial value, influences the optimization problem in EnergyScope
    en_yearly = en_yearly / en_yearly.loc['YEAR_2020'] 
    en_yearly.reset_index(inplace=True)
    en_yearly.rename(columns={'index': 'Year'}, inplace=True)
    c_inv_ampl = pd.merge(c_inv_ampl, en_yearly, on='Year', how='left')
    c_inv_ampl['Value'] *= en0 # Convert constant USD to constant k COP or cosntant TL
    c_inv_ampl['Value'] = ( c_inv_ampl['Value']*c_inv_ampl['Local'] + c_inv_ampl['Value']*c_inv_ampl['en']*(1-c_inv_ampl['Local']) ) # The imported fraction of goods is subject to exchange rate's fluctuations
    c_inv_ampl.drop(columns=['Local', 'en'], inplace=True)
    c_inv_ampl.set_index(['Year', 'Technologies'], inplace=True)
    c_inv_ampl = apy.DataFrame.from_pandas(c_inv_ampl)
    ampl.set_params('c_inv', c_inv_ampl)
    
    # We assume that all maintenance costs are local costs
    c_maint_ampl = ampl.get_param('c_maint').to_list()
    c_maint_ampl = pd.DataFrame(c_maint_ampl, columns=['Year', 'Technologies', 'Value'])
    c_maint_ampl['Value'] *= en0 # Convert constant USD to constant k COP or constant TL
    c_maint_ampl.set_index(['Year', 'Technologies'], inplace=True)
    c_maint_ampl = apy.DataFrame.from_pandas(c_maint_ampl)
    ampl.set_params('c_maint', c_maint_ampl)
    
    c_op_ampl = ampl.get_param('c_op').to_list()
    c_op_ampl = pd.DataFrame(c_op_ampl, columns=['Year', 'Resources', 'Value'])
    if country=='Colombia':
        Non_local_resources = ['URANIUM', 'H2', 'ELECTRICITY', 'AMMONIA_RE', 'METHANOL_RE', 'IMPORTED_COAL', 'METHANOL', 'H2_RE', 'AMMONIA', 'ELEC_EXPORT', 'IMPORTED_GAS', 'H2_EXPORT', 'GAS_RE_EXPORT', 'AMMONIA_EXPORT', 'METHANOL_EXPORT']
    elif country=='Turkey':
        Non_local_resources = ['URANIUM', 'H2', 'ELECTRICITY', 'AMMONIA_RE', 'METHANOL_RE', 'IMPORTED_COAL', 'GASOLINE', 'DIESEL', 'LFO', 'BIOETHANOL', 'BIODIESEL', 'METHANOL', 'H2_RE', 'AMMONIA', 'ELEC_EXPORT', 'IMPORTED_GAS', 'H2_EXPORT', 'GAS_RE_EXPORT', 'AMMONIA_EXPORT', 'METHANOL_EXPORT']
    c_op_ampl = pd.merge(c_op_ampl, en_yearly, on='Year', how='left')
    c_op_ampl['Value'] *= en0 # Convert constant USD to constant k COP or constant TL
    c_op_ampl.loc[c_op_ampl['Resources'].isin(Non_local_resources),'Value'] *= np.array(c_op_ampl.loc[c_op_ampl['Resources'].isin(Non_local_resources),'en'].astype(float).values).round(4) # The imported resources are subject to exchange rate's fluctuations
    c_op_ampl.drop(columns=['en'], inplace=True)
    c_op_ampl.set_index(['Year', 'Resources'], inplace=True)
    c_op_ampl = apy.DataFrame.from_pandas(c_op_ampl)
    ampl.set_params('c_op', c_op_ampl)
    
    gwp_cost_ampl = ampl.get_param('gwp_cost').to_list()
    gwp_cost_ampl = pd.DataFrame(gwp_cost_ampl, columns=['Year', 'Value'])
    gwp_cost_ampl['Value'] *= en0 # Convert constant USD to constant k COP or constant TL
    gwp_cost_ampl.set_index(['Year'], inplace=True)
    gwp_cost_ampl = gwp_cost_ampl.round(3)
    gwp_cost_ampl.to_csv('CO2_costs_COP.csv')
    gwp_cost_ampl = apy.DataFrame.from_pandas(gwp_cost_ampl)
    ampl.set_params('gwp_cost', gwp_cost_ampl)
    
    ## Run the AMPL optimization problem
    solve_result = ampl.run_ampl()
    ampl.get_results()
    ampl_collector.init_storage(ampl)
    ampl_collector.update_storage(ampl,curr_years_wnd,0)
    ampl.set_init_sol()
    elapsed = time.time()-t
    print('Time to solve the optimization problem: ',elapsed)
    ampl_collector.clean_collector()
    ampl_collector.pkl()       
    
    return [EnergyScope_output_file, ampl_0]
    
def plot_EnergyScope_outputs(EnergyScope_output_file, ampl_0):
    ampl_graph = AmplGraph(EnergyScope_output_file, ampl_0, case_study)
    
    # ampl_graph.graph_cost()
    # ampl_graph.graph_gwp_per_sector()
    # ampl_graph.graph_cost_inv_phase_tech()
    # ampl_graph.graph_cost_return()
    # ampl_graph.graph_cost_op_phase()

    # ampl_graph.graph_layer()
    # ampl_graph.graph_gwp()
    # ampl_graph.graph_tech_cap()
    # ampl_graph.graph_total_cost_per_year()
    # ampl_graph.graph_load_factor()
    # df_unused = ampl_graph.graph_load_factor_2()
    # ampl_graph.graph_new_old_decom()
    ampl_graph.graph_resource()

def post_process_EnergyScope_outputs(EnergyScope_output_file, ampl_0, variables_GEMMES):
    ampl_graph = AmplGraph(EnergyScope_output_file, ampl_0, case_study)
    z_Results = ampl_graph.ampl_collector
    
    C_inv = z_Results['C_inv_phase_tech_non_annualised'].copy()
    C_inv.rename(columns = {'C_inv_phase_tech_non_annualised':'Value'}, inplace = True)
    
    New_old_decom = z_Results['New_old_decom'].copy()
    New_old_decom = New_old_decom
    New_old_decom.fillna(0, inplace=True)
    C_inv['Capa'] = New_old_decom['F_new']
    C_inv.drop(['DAM_STORAGE','BEV_BATT','EFFICIENCY'], level='Technologies', inplace=True)
    
    ## For each technology, divide its investment costs between local and imported
    Technos_local_fraction = pd.read_csv('Technos_information.csv')
    Technos_local_fraction.drop(columns=['Lifetime','Included_in_real_cost_2021'], inplace=True)
    C_inv.reset_index(inplace=True)
    C_inv = pd.merge(C_inv, Technos_local_fraction, on='Technologies')
    C_inv.set_index(['Phases','Technologies'], inplace=True)
    C_inv.sort_values(['Phases','Technologies'], axis=0, inplace=True)
    C_inv['Imported'] = 1 - C_inv['Local']
    C_inv[['F','B','G','H']] = [1,0,0,0]
    
    ## For each technology, assign its investment costs across GEMMES' economic sectors
    # Infrastructure
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['GRID','H2_INFRASTRUCTURE']),[4,6]] = [0.8,0.2] # Infrastructure costs are splitted between the private and public sectors
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DHN']),[4,6]] = [0.7,0.3]
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['HVAC_LINE']),[4,6]] = [0.65,0.35]
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['CHARGING_STATION']),[4,6,7]] = [0,0.5,0.5]
    # private mobility
    list_private_mob_tech = ['MOTORCYCLE','CAR_GASOLINE','CAR_GASOLINE_BIS','CAR_DIESEL','CAR_NG','CAR_METHANOL','CAR_HEV','CAR_PHEV','MOTORCYCLE_ELECTRIC','CAR_BEV','CAR_FUEL_CELL']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_private_mob_tech),[4,7]] = [0,1] # Private mobility costs are supported by households
    # public mobility
    list_public_mob_tech = ['TRAMWAY_TROLLEY','BUS_COACH_DIESEL','BUS_COACH_DIESEL_BIS','BUS_COACH_GASOLINE','BUS_COACH_HYDIESEL','BUS_COACH_CNG_STOICH','BUS_COACH_FC_HYBRIDH2','TRAIN_PUB']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_public_mob_tech),[4,6]] = [0,1] # Public mobility costs are supported by the State 
    # cooling
    shares_cooling = pd.read_csv('shares_cooling.csv')
    shares_cooling.set_index('Phase',inplace=True)
    list_cooling_tech = ['DEC_ELEC_COLD','DEC_THHP_GAS_COLD']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_cooling_tech),4] = 0
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_ELEC_COLD']),[5,6,7]] = shares_cooling.values
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_THHP_GAS_COLD']),[5,6,7]] = shares_cooling.values 
    # Low-temperature heating
    C_inv['merge_index'] = C_inv.index.get_level_values('Phases')
    shares_LTH = pd.read_csv('shares_LTH.csv')
    shares_LTH.set_index('Phase',inplace=True)
    shares_LTH['merge_index'] = C_inv['merge_index'].unique()
    C_inv_bis = pd.merge(C_inv, shares_LTH, on='merge_index')
    C_inv_bis.index = C_inv.index
    list_LTH_tech = ['DHN_HP_ELEC','DHN_COGEN_GAS','DHN_COGEN_WOOD','DHN_COGEN_WASTE','DHN_COGEN_WET_BIOMASS','DHN_COGEN_BIO_HYDROLYSIS','DHN_BOILER_GAS','DHN_BOILER_WOOD','DHN_BOILER_OIL','DHN_DEEP_GEO','DHN_SOLAR','DEC_HP_ELEC','DEC_THHP_GAS','DEC_COGEN_GAS','DEC_COGEN_OIL','DEC_ADVCOGEN_GAS','DEC_ADVCOGEN_H2','DEC_BOILER_GAS','DEC_BOILER_WOOD','COAL_STOVE','DEC_BOILER_OIL','DEC_SOLAR','DEC_DIRECT_ELEC']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_LTH_tech),[4,5,6,7]] = C_inv_bis.iloc[C_inv_bis.index.get_level_values('Technologies').isin(list_LTH_tech),[9,10,11,12]].values
    C_inv.drop(columns=['merge_index'],inplace=True)
    
    ## Summarise in one data frame the division of investment costs between local and imported and between the different economic sectors
    output_for_GEMMES = pd.DataFrame(index=C_inv.index.get_level_values(0).unique())
    output_for_GEMMES['capex_F_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_F_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_B_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_B_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_G_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_G_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_H_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['H']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_H_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['H']).groupby(level=[0]).sum()    
    
    ## For each technology, divide its maintenance costs between local and imported and between the different economic sectors
    C_maint = z_Results['C_op_phase_tech_non_annualised']
    C_maint.rename(columns = {'C_op_phase_tech_non_annualised':'Value'}, inplace = True)
    C_maint['Local'] = 1 # All maintenance costs are supposed to be local since they consist mainly of labour costs 
    C_maint['Imported'] = 1 - C_maint['Local']
    C_maint.drop(['NUCLEAR','DAM_STORAGE','BEV_BATT','EFFICIENCY'], level='Technologies', inplace=True)
    C_maint[['F','B','G','H']] = C_inv.iloc[~C_inv.index.get_level_values('Phases').isin(['2015_2020']),[4,5,6,7]].values        
    
    ## Classify resources between local, imported and exported
    # C_op computed by EnergyScope is annualised, unlike C_inv. We need to get a non-annualised version of it
    annualised_factor = pd.DataFrame(index=z_Results['C_inv_phase'].index, data=z_Results['C_inv_phase'].values / z_Results['C_inv_phase_non_annualised'].values )
    annualised_factor['merge_index'] = annualised_factor.index
    C_op = z_Results['C_op_phase_res'].copy()
    C_op.rename(columns = {'C_op_phase_res':'Value'}, inplace = True)
    C_op_bis = C_op.copy()
    C_op_bis['merge_index'] = C_op_bis.index.get_level_values(0)
    C_op_bis = pd.merge(C_op_bis, annualised_factor, on='merge_index')
    C_op_bis.index = C_op.index
    C_op_bis.drop(columns=['merge_index'], inplace=True)
    C_op['Value'] = C_op_bis['Value'].values/C_op_bis[0].values
    C_op['Local'] = 0
    Local_resources = ['GASOLINE','DIESEL','BIOETHANOL','BIODIESEL','LFO','LOCAL_GAS','WOOD','LOCAL_COAL','CO2_CAPTURED','CO2_INDUSTRY','RES_WIND','RES_SOLAR','RES_HYDRO','CO2_ATM','WET_BIOMASS','WASTE','RES_GEO']
    C_op.iloc[C_op.index.get_level_values('Resources').isin(Local_resources),1] = 1
    C_op['Exported'] = 0
    Exported_resources = ['ELEC_EXPORT','H2_EXPORT','GAS_RE_EXPORT','AMMONIA_EXPORT','METHANOL_EXPORT','CO2_EMISSIONS']
    C_op.iloc[C_op.index.get_level_values('Resources').isin(Exported_resources),2] = 1
    C_op['Imported'] = 1 - C_op['Local'] -  C_op['Exported']
    C_op[['F','B','G','H']] = [1,0,0,0]
    
    ## Summarise in one data frame the division between local, imported and exported resources. All resource costs are assigned to the private sector.
    output_for_GEMMES['opex_F_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['F']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['F']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_F_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['F']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['F']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_B_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['B']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['B']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_B_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['B']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['B']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_G_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['G']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['G']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_G_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['G']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['G']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_H_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['H']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['H']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_H_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['H']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['H']).groupby(level=[0]).sum()
    output_for_GEMMES['exports_CO'] = (C_op['Value'] * C_op['Exported']).groupby(level=[0]).sum()
    output_for_GEMMES.loc['2015_2020','exports_CO'] = 0

    ## Reconstruct the costs for the first phase based on YEAR_2020 data
    Cost_breakdown_non_annualised = z_Results['Cost_breakdown_non_annualised']
    Cost_breakdown_non_annualised = Cost_breakdown_non_annualised[Cost_breakdown_non_annualised.index.get_level_values('Years').isin(['YEAR_2020'])]
    Cost_breakdown_non_annualised.rename(columns={'C_maint':'C_maint_CO'}, inplace=True)
    Cost_breakdown_non_annualised['C_maint_M'] = 0
    Cost_breakdown_non_annualised_bis = Cost_breakdown_non_annualised.copy()
    Cost_breakdown_non_annualised_bis['Local'] = 0
    Cost_breakdown_non_annualised_bis.iloc[Cost_breakdown_non_annualised_bis.index.get_level_values('Elements').isin(Local_resources),4] = 1
    Cost_breakdown_non_annualised_bis['Imported'] = 1 - Cost_breakdown_non_annualised_bis['Local']
    Cost_breakdown_non_annualised_bis.iloc[Cost_breakdown_non_annualised_bis.index.get_level_values('Elements').isin(Exported_resources),5] = 0
    Cost_breakdown_non_annualised_bis['C_op_CO'] = Cost_breakdown_non_annualised_bis['C_op'] * Cost_breakdown_non_annualised_bis['Local']
    Cost_breakdown_non_annualised_bis['C_op_M'] = Cost_breakdown_non_annualised_bis['C_op'] * Cost_breakdown_non_annualised_bis['Imported']
    Cost_breakdown_non_annualised_bis = Cost_breakdown_non_annualised_bis.sum()
    Cost_breakdown_non_annualised_bis.drop(index=['C_inv','C_maint_CO','C_maint_M','C_op','Local','Imported'], inplace=True)
    Technos_information = pd.read_csv('Technos_information.csv')
    Technos_information.rename(columns={'Technologies':'Elements'}, inplace=True)
    Cost_breakdown_non_annualised = pd.merge(Cost_breakdown_non_annualised, Technos_information, on='Elements')
    Cost_breakdown_non_annualised['C_inv_per_year'] = Cost_breakdown_non_annualised['C_inv'] / Cost_breakdown_non_annualised['Lifetime']
    Cost_breakdown_non_annualised['C_inv_per_year_in_real_cost_2021'] = Cost_breakdown_non_annualised['C_inv_per_year'] * Cost_breakdown_non_annualised['Included_in_real_cost_2021']
    Cost_breakdown_non_annualised.set_index('Elements', inplace=True)
    Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.sum()
    Cost_breakdown_2021_for_comparison_with_real_cost = Cost_breakdown_non_annualised.copy()
    Cost_breakdown_non_annualised.drop(index=['C_inv','C_op','Local','Lifetime','Included_in_real_cost_2021','C_inv_per_year_in_real_cost_2021'], inplace=True)
    Cost_breakdown_2021_for_comparison_with_real_cost.drop(index=['C_inv','C_op','Local','Lifetime','Included_in_real_cost_2021','C_inv_per_year'], inplace=True)
    Cost_breakdown_non_annualised = pd.concat([Cost_breakdown_non_annualised, Cost_breakdown_non_annualised_bis])
    Cost_breakdown_2021_for_comparison_with_real_cost = pd.concat([Cost_breakdown_2021_for_comparison_with_real_cost, Cost_breakdown_non_annualised_bis])
    Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.round(1)
    # Cost_breakdown_non_annualised.to_csv('Enegy_system_cost_2021.csv')  
    output_for_GEMMES.iloc[0,0:8] = Cost_breakdown_non_annualised['C_inv_per_year'] * output_for_GEMMES.iloc[0,0:8] / output_for_GEMMES.iloc[0,0:8].sum() * 5 # We multiply the yearly investment by the number of years in the phase
    output_for_GEMMES.loc['2015_2020',['opex_F_CO','opex_B_CO','opex_G_CO','opex_H_CO']] = Cost_breakdown_non_annualised[['C_maint_CO', 'C_op_CO']].sum() * output_for_GEMMES.loc['2020_2025',['opex_F_CO','opex_B_CO','opex_G_CO','opex_H_CO']] / output_for_GEMMES.loc['2020_2025',['opex_F_CO','opex_B_CO','opex_G_CO','opex_H_CO']].sum() * 5
    output_for_GEMMES.loc['2015_2020',['opex_F_M','opex_B_M','opex_G_M','opex_H_M']] = Cost_breakdown_non_annualised[['C_maint_M', 'C_op_M']].sum() * output_for_GEMMES.loc['2020_2025',['opex_F_M','opex_B_M','opex_G_M','opex_H_M']] / output_for_GEMMES.loc['2020_2025',['opex_F_M','opex_B_M','opex_G_M','opex_H_M']].sum() * 5
    Cost_breakdown_2021_for_comparison_with_real_cost = Cost_breakdown_2021_for_comparison_with_real_cost.sum() * 5 # Transform the yearly cost into a cost per phase
    
    ## Compute a adjustment factor to fit the costs from EnergyScope to the real cost of the energy system given by DNP
    variables_GEMMES_2021 = variables_GEMMES.loc[(variables_GEMMES.index>=2021) & (variables_GEMMES.index<2022)].mean()
    Real_energy_system_cost_2021 = 33.323773083 # billion 2021 COP, according to DNP
    adjustment_factor = Real_energy_system_cost_2021 / ( variables_GEMMES_2021['p'] * Cost_breakdown_2021_for_comparison_with_real_cost ) # The adjustment factor also allows to transform the phase costs into yearly costs (division by 5 included in the factor)
    
    
    ## Add to the resource costs of households, government and banks the bills that they pay for buying fuels and electricity to private firms
    # year_balance indicates the resources consumed or produced by each technology for each year
    year_balance = z_Results['Year_balance'].copy()
    # Add to year_balance the ownership of technologies by the different economic sectors
    year_balance[['F','B','G','H']] = [1,0,0,0]
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_private_mob_tech),['F','H']] = [0,1]
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_public_mob_tech),['F','G']] = [0,1]
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_cooling_tech),['F']] = 0
    # Define the ownership of cooling technologies
    if('DEC_ELEC_COLD' in year_balance.index.get_level_values('Elements')):
        year_balance.loc[year_balance.index.get_level_values('Elements').isin(['DEC_ELEC_COLD']),['B','G','H']] = shares_cooling.values
    if('DEC_THHP_GAS_COLD' in year_balance.index.get_level_values('Elements')):
        year_balance.loc[year_balance.index.get_level_values('Elements').isin(['DEC_THHP_GAS_COLD']),['B','G','H']] = shares_cooling.iloc[1:,:].values
    # Define the ownership of heating technologies
    year_balance['merge_index_2'] = year_balance.index.get_level_values('Years')
    shares_LTH['merge_index_2'] = year_balance['merge_index_2'].unique()
    year_balance_bis = pd.merge(year_balance, shares_LTH, on='merge_index_2')
    year_balance_bis.index = year_balance.index
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_LTH_tech),['F','B','G','H']] = year_balance_bis.loc[year_balance_bis.index.get_level_values('Elements').isin(list_LTH_tech),['F_y','B_y','G_y','H_y']].values
    year_balance_carbon_tax = year_balance.copy()
    # Restrict year_balance to the resources actually bought by households, government and banks
    year_balance = year_balance[year_balance['F']<0.999]
    year_balance = year_balance.loc[:, year_balance.columns.isin(['ELECTRICITY','LOCAL_GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE','H2','METHANOL','B','G','H'])]
    year_balance.loc[year_balance['ELECTRICITY']>0,'ELECTRICITY'] = np.nan
    year_balance = year_balance.abs()
    # Neglect hydrogen and methanol since their buying by households, government and banks represents negligible amounts of money
    year_balance.drop(columns=['H2','METHANOL'], inplace=True) 
    
    # Reconstruct the prices of resources
    year_balance_tot = z_Results['Year_balance'].copy()
    list_resources = ['LOCAL_GAS','IMPORTED_GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE']
    list_resources_with_elec = list_resources + ['ELECTRICITY']
    n_resources = len(list_resources_with_elec)
    year_balance_tot = year_balance_tot.loc[:, year_balance_tot.columns.isin(list_resources_with_elec)]
    year_balance_tot = year_balance_tot.iloc[year_balance_tot.index.get_level_values('Elements').isin(list_resources)]
    year_balance_tot = year_balance_tot.groupby(level=[0]).sum()
    Cost_breakdown = z_Results['Cost_breakdown'].copy()
    Cost_breakdown_res = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(list_resources_with_elec)]
    Cost_breakdown_res = pd.pivot_table(Cost_breakdown_res, values='C_op', index=['Years'], columns=['Elements'])
    Cost_breakdown_res['LOCAL_GAS'] = Cost_breakdown_res['LOCAL_GAS'] + Cost_breakdown_res['IMPORTED_GAS']
    Cost_breakdown_res.drop(columns=['IMPORTED_GAS'], inplace=True)
    prices_resources = Cost_breakdown_res.div(year_balance_tot)
    
    # Construct a price for locally produced electricity based on the electricity mix
    technos_res_elec = ['CCGT','IMPORTED_COAL_CENTRAL','LOCAL_COAL_CENTRAL','PV','WIND_ONSHORE','WIND_OFFSHORE','HYDRO_DAM','HYDRO_RIVER','GEOTHERMAL','GRID','HVAC_LINE','IMPORTED_GAS','LOCAL_GAS','IMPORTED_COAL','LOCAL_COAL']
    Cost_elec_approx = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(technos_res_elec)]
    year_balance_elec = z_Results['Year_balance'].copy()
    year_balance_elec = year_balance_elec[['IMPORTED_COAL','LOCAL_COAL','LOCAL_GAS','ELECTRICITY']]
    Cost_elec_approx['perc_for_elec'] = np.nan
    # perc_for_elec represents, for each resource, the fraction that is devoted to electricity production
    if('IMPORTED_COAL_CENTRAL' in year_balance_elec.index.get_level_values('Elements').to_list()):
        Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['IMPORTED_COAL']),'perc_for_elec'] = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['IMPORTED_COAL_CENTRAL']),'IMPORTED_COAL'].values / year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['IMPORTED_COAL']),'IMPORTED_COAL'].values
    if('LOCAL_COAL_CENTRAL' in year_balance_elec.index.get_level_values('Elements').to_list()):
        Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['LOCAL_COAL']),'perc_for_elec'] = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['LOCAL_COAL_CENTRAL']),'LOCAL_COAL'].values / year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['LOCAL_COAL']),'LOCAL_COAL'].values
    Local_gas_yearly = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['LOCAL_GAS']),'LOCAL_GAS'].to_frame()
    Local_gas_yearly.reset_index(inplace=True)
    Local_gas_yearly.drop(columns=['Elements'], inplace=True)
    Local_gas_yearly.set_index('Years', inplace=True)
    Imported_gas_yearly = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['IMPORTED_GAS']),'LOCAL_GAS'].to_frame()
    Imported_gas_yearly.reset_index(inplace=True)
    Imported_gas_yearly.drop(columns=['Elements'], inplace=True)
    Imported_gas_yearly.set_index('Years', inplace=True)   
    temp_local_gas    = Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['LOCAL_GAS']),'perc_for_elec'].to_frame()
    temp_imported_gas = Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['IMPORTED_GAS']),'perc_for_elec'].to_frame()
    perc_gas = (year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['CCGT']),'LOCAL_GAS'] / pd.merge(Local_gas_yearly, Imported_gas_yearly, on='Years', how='outer').sum(axis=1) ).to_frame()
    temp_local_gas    = pd.merge(temp_local_gas, perc_gas, on='Years', how='left')
    temp_imported_gas = pd.merge(temp_imported_gas, perc_gas, on='Years', how='left')
    temp_local_gas.drop(columns=['perc_for_elec'], inplace=True)
    temp_imported_gas.drop(columns=['perc_for_elec'], inplace=True)
    Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['LOCAL_GAS']),'perc_for_elec']    = temp_local_gas.values
    Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['IMPORTED_GAS']),'perc_for_elec'] = temp_imported_gas.values
    Cost_elec_approx.loc[:,'C_op'] = Cost_elec_approx['C_op'] * Cost_elec_approx['perc_for_elec']
    Cost_elec_approx.loc[:,'C_op'] = Cost_elec_approx.loc[:,'C_op'].abs()
    Cost_elec_approx.drop(columns=['perc_for_elec'],inplace=True)
    Cost_elec_approx = Cost_elec_approx.groupby(level=[0]).sum()
    Cost_elec_approx = Cost_elec_approx.sum(axis=1)
    year_balance_elec = year_balance_elec.loc[year_balance_elec['ELECTRICITY']>=0]
    year_balance_elec = year_balance_elec.groupby(level=[0]).sum()
    prices_resources['ELECTRICITY'] = Cost_elec_approx.values / year_balance_elec['ELECTRICITY']
      
    # Multiply the quantities of resources used by the resources' prices to obtain the cost of fuels and electricity bought by households, government and banks
    year_balance = pd.merge(year_balance, prices_resources, on='Years')
    year_balance.iloc[:,0:n_resources-1] = year_balance.iloc[:,0:n_resources-1].values * year_balance.iloc[:,n_resources+2:].values
    year_balance = year_balance.iloc[:,0:n_resources+2]
    year_balance['total_cost'] = year_balance.iloc[:,0:n_resources-1].sum(axis=1)
    year_balance = year_balance.iloc[:,n_resources-1:n_resources+3]
    year_balance['cost_B'] = year_balance['total_cost'] * year_balance['B']
    year_balance['cost_G'] = year_balance['total_cost'] * year_balance['G']
    year_balance['cost_H'] = year_balance['total_cost'] * year_balance['H']
    year_balance = year_balance.groupby(level=[0]).sum()
    year_balance = year_balance.iloc[:,4:] 
    year_balance['C_op_tot'] = Cost_breakdown.groupby(level=[0]).sum()['C_op']
    # Go from yearly costs to phase costs
    year_balance_shift = year_balance.copy()
    year_balance_shift = year_balance_shift.shift(1)
    year_balance_2021 = year_balance.iloc[0]
    year_balance = (year_balance + year_balance_shift) / 2 
    year_balance.loc['YEAR_2020'] = year_balance_2021
    # We compute the fraction of the total cost of resources which corresponds to fuels and electricity bought by households, government and banks
    year_balance['B % C_op'] = year_balance['cost_B'] / year_balance['C_op_tot']
    year_balance['G % C_op'] = year_balance['cost_G'] / year_balance['C_op_tot']
    year_balance['H % C_op'] = year_balance['cost_H'] / year_balance['C_op_tot']
    # This total cost's fraction is multiplied by the total cost excluding exports
    C_op_minus_exports = C_op.copy()
    C_op_minus_exports['Value'] = C_op_minus_exports['Value'] * (1 - C_op_minus_exports['Exported'])
    C_op_to_add = C_op_minus_exports['Value'].groupby(level=[0]).sum().to_frame()
    C_op_to_add_2015_2020 = C_op_to_add.loc['2020_2025'].to_frame().transpose()
    C_op_to_add_2015_2020.rename(index={'2020_2025':'2015_2020'}, inplace=True)
    C_op_to_add = pd.concat([C_op_to_add_2015_2020, C_op_to_add])
    C_op_to_add['B'] = year_balance['B % C_op'].values * C_op_to_add['Value'].values
    C_op_to_add['G'] = year_balance['G % C_op'].values * C_op_to_add['Value'].values
    C_op_to_add['H'] = year_balance['H % C_op'].values * C_op_to_add['Value'].values
    
    # The bills that households, government and banks pay for buying fuels and electricity to private firms are finally added to the reference dataframe
    output_for_GEMMES['opex_B_CO'] += C_op_to_add['B']
    output_for_GEMMES['opex_G_CO'] += C_op_to_add['G']
    output_for_GEMMES['opex_H_CO'] += C_op_to_add['H']
    
    
    ## Compute the carbon tax on the different sectors
    list_emissive_resources = ['LOCAL_COAL','LOCAL_GAS','IMPORTED_GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE','LFO']
    n_emissive_resources = len(list_emissive_resources)
    year_balance_carbon_tax = year_balance_carbon_tax.loc[:, year_balance_carbon_tax.columns.isin(list_emissive_resources+['F','B','G','H'])] # We neglect the carbon tax on electricity imports
    year_balance_biofuels = year_balance_carbon_tax.copy()
    year_balance_biofuels = year_balance_biofuels.iloc[year_balance_biofuels.index.get_level_values('Elements').isin(['BIODIESEL','BIOETHANOL'])]
    year_balance_biofuels = year_balance_biofuels.loc[:, year_balance_biofuels.columns.isin(['DIESEL','GASOLINE'])] 
    year_balance_biofuels = year_balance_biofuels.groupby(level=[0]).sum()
    year_balance_carbon_tax.drop(list_emissive_resources+['BIODIESEL','BIOETHANOL'],level='Elements',inplace=True)
    year_balance_carbon_tax[['gwp_op_DIESEL', 'gwp_op_GASOLINE', 'gwp_op_LFO', 'gwp_op_COAL', 'gwp_op_GAS', 'gwp_op_WASTE', 'gwp_op_WET_BIOMASS', 'gwp_op_WOOD']] = [0.3148, 0.3448, 0.3115, 0.4014, 0.2666, 0.1501, 0.0118, 0.0118]
    year_balance_carbon_tax_sum = year_balance_carbon_tax.groupby(level=[0]).sum()
    year_balance_carbon_tax_sum = year_balance_carbon_tax_sum.loc[:, year_balance_carbon_tax_sum.columns.isin(['DIESEL','GASOLINE'])] 
    year_balance_biofuels = 1 - year_balance_biofuels / year_balance_carbon_tax_sum.abs()
    year_balance_carbon_tax = pd.merge(year_balance_carbon_tax, year_balance_biofuels, on='Years')
    year_balance_carbon_tax[['gwp_op_DIESEL','gwp_op_GASOLINE']] *= year_balance_carbon_tax[['DIESEL_y','GASOLINE_y']].values
    year_balance_carbon_tax.iloc[:,0:n_emissive_resources-1] *= year_balance_carbon_tax.iloc[:,n_emissive_resources+3:2*n_emissive_resources+2].values
    year_balance_carbon_tax = year_balance_carbon_tax.iloc[:,0:n_emissive_resources+3]
    year_balance_carbon_tax.fillna(0,inplace=True)
    year_balance_carbon_tax['total_CO2'] = year_balance_carbon_tax.iloc[:,0:n_emissive_resources-1].sum(axis=1)
    co2_costs = pd.read_csv('CO2_costs_COP.csv')
    co2_costs.rename(columns={'Year':'Years'}, inplace=True)
    co2_costs = co2_costs.iloc[1:]
    co2_costs.set_index('Years', inplace=True)
    year_balance_carbon_tax = pd.merge(year_balance_carbon_tax, co2_costs, on='Years')
    year_balance_carbon_tax['CO2_F'] = year_balance_carbon_tax['total_CO2'] * year_balance_carbon_tax['F'] * year_balance_carbon_tax['Value']
    year_balance_carbon_tax['CO2_B'] = year_balance_carbon_tax['total_CO2'] * year_balance_carbon_tax['B'] * year_balance_carbon_tax['Value']
    year_balance_carbon_tax['CO2_G'] = year_balance_carbon_tax['total_CO2'] * year_balance_carbon_tax['G'] * year_balance_carbon_tax['Value']
    year_balance_carbon_tax['CO2_H'] = year_balance_carbon_tax['total_CO2'] * year_balance_carbon_tax['H'] * year_balance_carbon_tax['Value']
    year_balance_carbon_tax = year_balance_carbon_tax.iloc[:,n_emissive_resources+5:]
    year_balance_carbon_tax = year_balance_carbon_tax.groupby(level=[0]).sum()
    # Remove the negative carbon tax in 2050 for producing green gas
    neg_carbon_tax = year_balance_carbon_tax.loc['YEAR_2050','CO2_F']
    year_balance_carbon_tax.loc['YEAR_2050','CO2_F'] -= neg_carbon_tax
    year_balance_carbon_tax.loc['YEAR_2050','CO2_G'] += neg_carbon_tax
    year_balance_carbon_tax = year_balance_carbon_tax.abs()
    # Go from yearly costs to phase costs
    year_balance_carbon_tax_shift = year_balance_carbon_tax.copy()
    year_balance_carbon_tax_shift = year_balance_carbon_tax_shift.shift(1)
    year_balance_carbon_tax_shift.iloc[0,:] = year_balance_carbon_tax.iloc[0,:].values
    year_balance_carbon_tax = (year_balance_carbon_tax + year_balance_carbon_tax_shift) / 2   
    year_balance_carbon_tax = year_balance_carbon_tax.iloc[1:]
    
    
    ## Apply the adjustment factor so that the total energy system cost from EnergyScope fits the real cost of the energy system given by DNP
    output_for_GEMMES *= adjustment_factor
    year_balance_carbon_tax *= adjustment_factor
    # Re-write all costs according to a subdivision appropriate for GEMMES' equations
    output_for_GEMMES['ikefCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['ikefM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['ikebCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['ikebM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['ikegCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['ikegM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['ikehCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['H']).groupby(level=[0]).sum()
    output_for_GEMMES['ikehM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['H']).groupby(level=[0]).sum()
    output_for_GEMMES['pkefCO'] = output_for_GEMMES['capex_F_CO'] / output_for_GEMMES['ikefCO']
    output_for_GEMMES['pkefM']  = output_for_GEMMES['capex_F_M']  / output_for_GEMMES['ikefM'] / variables_GEMMES_2021['en']
    output_for_GEMMES['pkebCO'] = output_for_GEMMES['capex_B_CO'] / output_for_GEMMES['ikebCO']
    output_for_GEMMES['pkebM']  = output_for_GEMMES['capex_B_M']  / output_for_GEMMES['ikebM'] / variables_GEMMES_2021['en']
    output_for_GEMMES['pkegCO'] = output_for_GEMMES['capex_G_CO'] / output_for_GEMMES['ikegCO']
    output_for_GEMMES['pkegM']  = output_for_GEMMES['capex_G_M']  / output_for_GEMMES['ikegM'] / variables_GEMMES_2021['en']
    output_for_GEMMES['pkehCO'] = output_for_GEMMES['capex_H_CO'] / output_for_GEMMES['ikehCO']
    output_for_GEMMES['pkehM']  = output_for_GEMMES['capex_H_M']  / output_for_GEMMES['ikehM'] / variables_GEMMES_2021['en']
    output_for_GEMMES['ikef'] = output_for_GEMMES['ikefCO'] + output_for_GEMMES['ikefM']
    output_for_GEMMES['ikeb'] = output_for_GEMMES['ikebCO'] + output_for_GEMMES['ikebM']
    output_for_GEMMES['ikeg'] = output_for_GEMMES['ikegCO'] + output_for_GEMMES['ikegM']
    output_for_GEMMES['ikeh'] = output_for_GEMMES['ikehCO'] + output_for_GEMMES['ikehM']
    output_for_GEMMES['sigmamkef'] = output_for_GEMMES['ikefM'] / output_for_GEMMES['ikef']
    output_for_GEMMES['sigmamkeb'] = output_for_GEMMES['ikebM'] / output_for_GEMMES['ikeb']
    output_for_GEMMES['sigmamkeg'] = output_for_GEMMES['ikegM'] / output_for_GEMMES['ikeg']
    output_for_GEMMES['sigmamkeh'] = output_for_GEMMES['ikehM'] / output_for_GEMMES['ikeh']
    # Adjust the repartitions pke / ike so that the ike's have the same order of magnitude as ikf in GEMMES
    output_for_GEMMES['pkefCO'] *= 254
    output_for_GEMMES['pkefM']  *= 254
    output_for_GEMMES['ikef']   /= 254
    output_for_GEMMES['pkebCO'] *= 2.4
    output_for_GEMMES['pkebM']  *= 2.4
    output_for_GEMMES['ikeb']   /= 2.4
    output_for_GEMMES['pkegCO'] *= 34.9
    output_for_GEMMES['pkegM']  *= 34.9
    output_for_GEMMES['ikeg']   /= 34.9
    output_for_GEMMES['pkehCO'] *= 95.8
    output_for_GEMMES['pkehM']  *= 95.8
    output_for_GEMMES['ikeh']   /= 95.8
    output_for_GEMMES['icef'] = output_for_GEMMES['opex_F_CO'] + output_for_GEMMES['opex_F_M']
    output_for_GEMMES['sigmamicef'] = output_for_GEMMES['opex_F_M'] / output_for_GEMMES['icef']
    output_for_GEMMES['iceb'] = output_for_GEMMES['opex_B_CO'] + output_for_GEMMES['opex_B_M']
    output_for_GEMMES['sigmamiceb'] = output_for_GEMMES['opex_B_M'] / output_for_GEMMES['iceb']
    output_for_GEMMES['iceg'] = output_for_GEMMES['opex_G_CO'] + output_for_GEMMES['opex_G_M']
    output_for_GEMMES['sigmamiceg'] = output_for_GEMMES['opex_G_M'] / output_for_GEMMES['iceg']
    output_for_GEMMES['ceh'] = output_for_GEMMES['opex_H_CO'] + output_for_GEMMES['opex_H_M']
    output_for_GEMMES['sigmamceh'] = output_for_GEMMES['opex_H_M'] / output_for_GEMMES['ceh']
    output_for_GEMMES['pieM'] = 1 / variables_GEMMES_2021['en']
    output_for_GEMMES['xef'] = output_for_GEMMES['exports_CO'] / variables_GEMMES_2021['en']
    output_for_GEMMES['CTf'] = 0
    output_for_GEMMES['CTb'] = 0
    output_for_GEMMES['CTg'] = 0
    output_for_GEMMES['CTh'] = 0
    n = len(output_for_GEMMES.columns)
    output_for_GEMMES.iloc[1:,n-4:n] += year_balance_carbon_tax.values  
    
    ## Specifiy the values of other exogenous variables for GEMMES, not directly related to EnergyScope
    output_for_GEMMES['reducXrO'] = 0.085
    output_for_GEMMES.loc['2015_2020','reducXrO'] = 0.025
    output_for_GEMMES.loc[['2030_2035','2035_2040','2040_2045','2045_2050'],'reducXrO'] = 0.055 # comment this line for the baseline scenario, in which there is no energy transition
    
    # Play with iwst, v1 and iota0 to create a shock in interest rates
    output_for_GEMMES['iwst'] = 0.023175727
    # output_for_GEMMES.loc[['2025_2030','2030_2035','2035_2040','2040_2045','2045_2050'],'iwst'] += 0.01 # shock on foreign interest rate
    output_for_GEMMES['v1'] = 0.008543549
    # output_for_GEMMES.loc[['2025_2030','2030_2035','2035_2040','2040_2045','2045_2050'],'v1'] *= 1.2 # reaction of international markets in terms of risk perception of Colombia's government bonds 
    output_for_GEMMES['iota0'] = 0.04852755
    # output_for_GEMMES.loc[['2025_2030','2030_2035','2035_2040','2040_2045','2045_2050'],'iota0'] += 0.01 # shock on domestic interest rate
    output_for_GEMMES = output_for_GEMMES.round(3)
    aggregated_costs = output_for_GEMMES.copy()
    aggregated_costs = aggregated_costs[['capex_F_CO', 'capex_F_M', 'capex_B_CO', 'capex_B_M', 'capex_G_CO', 'capex_G_M', 'capex_H_CO', 'capex_H_M', 'opex_F_CO', 'opex_F_M', 'opex_B_CO','opex_B_M', 'opex_G_CO', 'opex_G_M', 'opex_H_CO', 'opex_H_M', 'exports_CO', 'CTf', 'CTb', 'CTg', 'CTh']]
    # aggregated_costs.to_csv('Energy_system_costs_aggregated.csv') # This file is not used in the coupling with GEMMES. However, it provides easier to read information to analyse the costs of the energy system.
    output_for_GEMMES.drop(columns=['capex_F_CO', 'capex_F_M', 'ikefCO', 'ikefM'], inplace=True)
    output_for_GEMMES.drop(columns=['capex_B_CO', 'capex_B_M', 'ikebCO', 'ikebM'], inplace=True)
    output_for_GEMMES.drop(columns=['capex_G_CO', 'capex_G_M', 'ikegCO', 'ikegM'], inplace=True)
    output_for_GEMMES.drop(columns=['capex_H_CO', 'capex_H_M', 'ikehCO', 'ikehM'], inplace=True)
    output_for_GEMMES.drop(columns=['opex_F_CO', 'opex_F_M', 'opex_B_CO','opex_B_M', 'opex_G_CO', 'opex_G_M', 'opex_H_CO', 'opex_H_M', 'exports_CO'], inplace=True)
    output_for_GEMMES.to_csv('Energy_system_costs.csv')   
    
def EnergyScope_output_csv(EnergyScope_output_file, ampl_0):
    ampl_graph = AmplGraph(EnergyScope_output_file, ampl_0, case_study)
    z_Results = ampl_graph.ampl_collector
    z_Results['Resources'].to_csv(os.path.join(EnergyScope_case_study_path,'Resources.csv'))
    z_Results['New_old_decom'].to_csv(os.path.join(EnergyScope_case_study_path,'Assets.csv'))
    z_Results['Assets'].to_csv(os.path.join(EnergyScope_case_study_path,'Assets.csv'))
    z_Results['Cost_breakdown'].to_csv(os.path.join(EnergyScope_case_study_path,'Cost_breakdown.csv'))
    z_Results['Cost_breakdown_non_annualised'].to_csv(os.path.join(EnergyScope_case_study_path,'Cost_breakdown_non_annualised.csv'))
    z_Results['Year_balance'].to_csv(os.path.join(EnergyScope_case_study_path,'Year_balance.csv'))
    z_Results['Gwp_breakdown'].to_csv(os.path.join(EnergyScope_case_study_path,'Gwp_breakdown.csv'))


def plot_GEMMES_outputs(variables_GEMMES):
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['yedot']/variables_GEMMES['ye'], label='a - Real GDP growth rate')
    plt.legend(loc='lower right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/a - Real GDP growth rate.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], (variables_GEMMES['x']-variables_GEMMES['im'])/variables_GEMMES['gdp'], label='b - Trade Balance (% gdp)')
    plt.legend(loc='lower right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/b - Trade Balance (% GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['en'], label='c - Nominal Exchange rate')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/c - Nominal Exchange rate.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], 10*variables_GEMMES['p'].pct_change(), label='d - Producer inflation rate (%)')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/d - Producer inflation rate (%).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], 10*variables_GEMMES['pc'].pct_change(), label='e - Consumer inflation rate (%)')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/e - Consumer inflation rate (%).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['Con']/(variables_GEMMES['pc']*variables_GEMMES['gdp']), label='f - Consumption as a share of real GDP')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/f - Consumption as a share of real GDP.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['Ik']/(variables_GEMMES['pk']*variables_GEMMES['gdp']), label='g - Investment as a share of real GDP')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/g - Investment as a share of real GDP.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['unem'], label='h - Unemployment rate(%)')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/h - Unemployment rate(%).png'), format='png')
    plt.figure()

    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['FD']/variables_GEMMES['GDP'], label='i - Fiscal deficit (%GDP)')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/i - Fiscal deficit (%GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], ( variables_GEMMES['Bg']+(variables_GEMMES['Bgfx']+variables_GEMMES['Lgfx']+variables_GEMMES['Lgfxtr'])*variables_GEMMES['en'] ) / variables_GEMMES['GDP'], label='j - Government total debt (% GDP)')
    plt.legend(loc='lower left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/j - Government total debt (% GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['IA']/variables_GEMMES['GDP'], label='k - Income Account of the Current Account (%GDP)')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/k - Current Account (%GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], -( variables_GEMMES['Rfxbdesdot']+variables_GEMMES['Dfxwdot']-(variables_GEMMES['FDI']/variables_GEMMES['en']+variables_GEMMES['Bgfxdot']+variables_GEMMES['Lgfxdot']+variables_GEMMES['Lfxfwdot']+variables_GEMMES['Lfxbwdot']+variables_GEMMES['Bgwdot']/variables_GEMMES['en']-variables_GEMMES['Rfxcbdot']) ) / variables_GEMMES['GDP'], label='l - Financial Account (%GDP)')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/l - Financial Account (%GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], (variables_GEMMES['Ldf']+(variables_GEMMES['Lfxfb']+variables_GEMMES['Lfxfw'])*variables_GEMMES['en'])/variables_GEMMES['GDP'], label='m - NFCs total debt (%GDP)')
    plt.legend(loc='lower right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/m - NFCs total debt (%GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['Rfx']*variables_GEMMES['en']/variables_GEMMES['GDP'], label='n - FX reserves (%GDP)')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/n - FX reserves (%GDP).png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['rsk'], label='o - Country risk')
    plt.legend(loc='lower right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/o - Country risk.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['ibgfx'], label='p - Government FX bond rate')
    plt.legend(loc='lower right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/p - Government FX bond rate.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['er'], label='q - Real exchange rate')
    plt.legend(loc='lower right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/q - Real exchange rate.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['GDP']/(variables_GEMMES['pop']*variables_GEMMES['en']*variables_GEMMES['pw']), label='r - Per Capita Income in USD')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.savefig(os.path.join(EnergyScope_case_study_path,'graphs_GEMMES/r - Per Capita Income in USD.png'), format='png')
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['GDP'], label='GDP')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.figure()
    
    plt.figure()
    # plt.plot(variables_GEMMES['time'], variables_GEMMES['X'], label='Exports')
    plt.plot(variables_GEMMES['time'], variables_GEMMES['xrO']*variables_GEMMES['pO']*variables_GEMMES['en'], label='Fossil fuels exports')
    plt.plot(variables_GEMMES['time'], variables_GEMMES['xef']*variables_GEMMES['pef']*variables_GEMMES['en'], label='Renewable energy carriers exports')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.figure()
    
    plt.figure()
    plt.plot(variables_GEMMES['time'], variables_GEMMES['xrO'], label='xrO')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.figure()
    


import os, sys
from os import system
from pathlib import Path
import webbrowser
import time
import multiprocessing as mp
import pickle as pkl
import pandas as pd
import numpy as np
import amplpy as apy
from collections import namedtuple
import cppimport
import time
import matplotlib.pyplot as plt

## Add the relevant paths to be able to access all necessary python codes
curr_dir = Path(os.path.dirname(__file__))
pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))

# Add path to GEMMES codes
GEMMES_path = os.path.abspath(os.path.join(Path(__file__).parents[3], 'ColombiaEnergyScope'))
Cpp_path = os.path.join(GEMMES_path, 'SourceCode/cppCode')
sys.path.insert(0, pymodPath)
sys.path.insert(0, Cpp_path)
sys.path.insert(0, Cpp_path + "/run")

# Add path to EnergyScope codes
ESMY_path = os.path.join(curr_dir.parent,'ESMY')
EnergyScope_model_path = os.path.join(ESMY_path,'STEP_2_Pathway_Model')

# Load packages to be able to manipulate AMPL objects in python
from solve_GEMMES import solveGEMMES
from ampl_object import AmplObject
from ampl_preprocessor import AmplPreProcessor
from ampl_collector import AmplCollector
from ampl_graph import AmplGraph

## Read the GEMMES model
cppimport.settings['force_rebuild'] = True
solvePy = cppimport.imp('functionsForPy')

## Read the EnergyScope model and data files
if EnergyScope_granularity == 'MO':
    mod_1_path = [os.path.join(EnergyScope_model_path,'PESMO_model.mod'),
                os.path.join(EnergyScope_model_path,'PESMO_store_variables.mod'),
                os.path.join(EnergyScope_model_path,'PES_store_variables.mod')]
    mod_2_path = [os.path.join(EnergyScope_model_path,'fix.mod')]
    dat_path = [os.path.join(EnergyScope_model_path,country+'/PESMO_data_all_years.dat')] 
else:
    mod_1_path = [os.path.join(EnergyScope_model_path,'PESTD_model.mod'),
            os.path.join(EnergyScope_model_path,'PESTD_store_variables.mod'),
            os.path.join(EnergyScope_model_path,'PES_store_variables.mod')]
    mod_2_path = [os.path.join(EnergyScope_model_path,'fix.mod')]
    dat_path = [os.path.join(EnergyScope_model_path,country+'/PESTD_data_all_years.dat'),
                os.path.join(EnergyScope_model_path,country+'/PESTD_{}TD.dat'.format(nbr_tds))]

dat_path += [os.path.join(EnergyScope_model_path,'PES_data_all_years.dat'),
             os.path.join(EnergyScope_model_path,'PES_seq_opti.dat'),
             os.path.join(EnergyScope_model_path,country+'/PES_data_efficiencies.dat'),
             os.path.join(EnergyScope_model_path,country+'/PES_data_year_related.dat'),
             os.path.join(EnergyScope_model_path,'PES_data_set_AGE_2020.dat')]

dat_path_0 = dat_path + [os.path.join(EnergyScope_model_path,'PES_data_remaining.dat'),
             os.path.join(EnergyScope_model_path,'PES_data_decom_allowed_2020.dat')]

dat_path += [os.path.join(EnergyScope_model_path,'PES_data_remaining_wnd.dat'),
             os.path.join(EnergyScope_model_path,'PES_data_decom_allowed_2020.dat')]
    

## Name the EnergyScope output files
if(EnergyScope_granularity=='MO'):
    case_study = country+' - MO'
    expl_text  = country+' - monthly granularity'
else:
    case_study = country+' - TD'
    expl_text  = country+' - hourly granularity'

EnergyScope_output_path = os.path.join(curr_dir.parent,'out')
EnergyScope_case_study_path = os.path.join(EnergyScope_output_path,case_study)


## Options for ampl and gurobi (optimization within EnergyScope)
gurobi_options = ['predual=-1',
                'method = 2', # 2 is for barrier method
                'crossover=0',
                'prepasses = 3',
                'barconvtol=1e-6',
                'presolve=-1'] # Not a good idea to put it to 0 if the model is too big

gurobi_options_str = ' '.join(gurobi_options)

ampl_options = {'show_stats': 1,
                'log_file': os.path.join(EnergyScope_model_path,'log.txt'),
                'presolve': 10,
                'presolve_eps': 1e-6,
                'presolve_fixeps': 1e-6,
                'show_boundtol': 0,
                'gurobi_options': gurobi_options_str,
                '_log_input_only': False}
    
if __name__ == '__main__':
    main()
    
    
    
