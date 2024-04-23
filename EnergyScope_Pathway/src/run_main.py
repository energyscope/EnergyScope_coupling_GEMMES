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
import amplpy as apy

curr_dir = Path(os.path.dirname(__file__))

pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))
sys.path.insert(0, pymodPath)

GEMMES_path = os.path.join(curr_dir.parent,'Outputs_from_GEMMES/')

from ampl_object import AmplObject
from ampl_preprocessor import AmplPreProcessor
from ampl_collector import AmplCollector
from ampl_graph import AmplGraph

country = 'Turkey'
type_of_model = 'TD'
nbr_tds = 12

run_opti = False
simulate_TEJ_scenario = False
get_inputs_from_GEMMES = False # de-comment the lines with i_rate !
output_csv = True
graph = True
graph_comp = False
outputs_for_GEMMES = False

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
    dat_path = [os.path.join(pth_model,country+'/PESTD_data_all_years.dat'),
                os.path.join(pth_model,country+'/PESTD_{}TD.dat'.format(nbr_tds))]

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
        
        if(simulate_TEJ_scenario):
            if(type_of_model=='MO'):
                case_study = 'TEJ - MO'.format(type_of_model,n_year_opti,n_year_overlap)
                expl_text = 'Transición Energetica Justa - monthly granularity'.format(n_year_opti,n_year_overlap)
            else:
                case_study = 'TEJ - TD'.format(type_of_model,n_year_opti,n_year_overlap)
                expl_text = 'Transición Energetica Justa - hourly granularity'.format(n_year_opti,n_year_overlap)
        else:
            if(type_of_model=='MO'):
                if(country=='Colombia'):
                    case_study = 'Colombia - MO'.format(type_of_model,n_year_opti,n_year_overlap)
                    expl_text = 'Colombia - monthly granularity'.format(n_year_opti,n_year_overlap)
                else:
                    case_study = 'Turkey - MO'.format(type_of_model,n_year_opti,n_year_overlap)
                    expl_text = 'Turkey - monthly granularity'.format(n_year_opti,n_year_overlap)
            else:
                if(country=='Colombia'):
                    case_study = 'Colombia - TD'.format(type_of_model,n_year_opti,n_year_overlap)
                    expl_text = 'Colombia - hourly granularity'.format(n_year_opti,n_year_overlap)
                else:
                    case_study = 'Turkey - TD'.format(type_of_model,n_year_opti,n_year_overlap)
                    expl_text = 'Turkey - hourly granularity'.format(n_year_opti,n_year_overlap)
        
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

                if(get_inputs_from_GEMMES):
                    # i_rate = pd.read_csv(GEMMES_path + 'i_rate.csv')
                    # i_rate.set_index('Phase', inplace=True)
                    phases_ES = ['2015_2020', '2020_2025', '2025_2030', '2030_2035', '2035_2040', '2040_2045', '2045_2050']
                    # for j in range(len(phases_ES)):
                        # ampl.set_params('i_rate',{(phases_ES[j]):i_rate.iloc[j,0]})
                    
                    EUD_2021 = pd.read_csv(GEMMES_path + 'EUD_2021.csv')
                    EUD_2026 = pd.read_csv(GEMMES_path + 'EUD_2026.csv')
                    EUD_2031 = pd.read_csv(GEMMES_path + 'EUD_2031.csv')
                    EUD_2036 = pd.read_csv(GEMMES_path + 'EUD_2036.csv')
                    EUD_2041 = pd.read_csv(GEMMES_path + 'EUD_2041.csv')
                    EUD_2046 = pd.read_csv(GEMMES_path + 'EUD_2046.csv')
                    EUD_2051 = pd.read_csv(GEMMES_path + 'EUD_2051.csv')
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
        
        if output_csv:
            ampl_graph = AmplGraph(output_file, ampl_0, case_study)
            z_Results = ampl_graph.ampl_collector
            z_Results['Resources'].to_csv('Resources.csv')
            z_Results['Assets'].to_csv('Assets.csv')
            z_Results['Cost_breakdown'].to_csv('Cost_breakdown.csv')
            z_Results['Year_balance'].to_csv('Year_balance.csv')
            z_Results['Gwp_breakdown'].to_csv('Gwp_breakdown.csv')

        if graph:
            ampl_graph = AmplGraph(output_file, ampl_0, case_study)
            z_Results = ampl_graph.ampl_collector
            # z_Resources = z_Results['Resources'].copy()
            # z_Assets = z_Results['Assets'].copy()
            # z_Cost_breakdown = z_Results['Cost_breakdown'].copy()
            # z_Year_balance = z_Results['Year_balance'].copy()
            # z_gwp_breakdown = z_Results['Gwp_breakdown'].copy()
            
            # a_website = "https://www.google.com"
            # webbrowser.open_new(a_website)
            ampl_graph.graph_resource()
            # ampl_graph.graph_cost()
            # ampl_graph.graph_gwp_per_sector()
            # ampl_graph.graph_cost_inv_phase_tech()
            # ampl_graph.graph_cost_return()
            # ampl_graph.graph_cost_op_phase()
        
            # ampl_graph.graph_layer()
            ampl_graph.graph_gwp()
            ampl_graph.graph_tech_cap()
            # ampl_graph.graph_total_cost_per_year()
            # ampl_graph.graph_load_factor()
            # df_unused = ampl_graph.graph_load_factor_2()
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
            
        if outputs_for_GEMMES:
            ampl_graph = AmplGraph(output_file, ampl_0, case_study)
            z_Results = ampl_graph.ampl_collector
            
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
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_public_mob_tech),[3,5]] = [0,1] # Public mobility costs are supported by the State
            
            shares_cooling = pd.read_csv(GEMMES_path + 'shares_cooling.csv')
            shares_cooling.set_index('Phase',inplace=True)
            list_cooling_tech = ['DEC_ELEC_COLD','DEC_THHP_GAS_COLD']
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_cooling_tech),3] = 0
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_ELEC_COLD']),[4,5,6]] = shares_cooling.values
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(['DEC_THHP_GAS_COLD']),[4,5,6]] = shares_cooling.values
            
            C_inv['merge_index'] = C_inv.index.get_level_values('Phases')
            shares_LTH = pd.read_csv(GEMMES_path + 'shares_LTH.csv')
            shares_LTH.set_index('Phase',inplace=True)
            shares_LTH['merge_index'] = C_inv['merge_index'].unique()
            C_inv_bis = pd.merge(C_inv, shares_LTH, on='merge_index')
            C_inv_bis.index = C_inv.index
            list_LTH_tech = ['DHN_HP_ELEC','DHN_COGEN_GAS','DHN_COGEN_WOOD','DHN_COGEN_WASTE','DHN_COGEN_WET_BIOMASS','DHN_COGEN_BIO_HYDROLYSIS','DHN_BOILER_GAS','DHN_BOILER_WOOD','DHN_BOILER_OIL','DHN_DEEP_GEO','DHN_SOLAR','DEC_HP_ELEC','DEC_THHP_GAS','DEC_COGEN_GAS','DEC_COGEN_OIL','DEC_ADVCOGEN_GAS','DEC_ADVCOGEN_H2','DEC_BOILER_GAS','DEC_BOILER_WOOD','COAL_STOVE','DEC_BOILER_OIL','DEC_SOLAR','DEC_DIRECT_ELEC']
            C_inv.iloc[C_inv.index.get_level_values('Technologies').isin(list_LTH_tech),[3,4,5,6]] = C_inv_bis.iloc[C_inv_bis.index.get_level_values('Technologies').isin(list_LTH_tech),[8,9,10,11]].values
            C_inv.drop(columns=['merge_index'],inplace=True)
            # C_inv.to_csv(pth_output_all+'/'+case_study+'/C_inv_phase_tech_non_annualised.csv')
            
            
            C_maint = z_Results['C_op_phase_tech_non_annualised']
            C_maint.rename(columns = {'C_op_phase_tech_non_annualised':'Value'}, inplace = True)
            C_maint = C_maint.round(0)
            C_maint['Local'] = 1
            C_maint['Imported'] = 1 - C_maint['Local']
            C_maint[['F','B','G','H']] = C_inv.iloc[~C_inv.index.get_level_values('Phases').isin(['2015_2020']),[3,4,5,6]].values            
            # C_maint.to_csv(pth_output_all+'/'+case_study+'/C_op_phase_tech_non_annualised.csv')
            
            
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
            Local_resources = ['GASOLINE','DIESEL','BIOETHANOL','BIODIESEL','LFO','GAS','WOOD','COAL','CO2_EMISSIONS','CO2_CAPTURED','CO2_INDUSTRY','RES_WIND','RES_SOLAR','RES_HYDRO','CO2_ATM','WET_BIOMASS','WASTE','RES_GEO']
            C_op.iloc[C_op.index.get_level_values('Resources').isin(Local_resources),1] = 1
            C_op['Imported'] = 1 - C_op['Local']
            C_op[['F','B','G','H']] = [1,0,0,0]
            # C_op.to_csv(pth_output_all+'/'+case_study+'/C_op_phase_res_non_annualised.csv')   
            
            
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
            
            
            ### Add to C_op the money paid by B,G,H to F for buying the fuels and electricity
            
            year_balance = z_Results['Year_balance'].copy()
            
            year_balance[['F','B','G','H']] = [1,0,0,0]
            year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_private_mob_tech),['F','H']] = [0,1]
            year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_public_mob_tech),['F','G']] = [0,1]
            year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_cooling_tech),['F']] = 0
            year_balance.loc[year_balance.index.get_level_values('Elements').isin(['DEC_ELEC_COLD']),['B','G','H']] = shares_cooling.values
            year_balance.loc[year_balance.index.get_level_values('Elements').isin(['DEC_THHP_GAS_COLD']),['B','G','H']] = shares_cooling.iloc[1:,:].values
            
            year_balance['merge_index_2'] = year_balance.index.get_level_values('Years')
            shares_LTH['merge_index_2'] = year_balance['merge_index_2'].unique()
            year_balance_bis = pd.merge(year_balance, shares_LTH, on='merge_index_2')
            year_balance_bis.index = year_balance.index
            year_balance.loc[year_balance.index.get_level_values('Elements').isin(list_LTH_tech),['F','B','G','H']] = year_balance_bis.loc[year_balance_bis.index.get_level_values('Elements').isin(list_LTH_tech),['F_y','B_y','G_y','H_y']].values
            
            year_balance = year_balance[year_balance['F']<0.999]
            year_balance = year_balance.loc[:, year_balance.columns.isin(['ELECTRICITY','GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE','H2','METHANOL','B','G','H'])]
            year_balance.loc[year_balance['ELECTRICITY']>0,'ELECTRICITY'] = np.nan
            year_balance = year_balance.abs()
            year_balance.drop(columns=['H2','METHANOL'], inplace=True) #### Negligible amount
            
            
            # Reconstruct prices of resources
            
            year_balance_tot = z_Results['Year_balance'].copy()
            list_resources = ['GAS','WASTE','WET_BIOMASS','WOOD','DIESEL','GASOLINE']
            list_resources_with_elec = list_resources + ['ELECTRICITY']
            n_resources = len(list_resources_with_elec)
            year_balance_tot = year_balance_tot.loc[:, year_balance_tot.columns.isin(list_resources_with_elec)]
            year_balance_tot = year_balance_tot.iloc[year_balance_tot.index.get_level_values('Elements').isin(list_resources)]
            year_balance_tot = year_balance_tot.groupby(level=[0]).sum()
            
            Cost_breakdown = z_Results['Cost_breakdown'].copy()
            Cost_breakdown_res = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(list_resources_with_elec)]
            Cost_breakdown_res = pd.pivot_table(Cost_breakdown_res, values='C_op', index=['Years'], columns=['Elements'])

            prices_resources = Cost_breakdown_res.div(year_balance_tot)
            
            # Construct a price for locally produced electricity
            technos_res_elec = ['CCGT','IMPORTED_COAL_CENTRAL','LOCAL_COAL_CENTRAL','PV','WIND_ONSHORE','WIND_OFFSHORE','HYDRO_DAM','HYDRO_RIVER','GEOTHERMAL','GRID','HVAC_LINE','GAS','IMPORTED_COAL','LOCAL_COAL']
            Cost_elec_approx = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(technos_res_elec)]
            year_balance_elec = z_Results['Year_balance'].copy()
            year_balance_elec = year_balance_elec[['IMPORTED_COAL','LOCAL_COAL','GAS','ELECTRICITY']]
            Cost_elec_approx['perc_for_elec'] = np.nan
            if('IMPORTED_COAL_CENTRAL' in year_balance_elec.index.get_level_values('Elements').to_list()):
                Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['IMPORTED_COAL']),'perc_for_elec'] = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['IMPORTED_COAL_CENTRAL']),'IMPORTED_COAL'].values / year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['IMPORTED_COAL']),'IMPORTED_COAL'].values
            if('LOCAL_COAL_CENTRAL' in year_balance_elec.index.get_level_values('Elements').to_list()):
                Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['LOCAL_COAL']),'perc_for_elec'] = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['LOCAL_COAL_CENTRAL']),'LOCAL_COAL'].values / year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['LOCAL_COAL']),'LOCAL_COAL'].values
            Cost_elec_approx.loc[Cost_elec_approx.index.get_level_values('Elements').isin(['GAS']),'perc_for_elec'] = year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['CCGT']),'GAS'].values / year_balance_elec.loc[year_balance_elec.index.get_level_values('Elements').isin(['GAS']),'GAS'].values
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
            year_balance.iloc[:,0:n_resources] = year_balance.iloc[:,0:n_resources].values * year_balance.iloc[:,n_resources+3:].values
            
            year_balance = year_balance.iloc[:,0:n_resources+3]
            year_balance['total_cost'] = year_balance.iloc[:,0:n_resources].sum(axis=1)
            year_balance = year_balance.iloc[:,n_resources:n_resources+4]
            year_balance['cost_B'] = year_balance['total_cost'] * year_balance['B']
            year_balance['cost_G'] = year_balance['total_cost'] * year_balance['G']
            year_balance['cost_H'] = year_balance['total_cost'] * year_balance['H']
            year_balance = year_balance.groupby(level=[0]).sum()
            year_balance = year_balance.iloc[:,4:] 
            year_balance['C_op_tot'] = Cost_breakdown.groupby(level=[0]).sum()['C_op']
            year_balance_shift = year_balance.copy()
            year_balance_shift = year_balance_shift.shift(1)
            # Go from yearly costs to phase costs
            year_balance = (year_balance + year_balance_shift) / 2 
            year_balance = year_balance.iloc[1:]
            year_balance['B % C_op'] = year_balance['cost_B'] / year_balance['C_op_tot']
            year_balance['G % C_op'] = year_balance['cost_G'] / year_balance['C_op_tot']
            year_balance['H % C_op'] = year_balance['cost_H'] / year_balance['C_op_tot']
            
            C_op_to_add = C_op['Value'].groupby(level=[0]).sum().to_frame()
            C_op_to_add['B'] = year_balance['B % C_op'].values * C_op_to_add['Value'].values
            C_op_to_add['G'] = year_balance['G % C_op'].values * C_op_to_add['Value'].values
            C_op_to_add['H'] = year_balance['H % C_op'].values * C_op_to_add['Value'].values
            first_row = pd.DataFrame(index=['2015_2020'],columns=C_op_to_add.columns)
            C_op_to_add = pd.concat([first_row,C_op_to_add])
            
            output_for_GEMMES['opex_B_COP'] += C_op_to_add['B']
            output_for_GEMMES['opex_G_COP'] += C_op_to_add['G']
            output_for_GEMMES['opex_H_COP'] += C_op_to_add['H']
            first_line = pd.read_csv(GEMMES_path + 'Costs_per_phase_first_line.csv')
            first_line.set_index('Unnamed: 0', inplace=True)           
            output_for_GEMMES = output_for_GEMMES * first_line.loc['2015_2020',:].sum() / output_for_GEMMES.iloc[0,:].sum()
            output_for_GEMMES = output_for_GEMMES.round(3)
            output_for_GEMMES = output_for_GEMMES.iloc[1:,:]
            output_for_GEMMES = pd.concat([first_line, output_for_GEMMES])
            output_for_GEMMES.to_csv(pth_output_all+'/'+case_study+'/Outputs_for_GEMMES/Costs_per_phase.csv')
            
            Cost_breakdown_non_annualised = z_Results['Cost_breakdown_non_annualised']
            Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.groupby(level=[0]).sum()
            # Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.loc[Cost_breakdown_non_annualised.index=='YEAR_2020']
            Cost_breakdown_non_annualised = Cost_breakdown_non_annualised.round(0)
            Cost_breakdown_non_annualised.to_csv(pth_output_all+'/'+case_study+'/Outputs_for_GEMMES/Initial_cost.csv')
        
            
        ###############################################################################
        ''' main script ends here '''
        ###############################################################################
        
