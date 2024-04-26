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
from solve_GEMMES import solveGEMMES
from collections import namedtuple
import cppimport

curr_dir = Path(os.path.dirname(__file__))

pymodPath = os.path.abspath(os.path.join(curr_dir.parent,'pylib'))
GEMMES_path = '/home/piejacques/Bureau/ColombiaEnergyScope'
Cpp_path = GEMMES_path + '/SourceCode/cppCode'
sys.path.insert(0, pymodPath)
sys.path.insert(0, Cpp_path)
sys.path.insert(0, Cpp_path + "/src")

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

out = solveGEMMES(solvePy=solvePy, parms=newParms, solver="dopri", atol=1e-4, rtol=0, fac=0.85, facMin=0.1, facMax=4, nStepMax=300, hInit=0.025, hMin=0.025/100, hMax=0.2)

out.plot(y=["ip"], use_index=True)



# Import raw data from C++
samplesExogVarCpp0 = solvePy.samplesExogVar()
nSamplesVarExogVarCpp0 = solvePy.nSamplesVarExogVar()
nVarExogVarCpp0 = solvePy.nVarExogVar()
#build data frame in python, this will be the input passed to the Solve function    
samplesExogVar = pd.DataFrame(np.zeros([nSamplesVarExogVarCpp0[0] , nVarExogVarCpp0]))
for i in range(nVarExogVarCpp0):
    for j in range(nSamplesVarExogVarCpp0[0]):
        samplesExogVar[i][j] = samplesExogVarCpp0[i*nSamplesVarExogVarCpp0[0]+j]

Costs_ES = pd.read_csv('Costs_per_phase.csv')




outDopri2 = solve(solver="dopri", samplesExogVar=samplesExogVar, atol=1e-4, rtol=0, fac=0.85, facMin=0.1, facMax=4, nStepMax=300, hInit=0.025, hMin=0.025/100, hMax=0.2)














