.. EnergyScope_documentation documentation master file, created by
   sphinx-quickstart on Thu Sep 30 10:32:01 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

The EnergyScope Typical Day model
=================================
EnergyScope Typical Day (ESTD) is an open-source, whole-energy system model for national or regional energy systems. The model optimises the design and hourly operation of the energy system over a target year.


.. .. figure:: /images/estd_graphical_abstract.png
   :alt: Graphical abstract
   :name: fig:graphical_abstract
   :width: 16cm

EnergyScope Typical Day is developed by EPFL (Switzerland) and UCLouvain (Belgium).
This documentation introduces the version of EnergyScope applied to Colombia and Turkey. The main performances of EnergyScope are detailed in the :doc:`/sections/Overview` Section. The :doc:`/sections/Releases` Section gives more information on the various versions of the model, as well as applications and acknowledgments. Section :doc:`/sections/Model formulation` presents the structure and equations of the model, which apply both for the Colombian and Turkish case studies.
Finally, Sections :doc:`/sections/Input Data - Colombia` and :doc:`/sections/Input Data - Turkey` present the data, sources and assumptions specific to each case study.


Downloading EnergyScope
=======================

The public version of EnergyScope Typical Day can be downloaded in the Releases section or from its github repository (using the Clone or Download button on the right side of the screen): https://github.com/energyscope/EnergyScope

One might be interested by two different versions:

* `Open solver <https://github.com/energyscope/EnergyScope/tree/GLPK_latest>`_ : uses open-source solver and can directly be run, see `getting started with GLPK <https://energyscope.readthedocs.io/en/master/sections/Getting%20started.html>`_ .
* `Python wrapper <https://github.com/energyscope/EnergyScope/tree/EnergyScope.py>`_ : uses Python for pre/post processing and plotting. It supports ampl-cplex/gurobi solvers but can also work with open-source alternatives. See  `getting started with Python <https://energyscope.readthedocs.io/en/energyscope.py/sections/Getting%20started.html>`_

Main contributors
=================

* Stefano **Moret** (`website <https://www.stefanomoret.com/>`_): moret.stefano@gmail.com
* Gauthier **Limpens** : gauthierLimpens@gmail.com

There are many other developers, forming a community around the EnergyScope model !
You will meet them (and their work) in :doc:`/sections/Releases` section.


Contents
=========

.. toctree::
   :maxdepth: 1

   sections/Overview
   sections/Releases
   sections/Getting started
   sections/How to contribute
   sections/Model formulation
   sections/Input Data - Colombia
   sections/Input Data - Turkey
   sections/Bibliography

.. Indices and tables
   ==================
   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`

