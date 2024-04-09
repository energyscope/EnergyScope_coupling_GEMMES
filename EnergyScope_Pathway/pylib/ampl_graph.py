#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun. 13 2022

@author: rixhonx
"""

from pathlib import Path
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
import pandas as pd
import plotly.io as pio
from pandas.api.types import CategoricalDtype
pio.templates.default = 'simple_white'
# pio.kaleido.scope.mathjax = None
import numpy as np

import os,sys
from os import system

pylibPath = os.path.abspath("../pylib")
if pylibPath not in sys.path:
    sys.path.insert(0, pylibPath)

class AmplGraph:

    """

    The AmplGraph class allows to plot the relevant outputs (e.g. installed capacitites, used resources, costs)
    of an optimisation problem.

    Parameters
    ----------
    result_list: list(Pandas.DataFrame)
        Unpickled list where relevant outputs has been stored

    """

    def __init__(self, pkl_file, ampl_obj,case_study):
        self.pkl_file = pkl_file
        self.x_axis = [2020, 2025, 2030, 2035, 2040, 2045, 2050]
        # In 2020, 37.41% of electricity in EU-27 was produced from renewables (https://ec.europa.eu/eurostat/databrowser/view/NRG_IND_REN__custom_4442440/default/table?lang=en)
        self.re_share_elec = np.linspace(0.3741,1,len(self.x_axis))
        self.ampl_collector = self.unpkl(self)
        self.ampl_obj = ampl_obj
        self.case_study = case_study
        self.color_dict_full = self.dict_color_full()
        self.outdir = os.path.join(Path(self.pkl_file).parent.absolute(),'graphs/')
        if not os.path.exists(Path(self.outdir)):
            Path(self.outdir).mkdir(parents=True,exist_ok=True)

        self.threshold = 0.03
        self.category = self._group_sets()
        self.cost_return_eff = self._get_cost_return_for_each_year()
        self.pattern_shape_map_res={
            "ELECTRICITY" : "", "GASOLINE" : "", "DIESEL" : "", "BIOETHANOL" : "", "BIODIESEL" : "", "LFO" : "", "GAS" : "", "GAS_RE" : "",
            "WOOD" : "", "WET_BIOMASS" : "", "IMPORTED_COAL" : "", "LOCAL_COAL" : "", "URANIUM" : "", "WASTE" : "", "H2" : "", "H2_RE" : "", "AMMONIA" : "slateblue",
            "AMMONIA_RE" : "", "METHANOL" : "", "METHANOL_RE" : "", "CO2_EMISSIONS" : "", "RES_WIND" : "", "RES_SOLAR" : "",
            "RES_HYDRO" : "", "RES_GEO" : "", "ELEC_EXPORT" : "","CO2_ATM": "", "CO2_INDUSTRY": "", "CO2_CAPTURED": ""}

    @staticmethod
    def unpkl(self,pkl_file = None):
        if pkl_file == None:
            pkl_file = self.pkl_file
        open_file = open(pkl_file,"rb")
        loaded_results = pickle.load(open_file)
        open_file.close()

        return loaded_results
    
    @staticmethod
    def is_number(s): 

        """
        Return True if s is a number, False otherwise.

        """
        try:
            float(s)
            return True
        except ValueError:
            pass
    
        return False

    def graph_layer(self):
        pio.renderers.default = 'browser'
        
        col_plot = ['AMMONIA','ELECTRICITY','GAS','H2','HEAT_HIGH_T',
                'HEAT_LOW_T_DECEN','HEAT_LOW_T_DHN','HVC','METHANOL',
                'MOB_FREIGHT_BOAT','MOB_FREIGHT_RAIL','MOB_FREIGHT_ROAD','MOB_PRIVATE',
                'MOB_PUBLIC']
        results = self.ampl_collector['Year_balance'].copy()
        results = results[col_plot]
        for k in results.columns:
            df_to_plot = pd.DataFrame(index=results.index,columns=[k])
            temp = results.loc[:,k].dropna(how='all')
            for y in results.index.get_level_values(0).unique():
                temp_y = temp.loc[temp.index.get_level_values('Years') == y,:] 
                if not temp_y.empty:
                    temp_y = self._remove_low_values(temp_y)
                    df_to_plot.update(temp_y)
            df_to_plot.dropna(how='all',inplace=True)
            df_to_plot.reset_index(inplace=True)
            df_to_plot['Type'] = 'Production'
            df_to_plot['Type'].loc[df_to_plot[k]<0] = 'Consumption'
            neg_vars = df_to_plot.loc[df_to_plot[k]<0,'Elements'].unique()
            df_to_plot['Elements'] = df_to_plot['Elements'].astype("str")
            df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
            fig = px.area(df_to_plot, x='Years', color='Elements',y=k,
                           title=self.case_study + ' - {}'.format(k),
                           color_discrete_map=self.color_dict_full)
            fig.for_each_trace(lambda tr: tr.update(stackgroup=2 if tr.name in neg_vars else 1))
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
            fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
            fig.update_traces(mode='none')
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            pio.show(fig)
            if not os.path.exists(Path(self.outdir+"Layers/")):
                Path(self.outdir+"Layers").mkdir(parents=True,exist_ok=True)
            fig.write_image(self.outdir+"Layers/"+k+".pdf", width=1200, height=550)
            plt.close()
        
    def graph_resource(self):
        
        order_entry = ['ELECTRICITY','GASOLINE','DIESEL','LFO','IMPORTED_COAL', 'LOCAL_COAL',
                       'GAS','URANIUM','WOOD','WET_BIOMASS','WASTE',
                       'RES_SOLAR','RES_WIND',
                       'AMMONIA_RE','METHANOL_RE','H2_RE','GAS_RE']
                       #'BIODIESEL','BIOETHANOL']
        
        pio.renderers.default = 'browser'
        results = self.ampl_collector['Resources'].copy()
        df_to_plot = pd.DataFrame(index=results.index,columns=results.columns)
        for y in results.index.get_level_values(0).unique():
            temp = results.loc[results.index.get_level_values('Years') == y,'Res']  
            temp = self._remove_low_values(temp,threshold = 0)
            df_to_plot.update(temp)
        df_to_plot.dropna(how='all',inplace=True)
        
        df_to_plot.reset_index(inplace=True)
        df_to_plot['Resources'] = df_to_plot['Resources'].astype("str")
        
        df_to_plot['Resources'] = pd.Categorical(
            df_to_plot['Resources'], order_entry)
        df_to_plot.sort_values(by=['Resources'], axis=0, 
                               ignore_index=True, inplace=True)
        
        df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
        df_to_plot = df_to_plot.loc[df_to_plot['Resources'] != 'CO2_EMISSIONS']
        df_to_plot.dropna(inplace=True)
        df_to_plot['Res'] = df_to_plot['Res']/1000
        df_to_plot.loc[len(df_to_plot.index)] = ['2020','URANIUM',0.00000000001]
        
        fig = px.area(df_to_plot, x='Years', y = 'Res', color='Resources',
                      title=self.case_study + ' - Resources', text='Resources',
                      color_discrete_map=self.dict_color('Resources'))
                      #,pattern_shape="Resources", pattern_shape_map=self.pattern_shape_map_res)
        
        fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
        fig.update_traces(mode='none')
        fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        
        title = "<b>Primary energy supply</b><br>[TWh]"
        
        # temp = df_to_plot.groupby(['Years']).sum()
        # yvals = [0,min(round(temp['Res'])),max(round(temp['Res']))]
        
        # self.custom_fig(fig,title,yvals)
        # fig.write_image(self.outdir+"Resources.pdf", width=1200, height=550)
        fig.write_html(self.outdir+"Resources.html")
        plt.close()
    
    def graph_gwp(self):
        pio.renderers.default = 'browser'
        
        results = self.ampl_collector['Gwp_breakdown'].copy()
        results = results.drop(columns=['GWP_constr'])
        results.dropna(how='all',inplace=True)
        df_to_plot = pd.DataFrame(index=results.index,columns=results.columns)
        for y in results.index.get_level_values(0).unique():
            temp = results.loc[results.index.get_level_values('Years') == y,'GWP_op']  
            temp = self._remove_low_values(temp)
            df_to_plot.update(temp)
        df_to_plot.dropna(how='all',inplace=True)
        df_to_plot.reset_index(inplace=True)
        df_to_plot['Elements'] = df_to_plot['Elements'].astype("str")
        df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
        fig = px.area(df_to_plot, x='Years', y = 'GWP_op',color='Elements',
                     title=self.case_study + ' - GWP',
                     color_discrete_map=self.color_dict_full)
        fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
        fig.update_traces(mode='none')
        fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        # fig.write_image(self.outdir+"Gwp_breakdown.pdf", width=1200, height=550)
        fig.write_html(self.outdir+"Gwp_breakdown.html")
        plt.close()
    
    def graph_gwp_per_sector(self):
        pio.renderers.default = 'browser'
        
        """Get the gwp breakdown [ktCO2e/y] of the different sectors"""
        layers = ['GAS','H2','AMMONIA','METHANOL','ELECTRICITY','HEAT_HIGH_T',
                'HEAT_LOW_T_DECEN','HEAT_LOW_T_DHN','HVC',
                'MOB_FREIGHT_BOAT','MOB_FREIGHT_RAIL','MOB_FREIGHT_ROAD','MOB_PRIVATE',
                'MOB_PUBLIC']
        mob_freight_layers = ['MOB_FREIGHT_BOAT','MOB_FREIGHT_ROAD','MOB_FREIGHT_RAIL']
        
        CO2_layers = ['CO2_ATM','CO2_CAPTURED','CO2_INDUSTRY']
        
        order_entry = ['MOB_PRIVATE','MOB_PUBLIC','MOBILITY_FREIGHT','ELECTRICITY',
                       'HEAT_HIGH_T','HEAT_LOW_T_DHN','HEAT_LOW_T_DECEN',
                       'HVC','METHANOL','AMMONIA']
        
        resources = self.ampl_obj.sets['RESOURCES']
        technologies = self.ampl_obj.sets['TECHNOLOGIES']
        storage_tech = self.ampl_obj.sets['STORAGE_TECH']
        
        gwp_op = self.ampl_obj.get_elem('gwp_op',type_of_elem='Param').copy()
        year_balance_full = self.ampl_collector['Year_balance'].copy()
        year_balance_full.dropna(how='all',inplace=True)
        year_balance_full.drop(columns=CO2_layers,inplace=True)
        year_balance = year_balance_full.loc[~year_balance_full.index.get_level_values('Elements').isin(storage_tech)]
        
        year_balance_sto = year_balance_full.loc[year_balance_full.index.get_level_values('Elements').isin(storage_tech)]
        year_balance_sto.dropna(how='all',inplace=True)
        year_balance_sto.dropna(how='all',inplace=True,axis=1)
        year_balance_sto.reset_index(inplace=True)
        year_balance_sto.drop(columns=['Elements'],inplace=True)
        year_balance_sto = pd.melt(year_balance_sto, id_vars=['Years'], var_name=['Elements'], value_name='Cons')
        year_balance_sto = year_balance_sto.set_index(['Years','Elements'])
        year_balance_sto = year_balance_sto.groupby(level=[0,1]).sum()
        
        gwp_op.index.set_names(year_balance.index.names, inplace=True)  # set proper name to index
        gwp_op = gwp_op.rename_axis(index={'Resources':'Elements'},axis=1)
        
        total_prod = year_balance[year_balance>0].groupby(['Years']).sum()
        total_prod = total_prod[layers]
        total_prod.reset_index(inplace=True)
        total_prod = pd.melt(total_prod, id_vars=['Years'], var_name=['Layers'], value_name='total_prod')
        total_prod = total_prod.set_index(['Years','Layers'])
        
        end_uses = -year_balance.loc[year_balance.index.get_level_values('Elements')=='END_USES',:]
        end_uses.dropna(axis=1,inplace=True)
        end_uses.reset_index(inplace=True)
        end_uses.drop(columns=['Elements'],inplace=True)
        end_uses = pd.melt(end_uses, id_vars=['Years'], var_name=['Layers'], value_name='end_uses')
        end_uses = end_uses.set_index(['Years','Layers'])
        

        layers_in_out = self.ampl_obj.to_pd(self.ampl_obj.params['layers_in_out'].getValues())
        layers_in_out.reset_index(inplace=True)
        layers_in_out=layers_in_out.pivot(index=['index0','index1'],columns='index2',values='Value')
        layers_in_out.index.set_names(['Years','Elements'], inplace=True)
        layers_in_out = layers_in_out.mask(layers_in_out==0)
        layers_in_out.drop(columns=CO2_layers,inplace=True)
        layers_in_out.dropna(how='all',inplace=True)
        
        
        gwp_per_layer = pd.DataFrame(index=end_uses.index,columns=['gwp_op','GWP_EUD','GWP_TOTAL'])
        
        update_gwp_res = ['GAS','H2','AMMONIA','ELECTRICITY','DIESEL','GASOLINE','METHANOL','LFO']
        
        for res in update_gwp_res:
            temp = year_balance_full.loc[year_balance_full[res] > 0]
            temp['gwp_op'] = 0
            
            temp_res = gwp_op.mul(temp.loc[temp.index.get_level_values('Elements').isin(resources)][res],axis=0)
            temp_tech = temp.loc[temp.index.get_level_values('Elements').isin(technologies)]
            temp_res.dropna(inplace=True)
            temp.update(temp_res['gwp_op'])
            gwp_op_2 = gwp_op.reset_index()
            gwp_op_2=gwp_op_2.pivot(index=['Years'],columns=['Elements'],values='gwp_op')
            temp_gwp = temp_tech.mul(-gwp_op_2)
            temp_tech['gwp_tot'] = temp_gwp[temp_gwp>0].sum(axis='columns')
            temp_tech['gwp_op'] = temp_tech[res]/(temp_tech[temp_tech>0].sum(axis='columns')-temp_tech['gwp_tot']-temp_tech['gwp_op'])*temp_tech['gwp_tot']
            temp.update(temp_tech['gwp_op'])
            gwp_res = temp[[res,'gwp_op']].groupby(['Years']).sum()
            gwp_res['gwp_op'] = gwp_res['gwp_op']/gwp_res[res]
            gwp_res[res] = res
            gwp_res.reset_index(inplace=True)
            gwp_res.set_index(['Years',res],inplace=True)
            gwp_op.update(gwp_res)

        gwp_per_layer.update(gwp_op)
        gwp_per_layer['GWP_EUD'] = gwp_per_layer['gwp_op'].mul(end_uses['end_uses'])
        gwp_per_layer['GWP_TOTAL'] = gwp_per_layer['gwp_op'].mul(total_prod['total_prod'])
        
        update_gwp_remaining = [eud for eud in end_uses.index.get_level_values('Layers').unique() if eud not in update_gwp_res]
        
        for eud in update_gwp_remaining:
            temp = year_balance_full.loc[year_balance_full[eud] > 0]
            temp['gwp_op'] = 0
            temp_res = gwp_op.mul(temp.loc[temp.index.get_level_values('Elements').isin(resources)][eud],axis=0)
            temp_tech = temp.loc[temp.index.get_level_values('Elements').isin(technologies)]
            temp_res.dropna(inplace=True)
            temp.update(temp_res['gwp_op'])
            gwp_op_2 = gwp_op.reset_index()
            gwp_op_2=gwp_op_2.pivot(index=['Years'],columns=['Elements'],values='gwp_op')
            temp_gwp = temp_tech.mul(-gwp_op_2)
            temp_tech['gwp_tot'] = temp_gwp[temp_gwp>0].sum(axis='columns')
            temp_tech['gwp_op'] = temp_tech[eud]/(temp_tech[temp_tech>0].sum(axis='columns')-temp_tech['gwp_tot']-temp_tech['gwp_op'])*temp_tech['gwp_tot']
            temp.update(temp_tech['gwp_op'])
            temp = temp.groupby(['Years']).sum()
            temp = temp[[eud,'gwp_op']]
            temp[eud] = eud
            temp.reset_index(inplace = True)
            temp.set_index(['Years',eud],inplace=True)
            temp.rename(columns={'gwp_op':'GWP_TOTAL'},inplace=True)
            temp.index.names = ['Years','Layers']
            temp['gwp_op'] = temp['GWP_TOTAL'].div(total_prod['total_prod'])
            temp['GWP_EUD'] = temp['gwp_op'].mul(end_uses['end_uses'])
            gwp_per_layer.update(temp)

            
            gwp_op_3 = pd.DataFrame(temp['gwp_op'])
            gwp_op_3.index.names = ['Years','Elements']
            gwp_op = pd.concat([gwp_op, gwp_op_3])
        
        mob_freight = gwp_per_layer.loc[gwp_per_layer.index.get_level_values('Layers').isin(mob_freight_layers)]
        mob_freight = mob_freight.groupby(['Years']).sum()
        mob_freight.reset_index(inplace=True)
        mob_freight['Layers'] = 'MOBILITY_FREIGHT'
        mob_freight.set_index(['Years','Layers'],inplace=True)
        others = gwp_per_layer.loc[~gwp_per_layer.index.get_level_values('Layers').isin(mob_freight_layers)]
        gwp_per_layer = pd.concat([gwp_per_layer,mob_freight])
        
        year_balance_sto['gwp_op'] = 0
        year_balance_sto['gwp_op'] = -year_balance_sto['Cons'].mul(gwp_op['gwp_op'])
        year_balance_sto.index.set_names(['Years','Layers'], inplace=True)
        temp = -year_balance_sto.loc[year_balance_sto['gwp_op'].isna()]['Cons'].mul(gwp_per_layer['gwp_op'])
        temp.dropna(inplace=True)
        year_balance_sto.loc[year_balance_sto['gwp_op'].isna(),'gwp_op'] = temp
        year_balance_sto = year_balance_sto.groupby(['Years']).agg({'Cons': 'sum', 'gwp_op': 'sum'})
        year_balance_sto['GWP_EUD'] = year_balance_sto['gwp_op']
        year_balance_sto['GWP_TOTAL'] = year_balance_sto['gwp_op']
        year_balance_sto['gwp_op'] = year_balance_sto['gwp_op']/-year_balance_sto['Cons']
        year_balance_sto['Cons'] = 'STORAGE'
        year_balance_sto.rename(columns={'Cons':'Layers'},inplace=True)
        year_balance_sto.reset_index(inplace=True)
        year_balance_sto = year_balance_sto.set_index(['Years','Layers'])
        
        gwp_per_layer = pd.concat([gwp_per_layer, year_balance_sto])
        gwp_per_layer.reset_index(inplace=True)
        gwp_per_layer['Years'] = gwp_per_layer['Years'].str.replace('YEAR_', '')
        
        # fig = px.line(gwp_per_layer, x='Years', y = 'gwp_op',color='Layers',markers=True,
        #              title=self.case_study + ' - GWP_op per eud',
        #              color_discrete_map=self.color_dict_full)
        # fig.update_xaxes(categoryorder='array', categoryarray= sorted(gwp_per_layer['Years'].unique()))
        # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        # pio.show(fig)
        
        gwp_per_layer['Layers'] = gwp_per_layer['Layers'].astype("str")
        gwp_per_layer = gwp_per_layer.loc[gwp_per_layer['Layers'] != 'STORAGE']
        
        gwp_per_layer['Layers'] = pd.Categorical(
            gwp_per_layer['Layers'], order_entry)
        gwp_per_layer.sort_values(by=['Layers'], axis=0, 
                               ignore_index=True, inplace=True)
    
        gwp_per_layer['GWP_EUD'] = gwp_per_layer['GWP_EUD']/1000
        
        fig = px.area(gwp_per_layer, x='Years', y = 'GWP_EUD',color='Layers',
                      title=self.case_study + ' - GWP_per_sector',text='Layers',
                      color_discrete_map=self.color_dict_full)
        fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
        fig.update_traces(mode='none')
        fig.update_xaxes(categoryorder='array', categoryarray= sorted(gwp_per_layer['Years'].unique()))
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        
        title = "<b>Yearly emissions</b><br>[MtCO2/y]"
        temp = gwp_per_layer.groupby(['Years']).sum()
        yvals = [0,max(list(map(int,temp['GWP_EUD'])))]
        
        self.custom_fig(fig,title,yvals)
        fig.write_image(self.outdir+"Gwp_per_sector.pdf", width=1200, height=550)
        plt.close()
    
    def graph_cost(self):
        pio.renderers.default = 'browser'
        
        results = self.ampl_collector['Cost_breakdown'].copy()
        category = self.category
        
        c_inv = results.drop(columns=['C_op','C_maint'])
        c_inv.dropna(how='all',inplace=True)
        
        c_op = results.drop(columns=['C_inv','C_maint'])
        c_op.dropna(how='all',inplace=True)
        
        c_maint = results.drop(columns=['C_op','C_inv'])
        c_maint.dropna(how='all',inplace=True)
        
        df_to_plot_inv = pd.DataFrame(index=c_inv.index,columns=c_inv.columns)
        df_to_plot_op = pd.DataFrame(index=c_op.index,columns=c_op.columns)
        df_to_plot_maint = pd.DataFrame(index=c_maint.index,columns=c_maint.columns)
        for y in c_inv.index.get_level_values(0).unique():
            temp_inv = c_inv.loc[c_inv.index.get_level_values('Years') == y,'C_inv']  
            temp_inv = self._remove_low_values(temp_inv,threshold=0)
            df_to_plot_inv.update(temp_inv)
            temp_op = c_op.loc[c_op.index.get_level_values('Years') == y,'C_op']  
            temp_op = self._remove_low_values(temp_op,threshold=0)
            df_to_plot_op.update(temp_op)
            temp_maint = c_maint.loc[c_maint.index.get_level_values('Years') == y,'C_maint']  
            temp_maint = self._remove_low_values(temp_maint,threshold=0)
            df_to_plot_maint.update(temp_maint)
        df_to_plot_inv.dropna(how='all',inplace=True)
        df_to_plot_inv.reset_index(inplace=True)
        df_to_plot_inv['Type'] = 'C_inv'
        df_to_plot_inv.rename(columns={"C_inv": "Cost"},inplace=True)
        df_to_plot_inv['Category'] = df_to_plot_inv['Elements']
        df_to_plot_inv = df_to_plot_inv.replace({"Category": category})
        
        df_to_plot_op.dropna(how='all',inplace=True)
        df_to_plot_op.reset_index(inplace=True)
        df_to_plot_op['Type'] = 'C_op'
        df_to_plot_op.rename(columns={"C_op": "Cost"},inplace=True)
        df_to_plot_op['Category'] = df_to_plot_op['Elements']
        df_to_plot_op = df_to_plot_op.replace({"Category": category})
        
        df_to_plot_maint.dropna(how='all',inplace=True)
        df_to_plot_maint.reset_index(inplace=True)
        df_to_plot_maint['Type'] = 'C_maint'
        df_to_plot_maint.rename(columns={"C_maint": "Cost"},inplace=True)
        df_to_plot_maint['Category'] = df_to_plot_maint['Elements']
        df_to_plot_maint = df_to_plot_maint.replace({"Category": category})
        
        df_to_plot = pd.concat([df_to_plot_inv, df_to_plot_op, df_to_plot_maint], axis=0)
        df_to_plot['Elements'] = df_to_plot['Elements'].astype("str")
        df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
        fig = px.bar(df_to_plot, x='Years', y = 'Cost',color='Elements',facet_row='Type',
                     title=self.case_study + ' - Cost',
                     color_discrete_map=self.color_dict_full)
        fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        
        # fig.write_image(self.outdir+"Cost_breakdown_per_year.pdf", width=1200, height=550)
        fig.write_html(self.outdir+"Cost_breakdown_per_year.html")
        plt.close()
        
        re_share_elec = self.re_share_elec
        
        cost_elec_re = pd.DataFrame(columns=df_to_plot.columns)
        cost_elec_nre = pd.DataFrame(columns=df_to_plot.columns)
        for i,j in enumerate(['2020','2025','2030','2035','2040','2045','2050']):
            total_elec_cost = df_to_plot.loc[(df_to_plot['Years'] == j) & (df_to_plot['Elements'] == 'ELECTRICITY')]['Cost']
            if len(total_elec_cost) > 0:
                temp_re = pd.DataFrame({
                    'Years': j,
                    'Elements' : 'ELECTRICITY',
                    'Cost': re_share_elec[i]*total_elec_cost,
                    'Type': 'C_op',
                    'Category': 'RE_FUELS'
                    })
                temp_nre = pd.DataFrame({
                    'Years': j,
                    'Elements' : 'ELECTRICITY',
                    'Cost': total_elec_cost*(1-re_share_elec[i]),
                    'Type': 'C_op',
                    'Category': 'NRE_FUELS'
                    })
                cost_elec_re = pd.concat([cost_elec_re,temp_re],axis=0)
                cost_elec_nre = pd.concat([cost_elec_nre,temp_nre],axis=0)
        df_to_plot = df_to_plot.set_index(['Years','Elements','Category'])
        cost_elec_nre = cost_elec_nre.set_index(['Years','Elements','Category'])
        df_to_plot.update(cost_elec_nre)

        df_to_plot.reset_index(inplace=True)
        
        df_to_plot = pd.concat([df_to_plot,cost_elec_re],axis=0)
        
        df_to_plot = df_to_plot.groupby(['Years','Category'])['Cost'].sum()
        df_to_plot = df_to_plot.to_frame()
        df_to_plot.reset_index(inplace=True)
        
        df_to_plot['Cost'] = df_to_plot['Cost']/1000
        
        order_entry = ['INFRASTRUCTURE','STORAGE','MOB_PRIVATE','MOB_PUBLIC','MOBILITY_FREIGHT',
                       'ELECTRICITY','HEAT_HIGH_T','HEAT_LOW_T_DHN','HEAT_LOW_T_DECEN',
                       'HVC','METHANOL','AMMONIA','RE_FUELS','NRE_FUELS']
        
        order_entry  = [x for x in order_entry if x in list(df_to_plot['Category'])]
        
        df_to_plot['Category'] = pd.Categorical(
            df_to_plot['Category'], order_entry)
        df_to_plot.sort_values(by=['Category'], axis=0, 
                               ignore_index=True, inplace=True)
        
        fig = px.area(df_to_plot, x='Years', y = 'Cost',color='Category',
                      title=self.case_study + ' - Cost',text='Category',
                      color_discrete_map=self.color_dict_full)
        fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
        fig.update_traces(mode='none')
        fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        
        title = "<b>System cost</b><br>[b€<sub>2015</sub>/y]"
        temp = df_to_plot.groupby(['Years'])['Cost'].sum()
        temp = temp.to_frame()
        yvals = [0, round(temp,1).min().values[0], round(temp.loc['2020','Cost'],1), round(temp,1).max().values[0]]
        fig.write_html(self.outdir+"System_cost.html")
        
        # self.custom_fig(fig,title,yvals)
        # fig.write_image(self.outdir+"System_cost.pdf", width=1200, height=550)
        plt.close()
    
    def graph_cost_return(self):
        pio.renderers.default = 'browser'
        category = self.category
        results = self.ampl_collector['Cost_return'].copy()
        df_to_plot = pd.DataFrame(index=results.index,columns=results.columns)
        for y in results.index.get_level_values(0).unique():
            temp = results.loc[results.index.get_level_values('Years') == y,'C_inv_return']  
            temp = self._remove_low_values(temp,threshold=0)
            df_to_plot.update(temp)
        df_to_plot.update(results['cumsum'])
        df_to_plot.replace(0, np.nan, inplace=True)

        df_to_plot.dropna(how='all',inplace=True)
        df_to_plot.reset_index(inplace=True)
        df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
        df_to_plot['Technologies'] = df_to_plot['Technologies'].astype("str")
        
        # fig = px.bar(df_to_plot, x='Years', y = 'C_inv_return',color='Technologies',
        #              title=self.case_study + ' - Salvage value',
        #              color_discrete_map=self.color_dict_full)
        # fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        # pio.show(fig)
    
        df_to_plot['Category'] = df_to_plot['Technologies']
        
        df_to_plot = df_to_plot.replace({"Category": category})
        df_to_plot.drop(columns=['Technologies'], inplace=True)
        df_to_plot = df_to_plot.groupby(['Years','Category']).sum()
        
        df_to_plot['C_inv_return'] = df_to_plot['C_inv_return']/1000
        df_to_plot['cumsum'] = df_to_plot['cumsum']/1000
        
        order_entry = ['INFRASTRUCTURE','STORAGE','MOB_PRIVATE','MOB_PUBLIC','MOBILITY_FREIGHT',
                       'ELECTRICITY','HEAT_HIGH_T','HEAT_LOW_T_DHN','HEAT_LOW_T_DECEN',
                       'HVC','METHANOL','AMMONIA']
        
        df_to_plot.reset_index(inplace=True)
        
        order_entry  = [x for x in order_entry if x in list(df_to_plot['Category'])]
        
        df_to_plot['Category'] = pd.Categorical(
            df_to_plot['Category'], order_entry)
        df_to_plot.sort_values(by=['Category'], axis=0, 
                               ignore_index=True, inplace=True)
        
        df_to_plot.sort_values(by=['Category','Years'],inplace=True)
        df_to_plot = df_to_plot.set_index(['Years','Category'])
        df_to_plot['Share_return'] = 100*df_to_plot['C_inv_return'].div(df_to_plot['cumsum'])
        df_to_plot.reset_index(inplace=True)
        
        # if len(df_to_plot['Years'].unique()) == 1:
        #     fig = px.bar(df_to_plot, x='Years', y = 'C_inv_return',color='Category',
        #                  title=self.case_study + ' - Salvage value',
        #                  color_discrete_map=self.color_dict_full)
        #     fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        #     plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        #     pio.show(fig)
            
        #     title = "<b>Salvage value</b><br>[b€<sub>2015]"
        #     temp = df_to_plot.groupby(['Years']).sum()
        #     yvals = [0,min(round(temp['C_inv_return'])),max(round(temp['C_inv_return']))]
        #     self.custom_fig(fig,title,yvals,xvals=df_to_plot['Years'].unique(),type_graph = 'bar')
        # else:
        #     fig = px.area(df_to_plot, x='Years', y = 'C_inv_return',color='Category',
        #                  title=self.case_study + ' - Salvage value',
        #                  color_discrete_map=self.color_dict_full)
        #     fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        #     plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        #     pio.show(fig)
            
        #     title = "<b>Salvage value</b><br>[b€<sub>2015]"
        #     temp = df_to_plot.groupby(['Years']).sum()
        #     yvals = [0,min(round(temp['C_inv_return'])),max(round(temp['C_inv_return']))]
        #     self.custom_fig(fig,title,yvals,xvals=df_to_plot['Years'].unique())
            
        
        # fig.write_image(self.outdir+"Cost_return_1.pdf", width=1200, height=550)
        # plt.close()
        
        cost_return_eff = self.cost_return_eff.copy()
        cost_return_eff = cost_return_eff[~cost_return_eff['Years'].isin(['2020','2025'])]
        cost_return_eff['Category'] = cost_return_eff['Technologies']
        cost_return_eff = cost_return_eff.replace({"Category": category})
        cost_return_eff = cost_return_eff.groupby(['Years','Category'])['Cost_return'].sum()
        cost_return_eff = cost_return_eff.to_frame()
        cost_return_eff['Cost_return'] = cost_return_eff['Cost_return']/1000
        
        
        c_inv_cum = self.graph_cost_inv_phase_tech(plot=False)
        c_inv_cum = c_inv_cum[~c_inv_cum['Years'].isin(['2020','2025'])]
        c_inv_cum = c_inv_cum.set_index(['Years','Category'])
        
        df_to_plot_eff = c_inv_cum.merge(cost_return_eff,left_index=True, right_index=True, how='outer')
        df_to_plot_eff[df_to_plot_eff < 0] = 0
        
        df_to_plot_eff.reset_index(inplace=True)
        
        df_to_plot_eff['Category'] = pd.Categorical(
            df_to_plot_eff['Category'], order_entry)
        df_to_plot_eff.sort_values(by=['Category'], axis=0, 
                               ignore_index=True, inplace=True)
        
        df_to_plot_eff.sort_values(by=['Category','Years'],inplace=True)
        df_to_plot_eff = df_to_plot_eff.set_index(['Years','Category'])
        df_to_plot_eff['Share_return'] = 100*df_to_plot_eff['Cost_return'].div(df_to_plot_eff['cumsum'])
        df_to_plot_eff.reset_index(inplace=True)
        
        if len(df_to_plot['Years'].unique()) == 1:
            df_to_plot.sort_values(by=['Share_return'],inplace=True,ascending=False)
            fig = px.bar(df_to_plot, x='Category', y = 'Share_return',color='Category',
                         title=self.case_study + ' - Share salvage value',
                         color_discrete_map=self.color_dict_full)
            # fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            pio.show(fig)
            
            title = "<b>Respective share of salvage value</b><br>[%]"
            temp = df_to_plot.copy()
            yvals = [0,round(float(temp.loc[temp['Category'] == 'MOB_PRIVATE']['Share_return']),1),max(round(temp['Share_return'],1))]
            self.custom_fig(fig,title,yvals,xvals=df_to_plot['Category'].unique(),type_graph = 'bar')
            fig.update_xaxes(showticklabels=False,visible=False)
            fig.write_image(self.outdir+"Cost_return_2.pdf", width=1200, height=550)
            plt.close()
        # else:
        #     # fig = px.bar(df_to_plot, x='Category', y = 'Share_return',color='Category',
        #     #              pattern_shape="Years",barmode='group',
        #     #              title=self.case_study + ' - Share salvage value',
        #     #              color_discrete_map=self.color_dict_full)
        #     order_entry_new = df_to_plot.loc[df_to_plot['Years'] == '2050']
        #     order_entry_new.sort_values(by=['Share_return'],inplace=True,ascending=False)
        #     order_entry_new = order_entry_new['Category']
        #     fig = px.scatter(df_to_plot, x='Category', y = 'Share_return',color='Category',
        #                  symbol="Years",
        #                  title=self.case_study + ' - Share salvage value',
        #                  color_discrete_map=self.color_dict_full,
        #                  category_orders = {'Category': list(order_entry_new)})
        #     fig.update_traces(marker=dict(size=15,
        #                       line=dict(width=2,
        #                                 color='DarkSlateGrey')),
        #           selector=dict(mode='markers'))
        #     # fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        #     plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        #     pio.show(fig)
            
        #     title = "<b>Respective share of salvage value</b><br>[%]"
        #     temp = df_to_plot.groupby(['Category']).sum()
        #     yvals = [0,round(temp.loc[temp['Category'] == 'MOB_PRIVATE']['Share_return'],1),max(round(temp['Share_return'],1))]
        #     self.custom_fig(fig,title,yvals,xvals=df_to_plot['Category'].unique(),type_graph = 'bar')
        
        order_entry_new = df_to_plot_eff.loc[df_to_plot_eff['Years'] == '2050']
        order_entry_new.sort_values(by=['Share_return'],inplace=True,ascending=False)
        order_entry_new = order_entry_new['Category']
        fig = px.scatter(df_to_plot_eff, x='Category', y = 'Share_return',color='Category',
                     symbol="Years",
                     title=self.case_study + ' - Share salvage value',
                     color_discrete_map=self.color_dict_full,
                     category_orders = {'Category': list(order_entry_new)})
        fig.update_traces(marker=dict(size=15,
                          line=dict(width=2,
                                    color='DarkSlateGrey')),
              selector=dict(mode='markers'))
        # fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        
    
    def graph_cost_inv_phase_tech(self, ampl_collector = None, plot=True):
        pio.renderers.default = 'browser'
        category = self.category
        
        if ampl_collector == None:
            ampl_collector = self.ampl_collector
            
        results = ampl_collector['C_inv_phase_tech'].copy()
        df_to_plot = pd.DataFrame(index=results.index,columns=results.columns)
        for p in results.index.get_level_values(0).unique():
            temp = results.loc[results.index.get_level_values('Phases') == p,'C_inv_phase_tech']  
            temp = self._remove_low_values(temp, threshold=0)
            df_to_plot.update(temp)
        df_to_plot.dropna(how='all',inplace=True)
        df_to_plot.reset_index(inplace=True)
        df_to_plot_full = df_to_plot.copy()
        df_to_plot = df_to_plot.loc[~df_to_plot['Phases'].isin(['2015_2020'])]
        df_to_plot['Technologies'] = df_to_plot['Technologies'].astype("str")
        # fig = px.bar(df_to_plot, x='Phases', y = 'C_inv_phase_tech',color='Technologies',
        #               title=self.case_study + ' - C_inv_phase_tech',
        #               color_discrete_map=self.color_dict_full)
        # fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Phases'].unique()))
        # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        # pio.show(fig)
        
        df_to_plot_full['Category'] = df_to_plot_full['Technologies']
        
        df_to_plot_full = df_to_plot_full.replace({"Category": category})
        df_to_plot_full['Phases'] = df_to_plot_full['Phases'].map(lambda x: x[-4:])
        df_to_plot_full.rename(columns={'Phases':'Years'},inplace=True)
        
        
        df_to_plot_full = df_to_plot_full.groupby(['Years','Category'])['C_inv_phase_tech'].sum()
        df_to_plot_full = df_to_plot_full.to_frame()        
        
        df_to_plot_full.reset_index(inplace=True)
        years = df_to_plot_full['Years'].unique()
        categories = df_to_plot_full['Category'].unique()
        
        mi_temp = pd.MultiIndex.from_product([years,categories],names=['Years','Category'])
        temp = pd.DataFrame(0,index=mi_temp,columns=['C_inv_phase_tech'])
        temp.reset_index(inplace=True)
        
        df_to_plot_full = pd.concat([temp,df_to_plot_full])
        df_to_plot_full = df_to_plot_full.set_index(['Years','Category'])
        df_to_plot_full = df_to_plot_full.loc[~df_to_plot_full.index.duplicated(keep='last')]
        
        df_to_plot_full.sort_values(by=['Years'],inplace=True)
        
        for g_name, g_df in df_to_plot_full.groupby(['Category']):
            df_to_plot_full.loc[g_df.index,'cumsum'] = df_to_plot_full.loc[g_df.index,'C_inv_phase_tech'].cumsum()
        
        df_to_plot_full.reset_index(inplace=True)
        df_to_plot_full['cumsum'] = df_to_plot_full['cumsum']/1000
        df_to_plot_full['C_inv_phase_tech'] = df_to_plot_full['C_inv_phase_tech']/1000
        
        
        order_entry = ['INFRASTRUCTURE','STORAGE','MOB_PRIVATE','MOB_PUBLIC','MOBILITY_FREIGHT',
                       'ELECTRICITY','HEAT_HIGH_T','HEAT_LOW_T_DHN','HEAT_LOW_T_DECEN',
                       'HVC','METHANOL','AMMONIA']
        
        order_entry  = [x for x in order_entry if x in list(df_to_plot_full['Category'])]
        
        
        df_to_plot_full['Category'] = pd.Categorical(
            df_to_plot_full['Category'], order_entry)
        df_to_plot_full.sort_values(by=['Category'], axis=0, 
                               ignore_index=True, inplace=True)
        
        df_to_plot_full.sort_values(by=['Category','Years'],inplace=True)
        
        if plot:
            fig = px.area(df_to_plot_full, x='Years', y = 'cumsum',color='Category',
                          title=self.case_study + ' - C_inv_phase_tech',
                          color_discrete_map=self.color_dict_full)
            fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
            fig.update_traces(mode='none')
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot_full['Years'].unique()))
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            pio.show(fig)
            
            title = "<b>Investments over transition</b><br>[b€<sub>2015</sub>]"
            temp = df_to_plot_full.groupby(['Years'])['cumsum'].sum()
            temp = temp.to_frame()
            yvals = [0,round(temp,1).min().values[0],round(temp,1).max().values[0]]
            
            self.custom_fig(fig,title,yvals)
            fig.write_image(self.outdir+"C_inv_phase.pdf", width=1200, height=550)
            plt.close()
        
        return df_to_plot_full
    
    def graph_cost_op_phase(self, ampl_collector = None, plot=True):
        pio.renderers.default = 'browser'
        category = self.category
        
        if ampl_collector == None:
            ampl_collector = self.ampl_collector
        
        results_tech = ampl_collector['C_op_phase_tech'].copy()
        results_tech.reset_index(inplace=True)
        results_tech.rename(columns={'C_op_phase_tech':'C_op','Technologies' :'Elements'},inplace=True)
        results_tech['Phases'] = results_tech['Phases'].map(lambda x: x[-4:])
        results_tech.rename(columns={'Phases':'Years'},inplace=True)

        results_res = ampl_collector['C_op_phase_res'].copy()
        results_res.reset_index(inplace=True)
        results_res.rename(columns={'C_op_phase_res':'C_op','Resources':'Elements'},inplace=True)
        results_res['Phases'] = results_res['Phases'].map(lambda x: x[-4:])
        results_res.rename(columns={'Phases':'Years'},inplace=True)
        
        results_2020 = ampl_collector['Cost_breakdown'].copy()
        results_2020 = results_2020.loc[results_2020.index.get_level_values('Years') == 'YEAR_2020',:]
        results_2020.fillna(0,inplace=True)
        results_2020['C_op'] = results_2020['C_op']+results_2020['C_maint']
        results_2020.drop(columns=['C_inv','C_maint'],inplace=True)
        results_2020.reset_index(inplace=True)
        results_2020['Years'] = results_2020['Years'].map(lambda x: x[-4:])
        
        df_to_plot = pd.concat([results_2020,results_tech,results_res],axis=0,ignore_index=True)
        
        
        df_to_plot['Category'] = df_to_plot['Elements']
        
        df_to_plot = df_to_plot.replace({"Category": category})
    
        re_share_elec = self.re_share_elec
        
        cost_elec_re = pd.DataFrame(columns=df_to_plot.columns)
        cost_elec_nre = pd.DataFrame(columns=df_to_plot.columns)
        for i,j in enumerate(['2020','2025','2030','2035','2040','2045','2050']):
            total_elec_cost = df_to_plot.loc[(df_to_plot['Years'] == j) & (df_to_plot['Elements'] == 'ELECTRICITY')]['C_op']
            if len(total_elec_cost) > 0:
                temp_re = pd.DataFrame({
                    'Years': j,
                    'Elements' : 'ELECTRICITY',
                    'C_op': re_share_elec[i]*total_elec_cost,
                    'Category': 'RE_FUELS'
                    })
                temp_nre = pd.DataFrame({
                    'Years': j,
                    'Elements' : 'ELECTRICITY',
                    'C_op': total_elec_cost*(1-re_share_elec[i]),
                    'Category': 'NRE_FUELS'
                    })
                cost_elec_re = pd.concat([cost_elec_re,temp_re],axis=0)
                cost_elec_nre = pd.concat([cost_elec_nre,temp_nre],axis=0)
        df_to_plot = df_to_plot.set_index(['Years','Elements','Category'])
        cost_elec_nre = cost_elec_nre.set_index(['Years','Elements','Category'])
        df_to_plot.update(cost_elec_nre)

        df_to_plot.reset_index(inplace=True)
        
        df_to_plot = pd.concat([df_to_plot,cost_elec_re],axis=0)
        df_to_plot.sort_values(by=['Years'],inplace=True)

        df_to_plot.drop(columns=['Elements'], inplace=True)
        df_to_plot = df_to_plot.groupby(['Years','Category']).sum()
        
        df_to_plot.reset_index(inplace=True)
        years = df_to_plot['Years'].unique()
        categories = df_to_plot['Category'].unique()
        
        mi_temp = pd.MultiIndex.from_product([years,categories],names=['Years','Category'])
        temp = pd.DataFrame(0,index=mi_temp,columns=['C_op'])
        temp.reset_index(inplace=True)
        
        df_to_plot = pd.concat([temp,df_to_plot])
        df_to_plot = df_to_plot.set_index(['Years','Category'])
        df_to_plot = df_to_plot.loc[~df_to_plot.index.duplicated(keep='last')]
        
        df_to_plot.sort_values(by=['Years'],inplace=True)
        
        for g_name, g_df in df_to_plot.groupby(['Category']):
            df_to_plot.loc[g_df.index,'cumsum'] = df_to_plot.loc[g_df.index,'C_op'].cumsum()
        
        df_to_plot.reset_index(inplace=True)
        df_to_plot['cumsum'] = df_to_plot['cumsum']/1000
        
        
        order_entry = ['NRE_FUELS','RE_FUELS',
                       'INFRASTRUCTURE','STORAGE','MOB_PRIVATE','MOB_PUBLIC','MOBILITY_FREIGHT',
                       'ELECTRICITY','HEAT_HIGH_T','HEAT_LOW_T_DHN','HEAT_LOW_T_DECEN',
                       'HVC','METHANOL','AMMONIA']
        
        order_entry  = [x for x in order_entry if x in list(df_to_plot['Category'])]
        
        df_to_plot['Category'] = pd.Categorical(
            df_to_plot['Category'], order_entry)
        df_to_plot.sort_values(by=['Category'], axis=0, 
                                ignore_index=True, inplace=True)
        
        df_to_plot.sort_values(by=['Category','Years'],inplace=True)
        
        if plot:
            fig = px.area(df_to_plot, x='Years', y = 'cumsum',color='Category',
                          title=self.case_study + ' - C_op_phase_tech',
                          color_discrete_map=self.color_dict_full)
            fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
            fig.update_traces(mode='none')
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            pio.show(fig)
            
            title = "<b>Operation over transition</b><br>[b€<sub>2015</sub>]"
            temp = df_to_plot.copy()
            temp.drop(columns=['Category'], inplace=True)            
            temp = temp.groupby(['Years']).sum()
            NRE_2050 = float(df_to_plot.loc[(df_to_plot['Years'] == '2050') & (df_to_plot['Category'] == 'NRE_FUELS')]['cumsum'])
            RE_2050 = float(df_to_plot.loc[(df_to_plot['Years'] == '2050') & (df_to_plot['Category'] == 'RE_FUELS')]['cumsum'])
            yvals = [0,min(round(temp['cumsum'],1)),
                     round(NRE_2050,1),
                     round(NRE_2050+RE_2050,1),
                     max(round(temp['cumsum'],1))]
            
            self.custom_fig(fig,title,yvals)
            fig.write_image(self.outdir+"C_op_phase.pdf", width=1200, height=550)
            plt.close()
        
        return df_to_plot
    
    def graph_total_cost_per_year(self):
        pio.renderers.default = 'browser'
        
        results = self.ampl_collector['TotalCost'].copy()

        df_to_plot = results.reset_index()
        df_to_plot['index'] = df_to_plot['index'].str.replace('YEAR_', '')
        fig = px.line(df_to_plot, x='index', y = 'TotalCost',
                     title=self.case_study + ' - Total cost per year')
        pio.show(fig)
        fig.write_image(self.outdir+"Cost_total_per_year.pdf", width=1200, height=550)
        plt.close()
    
    def graph_tech_cap(self, ampl_collector = None, plot = True):
        pio.renderers.default = 'browser'
        
        if ampl_collector == None:
            ampl_collector = self.ampl_collector
            
        results = ampl_collector['Assets'].copy()
        dict_tech = self._group_tech_per_eud()
        df_to_plot_full = pd.DataFrame()
        for sector, tech in dict_tech.items():
            temp = results.loc[results.index.get_level_values('Technologies').isin(tech),'F']
            df_to_plot = pd.DataFrame(index=temp.index,columns=['F'])
            for y in temp.index.get_level_values(0).unique():
                temp_y = temp.loc[temp.index.get_level_values('Years') == y]
                temp_y.dropna(how='all',inplace=True)
                if not temp_y.empty:
                    temp_y = self._remove_low_values(temp_y)
                    df_to_plot.update(temp_y)
            df_to_plot.dropna(how='all',inplace=True)
            df_to_plot.reset_index(inplace=True)
            df_to_plot['Technologies'] = df_to_plot['Technologies'].astype("str")
            df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
            
            if plot:
                if len(df_to_plot.index.get_level_values(0).unique()) <= 1:
                    fig = px.bar(df_to_plot, x='Years', y = 'F',color='Technologies',
                                 title=self.case_study + ' - ' + sector+' - Installed capacity',
                                 color_discrete_map=self.color_dict_full)
                else:
                    fig = px.area(df_to_plot, x='Years', y = 'F',color='Technologies',
                             title=self.case_study + ' - ' + sector+' - Installed capacity',
                             color_discrete_map=self.color_dict_full)
                    fig.for_each_trace(lambda trace: trace.update(fillcolor = trace.line.color))
                    fig.update_traces(mode='none')
                    fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
                plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
                if len(df_to_plot.index.get_level_values(0).unique()) >= 1:
                    pio.show(fig)
                    if not os.path.exists(Path(self.outdir+"Tech_Cap/")):
                        Path(self.outdir+"Tech_Cap").mkdir(parents=True,exist_ok=True)
                    # fig.write_image(self.outdir+"Tech_Cap/"+sector+".pdf", width=1200, height=550)
                    fig.write_html(self.outdir+"Tech_Cap/"+sector+".html")
                plt.close()
            
            if len(df_to_plot_full) == 0:
                df_to_plot_full = df_to_plot
            else:
                df_to_plot_full = pd.concat([df_to_plot_full, df_to_plot])
            
        return df_to_plot_full
    
    def graph_new_old_decom(self):
        pio.renderers.default = 'browser'
        
        results = self.ampl_collector['New_old_decom'].copy()
        sto_tech = self.ampl_obj.sets['STORAGE_TECH']
        results = results.loc[~results.index.get_level_values('Technologies').isin(sto_tech),:]
        F_new = results.drop(columns=['F_old','F_decom'])
        F_new.dropna(how='all',inplace=True)
        F_old = results.drop(columns=['F_new','F_decom'])
        F_old.dropna(how='all',inplace=True)
        F_decom = results.drop(columns=['F_new','F_old'])
        F_decom.dropna(how='all',inplace=True)
        df_to_plot_new = pd.DataFrame(index=F_new.index,columns=F_new.columns)
        df_to_plot_old = pd.DataFrame(index=F_old.index,columns=F_old.columns)
        df_to_plot_decom = pd.DataFrame(index=F_decom.index,columns=F_decom.columns)
        for p in F_old.index.get_level_values(0).unique():
            temp_new = F_new.loc[F_new.index.get_level_values('Phases') == p,'F_new']  
            temp_new = self._remove_low_values(temp_new,threshold=0.00)
            df_to_plot_new.update(temp_new)
            temp_old = F_old.loc[F_old.index.get_level_values('Phases') == p,'F_old']  
            temp_old = self._remove_low_values(temp_old,threshold=0.001)
            df_to_plot_old.update(temp_old)
            temp_decom = F_decom.loc[F_decom.index.get_level_values('Phases') == p,'F_decom']  
            temp_decom = self._remove_low_values(temp_decom,threshold=0.001)
            df_to_plot_decom.update(temp_decom)
        df_to_plot_new.dropna(how='all',inplace=True)
        df_to_plot_new.reset_index(inplace=True)
        df_to_plot_new['Type'] = 'F_new'
        df_to_plot_new.rename(columns={"F_new": "Tech_Cap"},inplace=True)
        df_to_plot_old.dropna(how='all',inplace=True)
        df_to_plot_old.reset_index(inplace=True)
        df_to_plot_old['Type'] = 'F_old'
        df_to_plot_old.rename(columns={"F_old": "Tech_Cap"},inplace=True)
        df_to_plot_decom.dropna(how='all',inplace=True)
        df_to_plot_decom.reset_index(inplace=True)
        df_to_plot_decom['Type'] = 'F_decom'
        df_to_plot_decom.rename(columns={"F_decom": "Tech_Cap"},inplace=True)
        df_to_plot = pd.concat([df_to_plot_new,df_to_plot_old, df_to_plot_decom], axis=0)
        df_to_plot['Technologies'] = df_to_plot['Technologies'].astype("str")
        fig = px.bar(df_to_plot, x='Phases', y = 'Tech_Cap',color='Technologies',facet_row='Type',
                     title=self.case_study + ' - New & Old & Decom',
                     color_discrete_map=self.color_dict_full)
        fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Phases'].unique()))
        # fig.update_yaxes(matches=None)
        plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        pio.show(fig)
        fig.write_image(self.outdir+"New_Old_Decom.pdf", width=1200, height=550)
        plt.close()
        
    
    def graph_load_factor(self):
        pio.renderers.default = 'browser'
        
        results = self.ampl_collector['Assets'].copy()
        dict_tech = self.ampl_obj.sets['TECHNOLOGIES_OF_END_USES_TYPE']
        for sector, tech in dict_tech.items():
            temp = results.loc[results.index.get_level_values('Technologies').isin(tech),['F','F_year']]
            temp.dropna(how='all',inplace=True)
            temp['Load_factor'] = temp['F_year']/(8760*temp['F'])
            df_to_plot = pd.DataFrame(index=temp.index,columns=['Load_factor'])
            for y in temp.index.get_level_values(0).unique():
                temp_y = temp.loc[temp.index.get_level_values('Years') == y]
                temp_y.dropna(how='all',inplace=True)
                df_to_plot.update(temp_y)
            df_to_plot['Load_factor'] = df_to_plot['Load_factor'].fillna(0)
            df_to_plot.dropna(how='all',inplace=True)
            df_to_plot.reset_index(inplace=True)
            df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
            df_to_plot['Years'] = df_to_plot['Years'].astype("str")
            fig = px.bar(df_to_plot, x='Technologies', y = 'Load_factor',color='Years',
                     title=self.case_study + ' - ' + sector+' - Load factor',
                     color_discrete_map=self.color_dict_full)
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Technologies'].unique()))
            fig.update_layout(barmode='group', xaxis_tickangle=-45)
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            if len(df_to_plot.index.get_level_values(0).unique()) >= 1:
                pio.show(fig)
                if not os.path.exists(Path(self.outdir+"Load_factor/")):
                    Path(self.outdir+"Load_factor").mkdir(parents=True,exist_ok=True)
                fig.write_image(self.outdir+"Load_factor/"+sector+".pdf", width=1200, height=550)
            plt.close()
    
    def graph_load_factor_2(self):
        pio.renderers.default = 'browser'
        
        results = self.ampl_collector['Assets'].copy()
        dict_tech = self.ampl_obj.sets['TECHNOLOGIES_OF_END_USES_TYPE']
        c_p = self.ampl_obj.get_elem('c_p',type_of_elem = 'Param')
        c_p_t = self.ampl_obj.get_elem('c_p_t',type_of_elem='Param')
        if self.ampl_obj.type_model == 'MO':
            c_p_t = self.ampl_obj.from_agg_to_year(ts=c_p_t)
        else:
            c_p_t = self.ampl_obj.from_agg_to_year(ts=c_p_t.reset_index().set_index(['Typical_days', 'Hours']))
        c_p_inter = c_p_t.groupby(['Technologies']).sum()/8760
        
        threshold = 0.02
        df_unused = pd.DataFrame()
        
        for tech in c_p_inter.index:
            c_p.loc[(slice(None), tech),'c_p'] = c_p_inter.loc[tech].values[0]

        for sector, tech in dict_tech.items():
            temp = results.loc[results.index.get_level_values('Technologies').isin(tech),['F','F_year']]
            temp.dropna(how='all',inplace=True)
            temp['Load_factor_scaled'] = temp['F_year']/(8760*temp['F'])
            
            df_to_plot = pd.DataFrame(index=temp.index,columns=['F','F_year','Load_factor_scaled'])
            df_to_plot.update(temp)
            df_to_plot['Load_factor_scaled'] = df_to_plot['Load_factor_scaled'].fillna(0)
            df_to_plot['Load_factor_scaled'] = df_to_plot['Load_factor_scaled'].div(c_p['c_p'], axis = 0)
            df_to_plot.dropna(how='all',inplace=True)
            df_to_plot.reset_index(inplace=True)
            df_to_plot['Years'] = df_to_plot['Years'].str.replace('YEAR_', '')
            if len(df_unused) == 0:
                df_unused = df_to_plot.loc[df_to_plot['Load_factor_scaled']<threshold]
            else:
                df_unused = pd.concat([df_unused,df_to_plot.loc[df_to_plot['Load_factor_scaled']<threshold]])
            fig = px.bar(df_to_plot, x='Technologies', y = 'Load_factor_scaled',color='Years',
                      title=self.case_study + ' - ' + sector+' - Scaled load factor',
                      color_discrete_map=self.color_dict_full)
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Technologies'].unique()))
            fig.update_layout(barmode='group', xaxis_tickangle=-45)
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            if len(df_to_plot.index.get_level_values(0).unique()) >= 1:
                pio.show(fig)
                if not os.path.exists(Path(self.outdir+"Load_factor_scaled/")):
                    Path(self.outdir+"Load_factor_scaled").mkdir(parents=True,exist_ok=True)
                fig.write_image(self.outdir+"Load_factor_scaled/"+sector+".pdf", width=1200, height=550)
            plt.close()
            
        return df_unused
    
    def graph_comparison(self,output_files,type_of_graph):
        
        switcher = {'C_inv_phase_tech':self.graph_cost_inv_phase_tech,
                    'C_op_phase':self.graph_cost_op_phase,
                    'Tech_cap':self.graph_tech_cap}
        
        grph_mth = switcher.get(str(type_of_graph))
        
        result_0 = self.unpkl(self,pkl_file = output_files[0]) # Results for PF
        result_1 = self.unpkl(self,pkl_file = output_files[1]) # Results for MY
        
        result_0 = grph_mth(ampl_collector = result_0,plot = False)
        result_1 = grph_mth(ampl_collector = result_1,plot = False)
        
        if type_of_graph in ['C_op_phase','C_inv_phase_tech']:
            result_0 = result_0.set_index(['Years','Category'])
            result_1 = result_1.set_index(['Years','Category'])
        elif type_of_graph in ['Tech_cap']:
            result_0 = result_0.set_index(['Years','Technologies'])
            result_1 = result_1.set_index(['Years','Technologies'])
        
        
        df_to_plot = result_1 - result_0
        df_to_plot.reset_index(inplace=True)
        
        if type_of_graph in ['C_op_phase','C_inv_phase_tech']:
            fig = px.line(df_to_plot,x='Years',y='cumsum',color='Category',
                          title='Comparison - {}'.format(type_of_graph),
                          color_discrete_map=self.color_dict_full,markers=True)
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            pio.show(fig)
        elif type_of_graph in ['Tech_cap']:
            fig = px.line(df_to_plot,x='Years',y='F',color='Technologies',
                          title='Comparison - {}'.format(type_of_graph),
                          color_discrete_map=self.color_dict_full,markers=True)
            fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
            plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
            pio.show(fig)
        
        # fig = px.line(df_to_plot,x='Years',y='diff_vs_ref',color='Category',
        #               title='Comparison - {}'.format(type_of_graph),
        #               color_discrete_map=self.color_dict_full)
        # fig.update_xaxes(categoryorder='array', categoryarray= sorted(df_to_plot['Years'].unique()))
        # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        # pio.show(fig)
        
        # fig = px.bar(df_to_plot, x='Category', y = 'cumsum',color='Category',
        #               barmode='group',
        #               title='Comparison - {}'.format(type_of_graph),
        #               color_discrete_map=self.color_dict_full)
        # plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
        # fig.update_layout(barmode='group', bargap=0.30,bargroupgap=0.3)        
        # fig.update_xaxes(ticklabelposition='outside left')
        # pio.show(fig)
        

    def _get_cost_return_for_each_year(self):
        pio.renderers.default = 'browser'
        category = self.category
        
        F_new_old_decom = self.ampl_collector['New_old_decom'].copy()
        F_new = F_new_old_decom.drop(columns=['F_old','F_decom'])
        F_new = F_new.rename_axis(index={'Phases':'Phases_build'},axis=1)
        
        F_decom = self.ampl_collector['F_decom'].copy()
        f_decom_index = F_decom.index.names
        F_decom = F_decom.rename_axis(index={f_decom_index[0]:'Phases_decom',
                                           f_decom_index[1]:'Phases_build'})
        
        
        c_inv = self.ampl_obj.get_elem('c_inv',type_of_elem='Param')
        annualised_factor = self.ampl_obj.get_elem('annualised_factor',type_of_elem='Param')
        p_start = self.ampl_obj.sets['PHASE_START']
        p_stop = self.ampl_obj.sets['PHASE_STOP']
        lifetime = self.ampl_obj.get_elem('lifetime',type_of_elem = 'Param')
        phases = ['2015_2020'] + self.ampl_obj.sets['PHASE']
        remaining = self.ampl_obj.get_elem('remaining_years',type_of_elem = 'Param')
        technologies = self.ampl_obj.sets['TECHNOLOGIES']
        
        mi_cr = pd.MultiIndex.from_product([technologies,phases],names=['Technologies','Phase'])
        cost_return = pd.DataFrame(0,index=mi_cr,columns=['Cost_return'])
        
        for i,j in enumerate(phases):
            cost_return_temp = pd.DataFrame(0,index=technologies,columns=['Cost_return'])
            cost_return_temp.index.names = ['Technologies']
            phases_up_to = phases[:i+1]
            
            for p,q in enumerate(phases_up_to):
                remaining_up_to = remaining.loc[remaining.index.get_level_values('Phase')== phases[-(i-p+1)],:]
                remaining_up_to.rename(index={phases[-(i-p+1)]:q},inplace=True)
                remaining_up_to = remaining_up_to.groupby(['Technologies']).sum()
                
                y_start = p_start[q][0]
                y_stop = p_stop[q][0]
                
                annualised_factor_temp = annualised_factor.loc[q][0]
                
                lifetime_temp = lifetime.loc[lifetime.index.get_level_values('Years') == y_start,:]
                lifetime_temp = lifetime_temp.groupby(['Technologies']).sum()
                
                c_inv_start = c_inv.loc[c_inv.index.get_level_values('Years') == y_start,:]
                c_inv_start = c_inv_start.groupby(['Technologies']).sum()
                c_inv_stop = c_inv.loc[c_inv.index.get_level_values('Years') == y_stop,:]
                c_inv_stop = c_inv_stop.groupby(['Technologies']).sum()
                
                F_new_temp = F_new.loc[F_new.index.get_level_values('Phases_build') == q,:]
                F_new_temp = F_new_temp.groupby(['Technologies']).sum()
                F_decom_temp = F_decom.loc[(F_decom.index.get_level_values('Phases_build') == q) & 
                                           (F_decom.index.get_level_values('Phases_decom').isin(phases_up_to)),:]
                F_decom_temp = F_decom_temp.groupby(['Technologies']).sum()
                
                temp = pd.DataFrame(remaining_up_to['remaining_years'].div(lifetime_temp['lifetime']).mul(
                    F_new_temp['F_new']-F_decom_temp['F_decom'])*annualised_factor_temp*(
                        c_inv_start['c_inv'] + c_inv_stop['c_inv'])/2,columns=['Cost_return'])
                
                cost_return_temp += temp
                
            cost_return_temp['Phase'] = q
            cost_return_temp.reset_index(inplace=True)
            cost_return_temp = cost_return_temp.set_index(['Technologies','Phase'])
            cost_return.update(cost_return_temp)
        
        
        cost_return.sort_values(by=['Technologies','Phase'],inplace=True)
        cost_return.reset_index(inplace=True)
        cost_return['Phase'] = cost_return['Phase'].map(lambda x: x[-4:])
        cost_return.rename(columns={'Phase':'Years'},inplace=True)
        return cost_return
    
    def _remove_low_values(self,df_temp, threshold = None):
        if threshold == None:
            threshold = self.threshold
        max_temp = np.nanmax(df_temp)
        min_temp = np.nanmin(df_temp)
        df_temp = df_temp.loc[(abs(df_temp) > 1e-8) & ((df_temp >= threshold*max_temp) |
                              (df_temp <= threshold*min_temp))]
        return df_temp
    
    def _group_tech_per_eud(self):
        tech_of_end_uses_category = self.ampl_obj.sets['TECHNOLOGIES_OF_END_USES_CATEGORY'].copy()
        del tech_of_end_uses_category["NON_ENERGY"]
        for ned in self.ampl_obj.sets['END_USES_TYPES_OF_CATEGORY']['NON_ENERGY']:
            tech_of_end_uses_category[ned] = self.ampl_obj.sets['TECHNOLOGIES_OF_END_USES_TYPE'][ned]
        tech_of_end_uses_category['INFRASTRUCTURE'] = self.ampl_obj.sets['INFRASTRUCTURE']
        return tech_of_end_uses_category
   
    def _group_sets(self):
        categories = self._group_tech_per_eud()
        categories['STORAGE'] = self.ampl_obj.sets['STORAGE_TECH'].copy()
        categories['RE_FUELS'] = self.ampl_obj.sets['RE_RESOURCES'].copy()
        categories['INFRASTRUCTURE'] = self.ampl_obj.sets['INFRASTRUCTURE'].copy()
        re_fuels = self.ampl_obj.sets['RE_RESOURCES'].copy()
        resources = self.ampl_obj.sets['RESOURCES'].copy()
        nre_fuels = [res for res in resources if res not in re_fuels]
        categories['NRE_FUELS'] = nre_fuels
        
        categories_2 = dict()
        
        for k in categories:
            for j in categories[k]:
                if k == 'HEAT_LOW_T':
                    if j in self.ampl_obj.sets['TECHNOLOGIES_OF_END_USES_TYPE']["HEAT_LOW_T_DHN"]:
                        categories_2[j] = 'HEAT_LOW_T_DHN'
                    else:
                        categories_2[j] = 'HEAT_LOW_T_DECEN'
                elif k == 'MOBILITY_PASSENGER':
                    if j in self.ampl_obj.sets['TECHNOLOGIES_OF_END_USES_TYPE']["MOB_PUBLIC"]:
                        categories_2[j] = 'MOB_PUBLIC'
                    else:
                        categories_2[j] = 'MOB_PRIVATE'
                else :
                    categories_2[j] = k
        
        return categories_2
    
    
    def dict_color_full(self):
        year_balance = self.ampl_collector['Year_balance']
        elements = year_balance.index.get_level_values(1).unique()
        color_dict_full = dict.fromkeys(elements)
        categories = ['Sectors','Electricity','Heat_low_T','Heat_high_T','Mobility','Freight','Ammonia',
                   'Methanol','HVC','Conversion','Storage','Storage','Storage_daily','Resources',
                   'Infrastructure','Years','Phases']
        for c in categories:
            color_dict_full.update(self.dict_color(c))
        
        color_dict_full['END_USES'] = 'lightsteelblue'
        
        return color_dict_full
    
    @staticmethod
    def dict_color(category):
        color_dict = {}
        
        if category == 'Electricity':
            color_dict = {"NUCLEAR":"deeppink", "CCGT":"darkorange", "CCGT_AMMONIA":"slateblue", "IMPORTED_COAL_CENTRAL" : "black", "LOCAL_COAL_CENTRAL" : "dimgray", "PV" : "yellow", "WIND_ONSHORE" : "lawngreen", "WIND_OFFSHORE" : "green", "HYDRO_RIVER" : "blue", "GEOTHERMAL" : "firebrick", "ELECTRICITY" : "dodgerblue"}
        elif category == 'Heat_low_T':
            color_dict = {"DHN_HP_ELEC" : "blue", "DHN_COGEN_GAS" : "orange", "DHN_COGEN_WOOD" : "sandybrown", "DHN_COGEN_WASTE" : "olive", "DHN_COGEN_WET_BIOMASS" : "seagreen", "DHN_COGEN_BIO_HYDROLYSIS" : "springgreen", "DHN_BOILER_GAS" : "darkorange", "DHN_BOILER_WOOD" : "sienna", "DHN_BOILER_OIL" : "blueviolet", "DHN_DEEP_GEO" : "firebrick", "DHN_SOLAR" : "gold", "DEC_HP_ELEC" : "cornflowerblue", "DEC_THHP_GAS" : "lightsalmon", "DEC_COGEN_GAS" : "goldenrod", "DEC_COGEN_OIL" : "mediumpurple", "DEC_ADVCOGEN_GAS" : "burlywood", "DEC_ADVCOGEN_H2" : "violet", "DEC_BOILER_GAS" : "moccasin", "DEC_BOILER_WOOD" : "peru", "DEC_BOILER_OIL" : "darkorchid", "DEC_SOLAR" : "yellow", "DEC_DIRECT_ELEC" : "deepskyblue"}
        elif category == 'Heat_high_T':
            color_dict = {"IND_COGEN_GAS":"orange", "IND_COGEN_WOOD":"peru", "IND_COGEN_WASTE" : "olive", "IND_BOILER_GAS" : "moccasin", "IND_BOILER_WOOD" : "goldenrod", "IND_BOILER_OIL" : "blueviolet", "IND_BOILER_COAL" : "black", "IND_BOILER_WASTE" : "olivedrab", "IND_DIRECT_ELEC" : "royalblue"}
        elif category == 'Mobility':
            color_dict = {"TRAMWAY_TROLLEY" : "dodgerblue", "BUS_COACH_DIESEL" : "dimgrey", "BUS_COACH_HYDIESEL" : "gray", "BUS_COACH_CNG_STOICH" : "orange", "BUS_COACH_FC_HYBRIDH2" : "violet", "TRAIN_PUB" : "blue", "MOTORCYCLE" : "olivedrab", "CAR_GASOLINE" : "black", "CAR_DIESEL" : "lightgray", "CAR_NG" : "moccasin", "CAR_METHANOL":"orchid", "CAR_HEV" : "salmon", "CAR_PHEV" : "lightsalmon", "CAR_BEV" : "deepskyblue", "CAR_FUEL_CELL" : "magenta"}
        elif category == 'Freight':
            color_dict = {"TRAIN_FREIGHT" : "royalblue", "BOAT_FREIGHT_DIESEL" : "dimgrey", "BOAT_FREIGHT_NG" : "darkorange", "BOAT_FREIGHT_METHANOL" : "fuchsia", "TRUCK_DIESEL" : "darkgrey", "TRUCK_FUEL_CELL" : "violet", "TRUCK_ELEC" : "dodgerblue", "TRUCK_NG" : "moccasin", "TRUCK_METHANOL" : "orchid"}
        elif category == 'Ammonia':
            color_dict = {"HABER_BOSCH":"tomato", "AMMONIA" : "slateblue", "AMMONIA_RE" : "blue"}
        elif category == 'Methanol':
            color_dict = {"SYN_METHANOLATION":"violet","METHANE_TO_METHANOL":"orange","BIOMASS_TO_METHANOL":"peru", "METHANOL" : "orchid", "METHANOL_RE" : "mediumvioletred"}
        elif category == "HVC":
            color_dict = {"OIL_TO_HVC":"blueviolet", "GAS_TO_HVC":"orange", "BIOMASS_TO_HVC":"peru", "METHANOL_TO_HVC":"orchid"}
        elif category == 'Conversion':
            color_dict = {"H2_ELECTROLYSIS" : "violet", "H2_NG" : "magenta", "H2_BIOMASS" : "orchid", "GASIFICATION_SNG" : "orange", "PYROLYSIS" : "blueviolet", "ATM_CCS" : "black", "INDUSTRY_CCS" : "grey", "SYN_METHANOLATION" : "mediumpurple", "SYN_METHANATION" : "moccasin", "BIOMETHANATION" : "darkorange", "BIO_HYDROLYSIS" : "gold", "METHANE_TO_METHANOL" : "darkmagenta",'SMR':'orange'}
        elif category == 'Storage':
            color_dict = {"TS_DHN_SEASONAL" : "indianred", "BATT_LI" : "royalblue", "BEV_BATT" : "deepskyblue", "PHEV_BATT" : "lightskyblue", "PHS" : "dodgerblue", "TS_DEC_HP_ELEC" : "blue", "TS_DHN_DAILY" : "lightcoral", "TS_HIGH_TEMP" : "red", "SEASONAL_NG" : "orange", "SEASONAL_H2" : "violet", "SLF_STO" : "blueviolet", "TS_DEC_DIRECT_ELEC":"darkgoldenrod", "TS_DEC_THHP_GAS": "orange", "TS_DEC_COGEN_GAS":"coral", "TS_DEC_COGEN_OIL":"darkviolet", "TS_DEC_ADVCOGEN_GAS":"sandybrown", "TS_DEC_ADVCOGEN_H2": "plum", "TS_DEC_BOILER_GAS": "tan", "TS_DEC_BOILER_WOOD":"peru", "TS_DEC_BOILER_OIL": "darkviolet", "GAS_STORAGE": "orange", "H2_STORAGE": "violet", "CO2_STORAGE": "lightgray", "GASOLINE_STORAGE": "gray", "DIESEL_STORAGE": "silver", "AMMONIA_STORAGE": "slateblue", "LFO_STORAGE": "darkviolet"}
        elif category == 'Storage_daily':
            color_dict = {"BATT_LI" : "royalblue", "BEV_BATT" : "deepskyblue", "PHEV_BATT" : "lightskyblue", "TS_DEC_HP_ELEC" : "blue", "TS_DHN_DAILY" : "lightcoral", "TS_HIGH_TEMP" : "red", "TS_DEC_DIRECT_ELEC":"darkgoldenrod", "TS_DEC_THHP_GAS": "orange", "TS_DEC_COGEN_GAS":"coral", "TS_DEC_COGEN_OIL":"darkviolet", "TS_DEC_ADVCOGEN_GAS":"sandybrown", "TS_DEC_ADVCOGEN_H2": "plum", "TS_DEC_BOILER_GAS": "tan", "TS_DEC_BOILER_WOOD":"peru", "TS_DEC_BOILER_OIL": "darkviolet"}
        elif category == 'Resources':
            color_dict = {"ELECTRICITY" : "deepskyblue", "GASOLINE" : "gray", "DIESEL" : "silver", "BIOETHANOL" : "mediumorchid", "BIODIESEL" : "mediumpurple", "LFO" : "darkviolet", "GAS" : "orange", "GAS_RE" : "moccasin", "WOOD" : "peru", "WET_BIOMASS" : "seagreen", "LOCAL_COAL" : "black", "IMPORTED_COAL" : "dimgrey", "URANIUM" : "deeppink", "WASTE" : "olive", "H2" : "violet", "H2_RE" : "plum", "AMMONIA" : "slateblue", "AMMONIA_RE" : "blue", "METHANOL" : "orchid", "METHANOL_RE" : "mediumvioletred", "CO2_EMISSIONS" : "gainsboro", "RES_WIND" : "limegreen", "RES_SOLAR" : "yellow", "RES_HYDRO" : "blue", "RES_GEO" : "firebrick", "ELEC_EXPORT" : "chartreuse","CO2_ATM": "dimgray", "CO2_INDUSTRY": "darkgrey", "CO2_CAPTURED": "lightslategrey", "RE_FUELS": 'green','NRE_FUELS':'black'}
        elif category == 'Sectors':
            color_dict = {"ELECTRICITY" : "deepskyblue", "HEAT_HIGH_T":"red","HEAT_LOW_T_DECEN":"lightpink", "HEAT_LOW_T_DHN":"indianred", "MOB_PUBLIC":"gold", "MOB_PRIVATE":"goldenrod","MOBILITY_FREIGHT":"darkgoldenrod", "NON_ENERGY": "darkviolet", "INFRASTRUCTURE":"grey","HVC":"cyan",'STORAGE':'chartreuse'}
        elif category == 'Infrastructure':
            color_dict = {'EFFICIENCY': 'lime','DHN': 'orange','GRID': 'gold'}
        elif category == 'Years':
            color_dict = {'YEAR_2020': 'blue','YEAR_2025': 'orange','YEAR_2030': 'green', 'YEAR_2035': 'red', 'YEAR_2040': 'purple', 'YEAR_2045': 'brown', 'YEAR_2050':'pink'}
        elif category == 'Phases':
                color_dict = {'2015_2020': 'blue','2020_2025': 'orange','2025_2030': 'green', '2030_2035': 'red', '2035_2040': 'purple', '2040_2045': 'brown', '2045_2050':'pink'}
            
        return color_dict
    
    
    @staticmethod
    def custom_fig(fig,title,yvals,xvals=['2020','2025','2030','2035','2040',
                        '2045','2050'], ftsize=18,annot_text=None,annot_pos=None,type_graph = None):
    
        def round_repdigit(n, ndigits=0):     
            if n != 0:
                i = int(np.ceil(np.log10(abs(n))))
                x = np.round(n, ndigits-i)
                if i-ndigits >= 0:
                    x = int(x)
                return x     
            else:
                return 0
            
        gray = 'rgb(90,90,90)' 
        color = gray
        
        fig.update_layout(
            xaxis_color=color, yaxis_color=color,
            xaxis_mirror=False, yaxis_mirror=False,
            yaxis_showgrid=False, xaxis_showgrid=False,
            yaxis_linecolor='white', xaxis_linecolor='white',
            xaxis_tickfont_size=ftsize, yaxis_tickfont_size=ftsize,
            showlegend=False,
            title_text=title,titlefont=dict(family="Raleway",size=ftsize+10)
        )
        
        fig.update_xaxes(dict(ticks = "inside", ticklen=10))
        fig.update_xaxes(tickangle= 0,tickmode = 'array',tickwidth=2,tickcolor=gray,
                            tickfont=dict(
                                  family="Rawline",
                                  size=ftsize
                              ))
        fig.update_yaxes(dict(ticks = "inside", ticklen=10))
        fig.update_yaxes(tickangle= 0,tickmode = 'array',tickwidth=2,tickcolor=gray,
                            tickfont=dict(
                                  family="Rawline",
                                  size=ftsize
                              ))
        fig.update_layout(
            yaxis = dict(
                tickmode = 'array',
                tickvals = fig.layout.yaxis.tickvals,
                ticktext = list(map(str,yvals))
                ))
        
                
        factor=0.05
        nrepdigit = 0
        
        fig.update_yaxes(tickvals=yvals)
        
        xstring = isinstance(fig.data[0].x[0],str)
        
        if xstring: ## ONLY VALID IF THE FIRST TRACE HAS ALL VALUES
            xvals = xvals
            xmin = 0
            xmax = len(xvals) - 1
        else:
            xvals = pd.Series(sum([list(i.x) for i in fig.data],[]))
            xmin = xvals.min()
            xmax = xvals.max()
            xampl = xmax-xmin

        
        if xstring:
            if fig.layout.xaxis.range is None:
                if type_graph == 'bar':
                    fig.layout.xaxis.range = [xmin-factor*15, xmax+factor*15]
                else:
                    fig.layout.xaxis.range = [xmin-factor*3, xmax+factor*3]
            if fig.layout.xaxis.tickvals is None:
                fig.layout.xaxis.tickvals = xvals
        else:
            if fig.layout.xaxis.range is None:
                fig.layout.xaxis.range = [xmin-xampl*factor, xmax+xampl*factor]
            if fig.layout.xaxis.tickvals is None:
                fig.layout.xaxis.tickvals = [round_repdigit(x, nrepdigit) for x in [xmin, xmax]]
        
        if(isinstance(fig.layout.xaxis.tickvals, np.ndarray)):
            if (fig.layout.xaxis.tickvals.dtype != 'O'):
                fig.layout.xaxis.tickvals = sorted(fig.layout.xaxis.tickvals)
        else:
            fig.layout.xaxis.tickvals = sorted(fig.layout.xaxis.tickvals)
            
        fig.layout.xaxis.range = sorted(fig.layout.xaxis.range)
        
        
        yvals = yvals
        ymin = min(yvals)
        ymax = max(yvals)
        yampl = ymax-ymin
        
        if fig.layout.yaxis.range is None:
            fig.layout.yaxis.range = [ymin-yampl*factor, ymax+yampl*factor]
        if fig.layout.yaxis.tickvals is None:
            fig.layout.yaxis.tickvals = [round_repdigit(y, nrepdigit) for y in [ymin, ymax]]
            
        fig.layout.yaxis.tickvals = sorted(fig.layout.yaxis.tickvals)
        fig.layout.yaxis.range = sorted(fig.layout.yaxis.range)
        
        
        fig.update_layout(xaxis_title=None, yaxis_title=None)
        
        fig.add_shape(x0=fig.layout.xaxis.range[0],x1=fig.layout.xaxis.range[0],
                  y0=fig.layout.yaxis.tickvals[0],y1=fig.layout.yaxis.tickvals[-1],
                  type='line',layer="above",
                  line=dict(color=color,width=2),opacity=1)
        
        if type_graph == None:
            fig.add_shape(x0=xmin,x1=xmax,
                      y0=fig.layout.yaxis.range[0],y1=fig.layout.yaxis.range[0],
                      type='line',layer="above",
                      line=dict(color=color, width=2),opacity=1)
        
        fig.update_layout(margin_b = 10, margin_r = 30, margin_l = 30)#,margin_pad = 20)

