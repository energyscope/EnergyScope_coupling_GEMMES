import os, sys
from os import system
from pathlib import Path
import webbrowser
import time
import multiprocessing as mp
import pickle as pkl
import pandas as pd
import numpy as np
import amplpy as apy
from collections import namedtuple
import cppimport

curr_dir = Path(os.path.dirname(__file__))

pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))
GEMMES_path = '/home/piejacques/Bureau/ColombiaEnergyScope'
Cpp_path = GEMMES_path + '/SourceCode/cppCode'
sys.path.insert(0, pymodPath)
sys.path.insert(0, Cpp_path)
sys.path.insert(0, Cpp_path + "/src")

from solve_GEMMES import solveGEMMES

cppimport.settings['force_rebuild'] = True
solvePy = cppimport.imp('functionsForPy')

## Change parameters values in GEMMES
# Build default parms vector in python importing data from C++
parmsNames = solvePy.parmsNames()
# Declare a structure that stores parameters values and their names
namedParms = namedtuple("namedParms", parmsNames)
# build named parms vector using the parmsNamed structure and loading parms values from C++
newParms = namedParms(*solvePy.parms())
newParms = newParms._replace(sigmaxnpNew=1.2)
newParms = newParms._replace(kappa03=0.03526333*1.05)
newParms = newParms._replace(tauf=0.1859935*1.02)
newParms = newParms._replace(taub=0.1222547*1.02)
newParms = newParms._replace(tauw=0.08986282*1.02)
newParms = newParms._replace(tauvat=0.1089564*1.02)
newParms = newParms._replace(fi3=0.45)
newParms = newParms._replace(sigmaxnSpeed=0.48)
newParms = newParms._replace(reducXrO=0)

## Fix the trajectories of exogenous variables
Costs_ES_per_phase = pd.read_csv('Costs_per_phase.csv')
Costs_ES_per_phase.drop(columns=['Unnamed: 0'], inplace=True)

Costs_ES_per_year = pd.DataFrame(np.repeat(Costs_ES_per_phase.values, 5, axis=0))
Costs_ES_per_year = Costs_ES_per_year.loc[2:,:]
Costs_ES_per_year.reset_index(drop=True, inplace=True)

Thetas = pd.read_csv('Thetas.csv')
Thetas.drop(columns=['Unnamed: 0'], inplace=True)

samplesExogVar = pd.concat([Costs_ES_per_year,Thetas], axis=1)
samplesExogVar.columns = np.arange(len(samplesExogVar.columns))

## Run the GEMMES model
out = solveGEMMES(solvePy=solvePy, samplesExogVar=samplesExogVar, parms=newParms, solver="dopri", atol=1e-4, rtol=0, fac=0.85, facMin=0.1, facMax=4, nStepMax=300, hInit=0.025, hMin=0.025/100, hMax=0.2)
out.plot(y=["ip"], use_index=True)











