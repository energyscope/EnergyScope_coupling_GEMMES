# -*- coding: utf-8 -*-
"""
Created on Mon May 17 10:21 2021

@author: Xavier Rixhon
"""

import os, sys
from os import system
from pathlib import Path
import webbrowser
import time
import multiprocessing as mp
import pickle as pkl
import pandas as pd
import numpy as np

curr_dir = Path(os.path.dirname(__file__))

pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))
sys.path.insert(0, pymodPath)

from ampl_object import AmplObject
from ampl_preprocessor import AmplPreProcessor
from ampl_collector import AmplCollector
from ampl_graph import AmplGraph

country = 'Colombia'
type_of_model = 'MO'
nbr_tds = 12

run_opti = True
simulate_TEJ_scenario = False
graph = True
graph_comp = False

pth_esmy = os.path.join(curr_dir.parent,'ESMY')

pth_model = os.path.join(pth_esmy,'STEP_2_Pathway_Model')

if type_of_model == 'MO':
    mod_1_path = [os.path.join(pth_model,'PESMO_model.mod'),
                os.path.join(pth_model,'PESMO_store_variables.mod'),
                os.path.join(pth_model,'PES_store_variables.mod')]
    mod_2_path = [os.path.join(pth_model,'PESMO_initialise_2020.mod'),
                  os.path.join(pth_model,'fix.mod')]
    dat_path = [os.path.join(pth_model,country+'/PESMO_data_all_years.dat')]
else:
    mod_1_path = [os.path.join(pth_model,'PESTD_model.mod'),
            os.path.join(pth_model,'PESTD_store_variables.mod'),
            os.path.join(pth_model,'PES_store_variables.mod')]
    mod_2_path = [os.path.join(pth_model,'PESTD_initialise_2020.mod'),
              os.path.join(pth_model,'fix.mod')]
    dat_path = [os.path.join(pth_model,'PESTD_data_all_years.dat'),
                os.path.join(pth_model,'PESTD_{}TD.dat'.format(nbr_tds))]

dat_path += [os.path.join(pth_model,'PES_data_all_years.dat'),
             os.path.join(pth_model,'PES_seq_opti.dat'),
             os.path.join(pth_model,country+'/PES_data_efficiencies.dat'),
             os.path.join(pth_model,'PES_data_set_AGE_2020.dat')]

if(simulate_TEJ_scenario):
    dat_path += [os.path.join(pth_model,country+'/PES_data_year_related_TEJ.dat')]
else:
    dat_path += [os.path.join(pth_model,country+'/PES_data_year_related.dat')]

dat_path_0 = dat_path + [os.path.join(pth_model,'PES_data_remaining.dat'),
             os.path.join(pth_model,'PES_data_decom_allowed_2020.dat')]

dat_path += [os.path.join(pth_model,'PES_data_remaining_wnd.dat'),
             os.path.join(pth_model,'PES_data_decom_allowed_2020.dat')]

## Options for ampl and gurobi
gurobi_options = ['predual=-1',
                'method = 2', # 2 is for barrier method
                'crossover=0', #-1 let gurobi decide
                'prepasses = 3',
                'barconvtol=1e-6',
                'presolve=-1'] # Not a good idea to put it to 0 if the model is too big

gurobi_options_str = ' '.join(gurobi_options)

ampl_options = {'show_stats': 1,
                'log_file': os.path.join(pth_model,'log.txt'),
                'presolve': 10,
                'presolve_eps': 1e-6,
                'presolve_fixeps': 1e-6,
                'show_boundtol': 0,
                'gurobi_options': gurobi_options_str,
                '_log_input_only': False}

###############################################################################
''' main script '''
###############################################################################

if __name__ == '__main__':
    
    ## Paths
    pth_output_all = os.path.join(curr_dir.parent,'out')
    
    N_year_opti = [30]
    N_year_overlap = [0]


    for m in range(len(N_year_opti)):
        
        # TO DO ONCE AT INITIALISATION OF THE ENVIRONMENT
        i = 0
        n_year_opti = N_year_opti[m]
        n_year_overlap = N_year_overlap[m]
        
      
        case_study = '{}_{}_{}_gwp_limit_all_the_way'.format(type_of_model,n_year_opti,n_year_overlap)
        expl_text = 'GWP limit all the way up to 2050, to reach carbon neutrality with {} years of time window and {} years of overlap'.format(n_year_opti,n_year_overlap)
        
        output_folder = os.path.join(pth_output_all,case_study)
        output_file = os.path.join(output_folder,'_Results.pkl')
        ampl_0 = AmplObject(mod_1_path, mod_2_path, dat_path_0, ampl_options, type_model = type_of_model)
        ampl_0.clean_history()
        ampl_pre = AmplPreProcessor(ampl_0, n_year_opti, n_year_overlap)
        ampl_collector = AmplCollector(ampl_pre, output_file, expl_text)
        
        t = time.time()
        
        if run_opti:
        
            for i in range(len(ampl_pre.years_opti)):
            # TO DO AT EVERY STEP OF THE TRANSITION
                t_i = time.time()
                curr_years_wnd = ampl_pre.write_seq_opti(i).copy()
                ampl_pre.remaining_update(i)
                
                ampl = AmplObject(mod_1_path, mod_2_path, dat_path, ampl_options, type_model = type_of_model)

                solve_result = ampl.run_ampl()
                ampl.get_results()
                
                if i==0: 
                    ampl_collector.init_storage(ampl)
                
                if i > 0:
                    curr_years_wnd.remove(ampl_pre.year_to_rm)
                
                ampl_collector.update_storage(ampl,curr_years_wnd,i)
                
                ampl.set_init_sol()
                
                elapsed_i = time.time()-t_i
                print('Time to solve the window #'+str(i+1)+': ',elapsed_i)
                
                
                if i == len(ampl_pre.years_opti)-1:
                    elapsed = time.time()-t
                    print('Time to solve the whole problem: ',elapsed)
                    ampl_collector.clean_collector()
                    ampl_collector.pkl()
                    break         
        
        if graph:
            ampl_graph = AmplGraph(output_file, ampl_0, case_study)
            z_Results = ampl_graph.ampl_collector
            # z_Resources = z_Results['Resources'].copy()
            # z_Assets = z_Results['Assets'].copy()
            # z_Cost_breakdown = z_Results['Cost_breakdown'].copy()
            # z_Year_balance = z_Results['Year_balance'].copy()
            # z_gwp_breakdown = z_Results['Gwp_breakdown'].copy()
            
            C_inv = z_Results['C_inv_phase_tech_non_annualised'].copy()
            C_inv.rename(columns = {'C_inv_phase_tech_non_annualised':'Value'}, inplace = True)
            C_inv = C_inv.round(0)
            C_inv['Local'] = 0
            C_inv['Imported'] = 1 - C_inv['Local']
            C_inv[['F','B','G','H']] = [1,0,0,0]

            # C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DHN','GRID','HVAC_LINE']),[3,5]] = [0,1] # Costs supported by the PRIVATE SECTOR, actually (not by the state - grid costs for households are quite volatile, according to Santiago)
            
            list_private_mob_tech = ['MOTORCYCLE','CAR_GASOLINE','CAR_DIESEL','CAR_NG','CAR_METHANOL','CAR_HEV','CAR_PHEV','MOTORCYCLE_ELECTRIC','CAR_BEV','CAR_FUEL_CELL']
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_private_mob_tech),[3,6]] = [0,1] # Private mobility costs are supported by households
            
            list_public_mob_tech = ['TRAMWAY_TROLLEY','BUS_COACH_DIESEL','BUS_COACH_GASOLINE','BUS_COACH_HYDIESEL','BUS_COACH_CNG_STOICH','BUS_COACH_FC_HYBRIDH2','TRAIN_PUB']
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_public_mob_tech),[3,5]] = [0,1] # Private mobility costs are supported by the State
            
            shares_cooling = pd.read_csv(pth_model + '/shares_cooling.csv')
            shares_cooling.set_index('Phase',inplace=True)
            list_cooling_tech = ['DEC_ELEC_COLD','DEC_THHP_GAS_COLD']
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_cooling_tech),3] = 0
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_ELEC_COLD']),[4,5,6]] = shares_cooling.values
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_THHP_GAS_COLD']),[4,5,6]] = shares_cooling.values
            
            C_inv['merge_index'] = C_inv.index.get_level_values('Phases')
            shares_LTH = pd.read_csv(pth_model + '/shares_LTH.csv')
            shares_LTH.set_index('Phase',inplace=True)
            shares_LTH['merge_index'] = C_inv['merge_index'].unique()
            C_inv_bis = pd.merge(C_inv, shares_LTH, on='merge_index')
            C_inv_bis.index = C_inv.index
            list_LTH_tech = ['DHN_HP_ELEC','DHN_COGEN_GAS','DHN_COGEN_WOOD','DHN_COGEN_WASTE','DHN_COGEN_WET_BIOMASS','DHN_COGEN_BIO_HYDROLYSIS','DHN_BOILER_GAS','DHN_BOILER_WOOD','DHN_BOILER_OIL','DHN_DEEP_GEO','DHN_SOLAR','DEC_HP_ELEC','DEC_THHP_GAS','DEC_COGEN_GAS','DEC_COGEN_OIL','DEC_ADVCOGEN_GAS','DEC_ADVCOGEN_H2','DEC_BOILER_GAS','DEC_BOILER_WOOD','COAL_STOVE','DEC_BOILER_OIL','DEC_SOLAR','DEC_DIRECT_ELEC']
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_LTH_tech),[3,4,5,6]] = C_inv_bis.iloc[C_inv_bis.index.get_level_values('Technologies').isin(list_LTH_tech),[8,9,10,11]].values
            C_inv.drop(columns=['merge_index'],inplace=True)
            # C_inv.to_csv(pth_output_all+'/'+country+'/C_inv_phase_tech_non_annualised.csv')
            
            
            C_maint = z_Results['C_op_phase_tech_non_annualised']
            C_maint.rename(columns = {'C_op_phase_tech_non_annualised':'Value'}, inplace = True)
            C_maint = C_maint.round(0)
            C_maint['Local'] = 1
            C_maint['Imported'] = 1 - C_maint['Local']
            C_maint[['F','B','G','H']] = C_inv.iloc[~C_inv.index.get_level_values('Phases').isin(['2015_2020']),[3,4,5,6]].values            
            # C_maint.to_csv(pth_output_all+'/'+country+'/C_op_phase_tech_non_annualised.csv')
            
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
            Local_resources = ['GASOLINE','DIESEL','BIOETHANOL','BIODIESEL','LFO','GAS','WOOD','COAL','CO2_EMISSIONS','CO2_CAPTURED','CO2_INDUSTRY','RES_WIND','RES_SOLAR','RES_HYDRO','CO2_ATM','WET_BIOMASS','WASTE','RES_GEO']
            C_op.iloc[C_op.index.get_level_values('Resources').isin(Local_resources),1] = 1
            C_op['Imported'] = 1 - C_op['Local']
            C_op[['F','B','G','H']] = [1,0,0,0]
                 
            
            year_balance = z_Results['Year_balance'].copy()
            
            year_balance[['F','B','G','H']] = [1,0,0,0]
            year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_private_mob_tech),[31,34]] = [0,1]
            year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_public_mob_tech),[31,33]] = [0,1]
            year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_cooling_tech),[31]] = 0
            year_balance.iloc[year_balance.index.get_level_values('Elements').isin(['DEC_ELEC_COLD']),[32,33,34]] = shares_cooling.values
            year_balance.iloc[year_balance.index.get_level_values('Elements').isin(['DEC_THHP_GAS_COLD']),[32,33,34]] = shares_cooling.iloc[1:,:].values
            
            year_balance['merge_index_2'] = year_balance.index.get_level_values('Years')
            shares_LTH['merge_index_2'] = year_balance['merge_index_2'].unique()
            year_balance_bis = pd.merge(year_balance, shares_LTH, on='merge_index_2')
            year_balance_bis.index = year_balance.index
            year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_LTH_tech),[31,32,33,34]] = year_balance_bis.iloc[year_balance_bis.index.get_level_values('Elements').isin(list_LTH_tech),[36,37,38,39]].values
            
            year_balance = year_balance[year_balance['F']<0.999]
            year_balance = year_balance.loc[:, year_balance.columns.isin(['ELECTRICITY','GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE','H2','METHANOL','B','G','H'])]
            year_balance.loc[year_balance['ELECTRICITY']>0,'ELECTRICITY'] = np.nan
            year_balance = year_balance.abs()
            year_balance.drop(columns=['H2','METHANOL'], inplace=True) #### Negligible amount
            
            
            # Reconstruct prices of resources
            
            year_balance_tot = z_Results['Year_balance'].copy()
            list_resources = ['GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE']
            n_resources = len(list_resources) + 1 # include also electricity
            year_balance_tot = year_balance_tot.loc[:, year_balance_tot.columns.isin(list_resources)]
            year_balance_tot = year_balance_tot.iloc[year_balance_tot.index.get_level_values('Elements').isin(list_resources)]
            year_balance_tot = year_balance_tot.groupby(level=[0]).sum()
            
            Cost_breakdown = z_Results['Cost_breakdown'].copy()
            Cost_breakdown = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(list_resources)]
            Cost_breakdown = pd.pivot_table(Cost_breakdown, values='C_op', index=['Years'], columns=['Elements'])

            prices_resources = Cost_breakdown.div(year_balance_tot)
            prices_resources = prices_resources.round(3)

            
            # Construct a price for locally produced electricity





technos_res_elec = ['CCGT','COAL_IGCC','PV','WIND_ONSHORE','WIND_OFFSHORE','HYDRO_DAM','HYDRO_RIVER','GEOTHERMAL','GRID','HVAC_LINE','GAS','COAL']
Cost_elec_approx = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(technos_res_elec)]
year_balance_elec = year_balance[['COAL','GAS']]
Cost_elec_approx['perc_for_elec'] = np.nan
Cost_elec_approx.iloc[Cost_elec_approx.index.get_level_values('Elements').isin(['COAL']),3] = year_balance_elec.iloc[year_balance_elec.index.get_level_values('Elements').isin(['COAL_IGCC']),0].values / year_balance_elec.iloc[year_balance_elec.index.get_level_values('Elements').isin(['COAL']),0].values
Cost_elec_approx.iloc[Cost_elec_approx.index.get_level_values('Elements').isin(['GAS']),3] = year_balance_elec.iloc[year_balance_elec.index.get_level_values('Elements').isin(['CCGT']),1].values / year_balance_elec.iloc[year_balance_elec.index.get_level_values('Elements').isin(['GAS']),1].values
Cost_elec_approx.loc[:,'C_op'] = Cost_elec_approx['C_op'] * Cost_elec_approx['perc_for_elec']
Cost_elec_approx.loc[:,'C_op'] = Cost_elec_approx.loc[:,'C_op'].abs()
Cost_elec_approx.drop(columns=['perc_for_elec'],inplace=True)
Cost_elec_approx = Cost_elec_approx.groupby(level=[0]).sum()
Cost_elec_approx = Cost_elec_approx.sum(axis=1)


      
            # Compute the cost of each resource use for each techno
            
            year_balance = pd.merge(year_balance, prices_resources, on='Years')
            year_balance.iloc[:,0:n_resources] = year_balance.iloc[:,0:n_resources].values * year_balance.iloc[:,n_resources+3:].values
            
            

            # C_op.to_csv(pth_output_all+'/'+country+'/C_op_phase_res_non_annualised.csv')        

            
            output_for_GEMMES = pd.DataFrame(index=annualised_factor.index[1:])
            output_for_GEMMES = pd.DataFrame(index=annualised_factor.index)
            output_for_GEMMES['capex_F_COP'] = (C_inv['Value'] * C_inv['Local'] * C_inv['F']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_F_FX'] = (C_inv['Value'] * C_inv['Imported'] * C_inv['F']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_F_COP'] = (C_maint['Value'] * C_maint['Local'] * C_maint['F']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['F']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_F_FX'] = (C_maint['Value'] * C_maint['Imported'] * C_maint['F']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['F']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_B_COP'] = (C_inv['Value'] * C_inv['Local'] * C_inv['B']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_B_FX'] = (C_inv['Value'] * C_inv['Imported'] * C_inv['B']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_B_COP'] = (C_maint['Value'] * C_maint['Local'] * C_maint['B']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['B']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_B_FX'] = (C_maint['Value'] * C_maint['Imported'] * C_maint['B']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['B']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_G_COP'] = (C_inv['Value'] * C_inv['Local'] * C_inv['G']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_G_FX'] = (C_inv['Value'] * C_inv['Imported'] * C_inv['G']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_G_COP'] = (C_maint['Value'] * C_maint['Local'] * C_maint['G']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['G']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_G_FX'] = (C_maint['Value'] * C_maint['Imported'] * C_maint['G']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['G']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_H_COP'] = (C_inv['Value'] * C_inv['Local'] * C_inv['H']).groupby(level=[0]).sum()
            output_for_GEMMES['capex_H_FX'] = (C_inv['Value'] * C_inv['Imported'] * C_inv['H']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_H_COP'] = (C_maint['Value'] * C_maint['Local'] * C_maint['H']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Local'] * C_op['H']).groupby(level=[0]).sum()
            output_for_GEMMES['opex_H_FX'] = (C_maint['Value'] * C_maint['Imported'] * C_maint['H']).groupby(level=[0]).sum() + (C_op['Value'] * C_op['Imported'] * C_op['H']).groupby(level=[0]).sum()
            output_for_GEMMES = output_for_GEMMES.round(1)
            output_for_GEMMES.to_csv(pth_output_all+'/'+country+'/Outputs_for_GEMMES/Costs_per_phase.csv')
            
            Cost_breakdown_non_annualised = z_Results['Cost_breakdown_non_annualised']
            Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.groupby(level=[0]).sum()
            Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.loc[Cost_breakdown_non_annualised.index=='YEAR_2020']
            Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.round(0)
            Cost_breakdown_non_annualised.to_csv(pth_output_all+'/'+country+'/Outputs_for_GEMMES/Initial_cost.csv')
            
            # a_website = "https://www.google.com"
            # webbrowser.open_new(a_website)
            ampl_graph.graph_resource()
            # ampl_graph.graph_cost()
            # # ampl_graph.graph_gwp_per_sector()
            # ampl_graph.graph_cost_inv_phase_tech()
            # # ampl_graph.graph_cost_return()
            # ampl_graph.graph_cost_op_phase()
        
            # ampl_graph.graph_layer()1
            # ampl_graph.graph_gwp()
            # ampl_graph.graph_tech_cap()
            # ampl_graph.graph_total_cost_per_year()
            # # ampl_graph.graph_load_factor()
            # # df_unused = ampl_graph.graph_load_factor_2()
            # ampl_graph.graph_new_old_decom()
            
        if graph_comp:
            ampl_graph = AmplGraph(output_file, ampl_0,case_study)
            
            case_study_1 = '{}_{}_{}_gwp_limit_all_the_way'.format('TD',30,0)
            output_folder_1 = os.path.join(pth_output_all,case_study_1)
            output_file_1 = os.path.join(output_folder_1,'_Results.pkl')
            
            case_study_2 = '{}_{}_{}_gwp_limit_all_the_way'.format('TD',10,5)
            output_folder_2 = os.path.join(pth_output_all,case_study_2)
            output_file_2 = os.path.join(output_folder_2,'_Results.pkl')
            
            
            output_files = [output_file_1,output_file_2]
            
            # ampl_graph.graph_comparison(output_files,'C_inv_phase_tech')
            ampl_graph.graph_comparison(output_files,'C_op_phase')
            # ampl_graph.graph_comparison(output_files,'Tech_cap')
            

            
        ###############################################################################
        ''' main script ends here '''
        ###############################################################################
        
