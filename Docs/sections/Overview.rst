Overview
++++++++
.. _label_sec_overview:


:Version: |version| (|release|)
:Date: |today|
:Version main developers: Gauthier Limpens and Pierre Jacques (UCLouvain)
:Short summary: One cell *whole*-energy system model with an hourly resolution and data for analysing the Colombian and Turkish energy systems in 2035.

The EnergyScope model optimises the design and operation of all the energy sectors with the same level of details. The energy sectors are defined as electricity, heat, mobility and non-energy demand. 


The EnergyScope model is developped through a collaboration between UCLouvain (Belgium) and EPFL (Switerland). 
It was originally created by EPFL (Switzerland) in 2011.

EnergyScope is written in an algebraic language which can be compiled with an open source solver (GLPK) but also commercial one (AMPL).

Features
========

In the energy system community, several criteria are used to compare models. 
EnergyScope TD is a bottom-up energy system model and has been compared to 53 other models in :cite:`Limpens2021thesis`.

Each model is tailored to different applications. Regarding EnergyScope, we can outline the following strenghts:

- Modelling of the whole energy system
- Optimisation of hourly operation over a year
- Open source model
- Short computational time

On the other hand, the main weaknesses of EnergyScope can be summarized as follows:

- Spatial resolution: 1 cell
- Low technico-economic resolution
- No market equilibrium
- Deterministic optimisation
- 1 year time horizon

In the following sections, we briefly explain these strengths and weaknesses.


Strengths of the model
----------------------


Whole energy system
^^^^^^^^^^^^^^^^^^^


The current version of EnergyScope represents the four energy sectors of a given national or regional energy system. 
The sectors are coupled, in the sense that electricity can be used for other sectors, such as heat or mobility. As an example, :numref:`Figure %s <fig:bes_illustration>` shows the energy system as represented in the model for the case of Belgium. It accounts for:

- 28 energy carriers
- 112 technologies
- 12 end-use demands


.. figure:: /images/case_study_energy_system.png
   :alt: Illustrative example of a decentralised heating layer.
   :name: fig:bes_illustration
   :width: 16cm

   Application of the EnergyScope TD to the Belgian energy system: overview of the
   resources, technologies and demands implemented. Technologies (in bold) represent groups of
   technologies with different energy inputs (e.g. Boilers include gas boilers, oil boilers ...). ‘Decent.’
   represents the group of thermal storage for each decentralised heat production technology. Abbreviations:
   Atm. (atmospheric), battery electric vehicle (BEV), combined cycle gas turbine (CCGT),
   CC (carbon capture), carbon capture and storage (CCS) cogeneration of heat and power (CHP),
   district heating network (DHN), hydrogen (H2), heat pump (HP), integrated gasification combined
   cycle (IGCC), methan. (methanation), natural gas (NG), onshore (on.), offshore (off.), plug-in hybrid
   electric vehicle (PHEV), pumped hydro storage (PHS), photovoltaic (PV) and synthetic liquid fuel
   (SLF).

Optimisation of hourly operation over a year
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All days of the year are mapped onto a small set of typical days. This reduces the number of time slices accounted for in the model (usually 288 hours, corresponding to 12 days). 
Yet, a reconstruction method enables to capture energy stored across hours and across months of the year. :numref:`Figure %s <fig:estd_time_scale>` illustrates the different time scales captured by the model for optimization of the storage capacities.

.. figure:: /images/estd_different_time_scales.png
   :alt: Illustrative example of a decentralised heating layer.
   :name: fig:estd_time_scale
   :width: 16cm

   Illustration of the different time scales optimised by the model. 
   The hourly power balance is resolved over typical days (bottom), 
   while the level of charge of storage is captured at weekly to seasonal level (middle and top).
   This illustration is for the Swiss case study as presented in :cite:`Limpens2019`.

The model optimises the operation and design of the energy system, making sure that multiple constraints are respected across all time scales.

Open source
^^^^^^^^^^^

The model is both open source (github) and documented (this document). By doing so, the aim is to foster collaborations and enable multiple researchers to co-develop the model.

Short computational time
^^^^^^^^^^^^^^^^^^^^^^^^

The model has a short computational time (around **60 seconds** on a personal laptop), making it an ideal candidate for uncertainty quantification.


Weaknesses of the model
---------------------------

Spatial resolution: 1 cell
^^^^^^^^^^^^^^^^^^^^^^^^^^

This version of EnergyScope TD represents a single regional area, called a *cell*. 
This area is connected to neighbouring countries or regions. Imports and exports of electricity and molecules with these neighbouring countries or regions is represented in the model.

Low technico-economico resolution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current implementaion has a low level of technico-economic contraints. According to the model, energy generation technologies (except nuclear) can ramp up from 0 to full load within only one hour, which is not the case in reality. Regarding the modelling of operational costs, *operation cost* represents the cost of buying fuels and input resources to operate technologies, while *maintenance cost* accounts for the rest. *Maintenance cost* is assumed to be proportional to the capacity installed.


No market equilibrium
^^^^^^^^^^^^^^^^^^^^^

The data for demand consist in an aggregated yearly demand and an hourly profile across the year.
The yearly demand is exogenous to the optimization problem and therefore does not result from any equilibrium between supply and demand.
In other words, the system is forced to fulfill the imposed demand, even if this makes the its cost soar.


Deterministic optimisation
^^^^^^^^^^^^^^^^^^^^^^^^^^

The mathematical model of EnergyScope is a linear optimization problem in continuous time. 
It is resolved by using a linear programming solver which relies on deterministic optimisation. 
All the information is known *a priori* and the solver reaches a single optimum. 

Moreover, linear programming gives chaotic solutions, which can vary from white to black when slightly changing the value of one parameter.

Uncertainty quantification techniques enable to overcome this issue by running several times the model under different configurations. Running the model over a large sampling is made possible thanks to EnergyScope's short computational time.

1 year time horizon
^^^^^^^^^^^^^^^^^^^

EnergyScope TD is a snapshot model, in the sense that it models an optimal energy system for a target future year, without considering the currently existing system.




