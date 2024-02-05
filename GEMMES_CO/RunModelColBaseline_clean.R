#Load the package
library(Rcpp)

#Load the algorithm
source("Source/SourceCode.R")
source("Source/sourceCodeCalibration.R")
source("Source/utilities.R")

event1 <- list(triggerDate=4, reducXrO="0.025")

#Put the equations into the algorithm
SOEM <- cppMakeSys(fileName = "codeColombia_2023_v1_scen2_clean.R",reportVars=3, eventTime=list(event1))

parms=SOEM$parms

#Aligning parameters with initial values of FX public debt to avoid swings in the beginning
parms['sigmaG0']<-SOEM$y0['sigmafx']

#re-parametrising some of the propensity to consume parameters to avoid swings in the beginning
parms['mpcUB'] <- (SOEM$y0['Cdh']-1.621424)/735.1836 + exp(parms['lambdal0']*(-0.03199999 + parms['lambdal1'] + 0.03522769))* (-parms['mpcLB'] + (SOEM$y0['Cdh']-1.621424)/735.1836)
# CdhTar = mpc1*YDh + mpc2*(Dh + ITRh) + Ldchdot# (*Target desired consumption-nominal*)
# mpc1 = (1/(1 + exp(-lambdal0*(idep - lambdal1 - pdot/p))))*(UB1 - LowB1) + LowB1#(*Marginal propensity to consume out income #AG:hardcoded value*)

#Re-parametrising the social transfers
parms['fi3']=0.504722189217687
parms['fi4']=(106.573- parms['fi3']*SOEM$y0['Wf']*(SOEM$y0['pop'] - 2.124 - 20.08769 - 0.348))/(SOEM$y0['Wf']*SOEM$y0['pop'])
# ST = fi3*Wf*(pop - Lg - Lf - Lb) + fi4 * Wf*pop

#Investment function
parms['kappa0']<-0.027
# kappa0=0.0446637659861748
# ikfTar = (kappa0 + kappa1*(rf - pdot/p) + kappa2*u)*kf#(*Investment Real*)
parms['reducXrO']<--0.025

parms['reducXrO']<--0.025
parms['varsigmafdi4']<-0.40
parms['sigmaxnpNew']<-1
parms['scenInv']<-0
event1 <- list(triggerDate=4, reducXrO="0")
cppSOEM <- cppRK4(SOEM,parms=parms,times=seq(from=2019, to=2050, by=0.1), eventTime=list(event1))


#Increasing export propensities
parms['sigmaxnpNew']<-1.2
cppSOEM2 <- cppRK4(SOEM,parms=parms,times=seq(from=2019, to=2050, by=0.1), eventTime=list(event1))


res=list()
res[["Baseline"]]<-cppSOEM2