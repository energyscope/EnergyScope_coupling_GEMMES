
.. _app:estd_tk_data:

Input Data - Turkey
++++++++++++++++++++++++++++++++++++++++++++
..
.. role:: raw-latex(raw)
   :format: latex
   
This section details the input data utilized in applying the LP modeling framework to the case study of Turkey.
The primary objective is to provide data for modelling a prospective Turkish energy system for the year 2034.
Additionally, we provide the necessary data to reproduce the historical Turkish energy system for the year 2019,
serving as a validation of EnergyScope's accuracy in modeling this intricate system.

Since many data are common between the Colombian and Turkish case studies, we only present
the data and assumptions that differ between the two. If nothing is indicated, the same data and assumptions as for
Colombia can be used.

Like for Colombia, all costs are expressed as constant US Dollars for the year 2021 (USD\ :sub:`2021`). Costs which were initially
expressed in €\ :sub:`2015` were converted using the historical exchange rate for 2015 equal to 1.11 :cite:`ecb2015`.
The evolution of the cost from 2015 to 2021 for *technologies* is computed using the CEPCI, like for Colombia. However, the evolution
of the cost from 2015 to 2021 for *resources* is computed using the evolution of fuel costs for the case of Cyprus (as a proxi for Turkey),
with data from :cite:`IEA_oil_prices`.

.. _app:sec:ESTD_TK_resources:

Resources
=========

Local renewable resources
-------------------------

The energy transition heavily relies on renewable energies, which makes their
deployment potential a critical parameter. Yet, this potential was still very 
little used in 2019. As highlighted by :cite:t:`IEA_TK_2021`,
*in 2019, the share of fossil fuels in total primary energy supply [of Turkey] was
83%, which ranked the ninth-highest among IEA member countries.*

Solar, wind, hydro and geothermal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Table %s <tab:renewableTechPotentialIn2034_TK>` gives the Turkish potential for solar, wind, hydro and geothermal energy. These data are put into perspective with the values used for the calibration to the year 2019.
      
.. container::

   .. csv-table:: Comparison of installed capacity of technologies for renewable electricity generation in 2019 with their maximum potentials. Abbreviations: maximum (max.), photovoltaic panel (PV), District Heating Network (DHN), Concentrated Solar Power (CSP).
      :header: **Technology**, **2019**\ , **max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableTechPotentialIn2034_TK
   
      hydro dam , 15.7 [39a]_ , 19.9 [39c]_ , [GW]
      hydro river , 12.8 [39a]_ , 16.3 [39c]_ , [GW]
      rooftop PV , 6.0 [39b]_ , :math:`\approx`\ 120 [39d]_ , [GW]
      utility scale PV , 0 , :math:`\approx`\ 1350 [39d]_ , [GW]
      onshore wind , 7.6 [39e]_ , 48 [39e]_ , [GW]
      offshore wind , 0 , 66.2 [39f]_ , [GW]
      geothermal for electricity, 1.2 [39g]_ ,  4.2 [39h]_ , [GW]
      geothermal for heat (with DHN), 3.05 [39i]_ , 30.8 [39h]_ , [GW]
      CSP parabolic trough , 0, 107 [39d]_, [GW]
      CSP solar tower , 0, 107 [39d]_, [GW]
      Solar thermal (decentralised), 5.3 [39j]_ , no limit imposed, [GW]

   .. [39a]
      Data from :cite:`TK_gov_RE`
      
   .. [39b]
      Data from :cite:t:`IEA_TK_2021`

   .. [39c]
      A hydro potential of 35.1 [GW] is given by :cite:t:`Rebiere2019thesis`. We split it between hydro dam and hydro river using the 55%-45% shares from 2019.
      
   .. [39d]
      The real constraint on solar potential is not a constraint on installable capacity, but a constraint on available area, as described below.

   .. [39e]
      Ministry of Energy and Natural Resources, cited by :cite:t:`IEA_TK_2021`.

   .. [39f]
      :cite:t:`emeksiz_2019` computes an offshore wind potential of 9.2 GW with rather conservative asumptions (max. water depth of 50 m). It is in line with the 10 GW potential computable based on the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI. To this number is added the 57 GW potential of floating wind offshore, reported by the Offshore Wind Energy Association (DÜRED) in :cite:`Daily_Sabah_2021`.

   .. [39g]
      Computed using the electricity production from geothermia in 2019, given in :cite:`IEA_world_energy_balances_TK`, and the capacity factor of 85% sourced in :numref:`Table %s <tab:elec_prod_re_TK>` 

   .. [39h]
      :cite:t:`IEA_TK_2021` reports a 35 GW potential for geothermal energy in Turkey. :cite:t:`Balat_2004` affirms that 12% of this potential is appropriate for electricity generation and 88% for heat production.
      
   .. [39i]
      Computed using the heat generation from geothermia in 2019, given in :cite:`IEA_world_energy_balances_TK` (including heat for agriculture), and the capacity factor of 85% given in Table :numref:`%s <tbl:dhn_cogen_boiler>` 
      
   .. [39j]
      Computed using the heat generation from decentralised solar thermal in 2019, given in :cite:`IEA_world_energy_balances_TK`, and the capacity factor of 20.8% whose determination is given in Subsection "Technologies - Heating and cogeneration"
      

As described by eqs. :eq:`eq:solarAreaRooftopLimited` - :eq:`eq:solarAreaGroundHighIrrLimited`, the potential of solar technologies is constrained by the available areas for their deployment. The values for these available areas are given in :numref:`Table %s <tab:solarArea_TK>`. The values of maximum installed capacities indicated in :numref:`Table %s <tab:renewableTechPotentialIn2034_TK>` are a simplified translation of these equations into [GW] constraints.

.. container::

   .. csv-table:: Values of the parameters which constrain the solar potential of Turkey. Abbreviations: solar multiple (sm), high irradiation (high irr.), photovoltaic panel (PV), Concentrated Solar Power (CSP).
      :header: "Parameter", "Value", "Units"
      :widths: 15 15 15
      :name: tab:solarArea_TK

      ":math:`solar_{area,rooftop}`", "630 [40a]_ ", ":math:`[km^2]`"
      ":math:`solar_{area,ground}`", "7300 [40a]_ ", ":math:`[km^2]`"
      ":math:`solar_{area,ground,high~irr}`", "580 [40a]_ ", ":math:`[km^2]`"
      
   .. [40a]
      Computed based on the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI.
      
Note that the ground areas given in :numref:`Table %s <tab:renewableTechPotentialIn2034>`
are not the total areas occupied by the solar power plants, but only the areas occupied 
by the solar panels themselves. After taking into account the *ground cover ratio*, we can compute that
the value given for :math:`solar_{area,ground}` corresponds to covering
4.6% of Turkey's land surface with solar power plants (not taking into account the rooftop area
used by rooftop PV).

Biomass and non-renewable waste
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Table %s <tab:renewableResourcesPotentialIn2034_TK>` gives the Turkish potential for biomass and non-renewable waste, together with their values used for the calibration to the year 2019. Note that contrary to the case of Colombia, bioethanol and biodiesel are assumed to be imported from abroad. They are therefore not given in :numref:`Table %s <tab:renewableResourcesPotentialIn2034_TK>`, which gives only the local biomass potential.

.. container::

   .. csv-table:: Biomass and waste resources consumed in 2019 and their potential.
      :header: **Resources** , **2019** , **Max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableResourcesPotentialIn2034_TK

		woody biomass , 40.0 [41a]_ , 215.0 [41b]_ , [TWh]
		wet biomass , 0 , 250.0 [41c]_ , [TWh]
		non-renewable waste, 0.1 [41a]_ , 53.8 [41d]_ , [TWh]
   
   .. [41a]
      Computed based on :cite:`IEA_world_energy_balances_TK`

   .. [41b]
      We aggregate in woody biomass the numbers from :cite:`Biomass_Atlas_2017` for: dedicated woody and lignocellulosic biomass crops, total forestry potential, secondary residues from the wood industry, secondary residues from the sawmill industry, secondary residues from other wood processing industries, secondary residues from agro-industries, biowaste and post-consumer wood.
      
   .. [41c]
      We aggregate in woody biomass the numbers from :cite:`Biomass_Atlas_2017` for: straw & stubbles, prunings, dedicated crops, agro-industrial residues and road-side verge grass.
      
   .. [41d]
      Data could not be found for Turkey. The value taken for Italy by :cite:`borasio2022deep` was chosen to have a relevant order of magnitude, since Turkey and Italy had a grossly similar Total Energy Consumption in 2019 according to IEA data.
      
      
      
In order to compute the potentials for woody biomass and wet biomass, we take from :cite:`Biomass_Atlas_2017` the base potentials in 2030, defined by the authors as the sustainable (thus conservative) technical potential. The values expressed in kt dry mass were taken. Then, these kt dry mass were converted into energy units using a LHV of 18 [MJ/kg] for wet biomass and 19 [MJ/kg] for woody biomass. These values of LHV are the average values of the corresponding biomass types, extracted from :cite:`Phyllis2`.

The corresponding costs for 2034 and GHG emissions are given in :numref:`Table %s <tab:costs_resources_biomass_TK>`.

.. container::

   .. csv-table:: Cost and GHG emissions of biomass and waste resources, in 2034.
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` [42a]_ , **CO**:sub:`2direct` [42b]_
      :widths: 15 15 15 15
      :name: tab:costs_resources_biomass_TK
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		woody biomass , 33.9 [42c]_, 12 , 390
		wet biomass , 3.5 [42d]_, 12 , 390
		non-renewable waste, 28.1 , 150 , 260 [42e]_

.. [42a]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion. Note that this metric accounts for negative 
   upstream emissions, hence the very low value for the biomass resources.
   
.. [42b]
   Direct emissions related to combustion :cite:`Quaschning2015`. These data are not used in EnergyScope Turkey (since the capacity of technology CCS_industrial is set to zero), but they help us to check that the calibration of EnergyScope to the 2019 Turkish energy system is correct.

.. [42c]
   Taken as 85% of the cost for Belgium, in accordance with :cite:`Biomass_Atlas_2017`.
   
.. [42d]
   Taken as 50% of the cost for Belgium, in accordance with :cite:`Biomass_Atlas_2017`.

.. [42e]
   Assuming that the energy content can be assimilated to plastics.


Domestic fossil resources
-------------------------

Around 10% of Turkish oil consumption and 1% of gas consumption were covered by domestic supply in 2019 :cite:`IEA_TK_2021`. 
As a matter of simplicity, we assume that all oil and gas consumed in Turkey is imported. We thus neglect the new gas fields
which were recently discovered and might enter in operation in the coming decade. The only domestic fossil fuel resource considered
in EnergyScope is therefore coal. Local Turkish coal is typically low-quality lignite. Machines using local coal are therefore differentiated from
machines using imported coal in terms of cost and efficiency (see below). :numref:`Table %s <tab:costs_local_fossil_TK>` gives the cost and
GHG emissions associated to domestic Turkish coal.

.. container::

   .. csv-table:: Cost and GHG emissions of domestically produced fossil fuels, in 2034.
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` [43a]_ , **CO**:sub:`2direct` [43b]_
      :widths: 15 15 15 15
      :name: tab:costs_local_fossil_TK
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		local coal , 8.6 [43c]_ , 389 [43d]_, 434 [43d]_

.. [43a]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion. Note that this metric accounts for negative 
   upstream emissions, hence the null value for the biomass resources.
   
.. [43b]
   Direct emissions related to combustion from :cite:`Quaschning2015`, unless specified otherwise. These data are not used in EnergyScope Turkey (since the capacity of technology CCS_industrial is set to zero), but they help us to check that the calibration of EnergyScope to the 2019 Turkish energy system of is correct.

.. [43c]
   Computed based on data from :cite:`KAT2023101538`
   
.. [43d]
   Computed based on data from :cite:`KAT2023101538`, which indicate that domestic Turkish coal is 18% more emissive than imported coal.
   

Imported resources
------------------

Imported resources include coal, hydrocarbons (natural gas, gasoline, diesel, light fuel oil), bio-fuels and uranium. No constraint is set regarding their 
availability. Their costs in 2034 and GHG emissions are given in :numref:`Table %s <tab:costs_imported_resources_TK>`.

.. container::

   .. csv-table:: Cost and GHG emissions of imported resources, in 2034. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` [43a]_ , **CO**:sub:`2direct` [43b]_
      :widths: 15 15 15 15
      :name: tab:costs_imported_resources_TK
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		coal , 12.2 [43c]_, 401 , 360
		natural gas , 24.3 [43e]_, 267 , 200
		gasoline , 59.8 [43f]_, 345 , 250
		diesel , 65.9 [43f]_, 315 , 260 [43x]_
		LFO , 39.8 [43f]_, 312 , 260
		bioethanol , 133.4 [43g]_, 0 , 250
		biodiesel , 148.5 [43g]_, 0 , 260
		uranium, 4.7, 4, 0
   
.. [43e] 
   Figure 9.5 from :cite:`IEA_TK_2021` indicates that the costs (excluding taxes) of gas in Turkey and Belgium were the same for industry, but 2.5 lower for households in Turkey in 2019.
   The cost of gas is therefore taken as 70% of the Belgian cost.
   
.. [43f] 
   Figure 8.10 from :cite:`IEA_TK_2021` indicates that the costs (excluding taxes) of gasoline, diesel and LFO in Turkey and Belgium were practically the same in 2019. Hence, the Belgian costs are used.

.. [43g] 
   Taken as equal to Belgian costs.

.. [43x] 
   Emission intensity taken from :cite:`TK_CO2_2020` (year 2018)


Electricity imports and exports
-------------------------------

The availability of the cross-border electricity imports and exports, when defined as "resources", is considered as infinite. Indeed, the real constraint comes from the grid infrastructure for imports and exports, as expressed by eqs. :eq:`eq:elecImpLimited` and :eq:`eq:elecExpLimited`. The values of parameters for these equations are given in :numref:`Table %s <tab:elecImpExpParams_TK>`.

.. container::

   .. csv-table:: Values of the parameters which constrain cross-border electricity imports and exports.
      :header: "Parameter", "Value", "Units"
      :widths: 15 15 15
      :name: tab:elecImpExpParams_TK

      ":math:`elec_{import,max}`", "1.17 [44a]_ ", "[GW]"
      ":math:`elec_{export,max}`", "1.17 [44a]_ ", "[GW]"
      ":math:`f_{max}(HVAC)`", "9.0 [44b]_ ", "[GW]"
      
   .. [44a]
      Cross-border connection capacities in 2019 indicated in :cite:t:`IEA_TK_2021`.
      
   .. [44b]
      Value inspired from the interconnection projects described in :cite:t:`IEA_TK_2021`.


The costs and GHG emissions of electricity imports and exports are given in :numref:`Table %s <tab:costs_elec_import_export_TK>`.

.. container::

   .. csv-table:: Cost and GHG emissions associated to electricity imports and exports, in 2034. Abbreviations: Electricity (elec.).
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` , **CO**:sub:`2direct`
      :widths: 15 15 15 15
      :name: tab:costs_elec_import_export_TK
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		elec imports , 102.6 [45b]_, 206 [45a]_ , 0
		elec exports , 92.4 [45c]_ , 0 , 0

.. [45a] This value is based on the CO :sub:`2` intensity of the EU electricity grid and its projected decrease, in line with the EU's Climate objectives.
         Indeed, :cite:t:`IEA_TK_2021` indicates that in 2019, most of the electricity imports of Turkey came from Bulgaria, which is part of the European grid.

.. [45b]
   Taken equal as the Belgian cost.
    
.. [45c]
   The cost of electricity exports is assumed to be equal to 90% of the cost of electricity imports, to account for cross-border tariffs.


.. _sec:app1_end_uses_TK:

Energy demand and political framework
=====================================

Aggregated values for the calibration of the 2019 EUDs are given in :numref:`Table %s <tab:eud_2019>`. Details and assumptions for these EUDs are given in the following sub-sections, as well as their yearly profiles.

.. container::

   .. csv-table:: EUD in 2019. Abbreviations: end-use type (EUT)
      :header: **EUT** , **Households** , **Services** , **Industry**, **Transportation** , "Units"
      :widths: 30 20 20 20 15 10
      :name: tab:eud_2019
		
		electricity - baseload , 20535.1,27069,44803.8,933.4,[GWh]
		electricity - variable , 16944.5,22336,36969.9,770.2,[GWh]
		space heating , 205997.3,61791.1,23670.2,0,[GWh]
		hot water , 122077,34139.4,0,0,[GWh]
		process heating , 0,2645.3,62440.8,0,[GWh]
		space cooling , 74275.4,126474.1,39988.6,0,[GWh]
		process cooling , 0,8667.6,8447.4,0,[GWh]
		passenger mobility , 0,0,0,346531.6 ,[Mpkm]
		freight , 0,0,0,278728.1 ,[Mtkm]
		non-energy demand , 0,0,58996.0,2088.0,[GWh] 
   
The aim is to compute the evolution of these EUDs across years with GEMMES, which will then feed them to EnergyScope. However, as a first approximation,
the 2034 EUDs can simply be computed by multiplying the values of :numref:`Table %s <tab:eud_2021>` by 1.42. This factor is computed based on the projection
of final energy consumption given in :cite:`TK_national_energy_plan`.

.. _ssec:app1_electricity_end_uses_TK:

Electricity
-----------

Final electricity consumption in 2019 is taken from :cite:`Brockway_2024`. The electricity used for heating and cooling in 2019 is subtracted from it, based
on the values given in :cite:`Brockway_2024`. This aggregated electricity EUD is then divided between baseload and variable load according to the proportions
retrieved from the EPIAS Transparency Portal for the year 2019 (https://seffaflik.epias.com.tr/transparency/). This gives a share of 55% baseload and
45% variable load. Finally, the values for baseload and variable load are divided between the different economic sectors by using the proportions given in :cite:t:`IEA_world_energy_balances_TK` (and aggregating together industry, agriculture and fishing).

For :math:`\%_{elec}`, we normalize the real electricity demand from the year 2019, available on the EPIAS Transparency Portal
(https://seffaflik.epias.com.tr/transparency/).

.. _ssec:app1_heating_end_uses_TK:

Heating and cooling
-------------------

The aggregated EUDs for different heating and cooling types were retrieved from :cite:`Brockway_2024`. The time series :math:`\%_{sh}` and :math:`\%_{sc}` are 
based on our own computations, following the method described in :cite:`borasio2022deep`.

.. math::
    HDD = \sum_{t \in \text{T}}(T_{comf}(t) - T_{out}(t))\quad\text{if}\quad T_{out}(t) < 15°C\\
    HDD = 0\quad\text{if}\quad T_{out}(t) \geq 15°C
    :label: eq:HDD_TK
    
.. math::
    CDD = \sum_{t \in \text{T}}(T_{out}(t) - T_{comf}(t))\quad\text{if}\quad T_{out}(t) > 24°C\\
    CDD = 0\quad\text{if}\quad T_{out}(t) \leq 24°C
    :label: eq:CDD_TK

Hourly outdoor temperature time series were retrieved from :cite:`Renewables_ninja` for the cities of 
Istanbul, Izmir, Ankara, Ordu, Sanliurfa, Van and Antalya. The HDD and CDD time series for these individual
cities were then computed following eqs. :eq:`eq:HDD_TK` and :eq:`eq:CDD_TK`. The HDD and CDD time series for
Turkey were computed by taking a weighted average of these 7 time series, with weights 
(0.32, 0.13, 0.15, 0.09, 0.10, 0.08, 0.13). These weights were computed as proportional to the populations of the
areas surrounding those cities.

.. _ssec:app1_demand_mobility_TK:

Mobility
--------

Aggregated numbers are retrieved from :cite:`TK_traffic_survey_2021` for the demand for passenger mobility and freight.
These numbers are only for road transportation. The demand for passenger mobility is therefore divided by 98% to obtain
the total EUD for passenger mobility, which includes rail transport but excludes domestic aviation transport. Similarly,
the demand for freight is divided by 96% to obtain the total EUD for freight, which includes rail transport but excludes
coastal shipping, aviation and pipeline transport.

For :math:`\%_{pass}`, we assume that the passenger mobility EUD has the same profile for every day of the
year. This daily profile is taken from data for Switzerland (data from Figure 12 of :cite:`USTransportation`).
For :math:`\%_{fr}`, we take a uniform value over the 8760 hours of the year.

Non-energy
----------

Non-energy EUD value in 2019 is taken from :cite:t:`IEA_world_energy_balances_TK`. We assume it to be uniformly spread over the
8760 hours of the year.

.. _app:ESTD_TK_data_technologies:

Technologies
============

The technologies are regrouped by their main output types.

Electricity generation
----------------------

The electricity generation technologies are regrouped into two categories depending
on the resources used: renewable or not.

.. _ssec:app1_renewables_TK:

Renewables
~~~~~~~~~~

:numref:`Table %s <tab:elec_prod_re_TK>` gives the data for the renewable electricity generation technologies
modelled in EnergyScope Turkey, together with their sources. The data for :math:`f_{max}` were already
given in :numref:`Table %s <tab:renewableTechPotentialIn2034_TK>` ("max. potential"). The :math:`f_{min}`
values for renewable electricity technologies in 2034 are equal to their installed capacity in 2019,
already given in :numref:`Table %s <tab:renewableTechPotentialIn2034_TK>`. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.

.. container::

   .. csv-table:: Renewable electricity production technologies in 2034. Abbreviations: concentrated solar power 
      with parabolic trough (CSP PT), concentrated solar power with solar tower (CSP ST).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [47a]_ , **lifetime**, **c**:sub:`p` [2019], **c**:sub:`p` [2034]
      :widths: 19 18 24 23 15 15 15
      :name: tab:elec_prod_re_TK
		 
		  , [USD\ :sub:`2021`/MWh :sub:`fuel`], [USD\ :sub:`2021`/MWh :sub:`fuel`], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%], [%]
		 Hydro dam, 2333 [47e]_, 11.7 [47e]_, 1693, 40 [47b]_, 35.6 [47c]_ , 35.6 [47g]_
		 Hydro river, 1750 [47e]_, 8.2 [47e]_, 1263, 40 [47b]_, 35.6 [47c]_ , 44.0 [47h]_
		 Rooftop PV, 1040 [47d]_, 13.7 [47d]_, 2081, 40 [47d]_, 17.6 [47c]_ , 17.0 [47i]_
		 Utility scale PV, 474 [47d]_, 11.9 [47d]_, 2081, 40 [47d]_, 17.6 [47c]_ , 19.0 [47i]_
		 Onshore wind, 947 [47e]_, 23.7 [47d]_, 623, 30 [47f]_, 33.5 [47c]_ , 34.8
		 Offshore wind, 1177 [47e]_, 71.3 [47d]_, 623, 30 [47f]_, 41.2 , 41.2
		 Geothermal, 3738 [47e]_, 138.7 [47e]_, 24929, 30, 86 [47j]_ , 86 [47j]_
		 CSP PT, 1473 [47k]_, 88.3 [47k]_, 0 [47m]_ , 25, 23.7 [47l]_ , 23.7 [47l]_
		 CSP ST, 1083 [47k]_, 88.8 [47k]_, 0 [47m]_ , 25, 23.7 [47l]_ , 23.7 [47l]_
		 
.. [47a]
   Data from :cite:`weidema_ecoinvent_2013`

.. [47b]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_grande_2014`
   
.. [47c]
   Computed using the installed capacity reported in :cite:`TK_gov_RE` and the yearly electricity generation given by :cite:t:`IEA_TK_2021`

.. [47d]
   Data from :cite:`Danish_energy_agency_2023`
   
.. [47e]
   Data taken from :cite:`KAT2023101538` and converted from 2019 to 2021 USD using the CEPCI  
   
.. [47f]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_energie_2013`
   
.. [47g]
   Taken as equal to the value in 2019
   
.. [47h]
   Value taken from :cite:`CCDR_TK`
   
.. [47i]
   Retrieved from the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI	
   
.. [47j]
   Data from :cite:`association_des_entreprises_electriques_suisses_aes_electricite_2012`
	
.. [47k]
   The cost and its repartition between :math:`c_{inv}`	and :math:`c_{maint}` is taken from :cite:`CSP_IRENA`. The
   evolution through time is the one from :cite:`CSP_IEA`, assuming an identical evolution as the one of the LCOE.
   These data are cross-checked with the ones of the Figure 4 of :cite:`boretti_techno_economic_2021` and of the 
   Figure 2 of :cite:`viebahn_potential_2011`.
   
.. [47l]
   This value of :math:`c_{p}` is the mean value of the :math:`c_{p,t}` time series computed below.
   
.. [47m]
   Not computed yet. To be completed in the near future.	
   


:numref:`Table %s <tab:elec_prod_re_TK>` includes the values of the yearly capacity factor (:math:`c_p`) of technologies.
As described in the Model Formulation Section, the value of :math:`c_p` for intermittent renewables is in fact equal to one, while
it is the value of their hourly load factor, :math:`c_{p,t}`, which is binding. The value of :math:`c_p` given in 
:numref:`Table %s <tab:elec_prod_re_TK>` for intermittent renewables is in fact the mean value of :math:`c_{p,t}` over the year.
The yearly profile (which sums up to one) of :math:`c_{p,t}` for intermittent renewables is computed as follows.

Power production profile of PV [10]_ were retrieved from :cite:`Renewables_ninja` for the cities of 
Istanbul, Izmir, Ankara, Ordu, Sanliurfa, Van and Antalya. The yearly profile of :math:`c_{p,t}`
for PV in Turkey was then computed by taking a weighted average of these 7 time series, with weights 
(0.32, 0.13, 0.15, 0.09, 0.10, 0.08, 0.13). These weights were taken proportional to the populations of the
geographical regions encompassing these cities, given in :cite:`TK_geog_regions`.

The yearly profile of :math:`c_{p,t}` for onshore wind was computed in the same way, retrieving from
:cite:`Renewables_ninja` power production profiles of wind turbines [11]_ instead of PV.

The same 7 time series as for onshore wind were used for offshore wind, but the weighted average to obtain the yearly profile of :math:`c_{p,t}`
was computed by using the weights (0.2,0.2,0,0.3,0,0,0.3). These weights are proportional to the length of coastline near each city, according to
numbers from :cite:`TK_coast`.

Regarding CSP, the (non-normalized) time series for :math:`c_{p,t}` is computed with the oemof thermal :cite:`oemf_thermal` and 
pvlib :cite:`pvlib` packages (to extract pvgis data :cite:`pvgis`). These time series give the thermal GWh of energy produced
by thermal GW of *Collector* installed. These time series are computed for the 6 locations of respective (lat,lon):
(37.72, 27.9), (37.38, 30.75), (37.73, 33.69), (38.45, 36.95), (38.12, 39.62) and (38.25, 43.08). These locations were identified 
as the ones having the highest CSP potential, based on the open-source database from :cite:`dupont_2020`. The weighted mean
of these six time series is then computed, using the weights (0.05, 0.11, 0.3 , 0.13, 0.33, 0.09) which reflect the
respective potentials of these different locations, according to :cite:`dupont_2020`. The obtained mean time series is the
yearly :math:`c_{p,t}` time series for CSP in Turkey in 2034.

Finally, for hydro dam and hydro river, daily incoming water flow to hydro-electric facilities in Turkey was taken from the Turkish TSO website
for the 365 days of the year. These data were normalized to give a yearly profile :math:`c_{p,t}`, taking the same value for each hour of a same
day.

.. _ssec:app1_non-renewable_TK:

Non-renewable
~~~~~~~~~~~~~

:numref:`Table %s <tab:elec_prod_nre_TK>` gives the data for the non-renewable electricity generation technologies
modelled in EnergyScope Turkey, together with their sources. The minimum installed capacity (:math:`f_{min}`)
is zero, while the maximum installed capacity (:math:`f_{max}`) is set to a value high enough for each 
technology to potentially cover the entire demand - except for nuclear energy. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.
The efficiencies of each technology in 2019 and 2034 are given as well.

The values of (:math:`f_{min}`) and (:math:`f_{max}`) of nuclear energy are set differently. Indeed, the choice to build new
nuclear power plants is not simply based on a cost-benefit analysis. It results from political decisions, often closely linked to
international relations. We set :math:`f_{min} = 4.8` [GW] and :math:`f_{max} = 7.2` [GW] for nuclear power in Turkey in 2034.
Indeed, the Akuyu power plant of capacity 4.8 [GW] should be operational by then :cite:`CCDR_TK`. The value of 7.2 [GW] corresponds
to the capacity envisaged in Turkey's National Energy Plan for 2034 :cite:`TK_national_energy_plan`, although no plan to build a new
nuclear central besides Akuyu has yet been announced. We leave it to the cost optimization of EnergyScope to decide the capacity 
to be installed between those two bounds.

.. container::

   .. csv-table:: Non-renewable electricity production technologies in 2034. Abbreviations: combined cycle gas turbine (CCGT), capacity (capa.).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [48a]_ , **lifetime** [48b]_, **c**:sub:`p`, **efficiency** (2019), **efficiency** (2034), :math:`CO_{2-direct}` [48c]_
      :widths: 11 17 24 22 12 8 8 8 14
      :name: tab:elec_prod_nre_TK
		 
		  , [USD\ :sub:`2021`/kW :sub:`e`], [USD\ :sub:`2021`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%], [%], [tCO2/MWh :sub:`e`]
		 CCGT, 875 [48d]_, 27.8 [48d]_, 184, 25, 85, 53 [48e]_ , 53 [48e]_, 0.377
		 CCGT ammonia [48f]_, 875, 27.8, 184, 25, 59, 50, 50, 0
		 Local coal central, 1400 [48d]_, 64.6 [48d]_, 332, 35, 86 [48b]_, 39 [48h]_, 39 [48h]_, 0.9
		 Imported coal central, 1283 [48d]_, 41.5 [48g]_, 332, 35, 86 [48b]_, 45 [48e]_, 45 [48e]_, 0.9
		 Nuclear, 8751 [48d]_ , 145.1 [48k]_ , 708, 60 [48i]_ , 84 [48j]_ , 37, 37 , 0
		 
.. [48a]
   Data from :cite:`weidema_ecoinvent_2013`
   
.. [48b]
   Data from :cite:`bauer_new_2008`
   
.. [48c]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of electricity produced. Emissions computed based
   on resource used and specific emissions given in Table 9.
   
.. [48d]
   Data taken from :cite:`KAT2023101538` and converted from 2019 to 2021 USD using the CEPCI   
   
.. [48e] 
   Computed based on Background Note 4, p. 22 of :cite:`CCDR_TK`

.. [48f]
   Use of Ammonia in CCGT is at its early stage. Mitsubishi is developping 
   a 40 MW turbine and promises similar efficiency as gas CCGT :cite:`nose2021development`. 
   However, the high emissions of NOx requires a removal equipment which will reduce the 
   power plant efficiency. As gas and ammonia CCGT will be similar, we expect a similar cost and lifetime. 
   The only exception is the efficiency, which is assumed at 50% instead of 63% for a Belgian gas CCGT :cite:`ikaheimo2018power`.
   
.. [48g]
   1.2 GW\ \ :math:`_{\text{e}}` IGCC power plant
   :cite:`u.s._eia_-_energy_information_administration_updated_2013`.
   *c*:sub:`maint` is fixed cost (48.1 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y) +
   variable cost (0.82 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y assuming 7500
   h/y).   
   
.. [48h]
   Computed based on :cite:`IEA_world_energy_balances_TK`. It is not surprising to obtain such a low efficiency, 
   since the coal mined locally in Turkey is low-quality lignite.

.. [48i]
   Data from :cite:`association_des_enterprises_electriques_suisses_energie_2014`

.. [48j]
   Data for the year 2012 from :cite:`swiss_federal_office_of_energy_sfoe_swiss_2014` 
   
.. [48k]
   Data from :cite:`iea_-_international_energy_agency_iea_2014-1`

According to :cite:`IEA_TK_2021`, electricity generation in 2019 in Turkey was of 304.3 [TWh],
among which 37.2% from coal, 29.2% from hydro, 18.7% from natural gas, 7.2% from wind, 3.5% from solar
and 4% from geothermal, biomass and waste. The installed capacities of CCGT, local coal central
and imported coal central are calibrated based on this information.


Heating and cogeneration
------------------------

Tables :numref:`%s <tbl:ind_cogen_boiler>`, :numref:`%s <tbl:dhn_cogen_boiler>` and :numref:`%s <tbl:dec_cogen_boiler>`
previously gave the characteristics of the heating and cogeneration technologies modelled in EnergyScope. By using the
data from :cite:`Brockway_2024`, we can determine that the following capacities were installed in 2019:

.. container::

   .. csv-table:: Installed capacities of heating and cogeneration technologies in 2019. Abbreviations: Natural Gas (NG), Combined Heat and Power (CHP), Heat Pump (HP). 
      :header: **Technology**, **Installed capacity in 2019** [GW]
      :widths: 20 20
      :name: tab:intalled_capa_heating_TK
		 
		Industrial boiler NG, 7.4
		Industrial boiler coal, 3.0
		DHN CHP NG, 1.7
		DHN boiler wood, 5.9
		Decentralized HP, 5.0
		Decentralized boiler NG, 28.3
		Decentralized boiler oil, 23.3
		Coal stove, 15.0

Similarly to intermittent renewable electricity technologies, the time series for :math:`c_{p,t}` for solar thermal facilities must be computed.
To do so, global horizontal irradiation (GHI) profiles are retrieved from :cite:`Renewables_ninja` for the cities of Istanbul, Izmir, Ankara, Ordu, 
Sanliurfa, Van and Antalya. A weighted average of these 7 time series is then computed, with weights (0.32, 0.13, 0.15, 0.09, 0.10, 0.08, 0.13). These weights were taken proportional to the populations of the areas surrounding those cities. The :math:`c_{p,t}` time series for solar thermal in Turkey is obtained
by dividing this weighted average time series by 8760 (number of hours in the year) and by 1000 (standard irradiation). The mean capacity factor of solar 
thermal (i.e. the mean of its :math:`c_{p,t}` time series) is thus found to be 20.8%.


Cooling
-------

Based on data from :cite:`Brockway_2024`, we could determine the 2019 coefficient of performance of some cooling technnologies:

.. container::

   .. csv-table:: 2019 efficiency of cooling technologies. Abbreviations: Natural Gas (NG), Combined Heat and Power (CHP), Heat Pump (HP). 
      :header: **Technology**, **Installed capacity in 2019** [GW]
      :widths: 20 20
      :name: tab:intalled_capa_cooling_TK
		 
		Decentralised electricity cooling, 470
		Process cooling, 92.7

.. _sec:app1_vehicles_mobility_TK:

Transport
---------

Passenger mobility
~~~~~~~~~~~~~~~~~~

:numref:`Table %s <tbl:passenger_vehicles_TK>` gives the minimum and maximum shares
of each vehicle type in 2034. The shares in 2019 are also given.

.. container::

   .. table:: Fuel and electricity consumption for passenger mobility technologies in 2034 :cite:`codina_girones_strategic_2015`, and minimum/maximum shares allowed in the model. Abbreviations: Fuel Cell (FC), Hybrid Electric Vehicle (HEV), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), public (pub.).
      :name: tbl:passenger_vehicles_TK

      ================  ============================ ============================ ===============================
      **Vehicle type**  **f**:math:`_\textbf{min,%}` **f**:math:`_\textbf{max,%}` **f**:math:`_\textbf{%}` (2019) 
                        [%]                          [%]	                  [%]		
      Gasoline car      0                            100                          12 [52b]_ 
      Diesel car        0                            100                          50 [52b]_ 
      NG car            0                            100                          38 [52b]_ 
      HEV               0                            100                          0
      PHEV              0                            100                          0
      BEV               0                            100                          0
      FC car            0                            100                          0
      Methanol car      0                            100                          0
      Tram & Trolley    0                            0 [52a]_                     0
      Diesel bus        0                            100                          89 [52c]_ 
      Diesel HEV bus    0                            100                          0
      NG bus            0                            100                          0
      FC bus            0                            100                          0
      Train pub.        0                            50 [52a]_                    11 [52c]_ 
      ================  ============================ ============================ ===============================

.. [52a]
   Our own expert guesses.
   
.. [52b]
   Computed based on the information contained in :cite:`IEA_world_energy_balances_TK` and the Background Note 2 of :cite:`CCDR_TK`

.. [52c]
   Computed based on data from :cite:`TK_traffic_survey_2021`

Finally, the share of passenger mobility which can be supplied by public mobility is bounded by :math:`\%_{public,min}` and :math:`\%_{public,max}`. Similarly, the maximum share of private passenger mobility that can be supplied by motorcycles is given by :math:`\%_{private,motorc,max}` (see Eq. :eq:`eq:f_max_perc_motorcycle` in the Model Formulation Section). The values and assumptions for these three parameters are given in :numref:`Table %s <tab:passenger_mob_shares_TK>`.

.. container::

   .. csv-table:: Limiting shares for passenger mobility in 2019 and 2034.
      :header: **Parameter**, **Value in 2019**, **Value in 2034**
      :widths: 20 20 20 
      :name: tab:passenger_mob_shares_TK
		 
		 :math:`\%_{public_{min}}`, 37% [53a]_, 5% [53b]_
		 :math:`\%_{public_{max}}`, 37% [53a]_, 50% [53b]_
		 :math:`\%_{private_{motorc_{max}}}`, 0%, 0%
		 
.. [53a]
   Computed based on data from :cite:`TK_traffic_survey_2021`

.. [53b]
   Our own expert guesses.
   

Freight
~~~~~~~

The share of freight which can be supplied by different modes are bounded by the values :math:`\%_{fr,X,min}` and :math:`\%_{fr,X,max}`. 
These values are given in :numref:`Table %s <tab:freight_shares_TK>` for 2019 and 2034.

.. container::

   .. csv-table:: Limiting shares for freight in 2019 and 2034.
      :header: **Parameter**, **Value in 2019**, **Value in 2034**
      :widths: 20 20 20
      :name: tab:freight_shares_TK
		 
		 :math:`\%_{fr_{rail_{min}}}`, 0.04 [54a]_, 0
		 :math:`\%_{fr_{rail_{max}}}`, 0.04 [54a]_,  0.25 [54b]_
		 :math:`\%_{fr_{boat_{min}}}`, 0    [54c]_, 0
		 :math:`\%_{fr_{boat_{max}}}`, 0    [54c]_, 0
		 :math:`\%_{fr_{road_{min}}}`, 0, 0
		 :math:`\%_{fr_{road_{max}}}`, 1, 1
		  
.. [54a]
   Background Note 2 of :cite:`CCDR_TK`
   
.. [54b]
   Our own expert guess
   
.. [54c]
   Freight by boat is not included in EnergyScope Turkey because no data could be found

.. _sec:app1_ned_TK:

Non-energy demand
-----------------

Given the important
petroleum refining activity in Turkey, we assume that all non-energy EUD in 2019 was HVC. We keep
the same assumption for the year 2034.

.. _sec:app1_storage_TK:

Storage
-------

The values of :math:`f_{min/max}(Hydro~Dam)` and :math:`f_{min/max}(Dam~Storage)` are linked.
The ratio between the two is taken to be 450 [h]. The 2034 values of
:math:`f_{min}(Hydro~Dam)=15.7` [GW] and :math:`f_{max}(Hydro~Dam)=19.9` [GW] therefore translate into 
:math:`f_{min}(Dam~Storage)=7055` [GWh] and :math:`f_{max}(Dam~Storage)=8974` [GWh].

On top of hydro dams, it is envisaged that pumped hydro storage systems could be developed in Turkey. The main data
for these potential projects are taken from :cite:`PHS_TK` and summarised in :numref:`Table %s <tab:stodatabasic_TK>`.

.. container::

   .. csv-table:: Foreseen Pumped Hydro Storage (PHS) characteristics in 2034 in Turkey.
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr`, :math:`\eta_{sto-in}`, :math:`\eta_{sto-out}`, **t**:sub:`sto-out`, **lifetime**, **f**:sub:`max`
      :widths: 15 15 15 25 10 10 10 10 10
      :name: tab:stodatabasic_TK

		 , [USD\ :sub:`2021`/kWh], [USD\ :sub:`2021``/kWh/y], [kgCO :sub:`2`-eq/kWh], [%], [%], [h], [y], [GWh]
		 PHS, 129.7 [55c]_, 0 [55a]_, 8.33 [55b]_, 7 [55c]_, 86.6 [55d]_, 86.6 [55d]_, 50 [55e]_, 91 [55f]_
		 

.. [55a]
   Neglected.

.. [55b]
   Own calculation based on Hydro Dams emissions from previous work
   :cite:`Limpens2019,Moret2017PhDThesis`.

.. [55c]
   Data from :cite:`PHS_TK`
   
.. [55d]
   A round-trip efficiency of 75% (i.e. :math:`0.866^2`) is taken, identical to the one of the Coo-Trois-Ponts hydroelectric power station in Belgium.
   
.. [55e]
   Data verified in Table B1 of
   :cite:`Zakeri2015`.

.. [55f]
   Computed based on potential projects informed in :cite:`PHS_TK`


.. _App:Data:OtherParam_TK:

Others 
------

.. _ssec:app1_grid_TK:

Electricity grid
~~~~~~~~~~~~~~~~

Several data regarding cross-border interconnections are given in Section
*Electricity imports and exports*. The costs of new High-Voltage
transfer capacity (HVAC Line) with neighbouring countries are computed to be
:math:`c_{inv} = 2~\text{€}_{2015}`/kW/km and 
:math:`c_{maint} = 0.04~\text{€}_{2015}`/kW/km/year, based on :cite:`IEA_HVAC`,
:cite:`brown_synergies_2018` and :cite:`prina_multi-objective_2020`. By multiplying these
costs by 853 km (i.e. the distance between sofia and Ankara),
we obtain for the technology HVAC in EnergyScope in 2034:
:math:`c_{inv} = 1706~\text{M€}_{2015}`/GW and 
:math:`c_{maint} = 34.12~\text{M€}_{2015}`/GW/year.
We take the distance from capital city to capital city, and not the
distance from border to border, to grossly reflect the local grid
reinforcement costs that such new interconnection projects entail.

.. _app:DHN_grid_data_TK:

DHN grid
~~~~~~~~

The lower (:math:`\%_{dhn,min}`) and upper bounds (:math:`\%_{dhn,max}`) for the use of
DHN are chosen as 2% and 50%, respectively. These values are the same as
the ones from :cite:`borasio2022deep` for the case of Italy. Indeed, the population
density in urban and surburban areas is grossly similar in Italy and in Turkey.


.. _app:sec:ESTD_CO_CO2_emissions_TK:

GHG emissions
=============

As already explicited in :numref:`Table %s <tab:costs_imported_resources_TK>`, two CO :sub:`2`-eq
emissions metrics are used: CO :sub:`2,direct` and gwp :sub:`op`. The first one relates to 
the direct emissions associated with the fuels' combustion, while the second one is the
GWP100a-IPCC2013 metric: it covers emissions associated to extraction, transportation and combustion.
The former is used to complete the calibration of EnergyScope to the 2019 Turkish energy
system, whereas the second one determines the maximum GHG emissions allowed in 2034.


Calibration of EnergyScope to the 2019 energy system
----------------------------------------------------

After having found values for all parameters of the model, as described in the previous sections, it
is time to verify that the model's simulation of the 2019 Turkish energy system is coherent with historical
data. A practical check is to verify that CO :sub:`2`-eq emissions match. The resources' use and emissions 
simulated by running EnergyScope for the year 2019 are given in :numref:`Table %s <tab:2019_CO2_check>`.
They are compared in the table with the historical emissions. To do so, the value of 365.6 CO :sub:`2`-eq
in 2019 is taken from :cite:`TK_CO2_2023`. These emissions are then divided between coal, natural gas and
oil using the shares (0.43,0.24,0.33) of the year 2018 given in :cite:`IEA_TK_2021`. 

.. container::

   .. csv-table:: Resource use and CO :sub:`2`-eq emissions simulated by EnergyScope for the year 2019, compared with historical data. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resource** , **Quantity used in 2019** [90a]_ , **CO**:sub:`2direct` (per MWh of fuel) , **CO**:sub:`2direct` (total) [90a]_ , historical **CO**:sub:`2`-eq emissions
      :widths: 15 15 15 15 15
      :name: tab:2019_CO2_check
		
		 , [GWh] , [tCO :sub:`2`-eq/MWh :sub:`fuel`] , [MtCO :sub:`2`-eq] , [MtCO :sub:`2`-eq]
		local coal , 281 514 , 0.39 , 109.6 , 110.3 [90b]_
		imported coal , 144 877, 0.33 , 47.9 , 48.2 [90b]_
		natural gas , 440 926 , 0.20 , 88.2 , 88.2
		gasoline , 13 015 , 0.25 , 3.3, 3.3 [90c]_
		diesel , 214 907 , 0.26 , 55.9 , 57.1 [90c]_
		LFO , 220 204 , 0.26 , 57.3 , 58.5 [90c]_
		woody biomass , 40 000 , 0.39 , 15.6 , ~ [90d]_
		non-renewable waste , 121 , 0.26 , 0.03 , ~ [90d]_

.. [90a]
   Obtained after running EnergyScope TD with the 2019 data .

.. [90b]
   The historical emissions for local and imported coal are aggregated. We disaggregate them according to the proportions from the EnergyScope simulation for year 2019.

.. [90c]
   The historical emissions for gasoline, diesel and LFO are aggregated. We disaggregate them according to the proportions from the EnergyScope simulation for year 2019.

.. [90d]
   Not included in the scope of :cite:`TK_CO2_2023`

According to :cite:`TK_CO2_2023`, the total CO :sub:`2`-eq emissions from fossil fuels in Turkey were of 365.6 MtCO :sub:`2`-eq in 2019.
The sum of the values simulated with EnergyScope for fossil fuels (excluding woody biomass and waste) and given in
:numref:`Table %s <tab:2019_CO2_check>` is 362.1 MtCO :sub:`2`-eq. The difference between the two is of only 1% and is therefore acceptable.


Setting a gwp limit for the year 2034
-------------------------------------

The gwp :sub:`op` computed by EnergyScope for the 2019 Turkish energy system is of 435 MtCO :sub:`2`-eq. It is broken down by
resource type in :numref:`Table %s <tab:2019_gwp>`.

.. container::

   .. csv-table:: Resource use and gwp :sub:`op` simulated by EnergyScope for the year 2019. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resource** , **Quantity used in 2019** [91a]_ , **gwp**:sub:`op` (per MWh of fuel) , **gwp**:sub:`op` (total)
      :widths: 15 15 15 15
      :name: tab:2019_gwp
		
		 , [GWh] , [tCO :sub:`2`-eq/MWh :sub:`fuel`] , [MtCO :sub:`2`-eq]
		local coal , 281 514 , 0.43 , 122.2
		imported coal, 144 877 , 0.37 , 53.4
		natural gas , 440 926 , 0.27 , 117.6
		gasoline , 13 015 , 0.34 , 4.5
		diesel , 214 907 , 0.31 , 67.7
		LFO , 220 204 , 0.31 , 68.6
		woody biomass , 40 000 , 0.01 , 0.5
		non-renewable waste , 121, 0.15 , 0.02
		electricity imports, 558, 0.41, 0.2
		electricity exports, 0, 0, 0

.. [91a]
   Obtained after running EnergyScope with the 2019 data 
		
Decarbonisation of the energy system is enforced in EnergyScope by defining a threshold on the GWP (:math:`gwp_{limit}`). The simplest method
for choosing a value for :math:`gwp_{limit}` is to take a certain percentage of the 2019 gwp.





.. [10]
   Solar PV with system loss = 0.1, Tilt=35°, Azimut=180°
   
.. [11]
   4 MW wind turbine with Hub height=100m, Vestas V150 4000


