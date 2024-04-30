import numpy as np
import pandas as pd
    
def solveGEMMES(solvePy=None, time=None, y0=None, parms=None, samplesExogVar=None, solver="dopri", 
          atol=1e-4, rtol=0, fac=0.85, facMin=0.1, facMax=4, nStepMax=100, hInit = 0.01, hMin=0.0001, hMax=0.5):
    
    #INITIALIZATION
    if time is None:
        nt = solvePy.nt()
        tInit = solvePy.tInit()
        tEnd = solvePy.tEnd()
        time = np.arange(tInit, tEnd+0.1, 0.1) 
    else: 
        nt = time.size
        tInit = time[0]
        tEnd=time[time.size-1]

    if hMax>(tEnd-tInit)/(nt-1):
        hMax = (tEnd-tInit)/(nt-1)
    

    if y0 is None:
        y0 = solvePy.yInit()
    if parms is None:
        parms = solvePy.parms()
    if samplesExogVar is None:
        samplesExogVarCpp = solvePy.samplesExogVar()
        nSamplesVarExogVarCpp = solvePy.nSamplesVarExogVar()
        nVarExogVarCpp = solvePy.nVarExogVar()
    else:
        samplesExogVarCpp = [0.0]*samplesExogVar.size
        nSamplesVarExogVarCpp = [samplesExogVar.shape[0]]*samplesExogVar.shape[1]
        nVarExogVarCpp = samplesExogVar.shape[1]
        for i in range(nVarExogVarCpp):
            for j in range(nSamplesVarExogVarCpp[0]):
                samplesExogVarCpp[i*samplesExogVar.shape[0] + j] = samplesExogVar[i][j]
        
    nV = solvePy.nV()
    nIV = solvePy.nIV()
    returnRK4 = solvePy.returnType()
    
    # CALL C++ CODE FOR RK4
    if solver=="dopri":
        outCpp = solvePy.dopri(nt, tInit, tEnd, nV, nIV, y0, parms, samplesExogVarCpp, nSamplesVarExogVarCpp, nVarExogVarCpp,
                               atol, rtol, fac, facMin, facMax, nStepMax, hInit, hMin, hMax)    
    elif solver=="RK4Fixed":
        outCpp = solvePy.RK4Fixed(nt, tInit, tEnd, nV, nIV, y0, parms, samplesExogVarCpp, nSamplesVarExogVarCpp, nVarExogVarCpp)    
    else: 
        outCpp = solvePy.euler(nt, tInit, tEnd, nV, nIV, y0, parms, samplesExogVarCpp, nSamplesVarExogVarCpp, nVarExogVarCpp)    
    
    # FORMAT OUTPTUT
    varNames = solvePy.varNames()
    intermediateVarNames = solvePy.intermediateVarNames()
    derivVarNames = [varName+ "Dot" for varName in varNames]        
    
    
    if(returnRK4 == 3):
        outSize = 2*nV+nIV
        outNames = ['time'] + varNames + derivVarNames + intermediateVarNames
    elif (returnRK4 == 2):
        outSize = nV+nIV
        outNames = ['time'] + varNames + intermediateVarNames
    elif (returnRK4 == 1):
        outSize = 2*nV
        outNames = ['time'] + varNames + derivVarNames
    else:
        outSize = nV
        outNames = ['time'] + varNames
    print(outNames)
    print(len(outNames))
    print(outSize)
    outUnNamed = np.zeros((nt,outSize+1))
    for i in range(nt):
        outUnNamed[i,:] = [time[i]] + outCpp[(i*(outSize)):(i*(outSize)+(outSize))]
    out = pd.DataFrame(outUnNamed, columns=outNames, index=time)
    return out