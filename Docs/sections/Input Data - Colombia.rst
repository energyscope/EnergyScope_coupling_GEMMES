
.. _app:estd_co_data:

Input Data - Colombia
++++++++++++++++++++++++++++++++++++++++++++
..
.. role:: raw-latex(raw)
   :format: latex
..

This section details the input data utilized in applying the LP modeling framework to the Colombia case study.
The primary objective is to provide data for modelling a prospective Colombian energy system for the year 2036.
Additionally, we provide the necessary data to reproduce the historical Colombian energy system for the year 2021,
serving as a validation of EnergyScope's accuracy in modeling this intricate system.

The data can be grouped into three parts: resources (Section `Resources <#app:sec:ESTD_CO_resources>`__), demand (Section
`Demand <#sec:app1_end_uses>`__) and technologies (Section
`Technologies <#app:ESTD_CO_data_technologies>`__).

Regarding technologies, they are characterised by the following characteristics:
energy balances, cost (investment and maintenance) and environmental
impact (global warming potential (GWP)). Regarding weather-dependent technologies (wind, solar, etc.), real
production time series were collected for a representative year.

Regarding the GWP, LCA data are taken from the Ecoinvent
database v3.2 [1]_ :cite:`weidema_ecoinvent_2013` using the
“allocation at the point of substitution” method. GWP is assessed with
the “GWP100a - IPCC2013” indicator. For technologies, the GWP
accounts for the technology construction; for resources, it accounts for
extraction, transportation and combustion. In addition, data for fuel
combustion are taken from :cite:t:`Quaschning2015`.

Regarding the costs, they are all expressed in *real*\  [2]_ US Dollars for the year 2021 (USD\ :sub:`2021`).
If not specified, USD refers to USD\ :sub:`2021`. When no value is given, the costs are the same as in
the other versions of EnergyScope, except that they are expressed in USD\ :sub:`2021` instead of €\ :sub:`2015`.
The conversion from €\ :sub:`2015` to USD\ :sub:`2021` is performed via Eq. :eq:`eqn:currency_conv_1`. 

.. math::
    c_{inv} [\text{USD}_{2021}] = \frac{\text{CEPCI}_{2021} \ [\text{USD}_{2021}]}{\text{CEPCI}_{2015} \ [\text{USD}_{2015}]} \cdot \frac{\text{USD}_{2015}}{\text{€}_{2015}} \cdot c_{inv} [\text{€}_{2015}]
    :label: eqn:currency_conv_1

Where the historical exchange rate for 2015, :math:`\frac{\text{USD}_{2015}}{\text{€}_{2015}}`, is equal to 1.11 :cite:`ecb2015` and the CEPCI
:cite:`chemical_engineering_chemical_2016` is an index
taking into account the evolution of the equipment cost. The CEPCI values for recent years, extracted from :cite:`CEPCI`, are
given in :numref:`Table %s <tbl:cepci>`.

.. container::

   .. table:: CEPCI values
      :name: tbl:cepci

      ======== =========
      **Year** **CEPCI**
      ======== =========
      2010     550.8
      2011     585.7
      2012     584.6
      2013     567.3
      2014     576.1
      2015     556.8
      2016     541.7
      2017     567.5
      2018     603.1
      2019     607.5
      2020     596.2
      2021     708.8
      2022     816.0
      ======== =========

For the cost of resources, the evolution of the cost from 2015 to 2021 is not computed using the CEPCI, 
but instead using the supplementary data of the PEN 2050 :cite:`PEN2050`.

Note that originally, to express all costs in €\ :sub:`2015` in the other versions of EnergyScope, many
data expressed in other currencies or referring to another year had to be converted to €\ :sub:`2015`.
Most of these data came from the works :cite:`Moret2017PhDThesis,Limpens2019` and were expressed in CHF\ :sub:`2015`.
They were converted into €\ :sub:`2015` thanks to similar equations to :eq:`eqn:currency_conv_1`, using relevant annual exchange
rate values retrieved from the ECB and using CEPCI indices between relevant years.


.. _app:sec:ESTD_CO_resources:

Resources
=========

Local renewable resources
-------------------------

The energy transition heavily relies on renewable energies, which makes their
deployment potential a critical parameter. In 2021, 28% of the total final 
energy consumed in Colombia was renewable, mainly biomass and hydro :cite:`IEA_2023`.

The major renewable potentials are: solar, hydro, biomass and wind.
Additionnaly, Colombia has a limited geothermal potential. In EnergyScope, the limit for solar, wind, hydro and geothermal is expressed as a constraint on the capacity installable. The limit for biomass and waste, on the other hand, is expressed as a constraint on the resources available.

Solar, wind, hydro and geothermal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Table %s <tab:renewableTechPotentialIn2036>` gives the 2050 Colombian potential for solar, wind, hydro and geothermal energy. These data are put into perspective with the values used for the calibration to the year 2021.
      
.. container::

   .. csv-table:: Comparison of installed capacity of technologies for renewable electricity generation in 2021 with their maximum potentials. Abbreviations: maximum (max.), photovoltaic panel (PV), Concentrated Solar Power (CSP).
      :header: **Technology**, **2021**\  [5a]_ , **max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableTechPotentialIn2036
   
      hydro dam , 8.14 [5b]_ , 21.2 [5c]_ , [GW]
      hydro river , 3.78 [5b]_ , 3.78 [5c]_ , [GW]
      rooftop PV , 0.12 , :math:`\approx`\ 100 [5e]_ , [GW]
      utility scale PV , 0 , :math:`\approx`\ 700 [5e]_ , [GW]
      onshore wind , 0.02 , 7.3 [5f]_ , [GW]
      offshore wind , 0 , 48.8 [5g]_ , [GW]
      geothermal , 0 ,  1.2 [5h]_ , [GW]
      CSP parabolic trough , 0 , 13 [5e]_, [GW]
      CSP solar tower , 0 , 13 [5e]_, [GW]
      biomass central , 0.21 , ~ [5i]_, [GW]

   .. [5a]
      Data from :cite:`IEA_2023`, unless otherwise specified.

   .. [5b]
      :cite:`IEA_2023` gives an installed hydropower capacity of 11.91 GW in 2021. We split it between hydro dam and hydro river according to percentages received from Departamento Nacional de Planeación (DNP), the Colombian National Planning Department.
      
   .. [5c]
      Values from the scenario "Full Hydrogen Economy" in :cite:`plazas_nino_2024`.
      
   .. [5e]
      The real constraint on solar potential is not a constraint on installable capacity, but a constraint on available area, as described below.

   .. [5f]
      This potential corresponds to the 2050 target for onshore wind energy of the country's long-term development strategy (E2050 Colombia), as given in :cite:`IEA_2023`. This potential is in the same order of magnitude as the one indicated in :cite:`RE_potential_2023`.

   .. [5g]
      Sum of the potentials for fixed offshore wind and floating offshore wind indicated in :cite:`RE_potential_2023`. This potential is in the same order of magnitude as the one we computed using the methodology and open-source database from :cite:`dupont_2018`, available at https://github.com/EliseDup/WorldEROI.
      
   .. [5h]
      Data from :cite:`plazas_nino_2023`. This potential is in line with the one indicated in :cite:`RE_potential_2023`.
      
   .. [5i]
      No constraint on the number of GW installable. The real constraint is on the availability of woody biomass (see below).
        

As described by eqs. :eq:`eq:solarAreaRooftopLimited` - :eq:`eq:solarAreaGroundHighIrrLimited`, the potential of solar technologies is constrained by the available areas for their deployment. The values for these available areas, as well as the other parameters present in eqs. :eq:`eq:solarAreaRooftopLimited` - :eq:`eq:solarAreaGroundHighIrrLimited`, are given in :numref:`Table %s <tab:solarArea>`. The values of maximum installed capacities indicated in :numref:`Table %s <tab:renewableTechPotentialIn2036>` are a simplified translation of these equations into [GW] constraints.

.. container::

   .. csv-table:: Values of the parameters which constrain the solar potential of Colombia. Abbreviations: solar multiple (sm), high irradiation (high irr.), photovoltaic panel (PV), Concentrated Solar Power (CSP).
      :header: "Parameter", "Value", "Units"
      :widths: 15 15 15
      :name: tab:solarArea

      ":math:`solar_{area,rooftop}`", "530 [6a]_ ", ":math:`[km^2]`"
      ":math:`solar_{area,ground}`", "3800 [6a]_ ", ":math:`[km^2]`"
      ":math:`solar_{area,ground,high~irr}`", "70 [6a]_ ", ":math:`[km^2]`"
      ":math:`power\_density_{pv}`", "0.186 [6b]_ ", "[GW/:math:`km^2]`"
      ":math:`power\_density_{csp}`", "0.186 [6c]_ ", "[GW/:math:`km^2]`"
      ":math:`power\_density_{solar~thermal}`", "0.7 [6c]_ ", "[GW/:math:`km^2]`"
      ":math:`sm_{max}`", "4 [6c]_ ", ":math:`[-]`"
      
   .. [6a]
      Computed based on the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI. All the area with high irradiation is located in the department of La Guajira.
      
   .. [6b]
      Data from :cite:`dupont_2020` (mono-silicon PV).
      
   .. [6c]
      Based on existing design configurations (c.f. Section 2.5 of :cite:`dupont_2020`)
      
Note that the ground areas given in :numref:`Table %s <tab:renewableTechPotentialIn2036>`
are not the total areas occupied by the solar power plants, but only the areas occupied 
by the solar panels themselves. In utility plants, panels are oriented perpendicular 
to the sunlight. As a consequence, a space is required to avoid shadow between rows of panels.
In the literature, the *ground cover ratio* is defined as the total
spatial requirements of large scale solar PV relative to the area of the
solar panels. This ratio is estimated to have a value around five
:cite:`dupont_2020`, which means that for each square
meter of PV panel installed, four additional square meters are needed.
After taking into account this *ground cover ratio*, we can compute that
the value given for :math:`solar_{area,ground}` corresponds to covering
1.7% of Colombia's land surface with solar power plants (not taking into account the rooftop area
used by rooftop PV).

Biomass and non-renewable waste
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the literature, waste and biomass are often merged. In this work however, a
distinction is made between *biomass* and *non-renewable waste*. Non-renewable waste accounts for
all the fossil waste, such as plastics, whereas biomass is organic and
assumed renewable. Biomass is split into three categories: one that can be
digested by bacteria (*wet biomass*), such as apple peel; one that
cannot (*woody biomass*), such as wood; and one which consists of crops directly cultivated for
fuel production (*biofuels*). Hence, the organic waste
generated by the municipalities is accounted for in *woody or wet
biomass* and not as *non-renewable waste*. *Non-renewable waste* accounts for common sludges, municipal solid waste (MSW) landfill, MSW
not landfill (composting, recycling) and paper cardboard. Finally, *biofuels* are splitted into *bioethanol* and
*biodiesel*. These are assumed perfectly substitutable to fossil gasoline and diesel, respectively.

:numref:`Table %s <tab:renewableResourcesPotentialIn2036>` gives the Colombian potential for biomass and non-renewable waste, together with their values used for the calibration to the year 2021.

.. container::

   .. csv-table:: Biomass and waste resources consumed in 2021 and their potential.
      :header: **Resources** , **2021** , **Max. potential** , **Units**
      :widths: 15 15 15 15
      :name: tab:renewableResourcesPotentialIn2036

		bioethanol , 7.2 [7a]_ , 50 [7b]_ , [TWh]
		biodiesel , 2.5 [7a]_ , 50 [7b]_ , [TWh]
		woody biomass , 34.3 [7c]_ , 24.6 [7d]_ , [TWh]
		wet biomass , 0 , 29.9 [7d]_ , [TWh]
		non-renewable waste, 0 , 5.7 [7e]_ , [TWh]
   
   .. [7a]
      Data obtained from :cite:`IEA_2023` and slightly adapted for calibration purpose.
   
   .. [7b]
      Reliable data for the local potential of bio-fuels could not be obtained. Thus, a reasonable order of magnitude of 50 TWh was chosen for both biodiesel and bioethanol. Using the energy content of biodiesel and bioethanol from :cite:`noauthor_conversion_nodate` and a yield of 4 t/ha, we compute that fully utilizing this biomass potential would amount to covering 2.5% of Colombia's surface with crops for biofuel production. In 2021, 40% of Colombia's surface was dedicated to agriculture.

   .. [7c]
      Endogenous computation, based on the data of the EUDs and technologies in 2021. This value matches grossly the primary solid biomass data for year 2019 given in :cite:`IEA_world_energy_balances`.
      
   .. [7d]
      :cite:`Magne2024` performed a detailed assessment of the renewable biomass potential of all countries in South America. The corresponding data for Colombia were thus retrieved: the "forestry" potential gave the potential for woody biomass and the "agro-industrial" and "municipal waste" potentials were added to give the wet biomass potential.

   .. [7e] 
      According to :cite:`IDEAM2023`, Colombia annually produces around 1.5 million tons of non-renewable waste. We multiply this figure by an energy content of 13.7 MJ/kg (taken from :cite:`usEnergy_2019`) to obtain the total potential.
      
The corresponding cost for year 2036 and GHG emissions are given in :numref:`Table %s <tab:costs_resources_biomass>`. Two metrics are proposed for GHG emissions:
one accounting for the impact associated with extraction, transportation and
combustion (based on GWP100a-IPCC2013 :cite:`Moret2017PhDThesis`); the other accounting
only for direct emissions related to combustion (based on :cite:t:`Quaschning2015`). The first metric
is used when imposing constraints on the energy system's total emissions; the second one is used when calibrating the model to the year 2021 (see Section **GHG emissions**).

.. container::

   .. csv-table:: Cost and GHG emissions of biomass and waste resources.
      :header: **Resources** , **c**:sub:`op` [8a]_ , **gwp**:sub:`op` [8b]_ , **CO**:sub:`2direct`
      :widths: 15 15 15 15
      :name: tab:costs_resources_biomass
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		bioethanol , 88.2 , 0 , 250
		biodiesel , 47.3 , 0 , 270
		woody biomass , 4.7 , 11.8 , 390
		wet biomass , 0.7 , 11.8 , 390
		non-renewable waste, 2.7 , 150 , 260 [8c]_

.. [8a]
   Computed based on the supplementary data of the PEN 2050 :cite:`PEN2050`.

.. [8b]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion. Note that this metric accounts for negative 
   upstream emissions, hence the null or very low value for the different biomass resources.

.. [8c]
   Assuming that the energy content can be assimilated to plastics.


Fossil fuels
------------

A large share of fossil fuels used in Colombia is produced and refined domestically :cite:`IEA_2023`. They include coal and hydrocarbons (natural gas, gasoline, diesel, light fuel oil). However, Colombia is also importing an increasing amount of natural gas.


The availability of all fossil fuel resources is set to a value high enough to allow unlimited use in the model, except for local natural gas. Its availability in 2036 is set to to 13 TWh, based on :cite:`wtw2023`.

:numref:`Table %s <tab:costs_resources_fossil>` therefore gives the costs and GHG emissions associated with both domestic and imported fossil fuels in Colombia. Imported coal is included,
even though the model never selects it given the lower cost and unbounded potential of local coal.

.. container::

   .. csv-table:: Cost and GHG emissions of domestically produced and imported fossil fuels, in 2036. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resources** , **c**:sub:`op` [9a]_  , **gwp**:sub:`op` [9b]_ , **CO**:sub:`2direct` [9c]_
      :widths: 15 15 15 15
      :name: tab:costs_resources_fossil
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		local coal , 7.3 , 401 , 360
		imported coal , 11.2 , 401 , 360
		local natural gas , 25.4 , 267 , 200
		imported natural gas , 39.0 , 267 , 200
		local gasoline , 44.1 , 345 , 250
		local diesel , 23.7 , 315 , 270
		local LFO , 30.0 , 312 , 260

.. [9a]
   Computed based on the supplementary data of the PEN 2050 :cite:`PEN2050`.

.. [9b]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion
   
.. [9c]
   Direct emissions related to combustion :cite:`Quaschning2015`. These data are not used in EnergyScope Colombia (since the capacity of technology CCS_industrial is set to zero), but they help us to check that the calibration of EnergyScope to the 2021 Colombian energy system of is correct.




Electricity imports and exports
-------------------------------

The availability of the cross-border electricity imports and exports, when defined as "resources", is considered as infinite. Indeed, the real constraint comes from the grid infrastructure for imports and exports, as expressed by eqs. :eq:`eq:elecImpLimited` and :eq:`eq:elecExpLimited`. The values of parameters for these equations are given in :numref:`Table %s <tab:elecImpExpParams>`.

.. container::

   .. csv-table:: Values of the parameters which constrain cross-border electricity imports and exports.
      :header: "Parameter", "Value", "Units"
      :widths: 15 15 15
      :name: tab:elecImpExpParams

      ":math:`elec_{import,max}`", "0.395 [10a]_ ", "[GW]"
      ":math:`elec_{export,max}`", "0.535 [10b]_ ", "[GW]"
      ":math:`f_{max}(HVAC)`", "1.5 [10c]_ ", "[GW]"
      
   .. [10a]
      Import capacities from Ecuador indicated in :cite:`IEA_2023`.
      
   .. [10b]
      Export capacities to Ecuador indicated in :cite:`IEA_2023`.
      
   .. [10c]
      Value inspired from the interconnection projects described in :cite:`IEA_2023`.

The corresponding costs and GHG emissions are given in :numref:`Table %s <tab:costs_elec_import_export>`.

.. container::

   .. csv-table:: Cost and GHG emissions associated to electricity imports and exports, in 2036. Abbreviations: Electricity (elec.).
      :header: **Resources** , **c**:sub:`op` , **gwp**:sub:`op` [11a]_ , **CO**:sub:`2direct`
      :widths: 15 15 15 15
      :name: tab:costs_elec_import_export
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`] , [kgCO :sub:`2`-eq/MWh :sub:`fuel`]
		elec imports , 42.9 [11b]_ , 206 , 0
		elec exports , 38.6 [11c]_ , 0 , 0

.. [11a]
   GWP100a-IPCC2013 metric: impact associated to extraction, transportation and combustion. The value for electricity imports takes into account the projected progressive decarbonisation of Ecuador's electricity mix.

.. [11b]
   Computed based on the supplementary data of the PEN 2050 :cite:`PEN2050`.
   
.. [11c]
   The costs of electricity exports is assumed to be equal to 90% of the costs of electricity imports, to account for cross-border tariffs.
   

Export of electrofuels
----------------------

Electrofuels (or e-fuels) are a recent type of fuel. They are produced using (renewable) electricity. Thus, they do not act as an
energy source but rather as an energy carrier. The export of e-fuels is currently envisaged by Colombia as a possible strategy
for partially compensating for the planned decrease in fossil fuels' exports. Four types of e-fuels are considered in EnergyScope:
hydrogen, methane, ammonia and methanol. In the model's code, they are designated with the appendix 'RE' to distinguish them from 
their fossil-based counterparts.

The Belgian Hydrogen Import Coalition computed a projection of the import costs of e-fuels from international markets for the year 2035 :cite:`H2coalition2020shipping`. They indicate that 85% of cost would correspond to production cost, local transmission and local terminalling. The rest would correspond
to shipping and remote terminalling. Thus, the revenue of an e-fuel exporter like Colombia would be equal to 85% of the
computed import cost. The corresponding values are indicated in :numref:`Table %s <tab:costs_resources_efuels>`.

.. container::

   .. csv-table:: Cost and GHG emissions associated to electricity imports and exports, in 2036. Abbreviations: Electricity (elec.).
      :header: **Resources** , **c**:sub:`op` **(import)** , **c**:sub:`op` **(export)**
      :widths: 15 15 15
      :name: tab:costs_resources_efuels
		
		 , [USD\ :sub:`2021`/MWh :sub:`fuel`] [12a]_ , [USD\ :sub:`2021`/MWh :sub:`fuel`] [12b]_
		green hydrogen , 126.6 , 107.6
		e-methane , / , 107.6
		e-ammonia , 87.4 , 74.3
		e-methanol , 119.9 , 101.9

.. [12a]
   Taken as equal to the import cost of e-fuels from international market, computed by :cite:`H2coalition2020shipping`.
   
.. [12b]
   Estimated as 85% of the import cost.
   

.. _sec:app1_end_uses:

Energy demand and political framework
=====================================

Aggregated values for the calibration of the 2021 EUDs are given in :numref:`Table %s <tab:eud_2021>`. Details and assumptions for these EUDs are given in the following sub-sections, as well as their yearly profiles.

.. container::

   .. csv-table:: EUD in 2021. Abbreviations: end-use type (EUT)
      :header: **EUT** , **Households** , **Services** , **Industry**, **Transportation** , "Units"
      :widths: 30 20 20 20 15 10
      :name: tab:eud_2021
		
		electricity - baseload , 9049, 13309, 35771,0,[GWh]
		electricity - variable , 2785, 4096, 11008,0,[GWh]
		space heating , 13640.0 ,4033.4,21853.4 ,0,[GWh]
		hot water , 1136.7 ,0,10926.7 ,0,[GWh]
		process heating , 0,0,26473.9 ,0,[GWh]
		space cooling , 2556.0 ,2528.0 ,0,0,[GWh]
		process cooling , 0,0,277.8 ,0,[GWh]
		passenger mobility , 0,0,0,347881.0 ,[Mpkm]
		freight , 0,0,0,97783.0 ,[Mtkm]
		non-energy demand , 0,0,22423.0 ,0,[GWh] 
   
The aim is to compute the evolution of these EUDs across years with GEMMES, which will then feed them to EnergyScope. However, as a first approximation,
the 2036 EUDs can simply be computed by multiplying the values of :numref:`Table %s <tab:eud_2021>` by 1.4. To obtain the 2050 EUDs,
the values can instead be multiplied by 1.7. These multiplication factors are obtained from a projection for energy demand which was
given to us by Departamento Nacional de Planeación (DNP), the Colombian National Planning Department.

.. _ssec:app1_electricity_end_uses:

Electricity
-----------

The aggregated electricity consumed in Colombia in 2021 was 84.4 [TWh] :cite:`IEA_2023`. The electricity used for supplying cooling, mobility and non-energy demand is subtracted from it to give an electricity EUD of 76.0 [TWh]. This corresponds to the difference between the FEC and the EUD as they are defined
in EnergyScope (see the section on the `Conceptual modelling framework <#app:sec:conceptual_modelling_framework>`__). A part of the electricity is assumed 
to be fixed through time (e.g. electricity for industrial processes). The other part is varying, such as electricity used for lighting. To split the electricity EUD between households, services and industry, we use shares retrieved from the National energy plan 2022.

The daily profile of electricity generation across the year (nearly identical to the one of electricity consumption) is retrieved from the Sinergox XM website :cite:`SIN_genration_per_source`. We choose to take the average between the profiles of 2021 and 2022. Based on this average profile, the electricity EUD can be split between baseload and variable load. The daily profile is then complemented with an estimated typical hourly profile for each weekday :cite:`elec_hourly_weekday` in order to get an hourly profile across the year. This profile is then used to produce the :math:`\%_{elec}` time series, which is the normalised profile of the variable electricity load.



.. _ssec:app1_heating_end_uses:

Heating and cooling
-------------------

The aggregated EUD for different heating types and their decomposition into households, services and industry was retrieved from :cite:`plazas_nino_2023`,
then adapted through the calibration process to match the CO\ :math:`_2` emissions of Colombia in 2021. Process heating and hot water are supposed to be fixed through
time, unlike space heating which is spread over the year according to :math:`\%_{sh}`. We define process heat as the high temperature heat required in some
industrial processes. This heat cannot be supplied by technologies such as heat pumps or thermal solar.

Similarly, the aggregated EUD for space cooling and its sectoral decomposition was taken from :cite:`plazas_nino_2023`. The values for process cooling were retrieved from :cite:`upme_process_cooling_2024`. Again, process cooling is supposed to be fixed through time, unlike space cooling which is spread over the year according to :math:`\%_{sc}`. 

The time series :math:`\%_{sh}` and :math:`\%_{sc}` are based on our own computations, following the method
described in :cite:`borasio2022deep`. As explained in the supplementary material of :cite:`borasio2022deep`, *"hourly time series of energy demand for space
heating and cooling are evaluated differently from one modelled area to another by considering
the corresponding values of Heating (and Cooling) Degree Days (HDD). The methodology
used for the calculation of hourly heating and cooling time series is based on the definition of
HDD proposed by the Joint Research Centre (JRC) and adopted in* :cite:`ISPRA`. *After having chosen a
winter “comfort temperature”* (:math:`T_{comf}`) *of 18°C, and knowing the outdoor temperature of the
investigated place* (:math:`T_{out}`) *at a certain hour (t) of the day, the yearly HDD are given by the sum,
extended to all the hours of the year, of the difference between the indoor comfort temperature
and the outdoor temperature, where 15°C is the outdoor temperature threshold. The same
applies for yearly CDD definition, in which the summer “comfort temperature” is set to 21°C
and the outdoor temperature threshold is assumed to be equal to 24°C."*

.. math::
    HDD = \sum_{t \in \text{T}}(T_{comf}(t) - T_{out}(t))\quad\text{if}\quad T_{out}(t) < 15°C\\
    HDD = 0\quad\text{if}\quad T_{out}(t) \geq 15°C
    :label: eq:HDD
    
.. math::
    CDD = \sum_{t \in \text{T}}(T_{out}(t) - T_{comf}(t))\quad\text{if}\quad T_{out}(t) > 24°C\\
    CDD = 0\quad\text{if}\quad T_{out}(t) \leq 24°C
    :label: eq:CDD

Hourly outdoor temperature time series are retrieved from :cite:`Renewables_ninja` for the cities of 
Bogota, Medellin, Cali and Barranquilla. The HDD and CDD time series for these individual
cities are then computed following eqs. :eq:`eq:HDD` and :eq:`eq:CDD`. We observe that the HDD time
series for Cali and Barranquilla is null practically all year long. Idem for the CDD time series of
Bogota, Medellin and Cali. Thus, we compute the HDD time series for Colombia as a weighted average of
the time series of Bogota and Medellin. The CDD time series for Colombia is equal to the CDD time series
for Barranquilla. The respective weights of the HDD time series of Bogota and Medellin are 0.62 and 0.38,
which correspond to the ratio of the populations of the areas to which these cities belong.

.. _ssec:app1_demand_mobility:

Mobility
--------

The aggregated EUDs for passenger mobility and freight were retrieved from :cite:`plazas_nino_2023`, then
adapted through the calibration process to match the CO\ :math:`_2` emissions of Colombia in 2021. These EUDs are
spread over the year according to :math:`\%_{pass}` and :math:`\%_{fr}`, respectively. 

For :math:`\%_{pass}`, we assume that the passenger mobility EUD has the same profile for every day of the
year. This daily profile is taken from data for Switzerland (data from Figure 12 of :cite:`USTransportation`).
For :math:`\%_{fr}`, we take a uniform value over the 8760 hours of the year.

Non-energy
----------

Non-energy EUD value in 2021 is taken from :cite:`IEA_2023`. We assume it to be uniformly spread over the
8760 hours of the year.

.. _app:discount_and_interest_rates:

Discount rate and interest rate
-------------------------------

The discount rate represents the temporal preference between present and future financial value. In EnergyScope, the discount rate is used
for annualising investment costs and hence allow to compare them with yearly costs in the future. For the case of Colombia, a discount rate
of 6.4% is used, following :cite:`plazas_nino_2023`.

.. _app:ESTD_CO_data_technologies:

Technologies
============

The technologies are regrouped by their main output types.

Electricity generation
----------------------

The electricity generation technologies are regrouped into two categories depending
on the resources used: renewable or not.

.. _ssec:app1_renewables:

Renewables
~~~~~~~~~~

:numref:`Table %s <tab:elec_prod_re>` gives the data for the renewable electricity generation technologies
modelled in EnergyScope Colombia, together with their sources. The data for :math:`f_{max}` were already
given in :numref:`Table %s <tab:renewableTechPotentialIn2036>` ("max. potential"). The :math:`f_{min}`
values for renewable electricity technologies in 2036 are equal to their installed capacity in 2021,
already given in :numref:`Table %s <tab:renewableTechPotentialIn2036>`. Regarding hydro dam however, the value for
:math:`f_{min}` in 2036 is equal to the installed capacity in 2021, to which is added the capacity of the 
Hidroituango power plant currently under construction (2.4 GW). The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.

.. container::

   .. csv-table:: Renewable electricity production technologies in 2036. Abbreviations: concentrated solar power 
      with parabolic trough (CSP PT), concentrated solar power with solar tower (CSP ST).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [14aa]_ , **lifetime**, **c**:sub:`p`
      :widths: 19 18 24 23 15 15
      :name: tab:elec_prod_re
		 
		  , [USD\ :sub:`2021`/kW :sub:`e`], [USD\ :sub:`2021`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%]
		 Hydro dam, 3116 [14a]_, 31.2 [14a]_, 1693, 40 [14b]_, 50 [14c]_
		 Hydro river, 2825 [14a]_, 28.3 [14a]_, 1263, 40 [14b]_, 50 [14c]_
		 Rooftop PV, 1040 [14d]_, 13.7 [14d]_, 2081, 40 [14d]_, 19 [14e]_
		 Utility scale PV, 474 [14d]_, 11.9 [14d]_, 2081, 40 [14d]_, 21 [14e]_
		 Onshore wind, 1427 [14d]_, 23.7 [14d]_, 623, 30 [14f]_, 27 [14g]_
		 Offshore wind, 1773 [14d]_, 71.3 [14d]_, 623, 30 [14f]_, 50 [14h]_
		 Geothermal, 10576 [14i]_, 196.5 [14i]_, 24929, 30, 86 [14j]_
		 CSP PT collector, 6350 [14l]_ , 88.3 [14l]_ , 0 [14m]_ , 25, 83 [14n]_
		 CSP ST collector, 7777 [14l]_ , 88.8 [14l]_ , 0 [14m]_ , 25, 83 [14n]_
		 CSP PT power block, 1473 [14l]_ , 88.3 [14l]_ , 0 [14m]_ , 25, 33 [14o]_
		 CSP ST power block, 1083 [14l]_ , 88.8 [14l]_ , 0 [14m]_ , 25, 33 [14o]_
		 Biomass central, 2364 [14d]_, 98.6 [14d]_, 332, 35, 87
		 
.. [14aa]
   Data from :cite:`weidema_ecoinvent_2013`
   
.. [14a]
   Data based on costs reported for the neighbouring country Bolivia, in :cite:`ENDE2015` and :cite:`ENDE2019`

.. [14b]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_grande_2014`
   
.. [14c]
   Computed based on installed capacities and yearly production of hydro power pants in 2021, with data from :cite:`IEA_2023`.
   
.. [14d]
   Data from :cite:`Danish_energy_agency_2023`
   
.. [14e]
   Retrieved from the open-source database from :cite:`dupont_2020`, available at https://github.com/EliseDup/WorldEROI. 
   
.. [14f]
   Data taken from :cite:`association_des_entreprises_electriques_suisses_aes_energie_2013`  
   
.. [14g]
   Data from :cite:`plazas_nino_2023`.
   
.. [14h]
   Data from :cite:`Renewables_ninja`.
   
.. [14i]
   ORC cycle at 6 km depth for electricity generation. Based on Table 17 of :cite:`Carlsson2014`. We took the reference case in 2030.
   
.. [14j]
   Data from :cite:`association_des_entreprises_electriques_suisses_aes_electricite_2012`

.. [14l]
   Data collected by :cite:`dommisse2020modelling`.  
   
.. [14m]
   Not computed yet. To be completed in the near future.
   
.. [14n]
   Value obtained after running EnergyScope on the Colombian case study. The high capacity factor obtained is due to the heat storage associated with the CSP.
   
.. [14o]
   This value of :math:`c_{p}` is the mean value of the :math:`c_{p,t}` time series computed below.  
   
 

:numref:`Table %s <tab:elec_prod_re>` includes the values of the yearly capacity factor (:math:`c_p`) of technologies.
As described in the Model Formulation Section, the values of :math:`c_p` for intermittent renewables is in fact equal to one, while
it is the value of their hourly load factor, :math:`c_{p,t}`, which is binding. The value of :math:`c_p` given in 
:numref:`Table %s <tab:elec_prod_re>` for intermittent renewables is in fact the mean value of :math:`c_{p,t}` over the year.
The yearly profile (which sums up to one) of :math:`c_{p,t}` for intermittent renewables is computed as follows.

The areas with high solar potential are first identified using the open-source database from :cite:`dupont_2020`, available
at https://github.com/EliseDup/WorldEROI. The yearly PV production profile is then retrieved from :cite:`Renewables_ninja` 
for the following (lon,lat) coordinates: (3.75,-72.5), (4.5,-71.5), (5.25,-70.5) and (6.0,-69.0). The average between these
4 profiles is taken to give the yearly profile of :math:`c_{p,t}` for the PV rooftop and PV utility technologies.

Similarly, the areas with the highest potential for onshore wind are identified using the open-source database from
:cite:`dupont_2020`. The yearly wind turbine's production profile is then retrieved from :cite:`Renewables_ninja`
for the following (lon,lat) coordinates: (4.5,-71.25), (5.25,-71.0) and (6.0,-69.75). The weighted average between
these 3 profiles is then computed, with respective weights (0.25, 0.25, 0.5). This gives us the yearly profile of 
:math:`c_{p,t}` for onshore wind.

For wind offshore, based on the same open-source database, the profile at latitude (13.5,-81.75) is selected with
:cite:`Renewables_ninja`. 

Regarding CSP, the (non-normalized) time series for :math:`c_{p,t}` is computed with the oemof thermal :cite:`oemf_thermal` and 
pvlib :cite:`pvlib` packages (to extract pvgis data :cite:`pvgis`). These time series give the thermal GWh of energy produced
by thermal GW of *Collector* installed. These time series are computed 
for locations of (lat,lon)=(12,-72) and (lat,lon)=(12,-71.25). These locations were identified as the ones having the highest 
CSP potential, based on the open-source database from :cite:`dupont_2020`. The mean of the two time series is then computed
to give the yearly :math:`c_{p,t}` time series for Colombia in 2036.

Finally, for hydro dam and hydro river, daily incoming water flow to hydro-electric facilities in Colombia was taken from the Sinergox XM 
website :cite:`hydro_ts`. The daily data for years 2018 to 2022 were normalized and their average was computed to give a yearly profile
:math:`c_{p,t}`. This profile was given an hourly (instead of a daily) granularity by assuming a constant value for each hour of a same day.

.. _ssec:app1_non-renewable:

Non-renewable
~~~~~~~~~~~~~

:numref:`Table %s <tab:elec_prod_nre>` gives the data for the fossil electricity generation technologies
modelled in EnergyScope Colombia, together with their sources. The minimum installed capacity (:math:`f_{min}`)
is zero, while the maximum installed capacity (:math:`f_{max}`) is set to a value high enough for each 
technology to potentially cover the entire demand. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.
The installed capacity of each technology in 2021 is given as well.

.. container::

   .. csv-table:: Non-renewable electricity production technologies in 2036. Abbreviations: combined cycle gas turbine (CCGT), capacity (capa.).
      :header: **Technology**, **c**:sub:`inv`, **c**:sub:`maint`, **gwp**:sub:`constr` [15a]_ , **lifetime** [15b]_, **c**:sub:`p`, **efficiency**, :math:`CO_{2-direct}` [15c]_, installed capa. (2021) [15i]_
      :widths: 11 17 24 23 12 8 13 8 8
      :name: tab:elec_prod_nre
		 
		  , [USD\ :sub:`2021`/kW :sub:`e`], [USD\ :sub:`2021`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%], [%], [tCO2/MWh :sub:`e`], [GW]
		 CCGT, 1090 [15d]_, 27.8 [15d]_, 184, 25, 85, 63 [15e]_, 0.317, 2.43
		 CCGT ammonia [15f]_, 1090, 27.8, 184, 25, 59, 50, 0, 0
		 Coal central, 3555 [15g]_, 41.5 [15g]_, 332, 35, 86 [15b]_, 54 [15h]_, 0.667, 0.61
		 
.. [15a]
   Data from :cite:`weidema_ecoinvent_2013`
   
.. [15b]
   Data from :cite:`bauer_new_2008`
   
.. [15c]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of electricity produced. Emissions computed based
   on resource used and specific emissions given in Table 9.
   
.. [15d]
   Data from :cite:`iea_-_international_energy_agency_iea_2014-1`   
   
.. [15e]
   Data from :cite:`bauer_new_2008`, 0.4-0.5 GW CCGT in 2036 (realistic optimistic scenario)	 

.. [15f]
   Use of Ammonia in CCGT is at its early stage. Mitsubishi is developping 
   a 40 MW turbine and promises similar efficiency as gas CCGT :cite:`nose2021development`. 
   However, the high emissions of NOx requires a removal equipment which will reduce the 
   power plant efficiency. As gas and ammonia CCGT will be similar, we expect a similar cost and lifetime. 
   The only exception is the efficiency, which is assumed at 50% instead of 63% for a gas CCGT :cite:`ikaheimo2018power`.
   
.. [15g]
   1.2 GW\ \ :math:`_{\text{e}}` IGCC power plant
   :cite:`u.s._eia_-_energy_information_administration_updated_2013`.
   *c*:sub:`maint` is fixed cost (48.1 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y) +
   variable cost (0.82 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y assuming 7500
   h/y).   
   
.. [15h]
   Data from :cite:`bauer_new_2008`, IGCC in 2025 (realistic optimistic scenario)	 

.. [15i]
   Data from :cite:`IEA_2023`
   
   
Heating and cogeneration
------------------------

Tables :numref:`%s <tbl:ind_cogen_boiler>`,
:numref:`%s <tbl:dhn_cogen_boiler>` and
:numref:`%s <tbl:dec_cogen_boiler>` detail the data for
the considered industrial, centralized and decentralised CHP
technologies, respectively. In some cases, it is assumed that
industrial (Table :numref:`%s <tbl:ind_cogen_boiler>`)
and centralized (Table :numref:`%s <tbl:dhn_cogen_boiler>`) technologies are
the same.
:math:`f_{min}` and :math:`f_{max}` for
heating and CHP technologies are 0 and 1000 TW\ :sub:`th`,
respectively. The latter value is high enough for each technology to
supply the entire heat demand in its layer. The maximum
(:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100%
respectively, i.e. they are not constraining the model.


.. container::

   .. table:: Industrial heating and cogeneration technologies, in 2036. Abbreviations: Combined Heat and Power (CHP), electricity (Elec.), Natural Gas (NG).
      :name: tbl:ind_cogen_boiler
   
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      |              | :math:`c_    | :math:`c_    | :math:`gwp_  | :math:`li    | :math:`c_    | :math:`\eta  | :math:`\eta  | :math:`C     |
      |              | {inv}`       | {maint}`     | {constr}`    | fetime`      | {p}`         | _e`          | _{th}`       | O_{2,        |
      |              |              |              |              |              |              |              |              | direct}`     |
      |              |              |              |              |              |              |              |              | [16a]_       |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      |              | [USD         | [USD         | [kgCO        | [y]          | [%]          | [%]          | [%]          | [tCO2/       |
      |              | :sub:`2021`  | :sub:`2021`  | :sub:`2-eq.` |              |              |              |              | MWh          |
      |              | /kW          | /kW          | /kW          |              |              |              |              | :sub:`th`    |
      |              | :sub:`th`]   | :sub:`th`/y] | :sub:`th`]   |              |              |              |              | ]            |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | CHP NG       | 1989         | 127.8        | 1024         | 25           | 85           | 44           | 46           | 0.435        |
      |              | [16b]_       | [16c]_       | \            | \            |              | [16d]_       | [16d]_       |              |
      |              |              |              | :cite:`\     | :cite:`\     |              |              |              |              |
      |              |              |              | weidem\      | ove\         |              |              |              |              |
      |              |              |              | a_ecoi\      | _arup_\      |              |              |              |              |
      |              |              |              | nvent_2013`  | and_pa\      |              |              |              |              |
      |              |              |              |              | rtners\      |              |              |              |              |
      |              |              |              |              | _ltd_r\      |              |              |              |              |
      |              |              |              |              | eview_\      |              |              |              |              |
      |              |              |              |              | 2011`        |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | CHP          | 1527         | 55.9         | 165.3        | 25           | 85           | 18           | 53           | 0.735        |
      | Wood         | \            | \            | \            | \            |              | \            | \            |              |
      | [16e]_       | \            | \            | \            | \            |              | \            | \            |              |
      |              | :cite:`\     | :cite:`\     | :cite:`\     | :cite:`\     |              | :cite:`\     | :cite:`\     |              |
      |              | iea_\        | iea_\        | weidem\      | ove\         |              | iea_\        | iea_\        |              |
      |              | -_inte\      | -_inte\      | a_ecoi\      | _arup_\      |              | -_inte\      | -_inte\      |              |
      |              | rnatio\      | rnatio\      | nvent_2013`  | and_pa\      |              | rnatio\      | rnatio\      |              |
      |              | nal_en\      | nal_en\      |              | rtners\      |              | nal_en\      | nal_en\      |              |
      |              | ergy_a\      | ergy_a\      |              | _ltd_r\      |              | ergy_a\      | ergy_a\      |              |
      |              | gency_\      | gency_\      |              | eview_\      |              | gency_\      | gency_\      |              |
      |              | iea_20\      | iea_20\      |              | 2011`        |              | iea_20\      | iea_20\      |              |
      |              | 14-1`        | 14-1`        |              |              |              | 14-1`        | 14-1`        |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | CHP          | 4135         | 152.4        | 647.8        | 25           | 85           | 20           | 45           | 0.578        |
      | Waste        | [16f]_       | [16f]_       | [16g]_       | \            |              | \            | \            |              |
      |              |              |              |              | :cite:`\     |              | :cite:`\     | :cite:`\     |              |
      |              |              |              |              | ove\         |              | ove\         | ove\         |              |
      |              |              |              |              | _arup_\      |              | _arup_\      | _arup_\      |              |
      |              |              |              |              | and_pa\      |              | and_pa\      | and_pa\      |              |
      |              |              |              |              | rtners\      |              | rtners\      | rtners\      |              |
      |              |              |              |              | _ltd_r\      |              | _ltd_r\      | _ltd_r\      |              |
      |              |              |              |              | eview_\      |              | eview_\      | eview_\      |              |
      |              |              |              |              | 2011`        |              | 2011`        | 2011`        |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | Boiler       | 83           | 1.7          | 12.3         | 17           | 95           | 0            | 92.7         | 0.216        |
      | NG           | :cite:`\     | :cite:`\     | [16h]_       | \            |              |              | \            |              |
      |              | \            | \            |              | \            |              |              | :cite:`\     |              |
      |              | Mo\          | Mo\          |              | :cite:`\     |              |              | Mo\          |              |
      |              | ret201\      | ret201\      |              | eur\         |              |              | ret201\      |              |
      |              | 7PhDTh\      | 7PhDTh\      |              | opean_\      |              |              | 7PhDTh\      |              |
      |              | esis`        | esis`        |              | commis\      |              |              | esis`        |              |
      |              |              |              |              | sion_e\      |              |              |              |              |
      |              |              |              |              | nergy_\      |              |              |              |              |
      |              |              |              |              | 2008`        |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | Boiler       | 163          | 3.3          | 28.9         | 17           | 90           | 0            | 86.4         | 0.451        |
      | Wood         | \            | \            | \            | \            |              |              | \            |              |
      |              | :cite:`\     | :cite:`\     | \            | \            |              |              | :cite:`\     |              |
      |              | Mo\          | Mo\          | :cite:`\     | :cite:`\     |              |              | Mo\          |              |
      |              | ret201\      | ret201\      | weidem\      | eur\         |              |              | ret201\      |              |
      |              | 7PhDTh\      | 7PhDTh\      | a_ecoi\      | opean_\      |              |              | 7PhDTh\      |              |
      |              | esis`        | esis`        | nvent_2013`  | commis\      |              |              | esis`        |              |
      |              |              |              |              | sion_e\      |              |              |              |              |
      |              |              |              |              | nergy_\      |              |              |              |              |
      |              |              |              |              | 2008`        |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | Boiler       | 77           | 1.7          | 12.3         | 17           | 95           | 0            | 87.3         | 0.309        |
      | Oil          | [16i]_       | [16j]_       | \            | \            |              |              | \            |              |
      |              |              |              | \            | \            |              |              | :cite:`\     |              |
      |              |              |              | :cite:`\     | :cite:`\     |              |              | Mo\          |              |
      |              |              |              | weidem\      | eur\         |              |              | ret201\      |              |
      |              |              |              | a_ecoi\      | opean_\      |              |              | 7PhDTh\      |              |
      |              |              |              | nvent_2013`  | commis\      |              |              | esis`        |              |
      |              |              |              |              | sion_e\      |              |              |              |              |
      |              |              |              |              | nergy_\      |              |              |              |              |
      |              |              |              |              | 2008`        |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | Boiler       | 163          | 3.3          | 48.2         | 17           | 90           | 0            | 82           | 0.439        |
      | Coal         | [16l]_       | [16l]_       | \            | \            |              |              |              |              |
      |              |              |              | \            | \            |              |              |              |              |
      |              |              |              | :cite:`\     | :cite:`\     |              |              |              |              |
      |              |              |              | weidem\      | eur\         |              |              |              |              |
      |              |              |              | a_ecoi\      | opean_\      |              |              |              |              |
      |              |              |              | nvent_2013`  | commis\      |              |              |              |              |
      |              |              |              |              | sion_e\      |              |              |              |              |
      |              |              |              |              | nergy_\      |              |              |              |              |
      |              |              |              |              | 2008`        |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | Boiler       | 163          | 3.3          | 28.9         | 17           | 90           | 0            | 82           | 0.317        |
      | Waste        | [16l]_       | [16l]_       | [16m]_       | \            |              |              |              |              |
      |              |              |              |              | \            |              |              |              |              |
      |              |              |              |              | :cite:`\     |              |              |              |              |
      |              |              |              |              | eur\         |              |              |              |              |
      |              |              |              |              | opean_\      |              |              |              |              |
      |              |              |              |              | commis\      |              |              |              |              |
      |              |              |              |              | sion_e\      |              |              |              |              |
      |              |              |              |              | nergy_\      |              |              |              |              |
      |              |              |              |              | 2008`        |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+
      | Direct       | 469          | 2.1          | 1.47         | 15           | 95           | 0            | 100          | 0            |
      | Elec.        | [16n]_       | [16n]_       | \            |              |              |              |              |              |
      |              |              |              | \            |              |              |              |              |              |
      |              |              |              | :cite:`\     |              |              |              |              |              |
      |              |              |              | weidem\      |              |              |              |              |              |
      |              |              |              | a_ecoi\      |              |              |              |              |              |
      |              |              |              | nvent_2013`  |              |              |              |              |              |
      +--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+--------------+


.. [16a]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of heat produced. Emissions computed based on
   resource used and specific emissions given in Table 9.

.. [16b]
   Calculated as the average of investment costs for 50 kW\ \ :sub:`e`
   and 100 kW\ \ :sub:`e` internal combustion engine cogeneration
   systems :cite:`prognos_ag_energieperspektiven_2012`.

.. [16c]
   Calculated as the average of investment costs for 50 kW\ \ :sub:`e`
   and 100 kW\ \ :sub:`e` internal combustion engine cogeneration
   systems :cite:`rits_energieperspektiven_2007`.

.. [16d]
   200 kW\ \ :sub:`e` internal combustion engine cogeneration
   NG system, very optimistic scenario in 2035
   :cite:`bauer_new_2008`.

.. [16e]
   Biomass cogeneration plant (medium size) in 2030-2035.

.. [16f]
   Biomass-waste-incineration CHP, 450 scenario in 2035
   :cite:`iea_-_international_energy_agency_iea_2014-1`.

.. [16g]
   Impact of MSW incinerator in :cite:`Moret2017PhDThesis`,
   using efficiencies reported in the table.

.. [16h]
   Assuming same impact as industrial oil boiler.

.. [16i]
   925 kW\ \ :sub:`th` oil boiler (GTU 530)
   :cite:`walter_meier_ag_listes_2011`

.. [16j]
   Assumed to be equivalent to a NG boiler.

.. [16l]
   Assumed to be equivalent to a wood boiler.

.. [16m]
   Assuming same impact as industrial wood boiler.

.. [16n]
   Commercial/public small direct electric heating
   :cite:`nera_economic_consulting_uk_2009`.


.. container::

   .. table:: District heating technologies, in 2036. Abbreviations: biomass (bio.), CHP, digestion (dig.), hydrolysis (hydro.).
      :name: tbl:dhn_cogen_boiler

      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      |            | :math:`c_  | :math:`c_  | :math:`gwp_| :math:`li  | :math:`c_  | :math:`\eta| :math:`\eta| :math:`C   |
      |            | {inv}`     | {maint}`   | {constr}`  | fetime`    | {p}`       | _e`        | _{th}`     | O_{2,      |
      |            |            |            |            |            |            |            |            | direct}`   |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      |            | [USD       | [USD       | [kgCO      | [y]        | [%]        | [%]        | [%]        | [tCO2/     |
      |            | :sub:`2021`| :sub:`2021`| :sub:`2    |            |            |            |            | MWh        |
      |            | /kW        | /kW        | -eq.`/kW   |            |            |            |            | :sub:`th`  |
      |            | :sub:`th`] | :sub:`th`  | :sub:`th`] |            |            |            |            | ] [154]_   |
      |            |            | /y]        |            |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | HP         | 487        | 16.5       | 174.8      | 25         | 95         | 0          | 400        | 0          |
      |            | [155]_     | [156]_     | \          |            |            |            |            |            |
      |            |            |            | :cite:`\   |            |            |            |            |            |
      |            |            |            | wei\       |            |            |            |            |            |
      |            |            |            | dema_ec\   |            |            |            |            |            |
      |            |            |            | oinvent\   |            |            |            |            |            |
      |            |            |            | _2013`     |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP NG     | 1772       | 51.8       | 490.9      | 25         | 85         | 50         | 40         | 0.500      |
      |            | [157]_     | [157]_     | [158]_     | \          |            | [159]_     | [159]_     |            |
      |            |            |            |            | :cite:`\   |            |            |            |            |
      |            |            |            |            | ba\        |            |            |            |            |
      |            |            |            |            | uer_new\   |            |            |            |            |
      |            |            |            |            | _2008`     |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP        | 1527       | 55.9       | 165.3      | 25         | 85         | 18         | 53         | 0.736      |
      | Wood [160]_| :cite:`\   |            |            | :cite:`\   |            | :cite:`\   | :cite:`\   |            |
      |            | iea_\      |            |            | ove_\      |            | iea_\      | iea_\      |            |
      |            | -_inter\   |            |            | arup_an\   |            | -_inter\   | -_inter\   |            |
      |            | nationa\   |            |            | d_partn\   |            | nationa\   | nationa\   |            |
      |            | l_energ\   |            |            | ers_ltd\   |            | l_energ\   | l_energ\   |            |
      |            | y_agenc\   |            |            | _review\   |            | y_agenc\   | y_agenc\   |            |
      |            | y_iea_2\   |            |            | _2011`     |            | y_iea_2\   | y_iea_2\   |            |
      |            | 014-1`     |            |            |            |            | 014-1`     | 014-1`     |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP        | 4135       | 152.4      | 647.8      | 25         | 85         | 20         | 45         | 0.578      |
      | Waste      |            |            |            | :cite:`\   |            | :cite:`\   | :cite:`\   |            |
      | [160]_     |            |            |            | ove_\      |            | ove_\      | ove_\      |            |
      |            |            |            |            | arup_an\   |            | arup_an\   | arup_an\   |            |
      |            |            |            |            | d_partn\   |            | d_partn\   | d_partn\   |            |
      |            |            |            |            | ers_ltd\   |            | ers_ltd\   | ers_ltd\   |            |
      |            |            |            |            | _review\   |            | _review\   | _review\   |            |
      |            |            |            |            | _2011`     |            | _2011`     | _2011`     |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP        | 1941       | 158.0      | 647.8      | 25         | 85         | 13         | 16         | 2.488      |
      | bio.       | [161]_     | [161]_     | [162]_     |            | [161]_     | [161]_     | [161]_     |            |
      | dig.       |            |            |            |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP        | 6408       | 312.5      | 647.8      | 15         | 85         | 25.4       | 33.5       | 1.164      |
      | bio.       | [163]_     |            | [162]_     |            |            |            |            |            |
      | hydro.     |            |            |            |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | Boiler     | 83         | 1.7        | 12.3       | 17         | 95         | 0          | 92.7       | 0.216      |
      | NG         | :cite:`\   |            |            | :cite:`\   |            |            | :cite:`\   |            |
      |            | Moret2\    |            |            | \          |            |            | Moret2\    |            |
      |            | 017PhDT\   |            |            | europ\     |            |            | 017PhDT\   |            |
      |            | hesis`     |            |            | ean_com\   |            |            | hesis`     |            |
      |            |            |            |            | mission\   |            |            |            |            |
      |            |            |            |            | _energy\   |            |            |            |            |
      |            |            |            |            | _2008`     |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | Boiler     | 163        | 3.2        | 28.9       | 17         | 90         | 0          | 86.4       | 0.451      |
      | Wood       | :cite:`\   | :cite:`\   |            | :cite:`\   |            |            | :cite:`\   |            |
      |            | Moret2\    | Moret2\    |            | \          |            |            | Moret2\    |            |
      |            | 017PhDT\   | 017PhDT\   |            | europ\     |            |            | 017PhDT\   |            |
      |            | hesis`     | hesis`     |            | ean_com\   |            |            | hesis`     |            |
      |            |            |            |            | mission\   |            |            |            |            |
      |            |            |            |            | _energy\   |            |            |            |            |
      |            |            |            |            | _2008`     |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | Boiler     | 77         | 1.7        | 12.3       | 17         | 95         | 0          | 87.3       | 0.309      |
      | Oil        |            |            |            | :cite:`\   |            |            | :cite:`\   |            |
      |            |            |            |            | \          |            |            | Moret2\    |            |
      |            |            |            |            | europ\     |            |            | 017PhDT\   |            |
      |            |            |            |            | ean_com\   |            |            | hesis`     |            |
      |            |            |            |            | mission\   |            |            |            |            |
      |            |            |            |            | _energy\   |            |            |            |            |
      |            |            |            |            | _2008`     |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | Geo        | 2119       | 80.4       | 808.8      | 30         | 85         | 0          | 100        | 0          |
      | thermal    | [165]_     | [165]_     | \          | [165]_     |            |            |            |            |
      | [165]_     |            |            | :cite:`\   |            |            |            |            |            |
      |            |            |            | wei\       |            |            |            |            |            |
      |            |            |            | dema_ec\   |            |            |            |            |            |
      |            |            |            | oinvent\   |            |            |            |            |            |
      |            |            |            | _2013`     |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+
      | Solar      | 511        | 0.6        | 221.8      | 30         | 10         | 0          | 100        | 0          |
      | thermal    | [166]_     | [166]_     | \          | [166]_     |            |            |            |            |
      | [166]_     |            |            | :cite:`\   |            |            |            |            |            |
      |            |            |            | wei\       |            |            |            |            |            |
      |            |            |            | dema_ec\   |            |            |            |            |            |
      |            |            |            | oinvent\   |            |            |            |            |            |
      |            |            |            | _2013`     |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+------------+


.. [154]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of heat produced. Emissions computed based on
   resource used and specific emissions given in Table 9.

.. [155]
   Calculated with the equation: *c\ inv* [EUR\ \ :sub:`2011`] =
   :math:`3737.6 * E^{0.9}`, where :math:`E` is the electric power
   (kW\ \ :sub:`e`) of the compressor, assumed to be 2150
   kW\ \ :sub:`e`. Equation from
   :cite:`becker_methodology_2012`, taking only the cost of
   the technology (without installation factor).

.. [156]
   Ground-water heat pump with 25 years lifetime
   :cite:`iea_-_international_energy_agency_renewables_2007`.

.. [157]
   CCGT with cogeneration
   :cite:`iea_-_international_energy_agency_iea_2014-1`.

.. [158]
   Impact of NG CHP in from :cite:`Moret2017PhDThesis`,
   using efficiencies reported in the table.

.. [159]
   :math:`\eta`\ \ \ :sub:`e` and :math:`\eta`\ \ \ :sub:`th`
   at thermal peak load of a 200-250 MW\ \ :sub:`e` CCGT plant,
   realistic optimistic scenario in
   2035 :cite:`bauer_new_2008`.

.. [160]
   Assumed same technology as for industrial heat and CHP
   (:numref:`Table %s <tbl:ind_cogen_boiler>`)

.. [161]
   Cost estimations from
   :cite:`ro2007catalytic` and efficiencies from
   :cite:`poschl2010evaluation`. Data in line with IEA:
   :cite:`ETSAP2010_BiomassForHeatAndPower`

.. [162]
   Construction emissions is assimilated to an industrial CHP waste
   technology.

.. [163]
   Own calculation

.. [165]
   Geothermal heat-only plant with steam driven
   absorption heat pump 70/17\ \ :math:`^o`\ \ C at 2.3 km depth (from
   :cite:`DanishEnergyAgency2019`).

.. [166]
   Total system excluding thermal storage (from
   :cite:`DanishEnergyAgency2019`).



.. container::

   .. table:: Decentralised heating and cogeneration technologies, in 2036. Abbreviations: Combined Heat and Power (CHP), electricity (Elec.), Fuel Cell (FC), Heat Pump (HP), Natural Gas (NG) and thermal (th.).
      :name: tbl:dec_cogen_boiler


      +------------+------------+------------+------------+------------+------------+------------+------------+
      |            | :math:`c_  | :math:`c_  | :math:`gwp_| :math:`li  | :math:`c_  | :math:`\eta| :math:`\eta|
      |            | {inv}`     | {maint}`   | {constr}`  | fetime`    | {p}`       | _e`        | _{th}`     |
      |            |            |            |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      |            | [USD       | [USD       | [kgCO      | [y]        | [%]        | [%]        | [%]        |
      |            | :sub:`2021`| :sub:`2021`| :sub:`2    |            |            |            |            |
      |            | /kW        | /kW        | -eq.`/kW   |            |            |            |            |
      |            | :sub:`e`]  | :sub:`e`/y]| :sub:`e`]  |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | HP         | 695        | 29.7 [209]_| 164.9      | 18         | 100        | 0          | 300        |
      |            | [207]_     |            | \          | [209]_     |            |            |            |
      |            | [208]_     |            | \          |            |            |            |            |
      |            |            |            | \          |            |            |            |            |
      |            |            |            | :cite:`\   |            |            |            |            |
      |            |            |            | weid\      |            |            |            |            |
      |            |            |            | ema_e\     |            |            |            |            |
      |            |            |            | coinv\     |            |            |            |            |
      |            |            |            | ent_2\     |            |            |            |            |
      |            |            |            | 013`       |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Thermal    | 446 [210]_ | 13.0 [211]_| 381.9      | 20         | 100        | 0          | 150        |
      | HP         | [208]_     |            | \          |            |            |            |            |
      |            |            |            | \          |            |            |            |            |
      |            |            |            | \          |            |            |            |            |
      |            |            |            | :cite:`\   |            |            |            |            |
      |            |            |            | weid\      |            |            |            |            |
      |            |            |            | ema_e\     |            |            |            |            |
      |            |            |            | coinv\     |            |            |            |            |
      |            |            |            | ent_2\     |            |            |            |            |
      |            |            |            | 013`       |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP        | 1989       | 127.8      | 1024       | 20         | 100        | 44         | 46         |
      | NG [212]_  |            |            |            | \          |            |            |            |
      |            |            |            |            | :cite:`\   |            |            |            |
      |            |            |            |            | b\         |            |            |            |
      |            |            |            |            | auer_\     |            |            |            |
      |            |            |            |            | new_2\     |            |            |            |
      |            |            |            |            | 008`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | CHP        | 1844 [213]_| 113.1      | 1          | 20         | 100        | 39 [215]_  | 43 [215]_  |
      | Oil        |            | [213]_     | 024 [214]_ |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | FC NG      | 10229      | 190.6      | 2193       | 20         | 100        | 58 [218]_  | 22 [218]_  |
      |            | [216]_     | [217]_     | \          | \          |            |            |            |
      |            |            |            | \          | \          |            |            |            |
      |            |            |            | \          | \          |            |            |            |
      |            |            |            | :cite:`\   | :cite:`\   |            |            |            |
      |            |            |            | weid\      | gerbo\     |            |            |            |
      |            |            |            | ema_e\     | ni_fi\     |            |            |            |
      |            |            |            | coinv\     | nal_2\     |            |            |            |
      |            |            |            | ent_2\     | 008`\      |            |            |            |
      |            |            |            | 013`       |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | FC H\      | 10229      | 190.6      | 2193       | 20         | 100        | 58         | 22         |
      | :sub:`2`   |            |            |            | \          |            |            |            |
      | [219]_     |            |            |            | \          |            |            |            |
      |            |            |            |            | \          |            |            |            |
      |            |            |            |            | :cite:`\   |            |            |            |
      |            |            |            |            | gerbo\     |            |            |            |
      |            |            |            |            | ni_fi\     |            |            |            |
      |            |            |            |            | nal_2\     |            |            |            |
      |            |            |            |            | 008`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Boiler     | 224        | 6.7        | 4.8        | 17         | 100        | 0          | 90         |
      | NG         | \          | \          | \          | \          |            |            | \          |
      |            | \          | \          | \          | \          |            |            | \          |
      |            | \          | \          | \          | \          |            |            | :cite:`\   |
      |            | :cite:`\   | :cite:`\   | :cite:`\   | :cite:`\   |            |            | Moret\     |
      |            | Moret\     | Moret\     | Moret\     | eur\       |            |            | 2017P\     |
      |            | 2017P\     | 2017P\     | 2017P\     | opean\     |            |            | hDThe\     |
      |            | hDThe\     | hDThe\     | hDThe\     | _comm\     |            |            | sis`       |
      |            | sis`       | sis`       | sis`       | issio\     |            |            |            |
      |            |            |            |            | n_ene\     |            |            |            |
      |            |            |            |            | rgy_2\     |            |            |            |
      |            |            |            |            | 008`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Boiler     | 653        | 22.8       | 21.1       | 17         | 100        | 0          | 85         |
      | Wood       | \          | \          | [220]_     | \          |            |            | \          |
      |            | \          | \          |            | \          |            |            | \          |
      |            | \          | \          |            | \          |            |            | \          |
      |            | :cite:`\   | :cite:`\   |            | :cite:`\   |            |            | :cite:`\   |
      |            | pant\      | pant\      |            | eur\       |            |            | pant\      |
      |            | aleo_in\   | aleo_in\   |            | opean\     |            |            | aleo_in\   |
      |            | teg\       | teg\       |            | _comm\     |            |            | teg\       |
      |            | ratio\     | ratio\     |            | issio\     |            |            | ratio\     |
      |            | n_201\     | n_201\     |            | n_ene\     |            |            | n_201\     |
      |            | 4-1`       | 4-1`       |            | rgy_2\     |            |            | 4-1`       |
      |            |            |            |            | 008`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Coal stove | 653        | 22.8       | 21.1       | 17         | 100        | 0          | 85         |
      | [18a]_     |            |            |            |            |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Boiler     | 201        | 12.0 [221]_| 21.1\      | 17         | 100        | 0          | 85         |
      | Oil        | \          |            | \          | \          |            |            | \          |
      |            | \          |            | \          | \          |            |            | \          |
      |            | \          |            | \          | \          |            |            | :cite:`\   |
      |            | :cite:`\   |            | :cite:`\   | :cite:`\   |            |            | Moret\     |
      |            | walt\      |            | Moret\     | eur\       |            |            | 2017P\     |
      |            | er_me\     |            | 2017P\     | opean\     |            |            | hDThe\     |
      |            | ier_a\     |            | hDThe\     | _comm\     |            |            | sis`       |
      |            | g_lis\     |            | sis`       | issio\     |            |            |            |
      |            | tes_2\     |            |            | n_ene\     |            |            |            |
      |            | 011`       |            |            | rgy_2\     |            |            |            |
      |            |            |            |            | 008`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Solar      | 1016 [222]_| 11.4 [223]_| 221.2      | 20         | 11.3\      | 0          | NA         |
      | Th.        |            |            | \          | \          | [224]_     |            |            |
      |            |            |            | \          | \          |            |            |            |
      |            |            |            | \          | \          |            |            |            |
      |            |            |            | :cite:`\   | :cite:`\   |            |            |            |
      |            |            |            | weid\      | nera\      |            |            |            |
      |            |            |            | ema_e\     | _econ\     |            |            |            |
      |            |            |            | coinv\     | omic_co\   |            |            |            |
      |            |            |            | ent_2\     | nsu\       |            |            |            |
      |            |            |            | 013`       | lting\     |            |            |            |
      |            |            |            |            | _uk_2\     |            |            |            |
      |            |            |            |            | 009`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+
      | Direct     | 56 [225]_  | 0          | 1.47       | 15         | 100        | 0          | 100        |
      | Elec.      |            | .3 [226]_  | \          | \          |            |            |            |
      |            |            |            | \          | \          |            |            |            |
      |            |            |            | \          | \          |            |            |            |
      |            |            |            | :cite:`\   | :cite:`\   |            |            |            |
      |            |            |            | weid\      | nera\      |            |            |            |
      |            |            |            | ema_e\     | _econ\     |            |            |            |
      |            |            |            | coinv\     | omic_co\   |            |            |            |
      |            |            |            | ent_2\     | nsu\       |            |            |            |
      |            |            |            | 013`       | lting\     |            |            |            |
      |            |            |            |            | _uk_2\     |            |            |            |
      |            |            |            |            | 009`       |            |            |            |
      +------------+------------+------------+------------+------------+------------+------------+------------+

.. [207]
   10.9 kW\ \ :sub:`th` Belaria compact IR heat pump
   :cite:`hoval_sa_catalogue_2016`.

.. [208]
   Catalog data divided by 2.89. 2.89 is the ratio between
   Swiss catalog prices and prices found in the literature. Calculated
   by dividing the average price of a decentralised NG boiler (489
   CHF\ \ :sub:`2015`/kW\ \ :sub:`th`) in Swiss catalogs
   :cite:`viessman_viessman_2016` by the price for the
   equivalent technology found in literature (169
   CHF\ \ :sub:`2015`/kW\ \ :sub:`th`, from
   :cite:`Moret2017PhDThesis`).

.. [209]
   6 kW\ \ :sub:`th` air-water heat pump
   :cite:`nera_economic_consulting_uk_2009`.

.. [210]
   Specific investment cost for a 15.1 kW\ \ :sub:`th` absorption heat
   pump (Vitosorp 200-F) :cite:`viessman_viessman_2016`

.. [211]
   3% of *c\ inv* (assumption).

.. [212]
   Assumed same technology as for industrial CHP NG
   (:numref:`Table %s <tbl:ind_cogen_boiler>`)

.. [213]
   Assumed to be equivalent to a 100 kW\ \ :sub:`e`
   internal combustion engine cogeneration NG system
   :cite:`rits_energieperspektiven_2007,prognos_ag_energieperspektiven_2012`.

.. [214]
   Assuming same impact as decentralised NG CHP.

.. [215]
   Efficiency data for a 200 kW\ \ :sub:`e` diesel
   engine :cite:`weidema_ecoinvent_2013`

.. [216]
   System cost (including markup) for a 5 kW\ \ :sub:`e` solid-oxide FC
   system, assuming an annual production of 50000 units
   :cite:`battelle_manufacturing_2014`.

.. [217]
   2% of the investment
   cost :cite:`iea_-_international_energy_agency_iea_2014-1`.

.. [218]
   Solid-oxide FC coupled with a NG turbine, values for very
   optimistic scenario in 2025 :cite:`gerboni_final_2008`.

.. [219]
   Assumed to be equivalent to FC NG.

.. [220]
   Assuming same impact as NG and oil decentralised boilers.
   
.. [18a] 
   We take the same characteristics for coal stove as for wood boiler  

.. [221]
   6% of *c\ inv*, based on ratio between investment and OM cost of
   boiler of similar size
   in :cite:`european_commission_energy_2008`.

.. [222]
   504 CHF\ \ :sub:`2015`/m\ \ :math:`^2` for the UltraSol Vertical 1V
   Hoval system :cite:`hoval_sa_catalogue_2016`. For
   conversion from €\ \ :sub:`2015`/m\ \ :math:`^2` to
   €\ \ :sub:`2015`/kW\ \ :sub:`th`, it is assumed an annual heat
   capacity factor of 6.5% based on Uccles data.

.. [223]
   1.1% of the investment cost, based on ratio investment-to-OM cost
   in :cite:`nera_economic_consulting_uk_2009`.

.. [224]
   The calculation of the capacity factor for solar thermal is based on
   the IRM model :cite:`IRM_Atlas_Irradiation` with
   radiation data from the city of Uccles, Belgium.

.. [225]
   Resistance heaters with fan assisted air circulation
   in :cite:`european_commission_energy_2008`.

.. [226]
   In the lack of specific data, same investment-to-OM ratio as for
   direct electric heating in the industry sector
   (:numref:`Table %s <tbl:ind_cogen_boiler>`).

Cooling
-------

:numref:`Table %s <tab:cooling_technos>` gives the data for the cooling technologies modelled in EnergySope.
The cooling technologies are the ones previously modelled in :cite:`borasio2022deep`. All data are taken from
:cite:`borasio2022deep`, unless indicated otherwise. The minimum installed capacity (:math:`f_{min}`)
is zero, while the maximum installed capacity (:math:`f_{max}`) is set to a value high enough for each 
technology to potentially cover the entire demand. The maximum (:math:`f_{max,\%}`) and minimum
(:math:`f_{min,\%}`) shares are imposed to 0 and 100% respectively, i.e. they are not constraining the model.

.. container::

   .. csv-table:: Cooling technologies in 2036. Abbreviations: coefficient of performance (COP).
      :header: **Technology**, **c**:sub:`inv` [19a]_, **c**:sub:`maint` [19a]_, **gwp**:sub:`constr`, **lifetime** [15b]_, **c**:sub:`p`, **COP**
      :widths: 11 17 24 23 12 8 13
      :name: tab:cooling_technos
		 
		  , [USD :sub:`2021`/kW :sub:`e`], [USD :sub:`2021`/kW :sub:`e`/year], [kgCO :sub:`2`-eq./kW :sub:`e`], [year], [%], [%]
		 Electrical refrigeration cycle, 670, 28.6, 165, 20, 100, 318
		 Thermal refrigeration cycle, 430, 12.9, 382, 20, 100, 146
		 Industrial electric cooling, 872, 7.1, 175, 20, 95, 242
		 
.. [19a]
   Data taken from :cite:`borasio2022deep`

.. _sec:app1_vehicles_mobility:

Transport
---------

Passenger mobility
~~~~~~~~~~~~~~~~~~

The vehicles available for passenger mobility are regrouped into two
categories: public and private. Private vehicles account for vehicles
owned or rented by the user. On the other hand, public mobility accounts
for the shared vehicles, such as buses, coaches, trains, trams, metros and trolleys.
Vehicles' data from the literature are not directly transposable into the
model. Mobility data are usually given per vehicle, such as a
vehicle cost or an average occupancy per vehicle. These data from the literature are
summarised in :numref:`Table %s <tbl:mob_specific_costs_calculation>`.
All cost data are first expressed in € :sub:`2015`. They are converted in USD :sub:`2021` in other tables later on.

.. container::

   .. table:: Specific investment cost calculation based on vehicle investment data, in 2036. Abbreviations: average (av.), Fuel Cell (FC), Hybrid Electric Vehicle (HEV), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), public (pub.).
      :name: tbl:mob_specific_costs_calculation

      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | **Vehicle | :math:`Ve | :math:`Ma | :math:`Oc | :math:`Av.| :math:`Av.| :math:`li | :math:`gw | 
      | type**    | h.~Cost`  | intenance`| cupancy`  | ~distance`| ~speed`   | fetime`   | p_{       |
      |           |           | [241]_    |           |           |           | [242]_    | constr}`  |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      |           |           | [k€\      | [k€\      | [         | [1000     | [         | [         |                            
      |           |           | :math:`_\ | :math:`_\ | pass/     | km/y]     | km/h]     | years]    |                                
      |           |           | 2015`     | 2015`     | veh.]     |           |           |           |                                
      |           |           | /veh.]    | /veh./y]  |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Gasoline  | 21 [243]_ | 1.2       | 1.26      | 18 [245]_ | 40        | 10        | 17.2      | 
      | car       |           |           | [244]_    |           |           |           |           |                                
      |           |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Diesel    | 22 [243]_ | 1.2       | 1.26      | 18 [245]_ | 40        | 10        | 17.4      |
      | car       |           |           | [244]_    |           |           |           |           |                                
      |           |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | NG        | 22 [243]_ | 1.2       | 1.26      | 18 [245]_ | 40        | 10        | 17.2      |
      | car       |           |           | [244]_    |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | HEV       | 22 [243]_ | 1.74      | 1.26      | 18 [245]_ | 40        | 10        | 26.2      |
      | car       |           |           | [244]_    |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | PHEV      | 23 [243]_ | 1.82      | 1.26      | 18 [245]_ | 40        | 10        | 26.2      |
      | car       |           |           | [244]_    |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | BEV       | 23 [243]_ | 0.5       | 1.26      | 18 [245]_ | 40        | 10        | 19.4      |
      | [246]_    |           |           | [244]_    |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | FC        | 22 [243]_ | 0.5       | 1.26      | 18 [245]_ | 40        | 10        | 39.6      |
      | car       |           |           | [244]_    |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Tram      | 2500      | 50.0      | 200       | 60        | 20        | 30        | 0         |
      | and       |           |           |           |           |           |           | [247]_    |                                
      | metro     |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Diesel    | 220       | 11.0      | 24        | 39        | 15        | 15        | 0 [247]_  |
      | bus       |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Diesel    | 300       | 12.0      | 24        | 39        | 15        | 15        | 0 [247]_  |
      | HEV       |           |           |           |           |           |           |           |                                
      | bus       |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Gasoline  | 220       | 11.0      | 24        | 39        | 15        | 15        | 0 [247]_  |
      | bus       |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | NG        | 220       | 11.0      | 24        | 39        | 15        | 15        | 0 [247]_  |
      | bus       |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | FC        | 375       | 11.3      | 24        | 39        | 15        | 15        | 0 [247]_  |
      | bus       |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Train     | 10000     | 200.0     | 80        | 200       | 83        | 40        | 0 [247]_  |
      | pub.      |           |           |           |           |           |           |           |                                
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+


.. [241]
   own calculation. The maintenance cost
   was assumed proportional to the investment cost and depending the
   type of powertrain. the average speed of private cars is calculated
   assuming that it is used 5% of the time (i.e. 1h12). Knowing the
   annual distance, the value is approximately 40 km/h.

.. [242]
   In 2016, the average age of private cars was 8.9 years with a
   difference between regions :cite:`kwanten2016kilometres`.

.. [243]
   Costs are from mid-range vehicles estimation
   and projections of :cite:`national2013transitions`.

.. [244]
   The federal bureau office estimates
   a decreasing average occupancy for cars down to 1.26
   passenger/vehicle in 2030
   :cite:`BureaufederalduPlan2012`).

.. [245]
   In 2016, averaged yearly distance for
   private cars were between 9 500 and 21 100 kms depending on the type
   of powertrains, but in average around 18 000 kms.

.. [246]
   Low range BEV have been implemented. Otherwise the investment cost is
   more than twice.

.. [247]
   No data found.



In Belgium, the car occupancy rate is less than 1.3 passengers per car:
1.3 in 2015 and estimated at 1.26 in
:cite:`BureaufederalduPlan2012`. The annual distance of a
car depends on its type of motorization: from 9 500 km/year for a city
gasoline car, to 21 100 km/year for a CNG one. On average, the distance
is 18 000 km/year. The average age of a car is 8.9 years in 2016, with a
variation between regions: in Brussels it is 10 years. On average, the
distance is 18 000 km/year. The average age of a car is 8.9 years in
2016, with a rather strong variation between regions: in Brussels it is
10 years. Finally, a car drives on average slightly more than one hour
a day (1h12). By means of simplicity, we use these data for Colombia.

For public transportation, data for Belgium were collected from various reports
:cite:`taszka2018analyse,moawad2013light,james2012mass`.
These data were adapted based on discussions with Belgian experts in the
field. They are reported in :numref:`Table %s <tbl:mob_specific_costs_calculation>`.

Surprisingly, in 2036, vehicles' costs are similar regardless of the
power-train.  :numref:`Figure %s <fig:car_cost_over_transition>` shows how
the vehicle cost would vary over the transition, data from
:cite:`national2013transitions`. Today, we verify a strong
price difference between the different technologies; this difference
should decrease along with the development of new technologies. The price
difference between two technologies will become small as early as 2036
(:math:`\leq`\ 10%). In their work, the
:cite:t:`national2013transitions` estimates the cost of
promising technologies in 2015 lower than the real market price. This is
the case for BEV and FC vehicles, where the price ranges today around
60 k€\ :sub:`2015` . These differences can be justified by three facts:
these vehicles are usually more luxurious than others; The selling price
does not represent the manufacturing cost for prototypes; the study is
from 2013 and may have overestimated the production in 2015 and 2020.


.. figure:: /images/belgian_data/app_bestd_car_cost_transition.png
   :alt: Mid-range vehicle costs evolution during the transition. Reference (**1.0 (ref)**) is at 19.7 k€\ :sub:`2015`. Abbreviations: Carbon capture (CC), LFO, methanation (methan.), methanolation (methanol.), Natural Gas (NG), Synthetic Natural Gas (SNG), storage (sto.) and synthetic (syn.).
   :name: fig:car_cost_over_transition
   :width: 14cm

   Mid-range vehicle costs evolution during the transition. Reference
   (**1.0 (ref)**) is at 19.7 k€\ :sub:`2015`. Abbreviations: Carbon
   capture (CC), LFO, methanation (methan.), methanolation (methanol.),
   Natural Gas (NG), Synthetic Natural Gas (SNG), storage (sto.) and synthetic (syn.).

.. math::
   c_{inv} (i) = \frac{vehicle~cost (i)}{occupancy (i)\cdot average~speed (i)} ~~~~~~ \forall i \in \text{TECH OF EUT} (PassMob)
   :label: eq:c_inv_for_mob_pass_calculation
    
.. math::
   c_p = \frac{average~distance(i)}{average~speed(i)\cdot 8760} ~~~~~~ \forall i \in \text{TECH OF EUT} (PassMob)
   :label: eq:c_p_for_mob_pass_calculation
    
.. math::
   veh._{capa} (i) = occupancy (i)\cdot average~speed ~~~~~~ \forall i \in \text{TECH OF EUT} (PassMob)
   :label: eq:veh_capa_for_mob


From data of :numref:`Table %s <tbl:mob_specific_costs_calculation>`,
specific parameters for the model are deduced. The specific investment
cost (:math:`c_{inv}`) is calculated from the vehicle cost, its average speed
and occupancy, Eq. :eq:`eq:c_inv_for_mob_pass_calculation`. The cost is then converted from € :sub:`2015` to USD :sub:`2021`.
The capacity factor (:math:`c_{p}`) is calculated based on the ratio between
yearly distance and average speed, Eq. :eq:`eq:c_p_for_mob_pass_calculation`.
The vehicle capacity is calculated based on the average occupancy and
average speed, Eq. . :eq:`eq:veh_capa_for_mob`.
:numref:`Table %s <tbl:mob_costs>` summarises this information
for each passenger vehicle.

An additional vehicle is proposed: methanol car. 
This choice is motivated to offer a zero emission fuel that could be competitve compared to electric or hydrogen vehicles.
We assume that methanol is used through a spark-ignition engine in cars, 
and has similar performances compared to a gasoline car. 
This technology is added in the following tables.

.. container::

   .. table:: Passenger mobility financial information, in 2036 (based on data in :numref:`Table %s <tbl:mob_specific_costs_calculation>`). Abbreviations: Fuel Cell (FC), Hybrid Electric Vehicle (HEV), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), public (pub.).
      :name: tbl:mob_costs

      +-----------+----------+----------+----------+----------+----------+
      | **Vehicle | :math:`c_| :math:`c_| :math:`g | :math:`c_| :math:`V |
      | type**    | {inv}`   | {maint}` | wp_{     | p`       | eh.~capa`|
      |           |          |          | constr}` |          |          |
      +-----------+----------+----------+----------+----------+----------+
      |           | [USD/km  | [USD/km  | [kgCO\   | [%]      | [pass-km |
      |           | -pass]   | -pass    | :sub:`2` |          | /h/veh.] |
      |           |          | /h/y]    | -eq./km  |          |          |
      |           |          |          | -pass/h] |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Gasoline  | 594      | 33.8     | 342      | 5.1      | 50       |
      | car       |          |          |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Diesel    | 614      | 33.8     | 346      | 5.1      | 50       |
      | car       |          |          |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | NG car    | 606      | 33.8     | 342      | 5.1      | 50       |
      +-----------+----------+----------+----------+----------+----------+
      | HEV car   | 606      | 47.9     | 519      | 5.1      | 50       |
      +-----------+----------+----------+----------+----------+----------+
      | PHEV car  | 645      | 47.9     | 519      | 5.1      | 50       |
      +-----------+----------+----------+----------+----------+----------+
      | BEV       | 613      | 14.1     | 385      | 5.1      | 50       |
      |           |          |          |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | FC car    | 950      | 14.1     | 786      | 5.1      | 50       |
      |           | [21c]_   |          |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Methanol  | 594      | 33.8     | 342      | 5.1      | 50       |
      | car       |          |          |          |          |          |
      | [21b]_    |          |          |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Gasoline  | 30       | 1.7      | 17       | 5.1      | 10       |
      | motorcycle| [21d]_   | [21d]_   |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Electrical| 49       | 1.1      | 31       | 5.1      | 10       |
      | motorcycle| [21e]_   | [21e]_   |          |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Tram and  | 883      | 17.6     | 0        | 34.2     | 4000     |
      | metro     |          |          | [21a]_   |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Diesel    | 863      | 43.1     | 0        | 29.7     | 360      |
      | bus       |          |          | [21a]_   |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Diesel    | 1177     | 47.0     | 0        | 29.7     | 360      |
      | HEV bus   |          |          | [21a]_   |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | Gasoline  | 863      | 43.1     | 0        | 29.7     | 360      |
      | bus       |          |          | [21a]_   |          |          |
      +-----------+----------+----------+----------+----------+----------+
      | NG bus    | 863      | 43.1     | 0 [21a]_ | 29.7     | 360      |
      +-----------+----------+----------+----------+----------+----------+
      | FC bus    | 1471     | 44.1     | 0 [21a]_ | 29.7     | 360      |
      +-----------+----------+----------+----------+----------+----------+
      | Train     | 2127     | 76.6     | 0 [21a]_ | 27.5     | 6640     |
      | pub.      |          |          |          |          |          |
      +-----------+----------+----------+----------+----------+----------+

.. [21a]
   No data found

.. [21b]
   No data were found for methanol cars. Thus, we assume that the 
   technology is similar to a gasoline car (except the fuel).
   
.. [21c]
   Departing from the computations described above, this CAPEX value has been increased
   to be more in line with the values given in :cite:`EC_scen2020` and :cite:`Schnidrig2021`
   
.. [21d]
   A cost ratio of 5% between gasoline car and gasoline motorcycle is given in
   :cite:`plazas_nino_2023`. We thus compute the investment and maintenance costs of 
   gasoline motorcycle by multiplying the data of the technology 'gasoline car'
   by this ratio.

.. [21e]
   A cost ratio of 8% between BEV and electrical motorcycle is given in
   :cite:`plazas_nino_2023`. We thus compute the investment and maintenance costs of 
   electrical motorcycle by multiplying the data of the technology BEV
   by this ratio.
   

:numref:`Table %s <tbl:passenger_vehicles>` summarises
the projected energy efficiencies for the different vehicles. For public
vehicles in 2036, the energy efficiencies are calculated with a linear
interpolation between the 2010 and 2050 values presented in :numref:`Table %s <tbl:passenger_vehicles>` in
Codina Gironès et al :cite:`codina_girones_strategic_2015`.
For private vehicles, estimates of energy consumption of Belgian cars
in 2030 are taken from :cite:`BureaufederalduPlan2012`.
:numref:`Table %s <tbl:passenger_vehicles>` also gives the minimum and maximum shares
of each vehicle type in 2036. The shares in 2021 are given as well.

.. container::

   .. table:: Fuel and electricity consumption for passenger mobility technologies in 2036 :cite:`codina_girones_strategic_2015`, and minimum/maximum shares allowed in the model. Abbreviations: Fuel Cell (FC), Hybrid Electric Vehicle (HEV), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), public (pub.).
      :name: tbl:passenger_vehicles

      ===================== ============ =============== ============================ ============================ ======================================
      **Vehicle type**      **Fuel**     **Electricity** **f**:math:`_\textbf{min,%}` **f**:math:`_\textbf{max,%}` **f**:math:`_\textbf{%}` (2021) [22a]_
      \                     [Wh/km-pass] [Wh/km-pass]    [Wh/km-pass]                 [%]	                      [%]		
      Gasoline car          497  [22b]_  0               0                            100                          33
      Diesel car            435  [22b]_  0               0                            100                          0
      NG car                345  [22b]_  0               0                            100                          15
      HEV [22c]_            336  [22b]_  0               0                            100                          0
      PHEV [22d]_           138  [22b]_  109 [22b]_      0                            100                          0
      BEV                   0            161 [22e]_      0                            100                          0
      FC car                219  [22e]_  0               0                            100                          0
      Methanol car          460  [22b]_  0               0                            100                          0
      Gasoline motorcycle   149  [22f]_  0               0                            100			   55
      Electrical motorcycle 0 		 55  [22g]_      0			      100			   0
      Tram & Trolley        0            63  [22h]_      0                            50 [22i]_                    0
      Diesel bus            265          0               0                            100                          75
      Diesel HEV bus        198          0               0                            100                          0
      NG bus                268          0               0                            100                          0
      FC bus                225          0               0                            100                          0
      Train pub.            0            65 [22h]_       0                            30 [22i]_                    0
      ===================== ============ =============== ============================ ============================ ======================================

.. [22a]
   Data deduced from energy consumption of transport in :cite:`IEA_2023`.

.. [22b]
   calculation based on vehicle consumption in
   2030 :cite:`BureaufederalduPlan2012` and occupancy of
   2030 :cite:`BureaufederalduPlan2012`. According to
   :cite:`codina_girones_strategic_2015`, gas car are
   assumed to consume 25% more than diesel cars.

.. [22c]
   Using gasoline as only fuel.

.. [22d]
   It is assumed that electricity is used to cover 40% of the total
   distance and petrol to cover the remaining 60%.

.. [22e]
   Departing from the work of :cite:`Limpens2021thesis`, these efficiency values have been adapted
   to be more in line with the values given in :cite:`EC_scen2020` and :cite:`Schnidrig2021`

.. [22f]
   A fuel consumption ratio of 27% between gasoline motorcycle and gasoline car is given in
   :cite:`plazas_nino_2023`. We thus compute the fuel consumption of 
   gasoline motorcycle by multiplying the value of the technology 'gasoline car'
   by this ratio.
   
.. [22g]
   A fuel consumption ratio of 28% between electrical motorcycle and BEV is given in
   :cite:`plazas_nino_2023`. We thus compute the fuel consumption of 
   electrical motorcycle by multiplying the value of the technology BEV
   by this ratio.

.. [22h]
   Based on real data for the French case
   in 2004, from :cite:`enerdata2004efficacite`. An increase
   of efficiency of 25% was assume.

.. [22i]
   Our own expert guesses.


The size of the BEV batteries is assumed to be the one from a Nissan
Leaf (ZE0) (24 kWh [257]_). The size of the PHEV batteries is assumed to
be the one from Prius III Plug-in Hybrid (4.4 kWh [258]_). The
performances of BEV and PHEV batteries are assimilated to a Li-ion
battery as presented in :numref:`Table %s <tab:StoDataAdvanced>`. 
The state of charge of the electric vehicles (:math:`soc_{ev}`) is 
constrained to a minimum of 60% at 7 a.m. every days.

Finally, the share of passenger mobility which can be supplied by public mobility is bounded by :math:`\%_{public,min}` and :math:`\%_{public,max}`. Similarly, the maximum share of private passenger mobility that can be supplied by motorcycles is given by :math:`\%_{private,motorc,max}` (see Eq. :eq:`eq:f_max_perc_motorcycle` in the Model Formulation Section). The values and assumptions for these three parameters are given in :numref:`Table %s <tab:passenger_mob_shares>`.

.. container::

   .. csv-table:: Limiting shares for passenger mobility in 2021 and 2036.
      :header: **Parameter**, **Value in 2021**, **Value in 2036**
      :widths: 20 20 20 
      :name: tab:passenger_mob_shares
		 
		 :math:`\%_{public_{min}}`, 0%, 70%
		 :math:`\%_{public_{max}}` [23a]_, 70%, 70%
		 :math:`\%_{private_{motorc_{max}}}` [23b]_, 55%, 55%
		 
.. [23a]
   We assume that the maximum share of public passenger mobility in 2036 is the value it had in 2021. This value is taken from :cite:`plazas_nino_2023`.
   
.. [23b]
   We assume that the maximum share of motorcycles in 2036 is the value it had in 2021. This value is taken from :cite:`plazas_nino_2023`.  


Freight
~~~~~~~

The technologies available for freight are trains, trucks and
boats. Similarly to previous section, the data for freight are
given per vehicle type. These data are summarised in :numref:`Table %s <tbl:mob_specific_costs_calculation_freight>`.
All cost data are first expressed in € :sub:`2015`. They are converted in USD :sub:`2021` in other tables later on.

.. container::

   .. table:: Specific investment cost for freight vehicles, in 2036. Trucks data are from a report of 2019 :cite:`Karlstrom_fuetruck_2019`. Abbreviations: electric (elec.), Fuel Cell (FC) and Natural Gas (NG).
      :name: tbl:mob_specific_costs_calculation_freight
   
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | **Vehicle | :math:`Ve | :math:`Ma | :math:`To | :math:`Av.| :math:`Av.| :math:`li |
      | type**    | h.~Cost`  | intenance`| nnage`    | ~distance`| ~speed`   | fetime`   |
      |           |           | [24a]_    |           |           | [24a]_    |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      |           |           | [k€\      | [k€\      | [         | [1000     | [         |
      |           |           | :math:`_  | :math:`_  | pass/     | km/y]     | km/h]     |
      |           |           | {2015}`   | {2015}`   | veh.]     |           |           |
      |           |           | /veh.]    | /veh./y]  |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Freight   | 4020      | 80.4      | 550       | 210       | 70        | 40        |
      | train     |           |           |           |           |           |           |
      | [24a]_    |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Boat      | 2750      | 137.5     | 1200      | 30        | 30        | 40        |
      | Diesel    |           |           |           |           |           |           |
      | [24a]_    |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Boat NG   | 2750      | 137.5     | 1200      | 30        | 30        | 40        |
      | [24a]_    |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Boat      | 2750      | 137.5     | 1200      | 30        | 30        | 40        |
      | Methanol  |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Truck     | 167       | 8.4       | 10        | 36.5      | 45        | 15        |
      | Diesel    |           |           |           | [24b]_    |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Truck     | 167       | 8.4       | 10        | 36.5      | 45        | 15        |
      | Gasoline  |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Truck     | 181       | 5.4       | 10        | 36.5      | 45        | 15        |
      | FC        |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Truck     | 347       | 10.4      | 10        | 36.5      | 45        | 15        |
      | Elec.     |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+
      | Truck     | 167       | 8.4       | 10        | 36.5      | 45        | 15        |
      | NG        |           |           |           |           |           |           |
      +-----------+-----------+-----------+-----------+-----------+-----------+-----------+

.. [24a]
   Own calculation

.. [24b]
   In 2016, the average distance was between 16 974 up to 63 305 km per
   year depending on the truck category. Based on our own calculation,
   we found an average of 36 500 km per year.



Trucks have similar cost except for electric trucks. The latter has a
battery that supplies the same amount of kilometers as other
technologies. As a consequence, half of the truck's cost is related to the
battery pack.

.. math::
   c_{inv} (i) = \frac{vehicle~cost (i)}{tonnage (i)\cdot average~speed (i)} ~~~~~~ \forall i \in \text{TECH OF EUT} (FreightMob)
   :label: eq:c_inv_for_mob_calculation_fr
    
.. math::
   c_p = \frac{average~distance(i)}{average~speed(i)\cdot 8760} ~~~~~~ \forall i \in \text{TECH OF EUT} (FreightMob)
   :label: eq:c_p_for_mob_calculation_fr
    
.. math::
   veh._{capa} (i) = tonnage (i)\cdot average~speed ~~~~~~ \forall i \in \text{TECH OF EUT} (FreightMob)
   :label: eq:veh_capa_for_mob_fr


From :numref:`Table %s <tbl:mob_specific_costs_calculation_freight>`,
specific parameters for the model are deduced. Except for the technology
construction specific GHG emissions (:math:`gwp_{constr}`) where no data was
found. The specific investment cost (:math:`c_{inv}`) is calculated from the
vehicle cost, its average speed and occupancy in Eq.
:eq:`eq:c_inv_for_mob_calculation_fr`. The cost is then converted from € :sub:`2015` to USD :sub:`2021`.
The capacity factor (:math:`c_{p}`) is calculated based on the ratio between
yearly distance and average speed in Eq.
:eq:`eq:c_p_for_mob_calculation_fr`. The vehicle capacity is calculated based on the average occupancy and
average speed in Eq.
Eq. :eq:`eq:veh_capa_for_mob_fr`. :numref:`Table %s <tbl:mob_costs_fr>` summarises these information for each
freight vehicle.

Similarly to the methanol car, additional power trains have been added in order to open the competition between e-fuels and electric vehicles (including fuel cells electric vehicles). 
Methanol could be used, with projected performances similar to the ones reached when using methane. 
Based on this approach, two technologies have been added: methanol boats and methanol trucks.

.. container::

   .. table:: Freight financial information, in 2036. Abbreviations: electric (elec.), Fuel Cell (FC) and Natural Gas (NG).
      :name: tbl:mob_costs_fr
   
      +-------------+------------+-------------+-------------+-------------+
      | **Vehicle   | :math:`c_  | :math:`c_   | :math:`c_   | :math:`V    |
      | type**      | {inv}`     | {maint}`    | p`          | eh.~capa`   |
      |             |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+
      |             | [USD/km-t] |[USD/km-t/y] | [%]         | [t-km/h     |
      |             |            |             |             | /veh.]      |
      |             |            |             |             |             |
      |             |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+
      | Freight     | 147        | 2.9         | 34.2        | 38500       |
      | train       |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+
      | Boat Diesel | 108        | 5.4         | 11.4        | 36000       |
      +-------------+------------+-------------+-------------+-------------+
      | Boat NG     | 108        | 5.4         | 11.4        | 36000       |
      +-------------+------------+-------------+-------------+-------------+
      | Boat        | 108        | 5.4         | 11.4        | 36000       |
      | Methanol    |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+
      | Truck       | 524        | 26.2        | 9.3         | 450         |
      | Diesel      |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+
      | Truck       | 524        | 26.2        | 9.3         | 450         |
      | Gasoline    |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+
      | Truck FC    | 568        | 17.0        | 9.3         | 450         |
      +-------------+------------+-------------+-------------+-------------+
      | Truck Elec. | 1089       | 32.6        | 9.3         | 450         |
      +-------------+------------+-------------+-------------+-------------+
      | Truck NG    | 524        | 26.2        | 9.3         | 450         |
      +-------------+------------+-------------+-------------+-------------+
      | Truck       | 524        | 26.2        | 9.3         | 450         |
      | Methanol    |            |             |             |             |
      +-------------+------------+-------------+-------------+-------------+


Trains and boats benefit from a very high tonnage capacity, which
drastically reducees their specific investment cost (i.e. down to 4-5 times
lower than for trucks). :numref:`Table %s <tbl:mob_costs_fr>` summarises the
projected energy efficiencies for the different vehicles in 2036, except
for the specific GHG emissions for technology construction (:math:`gwp_{constr}`)
where no data was found.

.. container::

   .. table:: Fuel and electricity consumption for freight technologies, in 2036 :cite:`codina_girones_strategic_2015`. Abbreviations: electric (elec.), Fuel Cell (FC) and Natural Gas (NG).
      :name: tbl:freight_vehicles_efficiency
   
   

      ================ ========= ===============
      **Vehicle type** **Fuel**  **Electricity**
      \                [Wh/km-t] [Wh/km-t]
      Train freight    0         68
      Boat Diesel      107       0
      Boat NG          123       0
      Boat Diesel      107       0
      Truck Diesel     513       0
      Truck FC         440       0
      Truck Elec.      0         249  [26a]_
      Truck NG  [26b]_ 590       0
      Truck Diesel     513       0
      ================ ========= ===============

.. [26a]
   Energy intensity calculated based on the diesel one, and corrected
   with an electric to diesel powertrain ratio from
   :cite:`Karlstrom_fuetruck_2019`.

.. [26b]
   The efficiency is corrected with the ratio between NG bus and diesel
   bus.

Trains are considered to be only electric. Their efficiency in 2036 is
0.068 kWh/tkm :cite:`codina_girones_strategic_2015`. The
efficiency for freight transport by diesel truck is 0.51 kWh/tkm based
on the weighted average of the efficiencies for the vehicle mix
in :cite:`codina_girones_strategic_2015`. For NG and H\ :math:`_2`
trucks, no exact data were found. Hence, we assume that the efficiency
ratio between NG coaches and diesel coaches can be used for freight
(same for H\ :math:`_2` trucks). As a consequence, the efficiency of NG and H\ :math:`_2`
trucks are 0.59 and 0.44 kWh/tkm. Boats are considered to be diesel or
gas powered. In 2015, the energy intensity ratio between diesel boats
and diesel trucks was :math:`\approx`\ 20% [267]_. By assuming a
similar ratio in 2036, we find an efficiency of 0.107 kWh/tkm and 0.123
kWh/tkm for diesel and NG boats, respectively.

The share of freight which can be supplied by different modes are bounded by the values :math:`\%_{fr,X,min}` and :math:`\%_{fr,X,max}`. 
These values are given in :numref:`Table %s <tab:freight_shares>` for 2021 and 2036. Moreover, based on energy consumption of transport 
given in :cite:`IEA_2023`, we impose that in 2021, 50% of truck transport was carried out by diesel trucks and 50% by gasoline trucks.

.. container::

   .. csv-table:: Limiting shares for freight in 2021 and 2036.
      :header: **Parameter**, **Value in 2021**, **Value in 2036**
      :widths: 20 20 20
      :name: tab:freight_shares
		 
		 :math:`\%_{fr_{rail_{min}}}`, 0.21 [27a]_, 0
		 :math:`\%_{fr_{rail_{max}}}`, 0.21 [27a]_,  0.3 [27b]_
		 :math:`\%_{fr_{boat_{min}}}`, 0.09 [27a]_, 0
		 :math:`\%_{fr_{boat_{max}}}`, 0.09 [27a]_, 0.4 [27b]_
		 :math:`\%_{fr_{road_{min}}}`, 0, 0
		 :math:`\%_{fr_{road_{max}}}`, 1, 1
		  
.. [27a]
   Data from :cite:`plazas_nino_2023`.
   
.. [27b]
   Our own expert guesses.
    
.. _sec:app1_ned:

Non-energy demand
-----------------

:cite:t:`rixhon2021comprehensive` investigates the importance of non-energy demand worlwide and its projection based on the IEA reports (:cite:`iea2018petrochemicals`). 
Three main feedstocks have been chosen : ammonia, methanol and high-value chemicals (HVCs). The latter encompasses different molecules, mainly hydrocarbons chains. 
:numref:`Figure %s <fig:ned_prod_pathways>` illustrates the different conversion pathway to produce the different non-energy demand feedstocks.

.. figure:: /images/belgian_data/ned_pathways.png
   :alt: Illustration of the technologies that produce non-energy feedstocks. 
   :name: fig:ned_prod_pathways

   Illustration of the technologies that produce non-energy feedstocks. 
   For clarity, only the most relevant flows are drawn 
   (:numref:`Figure %s <fig:bes_illustration>` includes all the flows).
   Ammonia and methanol can be used in other sectors.


The non-energy EUD is usually expressed in TWh/y without specifying the split among the feedstocks, 
such as in the IEA Extended Energy Balances :cite:`IEA_world_energy_balances`. Given the important
petroleum refining activity in Colombia, we assume that all non-energy EUD in 2021 was HVC. We keep
the same assumption for the year 2036.

Similarly to electricity, two of the three feedstocks can be used for other end-use demands. As an example, ammonia can be used for electricity production or methanol for mobility.
:numref:`Table %s <tab:hvc_prod>` summarises the technologies that produce HVC. :numref:`Table %s <tab:methanol_prod>` summarises the technologies that produce methanol; Regarding ammonia, only the Haber-Bosch process is proposed in :numref:`Table %s <tab:ammonia_prod>`. 

.. container::

   .. table:: Production of High-Value Chemicals (HVCs) from different feedstocks, in 2036. 
      :name: tab:hvc_prod
   
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_     | :math:`c_     | :math:`life | :math:`c_p` | :math:`\eta_| :math:`\eta_| :math:`\eta_| :math:`CO_  |
      |             | {inv}`        | {maint}`      | time`       |             | {fuel}`     | {e}`        | {th,ht}`    | {2,direct}` |
      |             |               |               |             |             |             |             |             | [359]_      |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | [USD\ :math:`_| [USD\ :math:`_| [y]         | [%]         | [MWh/MWh\   | [MWh/MWh\   | [MWh/MWh\   | [tCO\       |
      |             | {2021}`/kW\   | {2021}`/kW\   |             |             | :math:`_    | :math:`_    | :math:`_    | :sub:`2`    |
      |             | :math:`_      | :math:`_      |             |             | {HVC}`]     | {HVC}`]     | {HVC}`]     | /MWh\       |
      |             | {fuel}`]      | {fuel}`/y]    |             |             |             |             |             | :sub:`e`]   |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Oil to HVC  | 558           | 3.0           | 15          | 100         | 1.82        | 0.021       | 0.017       | 0.213       |
      | :cite:`yan\ |               |               |             |             |             |             |             |             |
      | g2017comp\  |               |               |             |             |             |             |             |             |
      | arative,ren\|               |               |             |             |             |             |             |             |
      | 2009petro\  |               |               |             |             |             |             |             |             |
      | chemicals`  |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Gas to HVC  | 1127          | 28.1          | 25          | 100         | 2.79        | 0.47        | 0           | 0.299       |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | cruellas\   |               |               |             |             |             |             |             |             |
      | 2019\       |               |               |             |             |             |             |             |             |
      | techno`     |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Biomass     | 2462          | 73.3          | 20          | 100         | 2.38        | 0.029       | 0.052       | 0.669       |
      | to HVC      |               |               |             |             |             |             |             |             |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | haro\       |               |               |             |             |             |             |             |             |
      | 2013\       |               |               |             |             |             |             |             |             |
      | techno\     |               |               |             |             |             |             |             |             |
      | economic`   |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Methanol    | 985           | 88.5          | 20          | 100         | 1.24        | 0           | 0.045       | 0.304       |
      | to HVC      |               |               |             |             |             |             |             |             |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | tsiropoulos\|               |               |             |             |             |             |             |             |
      | 2018\       |               |               |             |             |             |             |             |             |
      | emerging,   |               |               |             |             |             |             |             |             |
      | reyniers\   |               |               |             |             |             |             |             |             |
      | 2017\       |               |               |             |             |             |             |             |             |
      | techno`     |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+




.. container::

   .. table:: Production of methanol from different feedstocks, in 2036.
      :name: tab:methanol_prod
   
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_     | :math:`c_     | :math:`life | :math:`c_p` | :math:`\eta_| :math:`\eta_| :math:`\eta_| :math:`CO_  |
      |             | {inv}`        | {maint}`      | time`       |             | {fuel}`     | {e}`        | {th}`       | {2,direct}` |
      |             |               |               |             |             |             |             |             | [359]_      |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | [USD\ :math:`_| [USD\ :math:`_| [y]         | [%]         | [%]         | [%]         | [%]         | [tCO\       |
      |             | {2021}`/kW\   | {2021}`/kW\   |             |             |             |             |             | :sub:`2`    |
      |             | :math:`_      | :math:`_      |             |             |             |             |             | /MWh\       |
      |             | {fuel}`]      | {fuel}`/y]    |             |             |             |             |             | :sub:`e`]   |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Biomass to  | 3559          | 54.4          | 20          | 85          | 62          | 2           | 22          | 0.236       |
      | methanol    |               |               |             |             |             |             |             |             |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | DanishEnerg\|               |               |             |             |             |             |             |             |
      | yAgency2019\|               |               |             |             |             |             |             |             |
      | a`\         |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Syn.        | 2372          | 67.2          | 20          | 67          | 0           | 0           | 26.1        | -0.248      |
      | methanolat\ |               |               |             |             |             |             |             |             |
      | ion [361]_  |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Methane     | 1354          | 59.1          | 20          | 1           | 65.4        | 0           | 0           | 0.306       |
      | to          |               |               |             |             |             |             |             |             |
      | methanol    |               |               |             |             |             |             |             |             |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | col\        |               |               |             |             |             |             |             |             |
      | lodi2\      |               |               |             |             |             |             |             |             |
      | 017de\      |               |               |             |             |             |             |             |             |
      | monst\      |               |               |             |             |             |             |             |             |
      | ratin\      |               |               |             |             |             |             |             |             |
      | g`          |               |               |             |             |             |             |             |             |
      | [362]_      |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+




.. container::

   .. table:: Production of ammonia with the Haber Bosch process, in 2036. Data from :cite:t:`ikaheimo2018power`.
      :name: tab:ammonia_prod
   
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_     | :math:`c_     | :math:`life | :math:`c_p` | :math:`\eta_| :math:`\eta_| :math:`\eta_| :math:`CO_  |
      |             | {inv}`        | {maint}`      | time`       |             | {fuel}`     | {e}`        | {th}`       | {2,direct}` |
      |             |               |               |             |             |             |             |             | [359]_      |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | [USD\ :math:`_| [USD\ :math:`_| [y]         | [%]         | [%]         | [%]         | [%]         | [tCO\       |
      |             | {2021}`/kW\   | {2021}`/kW\   |             |             |             |             |             | :sub:`2`    |
      |             | :math:`_      | :math:`_      |             |             |             |             |             | /MWh\       |
      |             | {fuel}`]      | {fuel}`/y]    |             |             |             |             |             | :sub:`e`]   |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Haber bosch | 1196          | 23.3          | 20          | 85          | 79.8        | 0           |10.7         | 0           |
      | [30a]_      |               |               |             |             | (NH3)       |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+

.. [30a]
   To produce 1 unit of ammonia, the system uses 1.13 units of H\ :math:`_2` and 0.123 of electricity.




.. _ssec:app1_syn_fuels:

Synthetic fuels production
--------------------------

Synthetic fuels are expected to play a key role to phase out fossil
fuels worldwide :cite:`Rosa2017`. :numref:`Figure %s <fig:CO2andPtGLayers>` 
represents the technologies related to
synthetic fuels, including the CO\ :math:`_2` layers. Synthetic fuels can be
imported (bio-ethanol, bio-Diesel, H\ :math:`_2` or SNG) or produced by converting
biomass and/or electricity. The wet biomass - usually organic waste -
can be converted through the *biogas plant* technology to synthetic natural gas (SNG). This
technology combines anaerobic digestion and cleaning processes. Woody
biomass can be used to produce H\ :math:`_2` through *gasification*, or different oils through
*pyrolysis* or SNG through *gasification to SNG*. The different oils account for LFO, Gasoline or Diesel. 
The other processes to produce
synthetic fuels are based on water electrolysis, where the
*electrolysers* convert electricity to H\ :math:`_2`. Then, the H\ :math:`_2` can be combined
with CO\ :math:`_2` and upgraded to SNG through the *methanation* technology. In
this case, the process requires CO\ :math:`_2` as a feedstock. Such CO\ :math:`_2` can either be captured from
large emitters, such as the industries and centralised heat
technologies, or directly captured from the air but at a higher
energetic and financial cost.

.. figure:: /images/belgian_data/PtG_and_CO2_layers.png
   :alt: Illustration of roduce synthetic fuels. For clarity, only the most relevant flows are drawn (:numref:`Figure %s <fig:bes_illustration>` includes all the flows).
   :name: fig:CO2andPtGLayers

   Illustration of the technologies and processes to produce synthetic
   fuels. For clarity, only the most relevant flows are drawn (
   :numref:`Figure %s <fig:bes_illustration>` includes all the flows).
   This figure also illustrates how carbon capture is implemented in the model. 
   The CO\ :math:`_2` emissions of large scale technologies can be either 
   released at the atmosphere or captured by the *Carbon Capture Industrial* 
   technolgy. Otherwise, CO\ :math:`_2` can be captured from the atmosphere at 
   a greater cost.


Hydrogen production
~~~~~~~~~~~~~~~~~~~

Three technologies are considered for hydrogen production: electrolysis,
NG reforming and biomass gasification. The last two options can include
CCS systems for limiting the CO\ :math:`_2` emissions. There exist
different technologies for electrolysis. In their work, the
:cite:t:`DanishEnergyAgency2019a` reviews the PEM-EC, A-EC and
SO-EC technologies. :numref:`Table %s <tbl:hydrogen_techs_danish>` summarises the key
characteristics of these technologies in year 2036.
   

.. container::

   .. table:: Characteristics of electrolyser technologies presented in :cite:`DanishEnergyAgency2019a`, in 2036. Efficiencies are represent as follow: Input (negative) and outputs (positive). Abbreviations: temperature (temp.), high temperature (h.t.), low temperature (l.t.), electricity (e), hydrogen (H\ :math:`_2` ).
      :name: tbl:hydrogen_techs_danish


      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_     | :math:`c_     | :math:`life | :math:`\eta_| :math:`\eta_| :math:`\eta_| :math:`\eta_|
      |             | {inv}`        | {maint}`      | time`       | e`          | {h.t.}`     | {H2}`       | {l.t.}`     |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+
      |             | [USD\ :math:`_| [USD\ :math:`_| [y]         | [%]         | [%]         | [%]         | [%]         |
      |             | {2015}`/kW\   | {2015}`/kW\   |             |             |             |             |             |
      |             | :math:`_      | :math:`_      |             |             |             |             |             |
      |             | {H_2}`]       | {H_2}`/y]     |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+
      | PEM-EC      | 870           | 40            | 15          | -100        |             | 63          | 12          |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+
      | A-EC        | 806           | 43            | 25          | -100        |             | 67          | 11          |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+
      | SO-EC       | 696           | 21            | 23          | -85         | -15         | 79          | 1.5         |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+



The different electrolyser technologies have a similar cost,
but they differ by their respective lifetime and electricity-to-hydrogen
efficiency. PEM-EC has the shortest lifetime and the lowest
electricity to hydrogen efficiency, therefore this technology will never be
implemented in the model [335]_. Electrolysers will be needed during times of
excesse electricity production, when heat demand is usually low.
Thus, they aim at maximising the production of hydrogen rather than low
temperature heat. For this reason, SO-EC appears to be the most promising
technology and will be implemented in the model. Thus, in this work, the term *Electrolysis*
refers to SO-EC. :numref:`Table %s <tbl:hydrogen>` contains the
data for the hydrogen production technologies, where €\ :sub:`2015` have been converted to USD\ :sub:`2021`.


.. container::

   .. table:: Hydrogen production technologies, in 2036.
      :name: tbl:hydrogen

      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      |               | :math:`c_     | :math:`c_     | :math:`life   | :math:`c_p`   | :math:`\eta_  | :math:`CO_    |
      |               | {inv}`        | {maint}`      | time`         |               | {H2}`         | {2,direct}`   |
      |               |               |               |               |               |               | [32a]_        |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      |               | [USD\ :math:`_| [USD\ :math:`_| [y]           | [%]           | [%]           | [tCO\ :sub:`2`|
      |               | {2021}`/kW\   | {2021}`/kW\   |               |               |               | /MWh\         |
      |               | :math:`_      | :math:`_      |               |               |               | :sub:`e`]     |
      |               | {H2}`]        | {H2}`/y]      |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Electrolysis  | 983           | 27.0          | 15            | 90            | 79            | 0             |
      | [32b]_        |               |               |               | [32c]_        | [32f]_        |               |
      | :cite:`\      |               |               |               |               |               |               |
      | DanishEnerg\  |               |               |               |               |               |               |
      | yAgency\      |               |               |               |               |               |               |
      | 2019a`        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | NG            | 962           | 88.8          | 25            | 86            | 73            | 0.273         |
      | reforming     |               |               |               |               |               |               |
      | [32d]_        |               |               |               |               |               |               |
      | :cite:`to\    |               |               |               |               |               |               |
      | ck_ther\      |               |               |               |               |               |               |
      | mo-envi\      |               |               |               |               |               |               |
      | ronomic\      |               |               |               |               |               |               |
      | _2013`        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Biomass       | 3567          | 251.3         | 25            | 86            | 43            | 0.902         |
      | gasification  |               |               |               |               |               |               |
      | [32e]_        |               |               |               |               |               |               |
      | :cite:`to\    |               |               |               |               |               |               |
      | ck_ther\      |               |               |               |               |               |               |
      | mo-envi\      |               |               |               |               |               |               |
      | ronomic\      |               |               |               |               |               |               |
      | _2013`        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Ammonia       | 932           | 88.6          | 25            | 86            | 66            | 0             |
      | cracking      |               |               |               |               |               |               |
      | [32g]_        |               |               |               |               |               |               | 
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+


.. [32a]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of fuel produced. Emissions computed based on
   resource used and specific emissions given in Table 9.

.. [32b]
   It uses electricity and high temperature heat as feedstock, see :numref:`Table %s <tbl:hydrogen_techs_danish>`.

.. [32c]
   Own assumptions.

.. [32d]
   It uses gas as feedstock, such as NG.

.. [32e]
   It uses wood biomass as feedstock.

.. [32f]
   To produce one unit of H\ :math:`_2`, the system requires 1.076 units of electricity and 0.19 units of heat high temperature. 
   We assume that, on top of the unit of H\ :math:`_2` produced, an extra 0.019 units of low temperature heat can be recovered 
   for district heating.

.. [32g]
   Cracking ammonia does not exist at industrial scale. Indeed, ammonia is produced from hydrogen throuth the Haber-Bosch process.
   Thus, we didn't found reliable data and did our own calculation based on Haber bosch process and methane cracking.



Synthetic methane and oils production
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Three technology options are considered for the conversion of biomass to
synthetic fuels: pyrolysis, gasification and biomethanation. The main
product of the pyrolysis process is bio-oil. Two different pyrolysis process are thus proposed. 
One producing light fuel oil, and another one producing a blend of gasoline and diesel. 
The main product of the gasification and
biomethanation processes are SNG, which is considered equivalent to
gas. Data for the technologies are reported in :numref:`Table %s <tbl:sng_pyro>` (from
:cite:`Moret2017PhDThesis`). The biomethanation process is
based on anaerobic digestion followed by a cleaning process in order to
have gas that can be reinjected in the gas network
:cite:`DanishEnergyAgency2019a,Energiforsk2016`. In the
table, efficiencies are calculated with respect to the wood in input
(50% humidity, on a wet basis lower heating value). ‘*Fuel*’ stands for the main
synthetic fuel in output. 
Finally, a last technology can produce methane from hydrogen and sequestrated CO\ :math:`_2`.


.. container::

   .. table:: Synthetic fuels (except H\ :math:`_2`) conversion technologies (from :cite:`DanishEnergyAgency2019a,Moret2017PhDThesis` or specified), in 2036.
      :name: tbl:sng_pyro
   
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_     | :math:`c_     | :math:`life | :math:`c_p` | :math:`\eta_| :math:`\eta_| :math:`\eta_| :math:`CO_  |
      |             | {inv}`        | {maint}`      | time`       |             | {fuel}`     | {e}`        | {th}`       | {2,direct}` |
      |             |               |               |             |             |             |             |             | [359]_      |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | [USD\ :math:`_| [USD\ :math:`_| [y]         | [%]         | [%]         | [%]         | [%]         | [tCO\       |
      |             | {2021}`/kW\   | {2021}`/kW\   |             |             |             |             |             | :sub:`2`    |
      |             | :math:`_      | :math:`_      |             |             |             |             |             | /MWh\       |
      |             | {fuel}`]      | {fuel}`/y]    |             |             |             |             |             | :sub:`e`]   |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Pyrolysis   | 1899          | 86.1          | 25          | 85          | 66.6        | 1.58        | -           | 0.586       |
      | to LFO      |               |               |             |             |             |             |             |             |
      | [363]_      |               |               |             |             |             |             |             |             | 
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Pyrolysis   | 1928          | 53.6          | 25          | 85          | 57.4        | 1.58        | -           | 0.586       |
      | to fuels    |               |               |             |             |             |             |             |             |
      | [363]_      |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Gasification| 2248          | 153.0         | 25          | 85          | 65          | 0           | 22          | 0.260       |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Biomethana\ | 1393          | 19.3          | 25          | 85          | 29.9        | 0           | 0           | 0.722       |
      | tion        |               |               |             |             |             |             |             |             |
      | [360]_      |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Hydrolisis  | 2248          | 153.0         | 15          | 100         | 42.3        | 0           | 4           | 0.306       |
      | methanation |               |               |             |             |             |             |             |             |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | gassn\      |               |               |             |             |             |             |             |             |
      | er201\      |               |               |             |             |             |             |             |             |
      | 1opti\      |               |               |             |             |             |             |             |             |
      | mal`        |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Syn.        | 370           | 94.4          | 30          | 86          | 83.3        | 0           | 0           | -0.198      |
      | methanation |               |               |             |             |             |             |             |             |
      | :cite:`\    |               |               |             |             |             |             |             |             |
      | g\          |               |               |             |             |             |             |             |             |
      | orre2\      |               |               |             |             |             |             |             |             |
      | 019pr\      |               |               |             |             |             |             |             |             |
      | oduct\      |               |               |             |             |             |             |             |             |
      | ion`        |               |               |             |             |             |             |             |             |
      +-------------+---------------+---------------+-------------+-------------+-------------+-------------+-------------+-------------+


.. [359]
   Direct emissions due to combustion. Expressed
   in ton CO\ :math:`_2` per MWh of fuel produced. Emissions computed based on
   resource used and produced and specific emissions given in Table 9.

.. [360]
   Costs are adapted from :cite:`ro2007catalytic` and
   technical data from :cite:`poschl2010evaluation`.

.. [361]
   Data from
   :cite:`perez2016methanol` to produce 1 MWh of methanol,
   the process requires 1.355 MWh of hydrogen and also 0.04 MWh of
   electricity, 0.107 MWh of heating and 0.210 units of cooling. The
   process is simplified to 1.5 MWh of hydrogen needed to produce 1 MWh
   of methanol.

.. [362]
   This technology might be removed. Indeed, in this version of the
   model, synthetic liquid fuels are gathered together. However, they
   should be split in methanol, ethanol, bio-diesel... As a consequence,
   producing methanol from methane is cheaper than importing diesel.
   However in this version, methanol can be directly used as diesel
   :math:`\rightarrow` a competitor.

.. [363]
   A distinction is made between pyrolysis to LFO and other fuels. 
   The first can produce oil for heating or non-energy demand. The second produce a 
   blend of diesel and gasoline (18% of gasoline and 39.4% of diesel).
   The characteristics of these technologies are taken from
   :cite:`Danish_energy_agency_2023_re_fuels` using the representative technology
   "Fischer-Tropsch".


Carbon capture and storage
~~~~~~~~~~~~~~~~~~~~~~~~~~

As represented in  :numref:`Figure %s <fig:CO2andPtGLayers>`, two
technologies are proposed to capture the CO\ :math:`_2`, one from atmosphere (*CC
atmospheric*) and the other one from exhaust gases of conversions processes
(*CC industry*), such as after a coal power plant. Indeed, resources
emit direct CO\ :math:`_2` from combustion and *CC industry* can concentrate CO\ :math:`_2`
contained in the exhaust gas and inject it in the layer for captured CO\ :math:`_2`. The
same process can be performed at a higher energy cost with CO\ :math:`_2` from
the atmosphere. No restriction on the available limit of CO\ :math:`_2` from the
atmosphere is considered. Data are summarised in :numref:`Table %s <tbl:CC_techs>`.

We suppose that *CC industry* has similar characteristics as a
sequestration unit on a coal power plant, as proposed in
:cite:`DanishEnergyAgency2019`. We evaluated the economical and technical
data based on our own calculations. We assumed
that the energy drop of the power plant represented the amount of energy
that the sequestration unit consumeed. We assume that this energy must be
supplied by electricity.

For *CC atmospheric*, :cite:t:`Keith2018` proposed an
installation where 1 ton of CO\ :math:`_2` is captured from the atmosphere with 1.3
kWh of natural gas and electricity. We assume that it can be done with
1.3 kWh of electricity. The thermodynamical limit is estimated to be
around 0.2 kWh of energy to sequestrate this amount
:cite:`Sanz-Perez2016`.


.. container::

   .. table:: Carbon capture (CC) technologies, in 2036. :math:`E_e` represents the electricity required to capture sequestrate CO\ :math:`_2`. :math:`\eta_{CO_2}` represents the amount of CO\ :math:`_2` sequestrated from the CO\ :math:`_2` source. Abbreviations: industrial (ind.), atmospheric (atm.).
      :name: tbl:CC_techs
 
 
      +-------------+---------------+---------------+-------------+-------------------+-------------+-------------+-------------+
      |             | :math:`c_     | :math:`c_     | :math:`life | :math:`E_e`       | :math:`\eta_| :math:`f_   | :math:`f_   |
      |             | {inv}`        | {maint}`      | time`       |                   | {CO_2}`     | {min,\%}`   | {max,\%}`   |
      |             |               |               |             |                   |             |             |             |
      +-------------+---------------+---------------+-------------+-------------------+-------------+-------------+-------------+
      |             | [USD\ :math:`_| [USD\ :math:`_| [y]         | [kWh :math:`_e`/  | [%]         | [%]         | [%]         |
      |             | {2021}`/kg\   | {2021}`/kg\   |             | kg :math:`_{CO_2}`|             |             |             |
      |             | :math:`_      | :math:`_      |             |                   |             |             |             |
      |             | {CO_2}`/h]    | {CO_2}`/h     |             |                   |             |             |             |
      |             |               | /y]           |             |                   |             |             |             |
      +-------------+---------------+---------------+-------------+-------------------+-------------+-------------+-------------+
      | CC Ind.     | 3644          | 91.3          | 40          | 0.233             | 90 [367]_   | 0           | 100         |
      +-------------+---------------+---------------+-------------+-------------------+-------------+-------------+-------------+
      | CC Atm.     | 7288 [368]_   | 180.9         | 40          | 1.3               | 100         | 0           | 100         |
      +-------------+---------------+---------------+-------------+-------------------+-------------+-------------+-------------+

.. [367]
   We consider that 10% of the CO\ :math:`_2` cannot be collected.

.. [368]
   Based on the economical data given in :cite:`Keith2018`
   and on own calculation.


No relevant data were found for the capacity factor (:math:`\textbf{c}_\textbf{p}`) and the
GWP associated to the construction of the unit.



.. _sec:app1_storage:

Storage
-------

Tables :numref:`%s <tab:StoDataBasic>` and
:numref:`%s <tab:StoDataAdvanced>` detail the data for the
storage technologies. :numref:`Table %s <tab:StoDataBasic>`
summarises the investment cost, GWP, lifetime and potential integration
of the different technologies. :numref:`Table %s <tab:StoDataAdvanced>` summarises the
technical performances of each technology.


.. container::
   

   .. table:: Storage technologies characteristics in 2036: costs, emissions and lifetime. Abbreviations: batteries (batt.), Battery Electric Vehicule (BEV), centralised (cen.), decentralised (dec.), Lithium-ions (Li-on), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), Pumped Hydro Storage (PHS), seasonal (seas.), temperature (temp.) and thermal storage (TS).
      :name: tab:stodatabasic

      +-----------+--------------+--------------+-----------+-----------+
      |           | :math:`c_    | :math:`c_    | :math:`gw | :math:`li |
      |           | {inv}`       | {maint}`     | p_{con    | fetime`   |
      |           |              |              | str}`     |           |
      +-----------+--------------+--------------+-----------+-----------+
      |           | [USD :math:`_| [USD :math:`_| [kgCO\    | [y]       |
      |           | {2021}`      | {2021}`      | :sub:`2`  |           |
      |           | /kWh]        | /kWh/y]      | -eq./kWh] |           |
      +-----------+--------------+--------------+-----------+-----------+
      | Li-on     | 426.5        | 0.66         | 61.3      | 15 [296]_ |
      | batt.     | [294]_       | [294]_       | [295]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | TS dec.   | 26.8         | 0.19         | 0         | 25        |
      |           | [300]_       | [300]_       | [297]_    | [300]_    |
      +-----------+--------------+--------------+-----------+-----------+
      | TS seas.  | 0.76         | 0.004        | 0         | 25        |
      | cen.      | [301]_       | [301]_       | [297]_    | [301]_    |
      +-----------+--------------+--------------+-----------+-----------+
      | TS daily  | 4.2          | 0.012        | 0         | 40        |
      | cen.      | [301]_       | [301]_       | [297]_    | [300]_    |
      +-----------+--------------+--------------+-----------+-----------+
      | TS high   | 39.6         | 0.42         | 0         | 25        |
      | temp.     |              |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | TS cold   | 35.3         | 0.42         | 0         | 20        |
      +-----------+--------------+--------------+-----------+-----------+
      | Gas       | 0.071        | 0.0018       | 0         | 30        |
      |           | [302]_       | [302]_       | [297]_    | [302]_    |
      +-----------+--------------+--------------+-----------+-----------+
      | H2        | 8.7          | 0.55         | 0         | 20        |
      |           | [303]_       | [303]_       | [297]_    | [303]_    |
      +-----------+--------------+--------------+-----------+-----------+
      | Diesel    | 8.8e-3       | 5.5 e-4      | 0         | 20        |
      | [304]_    |              |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | Gasoline  | 8.8e-3       | 5.5e-4       | 0         | 20        |
      | [304]_    |              |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | LFO       | 8.8e-3       | 5.5e-4       | 0         | 20        |
      | [304]_    |              |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | Ammonia   | 8.8e-3       | 5.5e-4       | 0         | 20        |
      | [304]_    |              |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | Methanol  | 8.8e-3       | 5.5e-4       | 0         | 20        |
      | [304]_    |              |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | CO2       | 69.9         | 0.70         | 0         | 20        |
      | [305]_    | [306]_       |              | [297]_    |           |
      +-----------+--------------+--------------+-----------+-----------+
      | Dam       | 0            | 0            | 0         | 40        |
      | storage   |              |              |           |           |
      +-----------+--------------+--------------+-----------+-----------+
      | PT        | 52.1 [307]_  | 0.5 [307]_   | 0         | 25        |
      | storage   |              |              |           |           |
      +-----------+--------------+--------------+-----------+-----------+
      | ST        | 26.9 [307]_  | 0.3 [307]_   | 0         | 25        |
      | storage   |              |              |           |           |
      +-----------+--------------+--------------+-----------+-----------+


.. [294]
   We assume a Lithium-ion NMC battery at a
   utility-scale in 2030 :cite:`DanishEnergyAgency2018` with
   average use of 100 cycles/year.

.. [295]
   Data from Table 4 of :cite:`limpens2018electricity`.

.. [296]
   Trade off between various sources:
   :cite:`Zakeri2015,DanishEnergyAgency2018`
   
.. [297]
   Neglected.

.. [300]
   Adapted from Table 5.2 of
   :cite:`Moritz2015`.

.. [301]
   The technologies used are pit thermal energy
   storage technology and Large-scale hot water tanks for seasonal and
   daily DHN storage, respectively. Data was taken for year 2030
   :cite:`DanishEnergyAgency2018`.

.. [302]
   Data from the Torup Lille
   project :cite:`DanishEnergyAgency2018`. The lifetime is
   assumed similar to a cavern for hydrogen storage.

.. [303]
   Based on tank storage from the JRC
   project:cite:`simoes2013jrc`. The cost is assumed as the
   average of 2020 and 2050 costs.

.. [304]
   In this implementation, the power of fuel imported can be constrained to be constant among the year. 
   Thus, a storage is created for the fuel, even if the storage cost is negligeable (see Eq. :eq:`eq:import_resources_constant`).
   Data were obtained by our own calculation.  


.. [305]
   Based on liquid CO\ :math:`_2` tank storage. Data from a
   datasheet of *Ever grow gas* company https://www.evergrowgas.com/.
   Lifetime and maintenance cost based on own calculation.

.. [306]
   Units: **c\ inv** [USD\ \ :sub:`2015`/tCO\ \ :sub:`2`],
   **c\ op** [USD\ \ :sub:`2015`/tCO\ \ :sub:`2`/y]
   
.. [307]
   Data collected by :cite:`dommisse2020modelling`.
   
   


Estimation for the gas storage is based on an existing facility using
salt caverns as reservoirs: Lille Torup in Danemark
:cite:`DanishEnergyAgency2018`. The project cost is
estimated to 254M€\ :sub:`2015` for an energy capacity of 4965 GWh. The
yearly operating cost is estimated to 6.5 M€\ :sub:`2015`. Part of it is
for electricity and gas self consumption. We assume that the electricity
is used for charging the system (compressing the gas) and the gas is
used for heating up the gas during the discharge. These quantities
slightly impact the charge and discharge efficiency of the system. The
charge and discharge power are 2200 and 6600 [MW] respectively. As the
technology is mature, we assume that the cost of the technology in 2036
will be similar to the one of the Lille Torup project.


.. container::

   .. table:: Storage technologies characteristics in 2036: efficiencies, energy to power ratios, losses and availabilities. Abbreviations: batteries (batt.), Battery Electric Vehicule (BEV), centralised (cen.), decentralised (dec.), Lithium-ions (Li-on), Natural Gas (NG), Plug-in Hybrid Electric Vehicle (PHEV), Pumped Hydro Storage (PHS), seasonal (seas.), temperature (temp.) and thermal storage (TS).
      :name: tab:stodataadvanced

      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      |               | :math:`\eta_  | :math:`\eta_  | :math:`t_     | :math:`t_     | :math:`%_     | :math:`%_     |
      |               | {sto,in}`     | {sto,out}`    | {sto,in}`     | {sto,out}`    | {sto_{loss}}` | {sto_{avail}}`|
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      |               | [-]           | [-]           | [h]           | [h]           | [s\ :math:`^  | [-]           |
      |               |               |               |               |               | {-1}`]        |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Li-on         | 0.95          | 0.95          | 4             | 4             | 2e-4          | 1             |
      | batt.         | [326]_        | [326]_        | [326]_        | [326]_        | [326]_ [327]_ |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | BEV           | 0.95          | 0.95          | 4             | 10            | 2e-4          | 0.2           |
      | batt.         | [326]_        | [326]_        | [328]_        | [328]_        | [326]_ [327]_ | [328]_        |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | PHEV          | 0.95          | 0.95          | 4             | 10            | 2e-4          | 0.2           |
      | batt.         | [326]_        | [326]_        | [328]_        | [328]_        | [326]_ [327]_ | [328]_        |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | PHS           | 0.866         | 0.866         | 4.30          | 4.83          | 0             | 1             |
      |               |               |               |               |               | [329]_        |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | TS dec.       | 1             | 1             | 4             | 4             | 82e-4         | 1             |
      |               | [329]_        | [329]_        | [328]_        | [328]_        | [330]_        |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | TS            | 1             | 1             | 150           | 150           | 6.06e-5       | 1             |
      | seas.         | [331]_        | [331]_        | [331]_        | [331]_        | [331]_        |               |
      | cen.          |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | TS            | 1             | 1             | 60.3          | 60.3          | 8.33e-3       | 1             |
      | daily         | [331]_        | [331]_        | [331]_        | [331]_        | [331]_        |               |
      | cen.          |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | TS high       | 1             | 1             | 2             | 2             | 3.55e-4       | 1             |
      | temp.         | [331]_        | [331]_        |               |               | [331]_        |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | TS cold       | 0.99          | 0.99          | 4             | 4             | 8.24e-3       | 1             |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | NG            | 0.99          | 0.995         | 2256          | 752           | 0             | 1             |
      |               | [332]_        | [332]_        | [332]_        | [332]_        |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | H\ :math:`_2` | 0.90          | 0.98          | 4             | 4             | 0             | 1             |
      |               | [333]_        | [333]_        | [333]_        | [333]_        |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Diesel        | 1             | 1             | 168           | 168           | 0             | 1             |
      | [334]_        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Gasoline      | 1             | 1             | 168           | 168           | 0             | 1             |
      | [334]_        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | LFO           | 1             | 1             | 168           | 168           | 0             | 1             |
      | [334]_        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Ammonia       | 1             | 1             | 168           | 168           | 0             | 1             |
      | [334]_        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Methanol      | 1             | 1             | 168           | 168           | 0             | 1             |
      | [334]_        |               |               |               |               |               |               |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | CO\ :math:`_2`| 1             | 1             | 1             | 1             | 0             | 1             |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | Dam storage   | 1             | 0.99          | 1             | 1             | 0             | 1             |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | PT storage    | 0.99          | 0.99          | 1.33          | 1.33          | 3.55e-4       | 1             |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      | ST storage    | 0.99          | 0.99          | 1.33          | 1.33          | 3.55e-4       | 1             |
      +---------------+---------------+---------------+---------------+---------------+---------------+---------------+
      


.. [326]
   Data verified in Table B1 of
   :cite:`Zakeri2015`.

.. [327]
   Data from Table 4 of
   :cite:`limpens2018electricity`.

.. [328]
   Own calculation.

.. [329]
   Neglected.

.. [330]
   Adapted from Table 5.2 of
   :cite:`Moritz2015`

.. [331]
   Based on the Pit thermal energy storage
   technology in 2030 for seasonal and Large-scale hot water tanks for
   DHN daily storage. Data from
   :cite:`DanishEnergyAgency2018`.

.. [332]
   Data from the Torup Lille
   project:cite:`DanishEnergyAgency2018`. Efficiencies are
   based on our own calculation based on electricity and gas consumed by
   the installation over a year.

.. [333]
   :cite:t:`Sadaghiani2017` an efficiency of
   88.6% in an ideal configuration for liquid hydrogen liquefaction.
   This high efficiency is used and we arbitrary impose that the charge
   efficiency is 90% and the discharge 98%. The tank design by JRC
   :cite:`simoes2013jrc` has a charge/discharge energy to
   power ratio of 4 hours.

.. [334]
   We assume a perfect storage with 1 week of charge/discharge time.

The last rows of Tables :numref:`%s <tab:StoDataBasic>` and :numref:`%s <tab:StoDataAdvanced>` concern
the Technology *Dam Storage*. As explained in the Model Formulation Section, hydro-electric dams are modelled
as two separate technologies in EnergyScope, linked by the constraints defined in eqs 
:eq:`eq:link_dam_storage_to_hydro_dam` - :eq:`eq:dam_storage_out`. Since all costs and gwp are already 
included in the technology of *Hydro Dam*, a null cost and a null gwp are assumed for *Dam Storage*.
The values of :math:`f_{min/max}(Hydro~Dam)` and :math:`f_{min/max}(Dam~Storage)` are also linked.
According to data received from Departamento Nacional de Planeación (DNP), the ratio between
the two is of 
:math:`2~240` [h]. The 2036 values of :math:`f_{min}(Hydro~Dam)=9.3` [GW] and :math:`f_{max}(Hydro~Dam)=51.2` [GW] 
therefore translate into :math:`f_{min}(Dam~Storage)=20~800` [GWh] and :math:`f_{max}(Dam~Storage)=114~400` [GWh].

.. _App:Data:OtherParam:

Others 
------

.. _ssec:app1_grid:

Electricity grid
~~~~~~~~~~~~~~~~

No data were found for the Belgian grid. Hence, by assuming that the
grid cost is proportional to the population, the Belgian grid cost can
be estimated based on the known Swiss grid cost. In 2015, the population
of Colombia and Switzerland were 11.25 and 8.24 millions, respectively
(Eurostat). The replacement cost of the Swiss electricity grid is 58.6
billions CHF\ :sub:`2015`
:cite:`association_des_entreprises_electriques_suisses_aes_scenarios_2012`
and its lifetime is 80 years :cite:`stump_swiss_2010`. The
electricity grid will need additional investment depending on the
penetration level of the decentralised and stochastic electricity
production technologies. The needed investments are expected to be 2.5
billions CHF\ :sub:`2015` for the high voltage grid and 9.4 billions
CHF\ :sub:`2015` for the medium and low voltage grid. This involves the
deployment of 25GW of PV and 5.3 GW of wind onshore. These values
correspond to the scenario 3 in
:cite:`association_des_entreprises_electriques_suisses_aes_scenarios_2012`.
The lifetime of these additional investments is also assumed to be 80
years.

By assuming a linear correlation between grid reinforcement and
intermittent renewable deployment, the specific cost of integration is
estimated to 393 MCHF per GW of renewable intermittent energy installed
(:math:`(9.4+2.5)`\ bCHF\ :math:`/(25+5.3)GW = 0.393`\ bCHF/GW).

As a consequence, the estimated cost of the Belgian grid is
:math:`58.6/1.0679\cdot 11.25/8.24=74.9` b€\ :sub:`2015`. And the extra
cost is :math:`393/1.0679\approx 367.8` M€\ :sub:`2015`/GW.

We assume that these costs are similar for Colombia and convert them into USD\ :sub:`2021`
to get a grid cost of 105.8 b USD\ :sub:`2021`/GW
and an extra reinforcement cost of 518.5 M USD\ :sub:`2021`/GW.

Several data regarding cross-border interconnections are given in Section
*Electricity imports and exports*. The costs of new High-Voltage
transfer capacity (HVAC Line) with neighbouring countries are computed to be
:math:`c_{inv} = 2~\text{€}_{2015}`/kW/km and 
:math:`c_{maint} = 0.04~\text{€}_{2015}`/kW/km/year, based on :cite:`IEA_HVAC`,
:cite:`brown_synergies_2018` and :cite:`prina_multi-objective_2020`. By multiplying these
costs by 766 km (i.e. the distance between Panama City and Bogotá) and converting them into USD\ :sub:`2021`,
we obtain for the technology HVAC in EnergyScope in 2036:
:math:`c_{inv} = 2164~\text{M USD}_{2021}`/GW and 
:math:`c_{maint} = 43.2~\text{M USD}_{2021}`/GW/year.
We take the distance from capital city to capital city, and not the
distance from border to border, to grossly reflect the local grid
reinforcement costs that such new interconnection projects entail.

Losses (:math:`\%_{net,loss}`) in the electricity
grid are fixed to 4.7%. This is the ratio between the losses in the grid
and the total annual electricity production in Belgium in
2016 :cite:`Eurostat2017`.

.. _app:DHN_grid_data:

DHN grid
~~~~~~~~

For the DHN, the investment into network is also accounted for. The
specific investment (:math:`c_{inv}`) is 882 CHF\ :sub:`2015`/kW\ :sub:`th` in
Switzerland. This value is based on the mean value of all points in
:cite:`s._thalmann_analyse_2013` (Figure 3.19), assuming a
full load of 1535 hours per year (see table 4.25 in
:cite:`s._thalmann_analyse_2013`). The lifetime of the DHN
is expected to be 60 years. DHN losses are assumed to be 5%.

As no relevant data were found for Colombia, the DHN infrastructure cost
of Switzerland was used. As a consequence, the investment cost
(:math:`c_{inv}`) is 1166 USD\ :sub:`2021`/kW\ :sub:`th`.

The lower (:math:`\%_{dhn,min}`) and upper bounds (:math:`\%_{dhn,max}`) for the use of
DHN are chosen as 0% and 50%, respectively. The latter value is the same as
the one from :cite:`borasio2022deep` for the case of Italy. Indeed, the population
density in urban and surburban areas is grossly similar in both countries.

Hydrogen network
~~~~~~~~~~~~~~~~

Producing and using green hydrogen comes with the development of a local hydrogen network.
:cite:`plazas_nino_2024` computed the total cost of the hydrogen system. According 
to their results, the cost for the transportation and distribution of hydrogen,
including infrastructure for maritime export, is roughly equal to the cost of green hydrogen’s 
production.

Thus, the total investment cost for green hydrogen production is computed, taking into account 
the values in EnergyScope of the investment cost for renewable electricity production and its
conversion into hydrogen. This total cost of production amounts to 2225 USD/kW :math:`_{electrolyser}`. Thus, a technology called 
"H2 infrastructure" is included, whose capacity is constrained to be equal to the installed
capacity of electrolysers, whose investment cost is 2225 USD/kW and whose other costs are null.

Charging stations for electrical vehicles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

According to the computations from :cite:`kerlero2024road`, the infrastructure costs for the charge
of electrical vehicles are equal to 20% of the cost of the vehicles themselves. In our case, it means
that electrical cars require an infrastructure investment of 123 USD/km-pass. Thus, a technology called 
"CHARGING STATION" is included, whose capacity is constrained to be equal to the installed
capacity of CAR BEV, whose investment cost is 123 USD/km-pass and whose other costs are null.

.. _app:sec:ESTD_CO_CO2_emissions:

GHG emissions
=============

As already explicited in :numref:`Table %s <tab:costs_resources_fossil>`, two CO :sub:`2`-eq
emissions metrics are used: CO :sub:`2,direct` and gwp :sub:`op`. The first one relates to 
the direct emissions associated with the fuels' combustion, while the second one is the
GWP100a-IPCC2013 metric: it covers emissions associated to extraction, transportation and combustion.
The former is used to complete the calibration of EnergyScope to the 2021 Colombian energy
system, whereas the second one determines the maximum GHG emissions allowed in 2036.


Calibration of EnergyScope to the 2021 energy system
----------------------------------------------------

After having found values for all parameters of the model, as described in the previous sections, it
is time to verify that the model simulation of the 2021 Colombian energy system is coherent with historical
data. A practical check is to verify that CO :sub:`2`-eq emissions match. Indeed, CO :sub:`2`-eq
emissions derive from the laws of natural sciences and are independent of the economic assumptions chosen.
They therefore give a more objective metric for comparison purposes.
The resource use simulated by the model in 2021 can be multiplied by CO :sub:`2,direct` to obtain CO :sub:`2`-eq
emissions, which are then compared to historical data. Thanks to this, we were able to correct some values
initially taken from :cite:`plazas_nino_2023` for the heating EUDs, passenger mobility EUD and freight EUD.
The resource use and emissions simulated by EnergyScope for the year 2021 after performing these corrections are
given in :numref:`Table %s <tab:2021_CO2_check>`.

.. container::

   .. csv-table:: Resource use and CO :sub:`2`-eq emissions simulated by EnergyScope for the year 2021, compared with historical data. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resource** , **Quantity used in 2021** [37a]_ , **CO**:sub:`2direct` (per MWh of fuel) , **CO**:sub:`2direct` (total) [37a]_ , 2021 **CO**:sub:`2`-eq emissions [37b]_
      :widths: 15 15 15 15 15
      :name: tab:2021_CO2_check
		
		 , [GWh] , [tCO :sub:`2`-eq/MWh :sub:`fuel`] , [MtCO :sub:`2`-eq] , [MtCO :sub:`2`-eq]
		coal , 41 005 , 0.36 , 14.8 , 14
		natural gas , 79 660 , 0.20 , 15.9 , 18
		gasoline , 63 438 , 0.25 , 15.9, 16.7 [37c]_
		diesel , 70 949 , 0.27 , 19.2 , 20.1 [37c]_
		LFO , 40 769 , 0.26 , 10.6 , 11.1 [37c]_
		bio-ethanol , 6 179 , 0.25 , 1.5 , ~ [37d]_
		bio-diesel , 2 540 , 0.27 , 0.7 , ~ [37d]_
		woody biomass , 38 880 , 0.39 , 15.2 , ~ [37d]_

.. [37a]
   Obtained after running EnergyScope with the 2021 data. 
   
.. [37b]
   Data from Figure 3.3 of :cite:`IEA_2023`.

.. [37c]
   In :cite:`IEA_2023`, the emissions for gasoline, diesel and LFO are aggregated. We disaggregate them according to the proportions from the EnergyScome simulation for year 2021.

.. [37d]
   Not given in :cite:`IEA_2023`.

According to :cite:`IEA_2023`, the total CO :sub:`2`-eq emissions from fossil fuels in Colombia were of 79.7 MtCO :sub:`2`-eq in 2021.
The sum of the values simulated with EnergyScope for fossil fuels (thus excluding bio-fuels and biomass) and given in
:numref:`Table %s <tab:2021_CO2_check>` is 77.1 MtCO :sub:`2`-eq. The difference between the two is of 3% and is therefore acceptable.


Setting a gwp limit for the year 2036
-------------------------------------

The gwp :sub:`op` computed by EnergyScope for the 2021 Colombian energy system is of 94 MtCO :sub:`2`-eq. It is broken down by
resource type in :numref:`Table %s <tab:2021_gwp>`.

.. container::

   .. csv-table:: Resource use and gwp :sub:`op` simulated by EnergyScope for the year 2021. Abbreviations: Liquid Fuel Oil (LFO).
      :header: **Resource** , **Quantity used in 2021** [38a]_ , **gwp**:sub:`op` (per MWh of fuel) , **gwp**:sub:`op` (total)
      :widths: 15 15 15 15
      :name: tab:2021_gwp
		
		 , [GWh] , [tCO :sub:`2`-eq/MWh :sub:`fuel`] , [MtCO :sub:`2`-eq]
		coal , 41 005 , 0.40 , 16.5
		natural gas , 79 660 , 0.27 , 21.2
		gasoline , 63 438 , 0.34 , 21.9
		diesel , 70 949 , 0.31 , 22.3
		LFO , 40 769 , 0.31 , 12.7
		bio-ethanol , 6 179 , 0 , 0
		bio-diesel , 2 540 , 0 , 0
		woody biomass , 38 880 , 0.01 , 0.5

.. [38a]
   Obtained after running EnergyScope with the 2021 data. 
   
   	
Decarbonisation of the energy system is enforced in EnergyScope by defining a threshold on the GWP (:math:`gwp_{limit}`). The simplest method
for choosing a value for :math:`gwp_{limit}` is to take a certain percentage of the 2021 gwp. 







.. [1]
   The database can be consulted online: http://www.ecoinvent.org

.. [2]
   *Real* values are expressed the net of inflation. They differ from
   *nominal* values, which are the actual prices in a given year,
   accounting for inflation.

.. [257]
   from https://en.wikipedia.org/wiki/Nissan_Leaf, consulted on
   29-01-2019

.. [258]
   from https://fr.wikipedia.org/wiki/Toyota_Prius, consulted on
   29-01-2019

.. [267]
   Value calculated based on the ratio between the transported tons and
   the consumed energy per technologies in 2015. Data from
   :cite:`EuropeanCommission2016`

.. [335]
   Not all the characteristics of the cell has been implemented, thus
   PEM-EC can be competitive compare to other technologies.



