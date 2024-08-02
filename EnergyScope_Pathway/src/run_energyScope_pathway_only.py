# -*- coding: utf-8 -*-
"""
May 2024

@authors: Pierre Jacques, Xavier Rixhon, Stanislas Augier
"""

import os, sys
from pathlib import Path
import webbrowser
import time
import pickle as pkl
import pandas as pd
import numpy as np
import amplpy as apy
import matplotlib.pyplot as plt

## Define the country studied and the time granularity of EnergyScope
country = 'Colombia'
EnergyScope_granularity = 'MO'
nbr_tds = 12

curr_dir = Path(os.path.dirname(__file__))
pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))
sys.path.insert(0, pymodPath)

ESMY_path = os.path.join(curr_dir.parent,'ESMY')
EnergyScope_model_path = os.path.join(ESMY_path,'STEP_2_Pathway_Model')

from ampl_object import AmplObject
from ampl_preprocessor import AmplPreProcessor
from ampl_collector import AmplCollector
from ampl_graph import AmplGraph

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


def main():
    plot_EnergyScope = False  
    csv_EnergyScope  = True

    output_EnergyScope = run_EnergyScope()

    if plot_EnergyScope:
        plot_EnergyScope_outputs(output_EnergyScope[0], output_EnergyScope[1])
    if csv_EnergyScope:
        EnergyScope_output_csv(output_EnergyScope[0], output_EnergyScope[1])


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
    c_inv_ampl.set_index(['Year', 'Technologies'], inplace=True)
    c_inv_ampl = apy.DataFrame.from_pandas(c_inv_ampl)
    ampl.set_params('c_inv', c_inv_ampl)
    
    # We assume that all maintenance costs are local costs
    c_maint_ampl = ampl.get_param('c_maint').to_list()
    c_maint_ampl = pd.DataFrame(c_maint_ampl, columns=['Year', 'Technologies', 'Value'])
    c_maint_ampl.set_index(['Year', 'Technologies'], inplace=True)
    c_maint_ampl = apy.DataFrame.from_pandas(c_maint_ampl)
    ampl.set_params('c_maint', c_maint_ampl)
    
    c_op_ampl = ampl.get_param('c_op').to_list()
    c_op_ampl = pd.DataFrame(c_op_ampl, columns=['Year', 'Resources', 'Value'])
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
    z_Resources = z_Results['Resources'].copy()
    z_Assets = z_Results['Assets'].copy()
    z_Cost_breakdown = z_Results['Cost_breakdown'].copy()
    z_Year_balance = z_Results['Year_balance'].copy()
    z_gwp_breakdown = z_Results['Gwp_breakdown'].copy()
    
    a_website = "https://www.google.com"
    webbrowser.open_new(a_website)
    ampl_graph.graph_cost()
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


if __name__ == '__main__':
    main()
    
    
    
