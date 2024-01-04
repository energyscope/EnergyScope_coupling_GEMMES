
.. _app:estd_tk_data:

Input Data - Turkey
++++++++++++++++++++++++++++++++++++++++++++
..
.. role:: raw-latex(raw)
   :format: latex
   
This section details the input data utilized in applying the LP modeling framework to the case study of Turkey.
The primary objective is to provide data for modelling a prospective Turkish energy system for the year 2035.
Additionally, we provide the necessary data to reproduce the historical Turkish energy system for the year 2019,
serving as a validation of EnergyScope's accuracy in modeling this intricate system.

Since many data are common between the Colombian and Turkish case studies, we will only present in the following sections
the data and assumptions that differ between the two. If nothing is indicated, the same data and assumptions as for
Colombia can be used.

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

:numref:`Table %s <tab:renewableTechPotentialIn2035_TK>` gives the Turkish potential for solar, wind, hydro and geothermal energy. These data are put into perspective with the values used for the calibration to the year 2019.
      
.. container::

   .. csv-table:: Comparison of installed capacity of technologies for renewable electricity generation in 2019 with their maximum potentials. Abbreviations: maximum (max.), photovoltaic panel (PV), District Heating Network (DHN), Concentrated Solar Power (CSP).
      :header: **Technology**, **2019**\ , **max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableTechPotentialIn2035_TK
   
      hydro dam , 15.7 [39a]_ , 19.9 [39c]_ , [GW]
      hydro river , 12.8 [39a]_ , 16.3 [39c]_ , [GW]
      rooftop PV , 6.0 [39b]_ , :math:`\approx`\ 120 [39d]_ , [GW]
      utility scale PV , 0 , :math:`\approx`\ 1350 [39d]_ , [GW]
      onshore wind , 7.6 [39e]_ , 48 [39e]_ , [GW]
      offshore wind , 0 , 66.2 [39f]_ , [GW]
      geothermal for electricity, 1.2 [39g]_ ,  4.2 [39h]_ , [GW]
      geothermal for heat (with DHN), 3.05 [39i]_ , 30.8 [39h]_ , [GW]
      CSP parabolic trough , 0 , 107 [39d]_, [GW]
      CSP solar tower , 0 , 107 [39d]_, [GW]
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
      Computed using the heat generation from geothermia in 2019, given in :cite:`IEA_world_energy_balances_TK` (including heat for agriculture), and the capacity factor of 85% given in Table :numref:`%s <tbl:dhn_cogen_boiler_TK>` 
      
   .. [39j]
      Computed using the heat generation from decentralised solar thermal in 2019, given in :cite:`IEA_world_energy_balances_TK`, and the capacity factor of 20.8% sourced in Table :numref:`%s <tbl:dhn_cogen_boiler_TK>` 

As described by eqs. :eq:`eq:solarAreaRooftopLimited` - :eq:`eq:solarAreaGroundHighIrrLimited`, the potential of solar technologies is constrained by the available areas for their deployment. The values for these available areas are given in :numref:`Table %s <tab:solarArea_TK>`. The values of maximum installed capacities indicated in :numref:`Table %s <tab:renewableTechPotentialIn2035_TK>` are a simplified translation of these equations into [GW] constraints.

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
      
Note that the ground areas given in :numref:`Table %s <tab:renewableTechPotentialIn2035>`
are not the total areas occupied by the solar power plants, but only the areas occupied 
by the solar panels themselves. After taking into account the *ground cover ratio*, we can compute that
the value given for :math:`solar_{area,ground}` corresponds to covering
4.6% of Turkey's land surface with solar power plants (not taking into account the rooftop area
used by rooftop PV).

Biomass and non-renewable waste
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Table %s <tab:renewableResourcesPotentialIn2035_TK>` gives the Turkish potential for biomass and non-renewable waste, together with their values used for the calibration to the year 2019. Note that contrary to the case of Colombia, bioethanol and biodiesel are assumed to be imported from abroad. They are therefore not given in :numref:`Table %s <tab:renewableResourcesPotentialIn2035_TK>`, which gives only the local biomass potential.

.. container::

   .. csv-table:: Biomass and waste resources consumed in 2021 and their potential.
      :header: **Resources** , **2019** , **Max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableResourcesPotentialIn2035_TK

		woody biomass , xxx , 215.0 [41a]_ , [TWh]
		wet biomass , xxx , 250.0 [41b]_ , [TWh]
		non-renewable waste, xxx , 53.8 [41c]_ , [TWh]
   
   .. [41a]
      We aggregate in woody biomass the numbers from :cite:`Biomass_Atlas_2017` for: dedicated woody and lignocellulosic biomass crops, total forestry potential, secondary residues from the wood industry, secondary residues from the sawmill industry, secondary residues from other wood processing industries, secondary residues from agro-industries, biowaste and post-consumer wood.
      
   .. [41b]
      We aggregate in woody biomass the numbers from :cite:`Biomass_Atlas_2017` for: straw & stubbles, prunings, dedicated crops, agro-industrial residues and road-side verge grass.
      
   .. [41c]
      Data could not be found for Turkey. The value taken for Italy by :cite:`borasio2022deep` was chosen to have a relevant order of magnitude, since Turkey and Italy had a grossly similar Total Energy Consumption in 2019 according to IEA data.
      
      
      
In order to compute the potentials for woody biomass and wet biomass, we take from :cite:`Biomass_Atlas_2017` the base potentials in 2030, defined by the authors as the sustainable (thus conservative) technical potential. The values expressed in kt dry mass were taken. Then, these kt dry mass were converted into energy units using a LHV of 18 [MJ/kg] for wet biomass and 19 [MJ/kg] for woody biomass. These values of LHV are the average values of the corresponding biomass types, extracted from :cite:`Phyllis2`.

Prices and GHG emissions of biomass resources given in :numref:`Table %s <tab:prices_resources_biomass_TK>` ... source ...

.. container::

   .. csv-table:: Price and GHG emissions of biomass and waste resources.
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` [42a]_ , **CO**:sub:`2direct` [42b]_
      :widths: 15 15 15 15
      :name: tab:prices_resources_biomass_TK
		
		 , [€\ :sub:`2015`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		woody biomass , 32.8 , 12 , 390
		wet biomass , 5.8 , 12 , 390
		non-renewable waste, 8.1 , 150 , 260 [42c]_

.. [42a]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion
   
.. [42b]
   Direct emissions related to combustion :cite:`Quaschning2015`. These data are not used in EnergyScope Turkey (since the capacity of technology CCS_industrial is set to zero), but they help us to check that the calibration of EnergyScope to the 2019 Turkish energy system is correct.

.. [42c]
   Assuming that the energy content can be assimilated to plastics.


Imported resources
------------------

A certain share of coal (and gas) is produced domestically ... :cite:`IEA_TK_2021`

Imported resources include coal, hydrocarbons (natural gas, gasoline, diesel, light fuel oil), bio-fuels and uranium.

No constraint regarding the availability of imported resources, since the cost-optimization already does the trick ?

Prices and GHG emissions given in :numref:`Table %s <tab:prices_imported_resources_TK>` ... source ...

.. container::

   .. csv-table:: Price and GHG emissions of domestically produced fossil fuels, in 2035. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` [43a]_ , **CO**:sub:`2direct` [43b]_
      :widths: 15 15 15 15
      :name: tab:prices_imported_resources_TK
		
		 , [€\ :sub:`2015`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		coal , 17.7 , 401 , 360
		natural gas , 44.3 , 267 , 200
		gasoline , 82.4 , 345 , 250
		diesel , 79.7 , 315 , 270
		LFO , 60.2 , 312 , 260
		bioethanol , 111.3 , 0 , 250
		biodiesel , 120.1 , 0 , 270
		uranium, 3.9, 4, 0

.. [43a]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion
   
.. [43b]
   Direct emissions related to combustion :cite:`Quaschning2015`. These data are not used in EnergyScope Turkey (since the capacity of technology CCS_industrial is set to zero), but they help us to check that the calibration of EnergyScope to the 2019 Turkish energy system of is correct.


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



Prices and GHG emissions given in :numref:`Table %s <tab:prices_elec_import_export_TK>` ... source ...

.. container::

   .. csv-table:: Price and GHG emissions associated to electricity imports and exports, in 2035. Abbreviations: Electricity (elec.).
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` , **CO**:sub:`2direct`
      :widths: 15 15 15 15
      :name: tab:prices_elec_import_export_TK
		
		 , [€\ :sub:`2015`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		elec imports , 84.3 , 413 [45a]_ , 0
		elec exports , 75.9 [45b]_ , 0 , 0

.. [45a] This value is based on the CO :sub:`2` intensity of the EU electricity grid. Indeed, :cite:t:`IEA_TK_2021` indicates
   that in 2019, most of the electricity imports of Turkey came from Bulgaria, which is part of the European grid.
   
.. [45b]
   The price of electricity exports is assumed to be equal to 90% of the price of electricity imports, to account for cross-border tariffs.


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
the 2035 EUDs can simply be computed by multiplying the values of :numref:`Table %s <tab:eud_2021>` by 1.42. This factor is computed based on the projection
of final energy consumption given in :cite:`TK_national_energy_plan`.

.. _ssec:app1_electricity_end_uses_TK:

Electricity
-----------

Final electricity consumption in 2019 is taken from PFU_DATABASE. The electricity used for heating and cooling in 2019 is subtracted from it, based
on the values given in PFU_DATABASE. This aggregated electricity EUD is then divided between baseload and variable load according to the proportions
retrieved from the EPIAS Transparency Portal for the year 2019 (https://seffaflik.epias.com.tr/transparency/). This gives a share of 55% baseload and
45% variable load. Finally, the values for baseload and variable load are divided between the different economic sectors by using the proportions given in :cite:t:`IEA_world_energy_balances_TK` (and aggregating together industry, agriculture and fishing).

For :math:`\%_{elec}`, we normalize the real electricity demand from the year 2019, available on the EPIAS Transparency Portal
(https://seffaflik.epias.com.tr/transparency/).

.. _ssec:app1_heating_end_uses_TK:

Heating and cooling
-------------------

The aggregated EUDs for different heating and cooling types were retrieved from PFU_DATABASE. The time series :math:`\%_{sh}` and :math:`\%_{sc}` are 
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

.. _app:discount_and_interest_rates_TK:

Discount rate and interest rate
-------------------------------

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
given in :numref:`Table %s <tab:renewableTechPotentialIn2035_TK>` ("max. potential"). The :math:`f_{min}`
values for renewable electricity technologies in 2035 are equal to their installed capacity in 2019,
already given in :numref:`Table %s <tab:renewableTechPotentialIn2035_TK>`. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.

.. container::

   .. csv-table:: Renewable electricity production technologies in 2035. Abbreviations: concentrated solar power 
      with parabolic trough (CSP PT), concentrated solar power with solar tower (CSP ST).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [47a]_ , **lifetime**, **c**:sub:`p` [2019], **c**:sub:`p` [2035]
      :widths: 19 18 24 23 15 15 15
      :name: tab:elec_prod_re_TK
		 
		  , [€ :sub:`2015`/kW :sub:`e`], [€ :sub:`2015`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%], [%]
		 Hydro dam, 4201 [47b]_, 21.0 [47b]_, 1693, 40 [47b]_, 35.6 [47c]_ , 35.6 [47u]_
		 Hydro river, 5045 [47b]_, 50.4 [47b]_, 1263, 40 [47b]_, 35.6 [47c]_ , 44.0 [47v]_
		 Rooftop PV, 738 [47d]_, 9.7 [47d]_, 2081, 40 [47d]_, 17.6 [47c]_ , 17.0 [47w]_
		 Utility scale PV, 335 [47d]_, 8.4 [47d]_, 2081, 40 [47d]_, 17.6 [47c]_ , 19.0 [47w]_
		 Onshore wind, 1010 [47d]_, 16.8 [47d]_, 623, 30 [47f]_, 33.5 [47c]_ , 34.8
		 Offshore wind, 1255 [47d]_, 50.6 [47d]_, 623, 30 [47f]_, 41.2 , 41.2
		 Geothermal, 7488 [47i]_, 142.3 [47i]_, 24929, 30, 86 [47j]_ , 86 [47j]_
		 CSP PT, 1045 [47k]_, 62.7 [47k]_, 0, 25 [47k]_, 23.7 [47k]_ , 23.7 [47k]_
		 CSP ST, 768 [47k]_, 63.0 [47k]_, 0, 25 [47k]_, 23.7 [47k]_ , 23.7 [47k]_
		 
.. [47a]
   Data from :cite:`weidema_ecoinvent_2013`

.. [47b]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_grande_2014`
   
.. [47c]
   Computed using the installed capacity reported in :cite:`TK_gov_RE` and the yearly electricity generation given by :cite:t:`IEA_TK_2021`

.. [47u]
   Taken as equal to the value in 2019
   
.. [47v]
   Value taken from :cite:`CCDR_TK`

.. [47d]
   ASK PAOLO.
   
.. [47w]
   Retrieved from the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI
   
.. [47f]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_energie_2013`
   
.. [47i]
   ORC cycle at 6 km depth for electricity generation. Based on Table 17 of :cite:`Carlsson2014`. We took the reference case in 2030
   
.. [47j]
   Data from :cite:`association_des_entreprises_electriques_suisses_aes_electricite_2012`
	
.. [47k]
   ASK PAOLO	


:numref:`Table %s <tab:elec_prod_re_TK>` includes the values of the yearly capacity factor (:math:`c_p`) of technologies.
As described in the Model Formulation Section, the values of :math:`c_p` for intermittent renewables is in fact equal to one, while
it is the value of their hourly load factor, :math:`c_{p,t}`, which is binding. The value of :math:`c_p` given in 
:numref:`Table %s <tab:elec_prod_re_TK>` for intermittent renewables is in fact the mean value of :math:`c_{p,t}` over the year.
The yearly profile (which sums up to one) of :math:`c_{p,t}` for intermittent renewables is computed as follows.

Power production profile of PV [10]_ were retrieved from :cite:`Renewables_ninja` for the cities of 
Istanbul, Izmir, Ankara, Ordu, Sanliurfa, Van and Antalya. The yearly profile of :math:`c_{p,t}`
for PV in Turkey was then computed by taking a weighted average of these 7 time series, with weights 
(0.32, 0.13, 0.15, 0.09, 0.10, 0.08, 0.13). These weights were taken proportional to the populations of the
areas surrounding those cities.

The yearly profile of :math:`c_{p,t}` for onshore wind was computed in the same way, retrieving from
:cite:`Renewables_ninja` power production profiles of wind turbines [11]_ instead of PV.

The same 7 time series as for onshore wind were used for offshore wind, but the weighted average to obtain the yearly profile of :math:`c_{p,t}`
was computed by using the weights (0.2,0.2,0,0.3,0,0,0.3). These weights were adjusted to reflect the length of the coastline near each city.

Finally, for hydro dam and hydro river, daily incoming water flow to hydro-electric facilities in Turkey was taken from the Turkish TSO website
for the 365 days of the year. These data were normalized to give a yearly profile :math:`c_{p,t}`, taking the same value for each hour of a same
day.

.. _ssec:app1_non-renewable_TK:

Non-renewable
~~~~~~~~~~~~~

:numref:`Table %s <tab:elec_prod_nre_TK>` gives the data for the non-renewable electricity generation technologies
modelled in EnergyScope Colombia, together with their sources. The minimum installed capacity (:math:`f_{min}`)
is zero, while the maximum installed capacity (:math:`f_{max}`) is set to a value high enough for each 
technology to potentially cover the entire demand - except for nuclear energy. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.
The efficiencies of each technology in 2019 and 2035 are given as well.

The values of (:math:`f_{min}`) and (:math:`f_{max}`) of nuclear energy are set differently. Indeed, the choice to build new
nuclear power plants is not simply based on market dynamics. It results from political decisions, often closely linked to
international relations.

:math:`f_{min} = 4.8` [GW] (normally installed in 2028)
:math:`f_{max} = 7.2` [GW] (voir national energy plan)

.. container::

   .. csv-table:: Non-renewable electricity production technologies in 2035. Abbreviations: combined cycle gas turbine (CCGT), capacity (capa.).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [48a]_ , **lifetime** [48b]_, **c**:sub:`p`, **efficiency** (2019), **efficiency** (2035), :math:`CO_{2-direct}` [48c]_
      :widths: 11 17 24 22 12 8 8 8 14
      :name: tab:elec_prod_nre_TK
		 
		  , [€ :sub:`2015`/kW :sub:`e`], [€ :sub:`2015`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%], [%], [%], [tCO2/MWh :sub:`e`]
		 CCGT, 772 [48d]_, 19.7 [48d]_, 184, 25, 85, 64 [48e]_ , 63 [48l]_, 0.317
		 CCGT ammonia [48f]_, 772, 19.6, 184, 25, 59, 50, 50, 0
		 Coal central, 3246 [48g]_, 49.0 [48g]_, 332, 35, 86 [48b]_, 32 [48h]_, 54 [48k]_, 0.667
		 Nuclear, 4846 [48i]_ , 103 :cite:`iea_-_international_energy_agency_iea_2014-1` , 708, 60 :cite:`association_des_enterprises_electriques_suisses_energie_2014` , 84 [48j]_ , 37, 37 , 0
		 
.. [48a]
   Data from :cite:`weidema_ecoinvent_2013`
   
.. [48b]
   Data from :cite:`bauer_new_2008`
   
.. [48c]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of electricity produced. Emissions computed based
   on resource used and specific emissions given in Table 9.
   
.. [48d]
   Data from :cite:`iea_-_international_energy_agency_iea_2014-1`   
   
.. [48e] Computed based on PFU_DATABASE	 

.. [48f]
   Use of Ammonia in CCGT is at its early stage. Mitsubishi is developping 
   a 40 MW turbine and promises similar efficiency as gas CCGT :cite:`nose2021development`. 
   However, the high emissions of NOx requires a removal equipment which will reduce the 
   power plant efficiency. As gas and ammonia CCGT will be similar, we expect a similar cost and lifetime. 
   The only exception is the efficiency, which is assumed at 50% instead of 63% for a gas CCGT :cite:`ikaheimo2018power`.
   
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
   Investment cost: 3431 €\ \ :sub:`2015`/kW\ \ :math:`_{\text{e}}`
   :cite:`iea_-_international_energy_agency_iea_2014-1` +
   dismantling cost in Switzerland: 1415    €\ \ :sub:`2015`/kW\ \ :math:`_{\text{e}}`
   :cite:`swissnuclear_financement_????`.

.. [48j]
   Data for the year 2012 from :cite:`swiss_federal_office_of_energy_sfoe_swiss_2014`
   
.. [48k]
   Data from :cite:`bauer_new_2008`, IGCC in 2025 (realistic optimistic scenario)
   
.. [48l]
   Data from :cite:`bauer_new_2008`, 0.4-0.5 GW CCGT in 2035 (realistic optimistic scenario)   
   
   

Heating and cogeneration
------------------------

Add COAL STOVE

.. container::

   .. table:: District heating technologies, in 2035. Abbreviations: biomass (bio.), CHP, digestion (dig.), hydrolysis (hydro.).
      :name: tbl:dhn_cogen_boiler_TK

      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      |            | :math:`c_  | :math:`c_  | :math:`gwp_| :math:`li  | :math:`c_  | :math:`\eta| :math:`\eta| :math:`C   |
      |            | {inv}`     | {maint}`   | {constr}`  | fetime`    | {p}`       | _e`        | _{th}`     | O_{2,      |
      |            |            |            |            |            |            |            |            | direct}`   |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      |            | [€         | [€         | [kgCO      | [y]        | [%]        | [%]        | [%]        | [tCO2/     |
      |            | :sub:`2015`| :sub:`2015`| :sub:`2    |            |            |            |            | MWh        |
      |            | /kW        | /kW        | -eq.`/kW   |            |            |            |            | :sub:`th`  |
      |            | :sub:`th`] | :sub:`th`  | :sub:`th`] |            |            |            |            | ]          |
      |            |            | /y]        |            |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | Geo        | 1500       | 57.0       | 808.8      | 30         | 85         | 0          | 100        | 0          |
      | thermal    | [165]_     | [165]_     | \          | [165]_     |            |            |            |            |
      | [165]_     |            |            | :cite:`\   |            |            |            |            |            |
      |            |            |            | wei\       |            |            |            |            |            |
      |            |            |            | dema_ec\   |            |            |            |            |            |
      |            |            |            | oinvent\   |            |            |            |            |            |
      |            |            |            | _2013`     |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+

.. [165]
   Geothermal heat-only plant with steam driven
   absorption heat pump 70/17\ \ :math:`^o`\ \ C at 2.3 km depth (from
   :cite:`DanishEnergyAgency2019`).

Cooling
-------

.. _sec:app1_vehicles_mobility_TK:

Transport
---------

Passenger mobility
~~~~~~~~~~~~~~~~~~

:numref:`Table %s <tbl:passenger_vehicles_TK>` also gives the minimum and maximum shares
of each vehicle type in 2035. The shares in 2019 are also given.

.. container::

   .. table:: Fuel and electricity consumption for passenger mobility technologies in 2035 :cite:`codina_girones_strategic_2015`, and minimum/maximum shares allowed in the model. Abbreviations: Fuel Cell (FC), Hybrid Electric Vehicle (HEV), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), public (pub.).
      :name: tbl:passenger_vehicles_TK

      ================  ============================ ============================ ===============================
      **Vehicle type**  **f**:math:`_\textbf{min,%}` **f**:math:`_\textbf{max,%}` **f**:math:`_\textbf{%}` (2019) 
      \                 [Wh/km-pass]                 [%]	                      [%]		
      Gasoline car      0                            1                            33
      Diesel car        0                            1                            0
      NG car            0                            1                            15
      HEV               0                            1                            0
      PHEV              0                            1                            0
      BEV               0                            1                            0
      FC car            0                            1                            0
      Methanol car      0                            1                            0
      Tram & Trolley    0                            0.05  [80a]_                 0
      Diesel bus        0                            1                            75
      Diesel HEV bus    0                            1                            0
      NG bus            0                            1                            0
      FC bus            20                            1                            0
      Train pub.        0                            0.30 [80a]_                  0
      ================  ============================ ============================ ===============================

.. [80a]
   Our own expert guesses.

Freight
~~~~~~~

The share of freight which can be supplied by different modes are bounded by the values :math:`\%_{fr,X,min}` and :math:`\%_{fr,X,max}`. 
These values are given in :numref:`Table %s <tab:freight_shares_TK>` for 2019 and 2035. Moreover, based on energy consumption of transport 
given in :cite:`IEA_2023`, we impose that in 2019, 50% of truck transport was carried out by diesel trucks and 50% by gasoline trucks.

Boat freight not taken into account because could not find any data.

.. container::

   .. csv-table:: Limiting shares for freight in 2019 and 2035.
      :header: **Parameter**, **Value in 2019**, **Value in 2035**
      :widths: 20 20 20
      :name: tab:freight_shares_TK
		 
		 :math:`\%_{fr_{rail_{min}}}`, 0.04 [81a]_, 0
		 :math:`\%_{fr_{rail_{max}}}`, 0.04 [81a]_,  0.25 [81b]_
		 :math:`\%_{fr_{boat_{min}}}`, 0    [81a]_, 0
		 :math:`\%_{fr_{boat_{max}}}`, 0    [81a]_, 0
		 :math:`\%_{fr_{road_{min}}}`, 0, 0
		 :math:`\%_{fr_{road_{max}}}`, 1, 1
		  
.. [81a]
   Data from :cite:`plazas_nino_2023`.
   
.. [81b]
   Our own expert guesses.

.. _sec:app1_ned_TK:

Non-energy demand
-----------------

Given the important
petroleum refining activity in Turkey, we assume that all non-energy EUD in 2019 was HVC. We keep
the same assumption for the year 2035.

.. _ssec:app1_syn_fuels_TK:

Synthetic fuels production
--------------------------

Hydrogen production
~~~~~~~~~~~~~~~~~~~

Synthetic methane and oils production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Carbon capture and storage
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _sec:app1_storage_TK:

Storage
-------

.. container::

   .. table:: Storage technologies characteristics in 2035: costs, emissions and lifetime. Abbreviations: batteries (batt.), Battery Electric Vehicule (BEV), centralised (cen.), decentralised (dec.), Lithium-ions (Li-on), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), Pumped Hydro Storage (PHS), seasonal (seas.), temperature (temp.) and thermal storage (TS).
      :name: tab:stodatabasic_TK

      +-----------+-----------+-----------+-----------+-----------+
      |           | :math:`c_ | :math:`c_ | :math:`gw | :math:`li |
      |           | {inv}`    | {maint}`  | p_{con    | fetime`   |
      |           |           |           | str}`     |           |
      +-----------+-----------+-----------+-----------+-----------+
      |           | [€:math:` | [€:math:` | [kgCO\    | [y]       |
      |           | \_{2015}` | \_{2015}` | :sub:`2`  |           |
      |           | /kWh]     | /kWh/y]   | -eq./kWh] |           |
      +-----------+-----------+-----------+-----------+-----------+
      | PHS       | 58.8      | 0 [297]_  | 8.33      | 50 [299]_ |
      |           |           |           | [298]_    |           |
      +-----------+-----------+-----------+-----------+-----------+

.. [297]
   Neglected.

.. [298]
   Own calculation based on Hydro Dams emissions from previous work
   :cite:`Limpens2019,Moret2017PhDThesis`.

.. [299]
   Data verified in Table B1 of
   :cite:`Zakeri2015`.

The PHS in Turkey can be resumed to the Coo-Trois-Ponts hydroelectric
power station. The characteristics of the station in 2015 are the
following: installed capacity turbine (1164MW), pumping (1035MW),
overall efficiency of 75%, all reservoirs capacity (5000 MWh). We assume
that the energy losses is shared equally between the pumping and
turbining, resulting by a charge/discharge efficiencies of 86.6%. The
energy to power ratio are 4h50 and 4h18 for charge and discharge,
respectively :cite:`Electrabel2014`. A project started to
increase the height of the reservoirs and thus increase the capacity by
425 MWh. In addition, the power capacity will be increase by 80MW. The
overall project cost is estimated to 50M€ and includes also renovation
of other parts. We arbitrary assume that 50% is dedicated for the
height increase. It results in an investment cost of 58.8€\ :sub:`2015`
per kWh of new capacity. The overall potential of the PHS could be
extended by a third reservoir with an extra capacity of around 1.2 GWh.
Hence, we assume that the upper limit of PHS capacity is 6.5 GWh. No
upper bound were constrained for other storage technologies.

.. _App:Data:OtherParam_TK:

Others 
------

.. _ssec:app1_grid_TK:

Electricity grid
~~~~~~~~~~~~~~~~

.. _app:DHN_grid_data_TK:

DHN grid
~~~~~~~~

The lower (:math:`\%_{dhn,min}`) and upper bounds (:math:`\%_{dhn,max}`) for the use of
DHN are chosen as 2% and 50%, respectively. The latter value is the same as
the one from :cite:`borasio2022deep` for the case of Italy. Indeed, the population
density in urban and surburban areas is grossly similar in Italy and in Turkey.

Energy demand reduction cost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~





.. [10]
   Solar PV with system loss = 0.1, Tilt=35°, Azimut=180°
   
.. [11]
   4 MW wind turbine with Hub height=100m, Vestas V150 4000


