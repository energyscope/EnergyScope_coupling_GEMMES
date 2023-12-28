
.. _app:estd_tk_data:

Input Data - Turkey
++++++++++++++++++++++++++++++++++++++++++++
..
.. role:: raw-latex(raw)
   :format: latex
   
This section details the input data utilized in applying the LP modeling framework to the Turkey case study. The primary objective is provide data to reproduce the historical Colombian energy system for the year 2021, serving as a validation of EnergyScope's accuracy in modeling this intricate system. Additionally, we provide data for modeling a prospective Turkey energy system for the year 2035.

The data can be grouped into three parts: resources (Section `Resources <#app:sec:ESTD_CO-2021_resources_TK>`__), demand (Section
`Demand <#sec:app1_end_uses_TK>`__) and technologies (Section
`Technologies <#app:BESTD_data_technologies_TK>`__).

.. _app:sec:ESTD_TK_resources:

Resources
=========

Local renewable resources
-------------------------

Solar, wind, hydro and geothermal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. _ssec:app1_electricity_end_uses_TK:

Electricity
-----------

The ratio between varying
electricity and fixed demand are calculated in order to fit the real curve 
in 2015 (data provided by ENTSO-E
https://www.entsoe.eu/). It results in a share of 32.5% of varying electricity demand  
and 67.5% of baseload electricity demand.

For *%\ elec* ... we use the real
2015 Belgian electricity demand (data provided by ENTSO-E
https://www.entsoe.eu/).

.. container::

   .. table:: Yearly electricity demand not related to heating by sector, in 2035.
      :name: tbl:elec_demand

      ========== =========== ============
      \          **Varying** **Constant**
      \          [TWh]       [TWh]
      Households 7.7         14.3
      Industry   11.1        33.7
      Services   11.0        14.1
      ========== =========== ============


.. _ssec:app1_heating_end_uses_TK:

Heating
-------

.. _ssec:app1_demand_mobility_TK:

Mobility
--------

The lower (:math:`%_{public,min}`) and upper bounds
(:math:`%_{public,max}`) for the use of public transport are 19.9% and
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

.. _ssec:app1_non-renewable_TK:

Non-renewable
~~~~~~~~~~~~~

Data for the considered fossil electricity production technologies are
listed in :numref:`Table %s <tbl:nonrenew_elec>`. The
maximum installed capacity (:math:`f_{max}`) is set to a value high enough
(100 000 TW\ :sub:`e`) for each technology to potentially cover the
entire demand.


.. container::

   .. table:: Non-renewable electricity supply technologies, in 2035. Abbreviations: Combined Cycles Gas Turbine (CCGT), Ultra-Supecritical (U-S), Integrated Gasification Combined Cycles (IGCC).
      :name: tbl:nonrenew_elec

      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | :math:`c_   | :math:`c_   | :math:`gwp_ | :math:`li   | :math:`c_   | :math:`\eta | :math:`C    |
      |             | {inv}`      | {maint}`    | {constr}`   | fetime`     | {p}`        | _e`         | O_{2,       |
      |             |             |             |             |             |             |             | direct}`    |
      |             |             |             |             |             |             |             | [81]_       |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      |             | [€          | [€          | [kgCO       | [y]         | [%]         | [%]         | [tCO2/      |
      |             | :sub:`2015` | :sub:`2015` | :sub:`2-eq.`|             |             |             | MWh         |
      |             | /kW         | /kW         | /kW         |             |             |             | :sub:`e`    |
      |             | :sub:`e`]   | :sub:`e`/y] | :sub:`e`]   |             |             |             | ] [81]_     |
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
      | CCGT        | 772         | 20          | 183.8       | 25          | 85.0        | 63 [84]_    | 0.317       |
      |             | :cite:`\    | :cite:`\    | \           | :cite:`\    |             |             |             |
      |             | i\          | i\          | :cite:`\    | b\          |             |             |             |
      |             | ea_-_\      | ea_-_\      | weid\       | auer_\      |             |             |             |
      |             | inter\      | inter\      | ema_e\      | new_2\      |             |             |             |
      |             | natio\      | natio\      | coinv\      | 008`        |             |             |             |
      |             | nal_e\      | nal_e\      | ent_2\      |             |             |             |             |
      |             | nergy\      | nergy\      | 013`\       |             |             |             |             |
      |             | _agen\      | _agen\      |             |             |             |             |             |
      |             | cy_ie\      | cy_ie\      |             |             |             |             |             |
      |             | a_201\      | a_201\      |             |             |             |             |             |
      |             | 4-1`        | 4-1`        |             |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | CCGT\       | 772         | 20          | 183.8       | 25          | 85.0        | 50          | 0           |
      | :sub:`AMMO\ |             |             | :cite:`\    |             |             |             |             |
      | NIA` [89]_  |             |             | weid\       |             |             |             |             |
      |             |             |             | ema_e\      |             |             |             |             |
      |             |             |             | coinv\      |             |             |             |             |
      |             |             |             | ent_2\      |             |             |             |             |
      |             |             |             | 013`\       |             |             |             |             |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | Coal        | 2517        | 30          | 331.6       | 35          | 86.8        | 49          | 0.735       |
      |             | [85]_       | [85]_       | :cite:`\    | \           | \           | [86]_       |             |
      |             |             |             | weid\       | :cite:`\    | :cite:`\    |             |             |
      |             |             |             | ema_e\      | b\          | b\          |             |             |
      |             |             |             | coinv\      | auer_\      | auer_\      |             |             |
      |             |             |             | ent_2\      | new_2\      | new_2\      |             |             |
      |             |             |             | 013`\       | 008`        | 008`        |             |             |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+
      | IGCC        | 3246        | 49          | 331.6       | 35          | 85.6        | 54          | 0.667       |
      |             | [87]_       | [87]_       | :cite:`\    | \           | \           | [88]_       |             |
      |             |             |             | weid\       | :cite:`\    | :cite:`\    |             |             |
      |             |             |             | ema_e\      | b\          | b\          |             |             |
      |             |             |             | coinv\      | auer_\      | auer_\      |             |             |
      |             |             |             | ent_2\      | new_2\      | new_2\      |             |             |
      |             |             |             | 013`\       | 008`        | 008`        |             |             |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+

.. [81]
   Direct emissions due to combustion. Expressed
   in ton CO2 per MWh of electricity produced. Emissions computed based
   on resource used and specific emissions given in :numref:`Table %s <tbl:prices_resources>`.

.. [82]
   Investment cost: 3431 €\ \ :sub:`2015`/kW\ \ :math:`_{\text{e}}`
   :cite:`iea_-_international_energy_agency_iea_2014-1` +
   dismantling cost in Switzerland: 1415
   €\ \ :sub:`2015`/kW\ \ :math:`_{\text{e}}`
   :cite:`swissnuclear_financement_????`.

.. [83]
   Data for the year 2012
   :cite:`swiss_federal_office_of_energy_sfoe_swiss_2014`

.. [84]
   0.4-0.5 GW\ \ :math:`_{e}` CCGT in 2035 (realistic optimistic
   scenario) :cite:`bauer_new_2008`.

.. [85]
   1.3 GW\ \ :math:`_{e}` advanced pulverized coal power
   plant
   :cite:`u.s._eia_-_energy_information_administration_updated_2013`.
   *c\ maint* is fixed cost (29.2 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y) +
   variable cost (0.51 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y assuming 7600
   h/y).

.. [86]
   Pulverized coal in 2025 (realistic optimistic scenario)
   :cite:`bauer_new_2008`.

.. [87]
   1.2 GW\ \ :math:`_{\text{e}}` IGCC power plant
   :cite:`u.s._eia_-_energy_information_administration_updated_2013`.
   *c\ maint* is fixed cost (48.1 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y) +
   variable cost (0.82 €\ \ :sub:`2015`/kW\ \ :sub:`e`/y assuming 7500
   h/y).

.. [88]
   IGCC in 2025 (realistic optimistic scenario)
   :cite:`bauer_new_2008`.

.. [89]
   Use of Ammonia in CCGT is at its early stage. Mitsubishi is developping 
   a 40 MW turbine and promises similar efficiency as gas CCGT :cite:`nose2021development`. 
   However, the high emissions of NOx requires a removal equipment which will reduce the 
   power plant efficiency. As gas and ammonia CCGT will be similar, we expect a similar cost and lifetime. 
   The only exception is the efficiency, which is assumed at 50% instead of 63% for a gas CCGT :cite:`ikaheimo2018power`.

Heating and cogeneration
------------------------

.. _sec:app1_vehicles_mobility_TK:

Transport
---------

Passenger mobility
~~~~~~~~~~~~~~~~~~

Freight mobility
~~~~~~~~~~~~~~~~

.. _sec:app1_ned_TK:

Non-energy demand
-----------------

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

.. _App:Data:OtherParam_TK:

Others 
------

.. _ssec:app1_grid_TK:

Electricity grid
~~~~~~~~~~~~~~~~

.. _app:DHN_grid_data_TK:

DHN grid
~~~~~~~~

Energy demand reduction cost
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


