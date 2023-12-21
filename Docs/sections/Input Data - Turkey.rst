
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

Dominating fossil fuels are implemented in the model and detailed in
Section
`[ssec:case_study_imported_res] <#ssec:case_study_imported_res>`__. They
can be regrouped in hydrocabons (gasoline, diesel, LFO and NG), coal and
uranium. Data is summarised in :numref:`Table %s <tbl:prices_resources_TK>` and are compared to
other sources, such as estimations from the JRC of prices for oil, gas
and coal :cite:`simoes2013jrc`. They base their work on a
communication of the European Commission
:cite:`eu2011roadmap`.


There are a long list of candidate to become renewable fuels. Historically, biomass has been converted into bio-fuels. 
Two types of these fuels are accounted: bio-diesel and bio-ethanol. They can substitute diesel and gasoline, respectively. 
More recently, a new type of renewable fuel is proposed and can be labeled electro-fuels. Indeed, these fuels are produced from electricity. 
We consider that the energy content of these fuels is renewable (i.e. from renewable electricity). 
Four type of fuels were considered: hydrogen, ammonia, methanol and methane. 
To avoid ambiguity between renewable fuels and their fossil equivalent, it is specified if the imported resources is renewable or fossil. 


.. caution::
   to be updated + explain where data comes from.

The only difference being 
Thus, we have gas and gas_re, or h2 and h2_re. Gas refers to what is usually called 'natural gas', while gas_re refers to methane from biogas, methanation of renewable hydrogen,...
Since, a specific study for the Belgian case has been conducted by a consortium of industries, :cite:t:`H2coalition2020shipping`, which estimate new prices for the imports.
:numref:`Table %s <tbl:prices_resources_TK>` summarises all the input data for the resources.


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

The EUD for heating, electricity and mobility in 2035 is calculated from
the forecast done by the EUC in 2035 for Colombia (see Appendix 2 in
:cite:`EuropeanCommission2016`). However, in
:cite:`EuropeanCommission2016`, the FEC is given for heating
and electricity. The difference between FEC and EUD is detailed in
Section
`[ssec:conceptual_modelling_framework] <#ssec:conceptual_modelling_framework>`__
and can be summarised as follows: the FEC is the amount of input energy
needed to satisfy the EUD in energy services. Except for HP, the FEC is
greater than EUD. We applied a conservative approach by assuming that
the EUD equal to the FEC for electricity and heating demand.

.. _ssec:app1_electricity_end_uses_TK:

Electricity
-----------

The values in table `1.3 <#tbl:elec_demand>`__ list the electricity
demand that is not related to heating for the three sectors in 2035. The
overall electricity EUD is given in
:cite:`EuropeanCommission2016`. However, only the FEC is
given by sectors. In order to compute the share of electricity by
sector, we assume that the electricity to heat ratio for the residential
and services remain constant between 2015 and 2035. This ratio can be
calculated from :cite:t:`EuropeanCommission-Eurostat.2018`,
these ratio of electricity consumed are 24.9% and 58.2% for residential
and services, respectively. As a consequence, the industrial electricity
demand is equal to the difference between the overall electricity demand
and the two other sectors.

A part of the electricity is assumed to be a fixed demand, such as
fridges in households and services, or industrial processes. The other
part is varying, such as the lighting demand. The ratio between varying
electricity and fixed demand are calculated in order to fit the real curve 
in 2015 (data provided by ENTSO-E
https://www.entsoe.eu/). It results in a share of 32.5% of varying electricity demand  
and 67.5% of baseload electricity demand.
demand of electricity is shared over the year according to *%\ elec*,
which is represented in  :numref:`Figure %s <fig:TS_elec>`. We use the real
2015 Belgian electricity demand (data provided by ENTSO-E
https://www.entsoe.eu/). *%\ elec* time series is the normalised value
of the difference between the real time series and its minimum value.

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

.. figure:: /images/belgian_data/ts_elec_Belgium.png
   :alt: Normalised electricity time series over the year.
   :name: fig:TS_elec

   Normalised electricity time series over the year.

.. _ssec:app1_heating_end_uses_TK:

Heating
-------

We applied the same methodology as in previous paragraph to compute the
residential, service heat yearly demand. The industrial heat processes
demand is assumed to be the overall industrial energy demand where
electricity and non energy use have been removed. Yearly EUD per sector
is reported in table `1.4 <#tbl:heat_demand>`__.

A part of the heat is assumed to be a fixed demand, such as hot water in
households and services, or industrial processes. The other part
represents the space heating demand and is varying. Similarly to the
electricity, the ratio between varying electricity and fixed demand are
the one of Switzerland, presented in
:cite:`Limpens2019,Moret2017PhDThesis` which are based on
:cite:`prognos_ag_energieperspektiven_2012`. The varying
demand of heat is shared over the year according to :math:`%_{sh}`. This time
series is based on our own calculation. The methodology is the
following: based on the temperature time series of Uccle 2015 (data from
IRM :cite:`Reyniers2012`); the HDH are calculated; and then
the time series. The HDH is a similar approach than the more commonly
used HDD. According to Wikipedia, HDD is defined as follows: “*HDD is a
measurement designed to quantify the demand for energy needed to heat a
building. HDD is derived from measurements of outside air temperature.
The heating requirements for a given building at a specific location are
considered to be directly proportional to the number of HDD at that
location. [...] Heating degree days are defined relative to a base
temperature*”. According to the European Environment Agency [37b]_, the
base temperature is 15.5\ :math:`^o`\ C, we took 16\ :math:`^o`\ C. HDH
are computed as the difference between ambient temperature and the
reference temperature at each hour of the year. If the ambient
temperature is above the reference temperature, no heating is needed.
:numref:`Figure %s <fig:HDD_BE_2015>` compares the result of our methodology
with real value collected by Eurostat [38]_. The annual HDD was 2633,
where we find 2507.

By normalising the HDH, we find :math:`%_{sh}`, which is represented in 

.. figure:: /images/belgian_data/belgium_HDD_2015.png
   :alt: Comparison of HDD between Eurostat and our own calculation.
   :name: fig:HDD_BE_2015

   Comparison of HDD between Eurostat and our own calculation.

.. figure:: /images/belgian_data/ts_sh_Belgium.png
   :alt: Normalised space heating time series over the year.
   :name: fig:TS_heat

   Normalised space heating time series over the year.

.. container::

   .. table:: Yearly heat end use demand per sector, in 2035.
      :name: tbl:heat_demand

      ========== ================= ============= ========================
      \          **Space heating** **Hot water** **Process heat**\  [39]_
      \          [TWh]             [TWh]         [TWh]
      Households 70.2              18.0          0
      Industry   13.1              3.4           50.4
      Services   34.8              7.8           0
      ========== ================= ============= ========================

   .. [39]
      We define process heat as the high temperature heat required in the
      industrial processes. This heat cannot be supplied by technologies
      such as heat pumps or thermal solar.

.. _ssec:app1_demand_mobility_TK:

Mobility
--------

The annual passenger transport demand in Colombia for 2035 is expected
to be 194 billions :cite:`EuropeanCommission2016`.
Passenger transport demand is divided between public and private
transport. The lower (:math:`%_{public,min}`) and upper bounds
(:math:`%_{public,max}`) for the use of public transport are 19.9% [40]_ and
50% of the annual passenger transport demand, respectively. The
passenger mobility demand is shared over the day according to
:math:`%_{pass}`. We assume a constant passenger mobility demand for every
day of the year. This latter is represented in Figure
:numref:`Figure %s <fig:TS_mobPass>` (data from Figure 12 of
:cite:`USTransportation`).
The annual freight transport demand in Colombia for 2035 is expected to
be 98e09 tons kilometers :cite:`EuropeanCommission2016`.
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

.. figure:: /images/belgian_data/ts_mob.png
   :alt: Normalised passenger mobility time series over a day. We assume a similar passenger mobility demand over the days of the year.  
   :name: fig:TS_mobPass
   :width: 6cm
   :height: 4cm

   Normalised passenger mobility time series over a day. We assume a
   similar passenger mobility demand over the days of the year.

.. _app:discount_and_interest_rates_TK:

Discount rate and interest rate
-------------------------------

To compute their profitability, companies apply a discount rate to the
investment they make. A discount rate is used for both cost of finance
and for risk perception and opportunity cost. The cost of finance is to
be compared with concepts like ‘hurdle rate’ or ‘rate of return’ usually
calculated in accordance to an annual return on investment. Each
individual investment physically occurring in year k, results in a
stream of payments towards the amortization of this investment spread
over several years in the future. The higher the cost of finance (or
hurdle rate), the higher the annual payments spread over the lifetime of
an investment and thus the higher the total cost. The hurdle rate
affects only the investment costs so the impact is bigger for capital
intensive technologies. We consider differentiated hurdle discount rates
for different groups of energy supply and demand technologies,
representing the different risk perception of industry versus
individuals.

According with :cite:t:`Meinke-Hubeny2017` who based their
work on the JRC EU TIMES model :cite:`simoes2013jrc` in line
with the PRIMES model :cite:`EuropeanCommission2016`, the
discount rate is around 7.5 up to 12% depending on the technologies.
Discount rate cannot be directly converted into interest rate as the
first is fixed by the market and the second is fixed by the central
banks. As the evidence presented in Figure
:numref:`Figure %s <fig:path_be_irate_discountrate>` indicates, while these two
interest rates tend to move together, they also may follow different
paths from time to time.


.. figure:: /images/belgian_data/path_be_i_rate_and_discount_rate.png
   :alt: Comparison of Belgian interest rate and discount rate. The following rate was chosen to represent the discount rate: floating loans rate over a 1M€ (other than bank overdraft) and up to 1 year initial rate fixation.
   :name: fig:path_be_irate_discountrate

   Comparison of Belgian interest rate and discount rate. The following
   rate was chosen to represent the discount rate: floating loans rate
   over a 1M€ (other than bank overdraft) and up to 1 year initial rate
   fixation.

For the different studies, the real discount rate for the public
investor :math:`i_{rate}` is fixed to 1.5%, which is similar to the floating
loan rate over a million euros (other than bank overdraft) and greater
than the central bank interest rate.

.. _app:ESTD_TK_data_technologies:

Technologies
============

Electricity production
----------------------

.. _ssec:app1_renewables_TK:

Renewables
~~~~~~~~~~

.. container::

   .. table:: Renewable electricity production technologies, in 2035. Abbreviations: onshore (on.), offshore (off.).
      :name: tbl:renew_elec_TK

      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      |             | :math:`c_   | :math:`c_   | :math:`gwp_ | :math:`li   | :math:`c_   | :math:`f_   | :math:`f_|
      |             | {inv}`      | {maint}`    | {constr}`   | fetime`     | {p}`        | {min}`      | {max}`   |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      |             | [€          | [€          | [kgCO       | [y]         | [%]         | [GW]        |[GW]      |
      |             | :sub:`2015` | :sub:`2015` | :sub:`2-eq.`|             |             |             |          |
      |             | /kW         | /kW         | /kW         |             |             |             |          |
      |             | :sub:`e`]   | :sub:`e`/y] | :sub:`e`]   |             |             |             |          |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      |    Solar    |    870      |    18.8     |    2081     |    25 [57]_ |    11.9     |    0        |    59.2  |
      |    PV       |    [57]_    |    [57]_    |    :cite:`\ |    :cite:`\ |    [58]_    |             |          |
      |             |             |             |    weidema_\|    eur\     |             |             |          |
      |             |             |             |    ecoinven\|    opean\   |             |             |          |
      |             |             |             |    t_2013`  |    _phot\   |             |             |          |
      |             |             |             |             |    ovolt\   |             |             |          |
      |             |             |             |             |    aic_t\   |             |             |          |
      |             |             |             |             |    echno\   |             |             |          |
      |             |             |             |             |    logy_\   |             |             |          |
      |             |             |             |             |    platf\   |             |             |          |
      |             |             |             |             |    orm_s\   |             |             |          |
      |             |             |             |             |    trate\   |             |             |          |
      |             |             |             |             |    gic_2\   |             |             |          |
      |             |             |             |             |    011`     |             |             |          |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      |    On.      |    1040     |    12.1     |    622.9    |    30 [60]_ |    24.3     |    0        |    10    |
      |    Wind     |    [60]_    |    [60]_    |    :cite:`\ |    :cite:`\ |    [58]_    |             |          |
      |    Turbine  |             |             |    weidema_\|    a\       |             |             |          |
      |             |             |             |    ecoinven\|    ssoci\   |             |             |          |
      |             |             |             |    t_2013`  |    ation\   |             |             |          |
      |             |             |             |             |    _des_\   |             |             |          |
      |             |             |             |             |    entre\   |             |             |          |
      |             |             |             |             |    prise\   |             |             |          |
      |             |             |             |             |    s_ele\   |             |             |          |
      |             |             |             |             |    ctriq\   |             |             |          |
      |             |             |             |             |    ues_s\   |             |             |          |
      |             |             |             |             |    uisse\   |             |             |          |
      |             |             |             |             |    s_aes\   |             |             |          |
      |             |             |             |             |    _ener\   |             |             |          |
      |             |             |             |             |    gie_2\   |             |             |          |
      |             |             |             |             |    013`     |             |             |          |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      |    Off.     |    4975     |    34.6     |    622.9    |    30 [60]_ |    41.2     |    0        |    6     |
      |    Wind     |    [60]_    |    [60]_    |    :cite:`\ |    :cite:`\ |    [58]_    |             |          |
      |    Turbine  |             |             |    weidema_\|    a\       |             |             |          |
      |             |             |             |    ecoinven\|    ssoci\   |             |             |          |
      |             |             |             |    t_2013`  |    ation\   |             |             |          |
      |             |             |             |             |    _des_\   |             |             |          |
      |             |             |             |             |    entre\   |             |             |          |
      |             |             |             |             |    prise\   |             |             |          |
      |             |             |             |             |    s_ele\   |             |             |          |
      |             |             |             |             |    ctriq\   |             |             |          |
      |             |             |             |             |    ues_s\   |             |             |          |
      |             |             |             |             |    uisse\   |             |             |          |
      |             |             |             |             |    s_aes\   |             |             |          |
      |             |             |             |             |    _ener\   |             |             |          |
      |             |             |             |             |    gie_2\   |             |             |          |
      |             |             |             |             |    013`     |             |             |          |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      |    Hydro    |    5045     |    50.44    |    1263     |    40       |    48.4     |    0.38     | 0.38     |
      |    River    |    :cite:`\ |    :cite:`\ |    :cite:`\ |    :cite:`\ |             |    :cite:`\ | :cite:`\ |
      |             |    assoc\   |    assoc\   |    weid\    |    assoc\   |             |    swis\    | swis\    |
      |             |    iatio\   |    iatio\   |    ema_e\   |    iatio\   |             |    s_fed\   | s_fed\   |
      |             |    n_des\   |    n_des\   |    coinv\   |    n_des\   |             |    eral_of\ | eral_of\ |
      |             |    _entr\   |    _entr\   |    ent_2\   |    _entr\   |             |    fic\     | fic\     |
      |             |    epris\   |    epris\   |    013`     |    epris\   |             |    e_of_en\ | e_of_en\ |
      |             |    es_el\   |    es_el\   |             |    es_el\   |             |    erg\     | erg\     |
      |             |    ectri\   |    ectri\   |             |    ectri\   |             |    y_sfo\   | y_sfo\   |
      |             |    ques_\   |    ques_\   |             |    ques_\   |             |    e_sta\   | e_sta\   |
      |             |    suiss\   |    suiss\   |             |    suiss\   |             |    tisti\   | tisti\   |
      |             |    es_ae\   |    es_ae\   |             |    es_ae\   |             |    que_2\   | que_2\   |
      |             |    s_gra\   |    s_gra\   |             |    s_gra\   |             |    013`     | 013`     |
      |             |    nde_2\   |    nde_2\   |             |    nde_2\   |             |             |          |
      |             |    014`     |    014`     |             |    014`     |             |             |          |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+
      | Geothermal  |    7488     |    142      |    24.9     |    30       |    86       |    0        |    0     |
      | [63]_       |    [63]_    |    [63]_    |    :cite:`\ |             |    :cite:`\ |             |          |
      |             |             |             |    weid\    |             |    assoc\   |             |          |
      |             |             |             |    ema_e\   |             |    iatio\   |             |          |
      |             |             |             |    coinv\   |             |    n_des\   |             |          |
      |             |             |             |    ent_2\   |             |    _entr\   |             |          |
      |             |             |             |    013`     |             |    epris\   |             |          |
      |             |             |             |             |             |    es_el\   |             |          |
      |             |             |             |             |             |    ectri\   |             |          |
      |             |             |             |             |             |    ques_\   |             |          |
      |             |             |             |             |             |    suiss\   |             |          |
      |             |             |             |             |             |    es_ae\   |             |          |
      |             |             |             |             |             |    s_ele\   |             |          |
      |             |             |             |             |             |    ctric\   |             |          |
      |             |             |             |             |             |    ite_2\   |             |          |
      |             |             |             |             |             |    012`     |             |          |
      +-------------+-------------+-------------+-------------+-------------+-------------+-------------+----------+

.. [57]
   Investment cost based on
   :cite:`DanishEnergyAgency2019`. OM cost scaled
   proportionally based on IEA data.

.. [58]
   Based on the real data of 2015 (data
   provided by ELIA, the Belgian TSO, which monitored 2952MW of PV,
   onshore and offshore in 2015 (Source: \url{https://www.elia.be/}, consulted the 06/12/2019.})).

.. [60]
   Onshore and offshore wind turbines in 2030
   :cite:`DanishEnergyAgency2019`. 
   For Offshore, a correction factor of
   2.58 is applied to have an LCOE of 79€/MWh in 2020, in line with
   recently published offer:
   https://www.enerdata.net/publications/daily-energy-news/belgium-agrees-79mwh-lcoe-three-offshore-wind-parks.html,
   visited on the 12-06-2020.   

.. [63]
   ORC cycle at 6 km depth for electricity
   production. Based on Table 17 of :cite:`Carlsson2014`. We
   took the reference case in 2030.

.. _ssec:app1_non-renewable_TK:

Non-renewable
~~~~~~~~~~~~~

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


