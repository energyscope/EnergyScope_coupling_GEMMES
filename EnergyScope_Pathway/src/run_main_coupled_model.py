# -*- coding: utf-8 -*-
"""
May 2024

@authors: Xavier Rixhon, Pierre Jacques, Stanislas Augier
"""

def main():
    plot_EnergyScope = False  
    csv_EnergyScope  = False
    output_GEMMES = run_GEMMES()
    gdp_current = output_GEMMES['gdp']
    diff = np.linalg.norm(gdp_current)
    n_iter = 0
    while(diff > 1e-1):
        gdp_previous = gdp_current
        n_iter += 1
        output_EnergyScope = run_EnergyScope(output_GEMMES)
        plot_EnergyScope_outputs(output_EnergyScope[0], output_EnergyScope[1]) #############################
        write_EnergyScope_outputs(output_EnergyScope[0], output_EnergyScope[1], output_GEMMES)
        output_GEMMES = run_GEMMES()
        gdp_current = output_GEMMES['gdp']
        diff = np.linalg.norm(gdp_current-gdp_previous) 
    time.sleep(1)
    print('Number of iterations before convergence between the two models: ', n_iter)
    
    if plot_EnergyScope:
        plot_EnergyScope_outputs(output_EnergyScope[0], output_EnergyScope[1])
    if csv_EnergyScope:
        EnergyScope_output_csv(output_EnergyScope[0], output_EnergyScope[1])

    plt.figure()
    plt.plot(output_GEMMES['time'], output_GEMMES['gdp'], label='gdp')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.figure()
    plt.plot(output_GEMMES['time'], output_GEMMES['p'], label='p')
    plt.legend(loc='upper left', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)
    plt.figure()
    plt.plot(output_GEMMES['time'], output_GEMMES['ip'], label='ip')
    plt.legend(loc='upper right', fancybox=True, shadow=True)
    plt.grid(True, color="#93a1a1", alpha=0.3)

            
def run_GEMMES():
    ## Change parameters values in GEMMES according to scenario definition
    # Build default parms vector in python importing data from C++
    parmsNames = solvePy.parmsNames()
    # Declare a structure that stores parameters values and their names
    namedParms = namedtuple("namedParms", parmsNames)
    # build named parms vector using the parmsNamed structure and loading parms values from C++
    newParms = namedParms(*solvePy.parms())
    newParms = newParms._replace(sigmaxnpNew=1.2)
    newParms = newParms._replace(kappa03=0.03526333*1.05)
    newParms = newParms._replace(tauf=0.1859935*1.02)
    newParms = newParms._replace(taub=0.1222547*1.02)
    newParms = newParms._replace(tauw=0.08986282*1.02)
    newParms = newParms._replace(tauvat=0.1089564*1.02)
    newParms = newParms._replace(fi3=0.45)
    newParms = newParms._replace(sigmaxnSpeed=0.48)
    newParms = newParms._replace(reducXrO=0)
    
    ## Fix the trajectories of exogenous variables
    Costs_ES_per_phase = pd.read_csv('Energy_system_costs.csv')
    Costs_ES_per_phase.drop(columns=['Phases'], inplace=True)

    Costs_ES_per_year = pd.DataFrame(np.repeat(Costs_ES_per_phase.values, 5, axis=0))
    Costs_ES_per_year = Costs_ES_per_year.loc[2:,:]
    Costs_ES_per_year.reset_index(drop=True, inplace=True)

    Thetas = pd.read_csv('Thetas.csv')
    Thetas.drop(columns=['Unnamed: 0'], inplace=True)

    samplesExogVar = pd.concat([Costs_ES_per_year,Thetas], axis=1)
    samplesExogVar.columns = np.arange(len(samplesExogVar.columns))

    ## Run the GEMMES model
    output_GEMMES = solveGEMMES(solvePy=solvePy, samplesExogVar=samplesExogVar, parms=newParms, solver="dopri", atol=1e-4, rtol=0, fac=0.85, facMin=0.1, facMax=4, nStepMax=300, hInit=0.025, hMin=0.025/100, hMax=0.2)
    output_GEMMES.index = output_GEMMES.index.round(1)

    ## Save the projection for EUDs for EnergyScope
    df_EUD = pd.read_csv('EUD_template.csv')
    share_elec_cst_H = 0.66
    share_elec_cst_S = 0.57
    share_elec_cst_F = 0.76
    list_years = [2021,2026,2031,2036,2041,2046,2051]
    list_EUDs = [df_EUD.copy()] * 7
    for i in range(7):
        list_EUDs[i] = df_EUD.copy()
        list_EUDs[i].set_index('parameter_name', inplace=True)
        output_GEMMES_i = output_GEMMES.loc[(output_GEMMES.index>=list_years[i]) & (output_GEMMES.index<list_years[i]+1)].mean()
        list_EUDs[i].loc[['ELECTRICITY', 'ELECTRICITY_VAR', 'HEAT_LOW_T_SH', 'HEAT_LOW_T_HW', 'SPACE_COOLING'], 'HOUSEHOLDS'] = [output_GEMMES_i['El_H']*share_elec_cst_H, output_GEMMES_i['El_H']*(1-share_elec_cst_H), output_GEMMES_i['HLTSH_H'], output_GEMMES_i['HLTHW_H'], output_GEMMES_i['SC_H']]
        list_EUDs[i].loc[['ELECTRICITY', 'ELECTRICITY_VAR', 'HEAT_LOW_T_SH', 'SPACE_COOLING'], 'SERVICES'] = [(output_GEMMES_i['El_B']+output_GEMMES_i['El_G'])*share_elec_cst_S, (output_GEMMES_i['El_B']+output_GEMMES_i['El_G'])*(1-share_elec_cst_S), output_GEMMES_i['HLTSH_B']+output_GEMMES_i['HLTSH_G'], output_GEMMES_i['SC_B']+output_GEMMES_i['SC_G']]
        list_EUDs[i].loc[['ELECTRICITY', 'ELECTRICITY_VAR', 'HEAT_HIGH_T', 'HEAT_LOW_T_SH', 'HEAT_LOW_T_HW', 'PROCESS_COOLING', 'NON_ENERGY'], 'INDUSTRY']  = [output_GEMMES_i['El_F']*share_elec_cst_F, output_GEMMES_i['El_F']*(1-share_elec_cst_F), output_GEMMES_i['HHT_F'], output_GEMMES_i['HLTSH_F'], output_GEMMES_i['HLTHW_F'], output_GEMMES_i['PC_F'], output_GEMMES_i['NE_F']]
        list_EUDs[i].loc[['MOBILITY_PASSENGER', 'MOBILITY_FREIGHT'], 'TRANSPORTATION'] = [output_GEMMES_i['MP_H'], output_GEMMES_i['MF_F']]
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
    output_GEMMES['LTH_tot'] = output_GEMMES['HLTHW_F'] + output_GEMMES['HLTSH_F'] + output_GEMMES['HLTSH_B'] + output_GEMMES['HLTSH_G'] + output_GEMMES['HLTHW_H'] + output_GEMMES['HLTSH_H']
    output_GEMMES['SC_tot'] = output_GEMMES['SC_B'] + output_GEMMES['SC_G'] + output_GEMMES['SC_H']
    list_phases = ['2019_2021','2021_2026','2026_2031','2031_2036','2036_2041','2041_2046','2046_2051']
    list_output_GEMMES = [output_GEMMES.loc[output_GEMMES.index<2021].mean()]
    for i in range(6):
        list_output_GEMMES.append(output_GEMMES.loc[(output_GEMMES.index>=list_years[i]) & (output_GEMMES.index<list_years[i+1])].mean())
    shares_LTH = pd.DataFrame(index=list_phases, columns=['F','B','G','H'])
    shares_cooling = pd.DataFrame(index=list_phases, columns=['B','G','H'])
    i_rate = pd.DataFrame(index=list_phases, columns=['i_rate'])
    for i in range(7):
        shares_LTH.loc[list_phases[i],'F'] = round((list_output_GEMMES[i].loc['HLTSH_F'] + list_output_GEMMES[i].loc['HLTHW_F']) / list_output_GEMMES[i].loc['LTH_tot'], 3)
        shares_LTH.loc[list_phases[i],'B'] = round(list_output_GEMMES[i].loc['HLTSH_B'] / list_output_GEMMES[i].loc['LTH_tot'], 3)
        shares_LTH.loc[list_phases[i],'G'] = round(list_output_GEMMES[i].loc['HLTSH_G'] / list_output_GEMMES[i].loc['LTH_tot'], 3)
        shares_LTH.loc[list_phases[i],'H'] = round((list_output_GEMMES[i].loc['HLTSH_H'] + list_output_GEMMES[i].loc['HLTHW_H']) / list_output_GEMMES[i].loc['LTH_tot'], 3)
        shares_cooling.loc[list_phases[i],'B'] = round(list_output_GEMMES[i].loc['SC_B'] / list_output_GEMMES[i].loc['SC_tot'], 3)
        shares_cooling.loc[list_phases[i],'G'] = round(list_output_GEMMES[i].loc['SC_G'] / list_output_GEMMES[i].loc['SC_tot'], 3)
        shares_cooling.loc[list_phases[i],'H'] = round(list_output_GEMMES[i].loc['SC_H'] / list_output_GEMMES[i].loc['SC_tot'], 3)
        i_rate.loc[list_phases[i],'i_rate'] = round(list_output_GEMMES[i].loc['ip'] - list_output_GEMMES[i].loc['pDot'] / list_output_GEMMES[i].loc['p'], 3)   
    shares_LTH.reset_index(inplace=True)
    shares_LTH.rename(columns={'index':'Phase'}, inplace=True)
    shares_LTH.to_csv('shares_LTH.csv', index=False)
    shares_cooling.reset_index(inplace=True)
    shares_cooling.rename(columns={'index':'Phase'}, inplace=True)
    shares_cooling.to_csv('shares_cooling.csv', index=False)
    i_rate.reset_index(inplace=True)
    i_rate.rename(columns={'index':'Phase'}, inplace=True)
    i_rate.to_csv('i_rate.csv', index=False)

    return output_GEMMES
    
def run_EnergyScope(output_GEMMES):
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
    
    ## Read the input data from GEMMES
    i_rate = pd.read_csv('i_rate.csv')
    i_rate['i_rate'] = i_rate['i_rate'] * (i_rate['i_rate']>=0) 
    i_rate['i_rate'] += 1e-4
    i_rate.set_index('Phase', inplace=True)
    phases_ES = ['2015_2020', '2020_2025', '2025_2030', '2030_2035', '2035_2040', '2040_2045', '2045_2050']
    for j in range(len(phases_ES)):
        ampl.set_params('i_rate',{(phases_ES[j]):i_rate.iloc[j,0]})
    EUD_2021 = pd.read_csv('EUD_2021.csv')
    EUD_2026 = pd.read_csv('EUD_2026.csv')
    EUD_2031 = pd.read_csv('EUD_2031.csv')
    EUD_2036 = pd.read_csv('EUD_2036.csv')
    EUD_2041 = pd.read_csv('EUD_2041.csv')
    EUD_2046 = pd.read_csv('EUD_2046.csv')
    EUD_2051 = pd.read_csv('EUD_2051.csv')
    EUD_2015 = EUD_2021.copy()
    EUD_dict = {0:EUD_2015, 1:EUD_2021, 2:EUD_2026, 3:EUD_2031, 4:EUD_2036, 5:EUD_2041, 6:EUD_2046, 7:EUD_2051}
    year_list = ['YEAR_2015', 'YEAR_2020', 'YEAR_2025', 'YEAR_2030', 'YEAR_2035', 'YEAR_2040', 'YEAR_2045', 'YEAR_2050']                  
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
    # print(ampl.get_param('end_uses_demand_year'))
    
    c_inv_ampl = ampl.get_param('c_inv').to_list()
    c_inv_ampl = pd.DataFrame(c_inv_ampl, columns=['Year', 'Technologies', 'Value'])
    Technos_local_fraction = pd.read_csv('Technos_information.csv')
    Technos_local_fraction.drop(columns='Lifetime', inplace=True)
    c_inv_ampl = pd.merge(c_inv_ampl, Technos_local_fraction, on='Technologies', how='left')
    c_inv_ampl.fillna(0, inplace=True)
    en0 = 3.74424417 # k COP / USD 2021
    en_yearly = pd.DataFrame(index=year_list, columns=['en'])
    list_years = [2019,2021,2026,2031,2036,2041,2046,2051]
    for i in range(8):
        en_yearly.iloc[i,0] = output_GEMMES.loc[(output_GEMMES.index>=list_years[i]) & (output_GEMMES.index<list_years[i]+1), 'en'].mean()
    en_yearly = en_yearly / en_yearly.loc['YEAR_2020'] 
    en_yearly.reset_index(inplace=True)
    en_yearly.rename(columns={'index': 'Year'}, inplace=True)
    c_inv_ampl = pd.merge(c_inv_ampl, en_yearly, on='Year', how='left')
    c_inv_ampl['Value'] *= en0 # Convert constant USD to constant k COP
    c_inv_ampl['Value'] = ( c_inv_ampl['Value']*c_inv_ampl['Local'] + c_inv_ampl['Value']*c_inv_ampl['en']*(1-c_inv_ampl['Local']) ) # The imported fraction of goods is subject to exchange rate's fluctuations
    c_inv_ampl.drop(columns=['Local', 'en'], inplace=True)
    c_inv_ampl.set_index(['Year', 'Technologies'], inplace=True)
    c_inv_ampl = apy.DataFrame.from_pandas(c_inv_ampl)
    ampl.set_params('c_inv', c_inv_ampl)
    
    # We assume that all maintenance costs are local costs
    c_maint_ampl = ampl.get_param('c_maint').to_list()
    c_maint_ampl = pd.DataFrame(c_maint_ampl, columns=['Year', 'Technologies', 'Value'])
    c_maint_ampl['Value'] *= en0 # Convert constant USD to constant k COP
    c_maint_ampl.set_index(['Year', 'Technologies'], inplace=True)
    c_maint_ampl = apy.DataFrame.from_pandas(c_maint_ampl)
    ampl.set_params('c_maint', c_maint_ampl)
    
    c_op_ampl = ampl.get_param('c_op').to_list()
    c_op_ampl = pd.DataFrame(c_op_ampl, columns=['Year', 'Resources', 'Value'])
    Imported_resources = ['URANIUM', 'H2', 'ELECTRICITY', 'AMMONIA_RE', 'METHANOL_RE', 'IMPORTED_COAL', 'METHANOL', 'H2_RE', 'AMMONIA', 'ELEC_EXPORT', 'IMPORTED_GAS']
    c_op_ampl = pd.merge(c_op_ampl, en_yearly, on='Year', how='left')
    c_op_ampl['Value'] *= en0 # Convert constant USD to constant k COP
    c_op_ampl.loc[c_op_ampl['Resources'].isin(Imported_resources),'Value'] *= np.array(c_op_ampl.loc[c_op_ampl['Resources'].isin(Imported_resources),'en'].astype(float).values).round(4) # The imported resources are subject to exchange rate's fluctuations
    c_op_ampl.drop(columns=['en'], inplace=True)
    c_op_ampl.set_index(['Year', 'Resources'], inplace=True)
    c_op_ampl = apy.DataFrame.from_pandas(c_op_ampl)
    ampl.set_params('c_op', c_op_ampl)
    
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
    z_Results = ampl_graph.ampl_collector
    # z_Resources = z_Results['Resources'].copy()
    # z_Assets = z_Results['Assets'].copy()
    # z_Cost_breakdown = z_Results['Cost_breakdown'].copy()
    # z_Year_balance = z_Results['Year_balance'].copy()
    # z_gwp_breakdown = z_Results['Gwp_breakdown'].copy()
    
    # a_website = "https://www.google.com"
    # webbrowser.open_new(a_website)
    ampl_graph.graph_resource()
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
    # ampl_graph.graph_cost()

def write_EnergyScope_outputs(EnergyScope_output_file, ampl_0, output_GEMMES):
    ampl_graph = AmplGraph(EnergyScope_output_file, ampl_0, case_study)
    z_Results = ampl_graph.ampl_collector
    
    C_inv = z_Results['C_inv_phase_tech_non_annualised'].copy()
    C_inv.rename(columns = {'C_inv_phase_tech_non_annualised':'Value'}, inplace = True)
    
    New_old_decom = z_Results['New_old_decom'].copy()
    New_old_decom = New_old_decom
    New_old_decom.fillna(0, inplace=True)
    C_inv['Capa'] = New_old_decom['F_new']
    C_inv.drop(['DAM_STORAGE','BEV_BATT','EFFICIENCY'], level='Technologies', inplace=True)
    
    Technos_local_fraction = pd.read_csv('Technos_information.csv')
    Technos_local_fraction.drop(columns='Lifetime', inplace=True)
    C_inv.reset_index(inplace=True)
    C_inv = pd.merge(C_inv, Technos_local_fraction, on='Technologies')
    C_inv.set_index(['Phases','Technologies'], inplace=True)
    C_inv.sort_values(['Phases','Technologies'], axis=0, inplace=True)
    C_inv['Imported'] = 1 - C_inv['Local']
    C_inv[['F','B','G','H']] = [1,0,0,0]
    
    # C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DHN','GRID','HVAC_LINE']),[3,5]] = [0,1] # These costs supported by the PRIVATE SECTOR, actually (not by the state - grid costs for households are quite volatile, according to DNP)
    
    list_private_mob_tech = ['MOTORCYCLE','CAR_GASOLINE','CAR_DIESEL','CAR_NG','CAR_METHANOL','CAR_HEV','CAR_PHEV','MOTORCYCLE_ELECTRIC','CAR_BEV','CAR_FUEL_CELL']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_private_mob_tech),[4,7]] = [0,1] # Private mobility costs are supported by households
    
    list_public_mob_tech = ['TRAMWAY_TROLLEY','BUS_COACH_DIESEL','BUS_COACH_GASOLINE','BUS_COACH_HYDIESEL','BUS_COACH_CNG_STOICH','BUS_COACH_FC_HYBRIDH2','TRAIN_PUB']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_public_mob_tech),[4,6]] = [0,1] # Public mobility costs are supported by the State
    
    shares_cooling = pd.read_csv('shares_cooling.csv')
    shares_cooling.set_index('Phase',inplace=True)
    list_cooling_tech = ['DEC_ELEC_COLD','DEC_THHP_GAS_COLD']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_cooling_tech),4] = 0
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_ELEC_COLD']),[5,6,7]] = shares_cooling.values
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_THHP_GAS_COLD']),[5,6,7]] = shares_cooling.values
    
    C_inv['merge_index'] = C_inv.index.get_level_values('Phases')
    shares_LTH = pd.read_csv('shares_LTH.csv')
    shares_LTH.set_index('Phase',inplace=True)
    shares_LTH['merge_index'] = C_inv['merge_index'].unique()
    C_inv_bis = pd.merge(C_inv, shares_LTH, on='merge_index')
    C_inv_bis.index = C_inv.index
    list_LTH_tech = ['DHN_HP_ELEC','DHN_COGEN_GAS','DHN_COGEN_WOOD','DHN_COGEN_WASTE','DHN_COGEN_WET_BIOMASS','DHN_COGEN_BIO_HYDROLYSIS','DHN_BOILER_GAS','DHN_BOILER_WOOD','DHN_BOILER_OIL','DHN_DEEP_GEO','DHN_SOLAR','DEC_HP_ELEC','DEC_THHP_GAS','DEC_COGEN_GAS','DEC_COGEN_OIL','DEC_ADVCOGEN_GAS','DEC_ADVCOGEN_H2','DEC_BOILER_GAS','DEC_BOILER_WOOD','COAL_STOVE','DEC_BOILER_OIL','DEC_SOLAR','DEC_DIRECT_ELEC']
    C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_LTH_tech),[4,5,6,7]] = C_inv_bis.iloc[C_inv_bis.index.get_level_values('Technologies').isin(list_LTH_tech),[9,10,11,12]].values
    C_inv.drop(columns=['merge_index'],inplace=True)
    
    # Transform C_inv into capital investments, prices and import propensities for each economic sector in GEMMES
    output_for_GEMMES = pd.DataFrame(index=C_inv.index.get_level_values(0).unique())
    output_for_GEMMES['capex_F_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_F_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_B_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_B_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_G_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_G_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_H_CO'] = (C_inv['Value'] * C_inv['Local']    * C_inv['H']).groupby(level=[0]).sum()
    output_for_GEMMES['capex_H_M']  = (C_inv['Value'] * C_inv['Imported'] * C_inv['H']).groupby(level=[0]).sum()    
    
    C_maint = z_Results['C_op_phase_tech_non_annualised']
    C_maint.rename(columns = {'C_op_phase_tech_non_annualised':'Value'}, inplace = True)
    C_maint['Local'] = 1
    C_maint['Imported'] = 1 - C_maint['Local']
    C_maint.drop(['NUCLEAR','DAM_STORAGE','BEV_BATT','EFFICIENCY'], level='Technologies', inplace=True)
    C_maint[['F','B','G','H']] = C_inv.iloc[~C_inv.index.get_level_values('Phases').isin(['2015_2020']),[4,5,6,7]].values        
    
    # C_op is annualised - we need to get a non-annualised version of it
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
    Local_resources = ['GASOLINE','DIESEL','BIOETHANOL','BIODIESEL','LFO','LOCAL_GAS','WOOD','LOCAL_COAL','CO2_EMISSIONS','CO2_CAPTURED','CO2_INDUSTRY','RES_WIND','RES_SOLAR','RES_HYDRO','CO2_ATM','WET_BIOMASS','WASTE','RES_GEO']
    C_op.iloc[C_op.index.get_level_values('Resources').isin(Local_resources),1] = 1
    C_op['Imported'] = 1 - C_op['Local']
    C_op[['F','B','G','H']] = [1,0,0,0]
    
    output_for_GEMMES['opex_F_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['F']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['F']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_F_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['F']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['F']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_B_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['B']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['B']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_B_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['B']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['B']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_G_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['G']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['G']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_G_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['G']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['G']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_H_CO'] = (C_maint['Value'] * C_maint['Local'] * C_maint['H']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['H']).groupby(level=[0]).sum()
    output_for_GEMMES['opex_H_M']  = (C_maint['Value'] * C_maint['Imported'] * C_maint['H']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['H']).groupby(level=[0]).sum()


    # Reconstruct the costs for the first phase based on YEAR_2020 data
    Cost_breakdown_non_annualised = z_Results['Cost_breakdown_non_annualised']
    Cost_breakdown_non_annualised = Cost_breakdown_non_annualised[Cost_breakdown_non_annualised.index.get_level_values('Years').isin(['YEAR_2020'])]
    Cost_breakdown_non_annualised.rename(columns={'C_maint':'C_maint_CO'}, inplace=True)
    Cost_breakdown_non_annualised['C_maint_M'] = 0
    Cost_breakdown_non_annualised_bis = Cost_breakdown_non_annualised.copy()
    Cost_breakdown_non_annualised_bis['Local'] = 0
    Cost_breakdown_non_annualised_bis.iloc[Cost_breakdown_non_annualised_bis.index.get_level_values('Elements').isin(Local_resources),4] = 1
    Cost_breakdown_non_annualised_bis['Imported'] = 1 - Cost_breakdown_non_annualised_bis['Local']
    Cost_breakdown_non_annualised_bis['C_op_CO'] = Cost_breakdown_non_annualised_bis['C_op'] * Cost_breakdown_non_annualised_bis['Local']
    Cost_breakdown_non_annualised_bis['C_op_M'] = Cost_breakdown_non_annualised_bis['C_op'] * Cost_breakdown_non_annualised_bis['Imported']
    Cost_breakdown_non_annualised_bis = Cost_breakdown_non_annualised_bis.sum()
    Cost_breakdown_non_annualised_bis.drop(index=['C_inv','C_maint_CO','C_maint_M','C_op','Local','Imported'], inplace=True)
    Technos_lifetime = pd.read_csv('Technos_information.csv')
    Technos_lifetime.rename(columns={'Technologies':'Elements'}, inplace=True)
    Cost_breakdown_non_annualised = pd.merge(Cost_breakdown_non_annualised, Technos_lifetime, on='Elements')
    Cost_breakdown_non_annualised['C_inv_per_year'] = Cost_breakdown_non_annualised['C_inv'] / Cost_breakdown_non_annualised['Lifetime']
    Cost_breakdown_non_annualised.set_index('Elements', inplace=True)
    Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.sum()
    Cost_breakdown_non_annualised.drop(index=['C_inv','C_op','Local','Lifetime'], inplace=True)
    Cost_breakdown_non_annualised = pd.concat([Cost_breakdown_non_annualised, Cost_breakdown_non_annualised_bis])
    Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.round(1)
    # Cost_breakdown_non_annualised.to_csv('Enegy_system_cost_2021.csv')  

    output_for_GEMMES.iloc[0,0:8] = Cost_breakdown_non_annualised['C_inv_per_year'] * output_for_GEMMES.iloc[0,0:8] / output_for_GEMMES.iloc[0,0:8].sum() * 5 # We multiply the yearly investment by the number of years in the phase
    output_for_GEMMES.loc['2015_2020',['opex_F_CO','opex_B_CO','opex_G_CO','opex_H_CO']] = Cost_breakdown_non_annualised[['C_maint_CO', 'C_op_CO']].sum() * output_for_GEMMES.loc['2020_2025',['opex_F_CO','opex_B_CO','opex_G_CO','opex_H_CO']] / output_for_GEMMES.loc['2020_2025',['opex_F_CO','opex_B_CO','opex_G_CO','opex_H_CO']].sum() * 5
    output_for_GEMMES.loc['2015_2020',['opex_F_M','opex_B_M','opex_G_M','opex_H_M']] = Cost_breakdown_non_annualised[['C_maint_M', 'C_op_M']].sum() * output_for_GEMMES.loc['2020_2025',['opex_F_M','opex_B_M','opex_G_M','opex_H_M']] / output_for_GEMMES.loc['2020_2025',['opex_F_M','opex_B_M','opex_G_M','opex_H_M']].sum() * 5
    
    output_GEMMES_2021 = output_GEMMES.loc[(output_GEMMES.index>=2021) & (output_GEMMES.index<2022)].mean()
    
    Real_energy_system_cost_2021 = 33.323773083 # billion 2021 COP, according to DNP
    corrective_factor = Real_energy_system_cost_2021 / ( output_GEMMES_2021['p'] * output_for_GEMMES.loc['2015_2020'].sum() ) # The corrective factor also allows to transform the phase costs into yearly costs (division by 5 included in the factor)
    
    
    ### Add to C_op the money paid by B,G,H to F for buying the fuels and electricity
    
    year_balance = z_Results['Year_balance'].copy()
    
    year_balance[['F','B','G','H']] = [1,0,0,0]
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_private_mob_tech),['F','H']] = [0,1]
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_public_mob_tech),['F','G']] = [0,1]
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_cooling_tech),['F']] = 0
    if('DEC_ELEC_COLD' in year_balance.index.get_level_values('Elements')):
        year_balance.loc[year_balance.index.get_level_values('Elements').isin(['DEC_ELEC_COLD']),['B','G','H']] = shares_cooling.values
    if('DEC_THHP_GAS_COLD' in year_balance.index.get_level_values('Elements')):
        year_balance.loc[year_balance.index.get_level_values('Elements').isin(['DEC_THHP_GAS_COLD']),['B','G','H']] = shares_cooling.iloc[1:,:].values
    
    year_balance['merge_index_2'] = year_balance.index.get_level_values('Years')
    shares_LTH['merge_index_2'] = year_balance['merge_index_2'].unique()
    year_balance_bis = pd.merge(year_balance, shares_LTH, on='merge_index_2')
    year_balance_bis.index = year_balance.index
    year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_LTH_tech),['F','B','G','H']] = year_balance_bis.loc[year_balance_bis.index.get_level_values('Elements').isin(list_LTH_tech),['F_y','B_y','G_y','H_y']].values
    
    year_balance = year_balance[year_balance['F']<0.999]
    year_balance = year_balance.loc[:, year_balance.columns.isin(['ELECTRICITY','LOCAL_GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE','H2','METHANOL','B','G','H'])]
    year_balance.loc[year_balance['ELECTRICITY']>0,'ELECTRICITY'] = np.nan
    year_balance = year_balance.abs()
    year_balance.drop(columns=['H2','METHANOL'], inplace=True) #### Negligible amount
    
    
    # Reconstruct prices of resources
    
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
    
    # Construct a price for locally produced electricity
    technos_res_elec = ['CCGT','IMPORTED_COAL_CENTRAL','LOCAL_COAL_CENTRAL','PV','WIND_ONSHORE','WIND_OFFSHORE','HYDRO_DAM','HYDRO_RIVER','GEOTHERMAL','GRID','HVAC_LINE','IMPORTED_GAS','LOCAL_GAS','IMPORTED_COAL','LOCAL_COAL']
    Cost_elec_approx = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(technos_res_elec)]
    year_balance_elec = z_Results['Year_balance'].copy()
    year_balance_elec = year_balance_elec[['IMPORTED_COAL','LOCAL_COAL','LOCAL_GAS','ELECTRICITY']]
    Cost_elec_approx['perc_for_elec'] = np.nan
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
    
      
    # Compute the cost of each resource use for each techno    
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
    year_balance_shift = year_balance.copy()
    year_balance_shift = year_balance_shift.shift(1)
    # Go from yearly costs to phase costs
    year_balance_2021 = year_balance.iloc[0]
    year_balance = (year_balance + year_balance_shift) / 2 
    year_balance.loc['YEAR_2020'] = year_balance_2021
    year_balance['B % C_op'] = year_balance['cost_B'] / year_balance['C_op_tot']
    year_balance['G % C_op'] = year_balance['cost_G'] / year_balance['C_op_tot']
    year_balance['H % C_op'] = year_balance['cost_H'] / year_balance['C_op_tot']
    
    C_op_to_add = C_op['Value'].groupby(level=[0]).sum().to_frame()
    C_op_to_add_2015_2020 = C_op_to_add.loc['2020_2025'].to_frame().transpose()
    C_op_to_add_2015_2020.rename(index={'2020_2025':'2015_2020'}, inplace=True)
    C_op_to_add = pd.concat([C_op_to_add_2015_2020, C_op_to_add])
    C_op_to_add['B'] = year_balance['B % C_op'].values * C_op_to_add['Value'].values
    C_op_to_add['G'] = year_balance['G % C_op'].values * C_op_to_add['Value'].values
    C_op_to_add['H'] = year_balance['H % C_op'].values * C_op_to_add['Value'].values
    
    # Add to C_op the money paid by B,G,H to F for buying the fuels and electricity
    output_for_GEMMES['opex_B_CO'] += C_op_to_add['B']
    output_for_GEMMES['opex_G_CO'] += C_op_to_add['G']
    output_for_GEMMES['opex_H_CO'] += C_op_to_add['H']
    
    
    # Apply a corrective factor so that the total energy system cost fits the actual cost given by DNP
    output_for_GEMMES *= corrective_factor
    output_for_GEMMES['ikefCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['ikefM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['F']).groupby(level=[0]).sum()
    output_for_GEMMES['ikebCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['ikebM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['B']).groupby(level=[0]).sum()
    output_for_GEMMES['ikegCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['ikegM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['G']).groupby(level=[0]).sum()
    output_for_GEMMES['ikehCO'] = (C_inv['Capa'] * C_inv['Local']    * C_inv['H']).groupby(level=[0]).sum()
    output_for_GEMMES['ikehM']  = (C_inv['Capa'] * C_inv['Imported'] * C_inv['H']).groupby(level=[0]).sum()
    output_for_GEMMES['pkefCO'] = output_for_GEMMES['capex_F_CO'] / output_for_GEMMES['ikefCO']
    output_for_GEMMES['pkefM']  = output_for_GEMMES['capex_F_M']  / output_for_GEMMES['ikefM'] / (output_GEMMES_2021['pw'] * output_GEMMES_2021['en'])
    output_for_GEMMES['pkebCO'] = output_for_GEMMES['capex_B_CO'] / output_for_GEMMES['ikebCO']
    output_for_GEMMES['pkebM']  = output_for_GEMMES['capex_B_M']  / output_for_GEMMES['ikebM'] / (output_GEMMES_2021['pw'] * output_GEMMES_2021['en'])
    output_for_GEMMES['pkegCO'] = output_for_GEMMES['capex_G_CO'] / output_for_GEMMES['ikegCO']
    output_for_GEMMES['pkegM']  = output_for_GEMMES['capex_G_M']  / output_for_GEMMES['ikegM'] / (output_GEMMES_2021['pw'] * output_GEMMES_2021['en'])
    output_for_GEMMES['pkehCO'] = output_for_GEMMES['capex_H_CO'] / output_for_GEMMES['ikehCO']
    output_for_GEMMES['pkehM']  = output_for_GEMMES['capex_H_M']  / output_for_GEMMES['ikehM'] / (output_GEMMES_2021['pw'] * output_GEMMES_2021['en'])
    output_for_GEMMES['ikef'] = output_for_GEMMES['ikefCO'] + output_for_GEMMES['ikefM']
    output_for_GEMMES['ikeb'] = output_for_GEMMES['ikebCO'] + output_for_GEMMES['ikebM']
    output_for_GEMMES['ikeg'] = output_for_GEMMES['ikegCO'] + output_for_GEMMES['ikegM']
    output_for_GEMMES['ikeh'] = output_for_GEMMES['ikehCO'] + output_for_GEMMES['ikehM']
    output_for_GEMMES['sigmamkef'] = output_for_GEMMES['ikefM'] / output_for_GEMMES['ikef']
    output_for_GEMMES['sigmamkeb'] = output_for_GEMMES['ikebM'] / output_for_GEMMES['ikeb']
    output_for_GEMMES['sigmamkeg'] = output_for_GEMMES['ikegM'] / output_for_GEMMES['ikeg']
    output_for_GEMMES['sigmamkeh'] = output_for_GEMMES['ikehM'] / output_for_GEMMES['ikeh']
    # output_for_GEMMES.drop(columns=['capex_F_CO', 'capex_F_M', 'ikefCO', 'ikefM'], inplace=True)
    # output_for_GEMMES.drop(columns=['capex_B_CO', 'capex_B_M', 'ikebCO', 'ikebM'], inplace=True)
    # output_for_GEMMES.drop(columns=['capex_G_CO', 'capex_G_M', 'ikegCO', 'ikegM'], inplace=True)
    # output_for_GEMMES.drop(columns=['capex_H_CO', 'capex_H_M', 'ikehCO', 'ikehM'], inplace=True)
    output_for_GEMMES['icef'] = output_for_GEMMES['opex_F_CO'] + output_for_GEMMES['opex_F_M']
    output_for_GEMMES['sigmamicef'] = output_for_GEMMES['opex_F_M'] / output_for_GEMMES['icef']
    output_for_GEMMES['iceb'] = output_for_GEMMES['opex_B_CO'] + output_for_GEMMES['opex_B_M']
    output_for_GEMMES['sigmamiceb'] = output_for_GEMMES['opex_B_M'] / output_for_GEMMES['iceb']
    output_for_GEMMES['iceg'] = output_for_GEMMES['opex_G_CO'] + output_for_GEMMES['opex_G_M']
    output_for_GEMMES['sigmamiceg'] = output_for_GEMMES['opex_G_M'] / output_for_GEMMES['iceg']
    output_for_GEMMES['ceh'] = output_for_GEMMES['opex_H_CO'] + output_for_GEMMES['opex_H_M']
    output_for_GEMMES['sigmamceh'] = output_for_GEMMES['opex_H_M'] / output_for_GEMMES['ceh']
    output_for_GEMMES['pieM'] = 1 / (output_GEMMES_2021['pw'] * output_GEMMES_2021['en'])
    # output_for_GEMMES.drop(columns=['opex_F_CO', 'opex_F_M', 'opex_B_CO','opex_B_M', 'opex_G_CO', 'opex_G_M', 'opex_H_CO', 'opex_H_M'], inplace=True)
    output_for_GEMMES = output_for_GEMMES.round(3)
    output_for_GEMMES.to_csv('Energy_system_costs.csv')   
    
def EnergyScope_output_csv(EnergyScope_output_file, ampl_0):
    ampl_graph = AmplGraph(EnergyScope_output_file, ampl_0, case_study)
    z_Results = ampl_graph.ampl_collector
    z_Results['Resources'].to_csv(os.path.join(EnergyScope_case_study_path,'Resources.csv'))
    z_Results['New_old_decom'].to_csv(os.path.join(EnergyScope_case_study_path,'Assets.csv'))
    z_Results['Assets'].to_csv(os.path.join(EnergyScope_case_study_path,'Assets.csv'))
    z_Results['Cost_breakdown'].to_csv(os.path.join(EnergyScope_case_study_path,'Cost_breakdown.csv'))
    z_Results['Year_balance'].to_csv(os.path.join(EnergyScope_case_study_path,'Year_balance.csv'))
    z_Results['Gwp_breakdown'].to_csv(os.path.join(EnergyScope_case_study_path,'Gwp_breakdown.csv'))


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

curr_dir = Path(os.path.dirname(__file__))

pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))
GEMMES_path = '/home/piejacques/Bureau/ColombiaEnergyScope'
Cpp_path = GEMMES_path + '/SourceCode/cppCode'
sys.path.insert(0, pymodPath)
sys.path.insert(0, Cpp_path)
sys.path.insert(0, Cpp_path + "/src")

ESMY_path = os.path.join(curr_dir.parent,'ESMY')
EnergyScope_model_path = os.path.join(ESMY_path,'STEP_2_Pathway_Model')

from solve_GEMMES import solveGEMMES
from ampl_object import AmplObject
from ampl_preprocessor import AmplPreProcessor
from ampl_collector import AmplCollector
from ampl_graph import AmplGraph

## Read the GEMMES model
cppimport.settings['force_rebuild'] = True
solvePy = cppimport.imp('functionsForPy')

## Define the country studied and the time granularity of EnergyScope
country = 'Colombia'
EnergyScope_granularity = 'MO'
nbr_tds = 12

## Read the EnergyScope model and data files
if EnergyScope_granularity == 'MO':
    mod_1_path = [os.path.join(EnergyScope_model_path,'PESMO_model.mod'),
                os.path.join(EnergyScope_model_path,'PESMO_store_variables.mod'),
                os.path.join(EnergyScope_model_path,'PES_store_variables.mod')]
    mod_2_path = [os.path.join(EnergyScope_model_path,'PESMO_initialise_2020.mod'),
                  os.path.join(EnergyScope_model_path,'fix.mod')]
    dat_path = [os.path.join(EnergyScope_model_path,country+'/PESMO_data_all_years.dat')] 
else:
    mod_1_path = [os.path.join(EnergyScope_model_path,'PESTD_model.mod'),
            os.path.join(EnergyScope_model_path,'PESTD_store_variables.mod'),
            os.path.join(EnergyScope_model_path,'PES_store_variables.mod')]
    mod_2_path = [os.path.join(EnergyScope_model_path,'PESTD_initialise_2020.mod'),
              os.path.join(EnergyScope_model_path,'fix.mod')]
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
                'crossover=0', #-1 let gurobi decide
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
    
    
    