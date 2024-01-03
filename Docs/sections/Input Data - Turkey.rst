
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
      :header: **Technology**, **2019**\  [39a]_ , **max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableTechPotentialIn2035_TK
   
      hydro dam , 15.7 [39b]_ , 19.9 [39c]_ , [GW]
      hydro river , 12.8 [39b]_ , 16.3 [39c]_ , [GW]
      rooftop PV , 6.0 , :math:`\approx`\ 120 [39d]_ , [GW]
      utility scale PV , 0 , :math:`\approx`\ 1350 [39d]_ , [GW]
      onshore wind , 7.6 [39e]_ , 48 [39e]_ , [GW]
      offshore wind , 0 , 66.2 [39f]_ , [GW]
      geothermal for electricity, 1.2 ,  4.2 [39g]_ , [GW]
      geothermal for DHN, 3.05, 30.8 [39g]_ , [GW]
      CSP parabolic trough , 0 , 107 [39d]_, [GW]
      CSP solar tower , 0 , 107 [39d]_, [GW]
      Solar thermal (decentralised), 5.3, no limit imposed, [GW]

   .. [39a]
      Data from :cite:t:`IEA_TK_2021`, unless otherwise specified.

   .. [39b]
      Data from :cite:`TK_gov_hydro`

   .. [39c]
      from :cite:t:`Rebiere2019thesis`
      
   .. [39d]
      The real constraint on solar potential is not a constraint on installable capacity, but a constraint on available area, as described below.

   .. [39e]
      Ministry of Energy and Natural Resources, cited by :cite:t:`IEA_TK_2021`.

   .. [39f]
      :cite:t:`emeksiz_2019` computes an offshore wind potential of 9.2 GW with rather conservative asumptions (max. water depth of 50 m). It is in line with the 10 GW potential computable based on the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI. To this number is added the 57 GW potential of floating wind offshore, reported by the Offshore Wind Energy Association (DÜRED) in :cite:`Daily_Sabah_2021`.
      
   .. [39g]
      :cite:t:`IEA_TK_2021` reports a 35 GW potential for geothermal energy in Turkey. :cite:t:`Balat_2004` affirms that 12% of this potential is appropriate for electricity generation and 88% for heat production.

As described by eqs. :eq:`eq:solarAreaRooftopLimited` - :eq:`eq:solarAreaGroundHighIrrLimited`, the potential of solar technologies is constrained by the available areas for their deployment. The values for these available areas are given in :numref:`Table %s <tab:solarArea_TK>`. The values of maximum installed capacities indicated in :numref:`Table %s <tab:renewableTechPotentialIn2035_TK>` are a simplified translation of these equations into [GW] constraints.

.. container::

   .. csv-table:: Values of the parameters which constrain the solar potential of Colombia. Abbreviations: solar multiple (sm), high irradiation (high irr.), photovoltaic panel (PV), Concentrated Solar Power (CSP).
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






Imported resources
------------------

Imported fossil fuels are implemented in the model. They
can be regrouped into hydrocabons (gasoline, diesel, LFO and NG), coal and
uranium. Data is summarised in :numref:`Table %s <tbl:prices_resources_TK>` and are compared to
other sources, such as estimations from the JRC of prices for oil, gas
and coal :cite:`simoes2013jrc`. They base their work on a
communication of the European Commission
:cite:`eu2011roadmap`.

.. container::

   .. table:: Price, GHG emissions and availability of resources, in 2035. Abbreviations: Liquid Fuel Oil (LFO), Natural Gas (NG) and Synthetic Natural Gas (SNG).
      :name: tbl:prices_resources_TK

      +-------------+-------------+-------------+-------------+-------------+
      | **Res\      | :math:`c_   | :math:`gwp_ | :math:`{CO}_| *avail*     |
      | ources**    | {op}`       | {op}`       | {2direct}`  |             |
      |             |             |             | [26]_       |             |
      +-------------+-------------+-------------+-------------+-------------+
      |             | [€\ :sub:`2\| [kgCO\      | [kgCO\      | [GWh]       |
      |             | 015`/MWh\   | :sub:`2-eq.`| :sub:`2-eq.`|             |
      |             | :sub:`fuel`]| /MWh\       | /MWh\       |             |
      |             |             | :sub:`fuel`]| :sub:`fuel`]|             |
      +-------------+-------------+-------------+-------------+-------------+
      | Electricity | 84.3 [27]_  | 206.4 [28]_ | 0           | 27.5        |
      | Import      |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Gasoline    | 82.4 [29]_  | 345 [28]_   | 250         | infinity    |
      |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Diesel      | 79.7 [30]_  | 315 [28]_   | 270         | infinity    |
      |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | LFO         | 60.1 [31]_  | 311.5 [28]_ | 260         | infinity    |
      |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Fossil      | 44.3 [32]_  | 267 [28]_   | 200         | infinity    |
      | Gas         |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Woody       | 32.8        | 11.8 [28]_  | 390         | 23.4        |
      | biomass     |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Wet-biomass | 5.8         | 11.8 [28]_  | 390         | 38.9        |
      +-------------+-------------+-------------+-------------+-------------+
      | non-RE      | 23.1        | 150  [28]_  | 260 [33]_   | 17.8        |
      | waste       |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Coal        | 17.6        | 401         | 360         | 33.3 [37]_  |
      |             |             | :cite:`\    |             |             |
      |             |             | we\         |             |             |
      |             |             | idema_ecoin\|             |             |
      |             |             | vent_2013`  |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Uranium     | 3.9 [34]_   | 3.9         | 0           | infinity    |
      |             |             | :cite:`\    |             |             |
      |             |             | we\         |             |             |
      |             |             | idema_ecoin\|             |             |
      |             |             | vent_2013`  |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Bio-diesel  | 120.0       | 0 [36]_     | 270         | infinity    |
      |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | B\          | 111.3 [35]_ | 0 [36]_     | 250         | infinity    |
      | io-gasoline |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Renew. gas  | 118.3       | 0 [36]_     | 200         | infinity    |
      |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Fossil  H2  | 87.5        | 364         | 0           | infinity    |
      | [25]_       |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Renew. H2   | 119.4       | 0 [36]_     | 0           | infinity    |
      |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Fossil      | 76          | 285         | 0           | infinity    |
      | Ammonia     |             |             |             |             |
      | [25]_       |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Renew.      | 81.8        | 0 [36]_     | 0           | infinity    |
      | Ammonia     |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Fossil      | 82.0        | 350         | 246         | infinity    |
      | Methanol    |             |             |             |             |
      | [25]_       |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+
      | Renew.      | 111.3       | 0 [36]_     | 246         | infinity    |
      | Methanol    |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+


.. [25]
   Own calculation for fossil hydrogen, ammonia and methanol. 
   Price and emissions are calculated based on fossil gas and based on conversion efficiencies.

.. [26]
   Direct emissions related to
   combustion:cite:`Quaschning2015`.

.. [27]
   Based on average market price in the year 2010 (50
   EUR\ \ :sub:`2010`/MWh, from
   :cite:`epex_spot_swissix_????`). Projected from 2010 to
   2035 using a multiplication factor of 1.36
   :cite:`prognos_ag_energieperspektiven_2012`. For security
   of supply reason, the availability is limited to 30% of yearly
   electricity EUD (See Section
   `[ssec:be_policies] <#ssec:be_policies>`__).

.. [28]
   GWP100a-IPCC2013 metric: impact associated to
   production, transport and combustion, see
   :cite:`Moret2017PhDThesis`

.. [29]
   Based on 1.49 CHF\ \ :sub:`2015`/L (average price in 2015 for
   gasoline 95 in Switzerland)
   :cite:`swiss_federal_office_of_statistics_sfos_ipc_2016`.
   Taxes (0.86 CHF\ \ :sub:`2015`/L,
   :cite:`beuret_evolution_2016`) are removed and the
   difference is projected from 2015 to 2035 using a multiplication
   factor of 1.24 :cite:`european_commission_energy_2011`.
   In line with :cite:`simoes2013jrc`.

.. [30]
   Based on 1.55 CHF\ \ :sub:`2015`/L (average price in 2015)
   :cite:`swiss_federal_office_of_statistics_sfos_ipc_2016`.
   Taxes (0.87 CHF\ \ :sub:`2015`/L,
   :cite:`beuret_evolution_2016`) are removed and the
   difference is projected from 2015 to 2035 using a multiplication
   factor of 1.24 :cite:`european_commission_energy_2011`.
   In line with :cite:`simoes2013jrc`.

.. [31]
   Based on 0.705 CHF\ \ :sub:`2015`/L (average price in 2015 for
   consumptions above 20000 L/y)
   :cite:`swiss_federal_office_of_statistics_sfos_indice_2016-1`.
   Taxes (0.22 CHF\ \ :sub:`2015`/L,
   :cite:`beuret_evolution_2016`) are removed and the
   difference is projected from 2015 to 2035 using a multiplication
   factor of 1.24 :cite:`european_commission_energy_2011`.
   In line with :cite:`simoes2013jrc`.

.. [32]
   Based on the EUC estimated cost of resources in
   2030, see Table 5 from :cite:`simoes2013jrc`.

.. [33]
   Assuming that the energy content can be assimilated to plastics and
   extended to LFO.

.. [34]
   Average of the data points for 2035 in
   :cite:`f._ess_kosten_2011`, accounting for the efficiency
   of nuclear power plants (:numref:`Table %s <tbl:nonrenew_elec>`).

.. [35]
   Data extrapolated from
   :cite:`brynolf2018electrofuels`

.. [36]
   Emissions related to electro-fuels
   and bio-fuels production are neglected.
   
.. [37]
   Colombia is phasing out coal. Coal is still used in industrial processes.
   In 2015, 33.3 TWh of coal were used. Thus, the amount available should be lower than this value.

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
		passenger mobility , 0,0,0,346532.0 ,[Mpkm]
		freight , 0,0,0,278728.0 ,[Mtkm]
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

For *%\ elec*, we normalize the real electricity demand from the year 2019, available on the EPIAS Transparency Portal
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

The lower (:math:`%_{public,min}`) and upper bounds
(:math:`%_{public,max}`) for the use of public transport are 5% and
50% of the annual passenger transport demand, respectively. 

The freight can be supplied by trucks, trains or boats. The lower
(:math:`%_{fr,rail,min}`) and upper bounds (:math:`%_{fr,rail,max}`) for the use of
freight trains are 10.9% and 25% of the annual freight transport
demand, respectively. The lower (:math:`%_{fr,boat,min}`) and upper bounds
(:math:`%_{fr,boat,max}`) for the use of freight inland boats are 15.6% and
30% of the annual freight transport demand, respectively. The lower
(:math:`%_{fr,trucks,min}`) and upper bounds (:math:`%_{fr,trucks,max}`) for the use
of freight trucks are 0% and 100% of the annual freight transport
demand, respectively. The bounds and technologies information are
latter summarised in Table
`1.15 <#tbl:freight_vehicles_efficiency>`__.

.. _app:discount_and_interest_rates_TK:

Discount rate and interest rate
-------------------------------

.. _app:ESTD_TK_data_technologies:

Technologies
============

Electricity production
----------------------

.. _ssec:app1_renewables_TK:

Renewables
~~~~~~~~~~

:numref:`Table %s <tab:elec_prod_re_TK>` gives the data for the renewable electricity generation technologies
modelled in EnergyScope Turkey, together with their sources. The data for :math:`f_{max}` were already
given in :numref:`Table %s <tab:renewableTechPotentialIn2035_TK>` ("max. potential"). The :math:`f_{min}`
values for renewable electricity technologies in 2035 are equal to their installed capacity in 2021,
already given in :numref:`Table %s <tab:renewableTechPotentialIn2035>`. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.

.. container::

   .. csv-table:: Renewable electricity production technologies in 2035. Abbreviations: concentrated solar power 
      with parabolic trough (CSP PT), concentrated solar power with solar tower (CSP ST).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [82a]_ , **lifetime**, **c**:sub:`p`
      :widths: 19 18 24 23 15 15
      :name: tab:elec_prod_re_TK
		 
		  , [€ :sub:`2015`/kW :sub:`e`], [€ :sub:`2015`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%]
		 Hydro dam, 4201 [82b]_, 21.0 [82b]_, 1693, 40 [82b]_, 50 [82c]_
		 Hydro river, 5045 [82b]_, 50.4 [82b]_, 1263, 40 [82b]_, 50 [82c]_
		 Rooftop PV, 738 [82d]_, 9.7 [82d]_, 2081, 40 [82d]_, 19 [82e]_
		 Utility scale PV, 335 [82d]_, 8.4 [82d]_, 2081, 40 [82d]_, 21 [82e]_
		 Onshore wind, 1010 [82d]_, 16.8 [82d]_, 623, 30 [82f]_, 27 [82g]_
		 Offshore wind, 1255 [82d]_, 50.6 [82d]_, 623, 30 [82f]_, 50 [82h]_
		 Geothermal, 7488 [82i]_, 142.3 [82i]_, 24929, 30, 86 [82j]_
		 CSP PT, 1045 [82k]_, 62.7 [82k]_, 0, 25 [82k]_, 32 [82k]_
		 CSP ST, 768 [82k]_, 63.0 [82k]_, 0, 25 [82k]_, 32 [82k]_
		 Biomass central, 1677 [82l]_, 69.9 [82l]_, 332, 35, 87
		 
.. [82a]
   Data from :cite:`weidema_ecoinvent_2013`

.. [82b]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_grande_2014`
   
.. [82c]
   Computed based on installed capacities and yearly production of hydro power pants in 2021, with data from :cite:`IEA_2023`.
   
.. [82d]
   ASK PAOLO.
   
.. [82e]
   Retrieved from the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI. 
   
.. [82f]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_energie_2013`  
   
.. [82g]
   Data from :cite:`plazas_nino_2023`.
   
.. [82h]
   Data from :cite:`Renewables_ninja`.
   
.. [82i]
   ORC cycle at 6 km depth for electricity generation. Based on Table 17 of :cite:`Carlsson2014`. We took the reference case in 2030.
   
.. [82j]
   Data from :cite:`association_des_entreprises_electriques_suisses_aes_electricite_2012`
	
.. [82k]
   ASK PAOLO	 
   
.. [82l]
   ASK PAOLO	

:numref:`Table %s <tab:elec_prod_re>` includes the values of the yearly capacity factor (:math:`c_p`) of technologies.
As described in the model formulation Section, the values of :math:`c_p` for intermittent renewables is in fact equal to one, while
it is the value of their hourly load factor, :math:`c_{p,t}`, which is binding. The value of :math:`c_p` given in 
:numref:`Table %s <tab:elec_prod_re>` for intermittent renewables is in fact the mean value of :math:`c_{p,t}` over the year.
The yearly profile (which sums to one) of :math:`c_{p,t}` for intermittent renewables is computed as follows.

Power production profile of PV [10]_ were retrieved from :cite:`Renewables_ninja` for the cities of 
Istanbul, Izmir, Ankara, Ordu, Sanliurfa, Van and Antalya. The yearly profile of :math:`c_{p,t}`
for PV in Turkey was then computed by taking a weighted average of these 7 time series, with weights 
(0.32, 0.13, 0.15, 0.09, 0.10, 0.08, 0.13). These weights were computed as proportional to the populations of the
areas surrounding those cities.

The yearly profile of :math:`c_{p,t}` for solar thermal technologies in Turkey was computed in the same way, retrieving from
:cite:`Renewables_ninja` global horizontal irradiation (GHI) profiles instead of power production profiles of PV. Idem for the
yearly profile of :math:`c_{p,t}` for onshore wind, by retrieving from :cite:`Renewables_ninja` power production profiles of
wind turbines [11]_ instead of PV.

The same 7 time series as for onshore wind were used for offshore wind, but the weighted average to obtain the yearly profile of :math:`c_{p,t}`
was computed by using the weights (0.2,0.2,0,0.3,0,0,0.3). These weights were adjusted to reflect the length of the coastline near each city.

Finally, for hydro dam and hydro river, daily incoming water flow to hydro-electric facilities in Turkey was taken from the Turkish TSO website
for the 365 days of the year. These data were normalized to give a yearly profile :math:`c_{p,t}`, taking the same value for each hour of a same
day.

.. _ssec:app1_non-renewable_TK:

Non-renewable
~~~~~~~~~~~~~

Data for the considered fossil electricity production technologies are
listed in :numref:`Table %s <tbl:nonrenew_elec>`. 


.. container::

   .. table:: Non-renewable electricity supply technologies, in 2035. Abbreviations: Combined Cycles Gas Turbine (CCGT), Ultra-Supecritical (U-S), Integrated Gasification Combined Cycles (IGCC).
      :name: tbl:nonrenew_elec

      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_   | :math:`c_   | :math:`gwp_ | :math:`li   | :math:`c_   | :math:`\eta | :math:`C    |
      |             | {inv}`      | {maint}`    | {constr}`   | fetime`     | {p}`        | _e`         | O_{2,       | 
      |             |             |             |             |             |             |             | direct}`    |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | [€          | [€          | [kgCO       | [y]         | [%]         | [%]         | [tCO2/      | 
      |             | :sub:`2015` | :sub:`2015` | :sub:`2-eq.`|             |             |             | MWh         |
      |             | /kW         | /kW         | /kW         |             |             |             | :sub:`e`    |
      |             | :sub:`e`]   | :sub:`e`/y] | :sub:`e`]   |             |             |             | ]           |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Nuclear     | 4846 [82]_  | 103         | 707.9       | 60          | 84.9        | 37          | 0           |
      |             |             | :cite:`\    | \           | :cite:`\    | [83]_       |             |             |
      |             |             | i\          | :cite:`\    | as\         |             |             |             |
      |             |             | ea_-_\      | weid\       | socia\      |             |             |             |
      |             |             | inter\      | ema_e\      | tion_\      |             |             |             |
      |             |             | natio\      | coinv\      | des_e\      |             |             |             |
      |             |             | nal_e\      | ent_2\      | nterp\      |             |             |             |
      |             |             | nergy\      | 013`\       | rises\      |             |             |             |
      |             |             | _agen\      |             | _elec\      |             |             |             |
      |             |             | cy_ie\      |             | triqu\      |             |             |             |
      |             |             | a_201\      |             | es_su\      |             |             |             |
      |             |             | 4-1`\       |             | isses\      |             |             |             |
      |             |             |             |             | _ener\      |             |             |             |
      |             |             |             |             | gie_2\      |             |             |             |
      |             |             |             |             | 014`        |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+

.. [82]
   Investment cost: 3431 €\ \ :sub:`2015`/kW\ \ :math:`_{\text{e}}`
   :cite:`iea_-_international_energy_agency_iea_2014-1` +
   dismantling cost in Switzerland: 1415
   €\ \ :sub:`2015`/kW\ \ :math:`_{\text{e}}`
   :cite:`swissnuclear_financement_????`.

.. [83]
   Data for the year 2012
   :cite:`swiss_federal_office_of_energy_sfoe_swiss_2014`


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
These values are given in :numref:`Table %s <tab:freight_shares>` for 2021 and 2035. Moreover, based on energy consumption of transport 
given in :cite:`IEA_2023`, we impose that in 2021, 50% of truck transport was carried out by diesel trucks and 50% by gasoline trucks.

Boat freight not taken into account because could not find any data.

.. container::

   .. csv-table:: Limiting shares for freight in 2021 and 2035.
      :header: **Parameter**, **Value in 2021**, **Value in 2035**
      :widths: 20 20 20
      :name: tab:freight_shares
		 
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
petroleum refining activity in Turkey, we assume that all non-energy EUD in 2021 was HVC. We keep
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

The PHS in Colombia can be resumed to the Coo-Trois-Ponts hydroelectric
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


