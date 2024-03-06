

Cost_breakdown = z_Results['Cost_breakdown']
year_balance = z_Results['Year_balance']

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
Cost_elec_approx = Cost_elec_approx / Cost_elec_approx.loc['YEAR_2020']
Cost_elec_approx = Cost_elec_approx.round(2)
Cost_elec_approx.to_csv(pth_output_all+'/'+country+'/Outputs_for_GEMMES/Elec_price_evolution.csv')

 # z_elec = year_balance.copy()
 # z_elec = z_elec.loc[:, z_elec.columns=='ELECTRICITY']
 # z_elec = z_elec.loc[z_elec['ELECTRICITY']>=0]
 # z_elec = z_elec.groupby(level=[0]).sum()
 
 # elec_price = z_elec.copy()
 # elec_price['ELECTRICITY'] = Cost_elec_approx.values / z_elec['ELECTRICITY']

### Cooling se comporte comme Cost_elec_approx

year_balance_LTH = year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_LTH_tech)]
year_balance_LTH = year_balance_LTH[['ELECTRICITY','GAS','WASTE','WET_BIOMASS','WOOD']]
year_balance_LTH.loc[year_balance_LTH['ELECTRICITY']>0,'ELECTRICITY'] = np.nan
year_balance_LTH = year_balance_LTH.groupby(level=[0]).sum()
year_balance_LTH.drop(columns=['WASTE','WET_BIOMASS'], inplace=True) # Negligible amount

year_balance_private_mob = year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_private_mob_tech)]
year_balance_private_mob = year_balance_private_mob[['DIESEL','ELECTRICITY','GAS','GASOLINE','H2','METHANOL']]
year_balance_private_mob = year_balance_private_mob.groupby(level=[0]).sum()
year_balance_private_mob.drop(columns=['DIESEL','H2','METHANOL'], inplace=True) # Negligible amount

year_balance_public_mob = year_balance.iloc[year_balance.index.get_level_values('Elements').isin(list_public_mob_tech)]
year_balance_public_mob = year_balance_public_mob[['DIESEL','ELECTRICITY','GAS','GASOLINE','H2']]
year_balance_public_mob = year_balance_public_mob.groupby(level=[0]).sum()
year_balance_public_mob.drop(columns=['H2'], inplace=True) # Negligible amount

year_balance_private_mob['ELECTRICITY'] = year_balance_private_mob['ELECTRICITY'] / year_balance_LTH.loc['YEAR_2020','ELECTRICITY'] ##### Careful #####
year_balance_private_mob[['GAS','GASOLINE']] = year_balance_private_mob[['GAS','GASOLINE']] / year_balance_private_mob.loc['YEAR_2020',['GAS','GASOLINE']]
year_balance_private_mob = year_balance_private_mob.round(2)
year_balance_private_mob.to_csv(pth_output_all+'/'+country+'/Outputs_for_GEMMES/Quantities_for_private_mob_evolution.csv')

year_balance_public_mob[['GAS','ELECTRICITY']] = year_balance_public_mob[['GAS','ELECTRICITY']] / year_balance_LTH.loc['YEAR_2020',['GAS','ELECTRICITY']] ##### Careful #####
year_balance_public_mob[['DIESEL','GASOLINE']] = year_balance_public_mob[['DIESEL','GASOLINE']] / year_balance_public_mob.loc['YEAR_2020',['DIESEL','GASOLINE']]
year_balance_public_mob = year_balance_public_mob.round(2)
year_balance_public_mob.to_csv(pth_output_all+'/'+country+'/Outputs_for_GEMMES/Quantities_for_public_mob_evolution.csv')

year_balance_LTH = year_balance_LTH / year_balance_LTH.loc['YEAR_2020']
year_balance_LTH = year_balance_LTH.round(2)
year_balance_LTH.to_csv(pth_output_all+'/'+country+'/Outputs_for_GEMMES/Quantities_for_heating_evolution.csv')


year_balance_boum = z_Results['Year_balance'].copy()
year_balance_boum.loc[year_balance_boum['GASOLINE']<0,'GASOLINE'] = np.nan
year_balance_boum = year_balance_boum.groupby(level=[0]).sum()
# year_balance_boum.drop(index=['YEAR_2015'],inplace=True)

prices_resources = pd.read_csv(pth_model+'/'+country+'/Prices_resources.csv')
prices_resources.set_index('Unnamed: 0', inplace=True)
prices_resources = prices_resources.iloc[1: , :]

bidul = year_balance_boum['GASOLINE'].values * prices_resources['GASOLINE'].values

Cost_breakdown = Cost_breakdown.iloc[Cost_breakdown.index.get_level_values('Elements').isin(['GASOLINE'])]
Cost_breakdown *= 5
Cost_breakdown['C_op_shifted'] = Cost_breakdown['C_op'].shift(1)
Cost_breakdown['mean'] = (Cost_breakdown['C_op_shifted'] + Cost_breakdown['C_op']) / 2
C_op_gasoline = C_op.iloc[C_op.index.get_level_values('Resources').isin(['GASOLINE'])]




