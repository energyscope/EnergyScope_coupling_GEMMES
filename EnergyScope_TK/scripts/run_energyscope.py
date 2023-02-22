# -*- coding: utf-8 -*-
"""
This script modifies the input data and runs the EnergyScope model

@author: Paolo Thiran, Matija Pavičević, Xavier Rixhon, Gauthier Limpens
"""

import os
from pathlib import Path
import energyscope as es
import select_TDs as TD

# TODO
#  finish documentation and export it
#  Update uq_estd_
#  Add other automatic plots

if __name__ == '__main__':
    analysis_only = False
    compute_TDs = True

    # define project path
    project_path = Path(__file__).parents[1]

    # loading the config file into a python dictionnary
    config = es.load_config(config_fn='config_ref.yaml', project_path=project_path)
    config['Working_directory'] = os.getcwd() # keeping current working directory into config
    
   # Reading the data of the csv
    es.import_data(config)
    
    if compute_TDs:
        data_dir = '/home/pjacques/Desktop/PhD/EnergyScope_GEMMES_coupling/EnergyScope_TK/energyscope/preprocessing/STEP_1_TD_selection'
        TD.build_TD_of_days(config, data_dir)

    ##TODO Student work: Write the updates in data HERE
    # Example to change data: update wood availability to 23 400 GWh (ref value here)
    # config['all_data']['Resources'].loc['WOOD', 'avail'] = 23400
    # Example to change share of public mobility into passenger mobility into 0.5 (ref value here)
    # config['all_data']['Misc']['share_mobility_public_max'] = 0.5
    
    if not analysis_only:
        # Printing the .dat files for the optimisation problem       
        es.print_data(config)

        # Running EnergyScope
        es.run_ES(config)

    # Example to print the sankey from this script
    if config['print_sankey']:
        sankey_path = config['cs_path']/ config['case_study'] / 'output' / 'sankey'
        es.drawSankey(path=sankey_path)

    # Reading outputs
    outputs = es.read_outputs(config['case_study'], hourly_data=True, layers=['layer_ELECTRICITY','layer_HEAT_LOW_T_DECEN'])

    # Plots (examples)
    # primary resources used
    fig2, ax2 = es.plot_barh(outputs['resources_breakdown'][['Used']], title='Primary energy [GWh/y]')
    # elec assets
    elec_assets = es.get_assets_l(layer='ELECTRICITY', eff_tech=config['all_data']['Layers_in_out'],
                                  assets=outputs['assets'])
    fig3, ax3 = es.plot_barh(elec_assets[['f']], title='Electricity assets [GW_e]',
                             x_label='Installed capacity [GW_e]')
    # layer_ELECTRICITY for the 12 tds
    # elec_layer_plot = es.plot_layer_elec_td(outputs['layer_ELECTRICITY'])
    # layer_HEAT_LOW_T_DECEN for the 12 tds
    # fig,ax = es.hourly_plot(plotdata=outputs['layer_HEAT_LOW_T_DECEN'], nbr_tds=12)
    



