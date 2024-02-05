generateModelFile<-function(modelFile,exogText,initialValues,dataParameters,time){
	
	#Lire le fichier originel
	modelFileToCalib=paste(strsplit(modelFile,'\\.')[[1]][1],"ToCalibrate.R",sep="")
	modelCode <- readChar(modelFile, file.info(modelFile)$size)
	modelCode <- sub("@ADDEXOG", exogText, modelCode)
	modelCode <- sub("@ADDINIT", paste(initialValues$Name,"=",initialValues$Value,collapse = "\n"), modelCode)
	modelCode <- sub("@ADDPARAMS", paste(dataParameters$Name,"=",dataParameters$`Init Value`,collapse = "\n"), modelCode)
	modelCode <- sub("@TIME", paste("begin=",time[1],"\nend=",time[2],"\nby=",time[3]), modelCode)
	writeChar(object=modelCode, modelFileToCalib, nchars=nchar(modelCode), eos=NULL)
	return(modelFileToCalib)
}

calibrateModel<-function(sysMinDist,dataParameters,dataVariables,dataSeries,nbOfRuns=1,plotOptim=T,plotFileName=NA,resultFile=NULL,printEvol=T,timeframe){
	
	########################################
	## PARAMETERS CALIBRATION USING CMAES ##
	########################################
	
	#Getting the series to be fitted
	targetNames<-dataVariables$Name[which(dataVariables$Fitted==1)]
	target<-as.data.frame(dataSeries[,targetNames])
	names(target)<-targetNames
	## dataMinDist is the data set used for optimization
	## WARNING ## elements in dataMinDist must be named ## WARNING ##
	dataMinDist <- lapply(1:ncol(target), function(i) target[,i])
	names(dataMinDist) <- targetNames
	#This is the old version
	# dataMinDist <- as.matrix(target)
	
	## fixedParms can be used to fix parameters u do not want CMAES to estimate
	# it is a vector of 1 (for parameters to optimize) and 0 (for fixed parameters)
	fixedParms <- rep(FALSE, length(sysMinDist$parms))
	paramsToCalibrate<-dataParameters$Name[which(dataParameters$`To Calibrate`==1)]
	fixedParms[which(names(sysMinDist$parms)%in%paramsToCalibrate)]=TRUE
	
	## lowerParms and upperParms are lower and upper bounds for the parameters values 
	# They are OPTIONNAL, and set at +/- Inf by default
	# Even fixed parameters need to have a lower/upper bound, although it will not be used and can be set to any arbitrary value
	lowerParms <- rep(-Inf, length(sysMinDist$parms))
	lowerValuesName<-dataParameters$Name[which(!is.na(dataParameters$Min))]
	lowerParms[which(names(sysMinDist$parms)%in%lowerValuesName)]=dataParameters$Min[which(!is.na(dataParameters$Min))] 
	upperParms <- rep(+Inf, length(sysMinDist$parms))
	upperValuesName<-dataParameters$Name[which(!is.na(dataParameters$Max))]
	upperParms[which(names(sysMinDist$parms)%in%upperValuesName)]=dataParameters$Max[which(!is.na(dataParameters$Max))] 
	
	## samplingTime is a list of vectors defining the sampling date of the observations in dataMinDist
	# if left empty, it is assumed that sampling dates are annual
	
	samplingTime <- lapply(dataMinDist, function(x) dataSeries$time)
	names(samplingTime) <- names(dataMinDist)
	## pointsWeight is a list of vectors defining the weigth associated to each observation in dataMinDist when computing the distance
	# by default, all points receive the same weigth (1)
	pointsWeight <- lapply(dataMinDist, function(x) rep(1, length(x)))
	names(pointsWeight) <- names(dataMinDist)
	
	
	## PARAMETERS FOR CMAES ##
	# Reduce sigma if the algorithm diverges, or increase it to reduce the probability of stopping in a local extrema
	# decrease lambda to reduce computation time, or increase it to reduce the probability of stopping in a local extrema
	# I advise not to change nIterMax
	# Below are default values considered as optimal for optimization of a "reasonably simple" function
	# but on complex problems it is often necessary increase lambda or to adjust sigma to the sensitivity of the system to parameters values
	lambda <- 4*floor(4+3*log(sum(fixedParms))) # number of points per generation
	sigma <- 0.1       # standard deviation at initialization (i.e. initial dispersion of the points)
	nIterMax <- 200 + 50*(sum(fixedParms)+3)**2/sqrt(lambda)       # max number of iterations before termination
	tol <- 1e-3                                                    # numerical tolerance
	
	
	## CREATE AND COMPILE CPP CODE
	
	## TEST IF THE FUNCTION CORRECTLY COMPUTES THE DISTANCE
	# here, we compute the distance once, for a given set of parameters (there is no parameters optimization)
	# using the c++ code and an R code
	# this is not necessary, and is mostly here to check if the c++ code works correctly
	## WARNING ## @ANTOINE, I changed slightly the way to compute the distance compared to your original code ## WARNING ##
	#           # 1) I shifted the indices to be at the correct time period
	#           # 2) I don't use data from the initial position for the fit (I'll add it back later)
	
	# Compute distance in R
	# sys <- cppMakeSys(fileName = "calib/EquationsOpenEconomyModelToCalibrate.R",reportVars=3)
	# resSys <- cppRK4(sysMinDist)
	# resSys<-resSys[,-1]
	# indices<-c(0, seq(1,39)*100)+1
	# simul<-resSys[indices,targetNames]
	# fitR=0
	# maxIncreas=0
	# varMax=""
	# par(mfrow=c(1,3))
	# for(i in 1:length(targetNames)){
	# 	name=targetNames[i]
	# 	varMax=ifelse(maxIncreas<sum(abs((simul[,name]-target[,name])/target[,name])),targetNames[i],varMax)
	# 	fitR=fitR+sum(abs((simul[,name]-target[,name])/target[,name]))	
	# 	maxIncreas=ifelse(maxIncreas<sum(abs((simul[,name]-target[,name])/target[,name])),sum(abs((simul[,name]-target[,name])/target[,name])),maxIncreas)
	# 	matplot(1:nrow(simul),cbind(target[1:nrow(simul),targetNames[i]],simul[targetNames[i]]),type='l',main=targetNames[i],ylab="",xlab="")
	# }
	
	#ISSUE WITH INITIAL VALUES
	
	#THIS NEEDS TO BE CHANGED BUT FOR NOW DOES THE TRICK: 
	# THE ORDER OF VARIABLES IN DATAMINDIST NEEDS TO BE THE SAME AS THE ORDER OF THE VARIABLES IN THE MODEL DEFINITION, 
	# FIRST STATE AND THEN INTERMEDIATE
	# varOrder <- sys$parms
	# dataMinDist <- dataMinDist[, varOrder]
	# Compute distance in C++
	# fitCpp <- cppComputeOneDist(sys=sysMinDist,
	# 														reportVars = 3,
	# 														dataMinDist=dataMinDist,
	# 														samplingTime = samplingTime, 
	# 														pointsWeight = pointsWeight)
	# 
	# cat("Distance in R:   ", fitR, "\nDistance in C++: ", fitCpp) # if those two are not equal, there is an error somewhere...
	
	# write.table(cbind(sysMinDist$parms,fixedParms,lowerParms,upperParms),file="parm.csv",sep=";",dec=",")
	# write.table(dataMinDist,file="minDist.csv",sep=";",dec=",")
	
	## CALL THE CPP FUNCTION TO PERFORM OPTIMIZATION
	
	allPars<-matrix(nrow=(length(sysMinDist$parms)+1),ncol=nbOfRuns)
	# write.csv(cbind(lowerParms,upperParms),file="test.csv")
	rownames(allPars)<-c(names(sysMinDist$parms),"fit")
	bestFit=Inf
	bestIndex=0
	# allSols<-list()
	# allSols[[1]]<-resSys
	for(i in 1:nbOfRuns){
		
		sol <- cppMinDist(sys=sysMinDist,
											parms=dataParameters$`Init Value`,
											fixedParms = fixedParms, 
											lowerParms = lowerParms,
											upperParms = upperParms,
											dataMinDist=dataMinDist,
											samplingTime = samplingTime,
											pointsWeight = pointsWeight, 
											lambda = lambda,
											sigma = sigma,
											nIterMax = nIterMax,
											tol = tol, 
											standardizeParms=TRUE,
											useParallel=TRUE)
		
		if(sol$criterion<bestFit){
			bestFit=sol$criterion
			bestIndex=i
		}
		trueParms <- c(sol$parms)
		# print(names(sys$parms))
		names(trueParms) <- names(sysMinDist$parms)
		allPars[,i]=c(trueParms,sol$criterion)
		# resSysCalib <- cppRK4(sys,parms=trueParms)
		# write.csv(resSysCalib,file=paste("solutions/solCon_",i,".csv",sep=""))
		# allSols[[i+1]]=resSysCalib
		if(printEvol){
			cat("Distance at the estimated parameters: ", sol$criterion,'\n')
			cat(paste(i," of ",nbOfRuns,'\n'))
		}
	}
	
	if(!is.null(resultFile))
		write.csv(allPars,file=paste(nbOfRuns,resultFile))
	
	if(plotOptim){
		
		trueParms <- allPars[,bestIndex]
		names(trueParms) <- names(sysMinDist$parms)
		names(trueParms) <- names(sysMinDist$parms)
		resSysCalib <- cppRK4(sysMinDist,parms=trueParms)
		
		indices<-c(0, seq(1,nrow(target)-1)*100)+1
		simul<-resSysCalib[indices,targetNames]
		if(is.null(dim(targetNames))){
			targetNames=as.vector(targetNames)
			simul<-as.data.frame(simul)
			names(simul)<-targetNames
		}
		
		nbPlots<-ceiling(length(targetNames)/3)
		for (nb in 1:nbPlots){
			if(!is.na(plotFileName)){
				thisFileName <- paste(strsplit(plotFileName,'\\.')[[1]][1],nb,".png",sep="")
				png(filename=thisFileName,width = 960,height=480)
			}
			
			remainingPlots=min(3,length(targetNames)-(nb-1)*3)
			par(mfrow=c(2,remainingPlots))
			for(i in 1:remainingPlots){
				index<-(nb-1)*3+i
				name=targetNames[index]
				matplot(timeframe,cbind(target[,targetNames[index]],simul[targetNames[index]]),type='l',main=targetNames[index],ylab="",xlab="")
				legend("topleft",lty=1:2,col=1:2,legend=c("Observations","Simulations"),bty='n')
			}
			for(i in 1:remainingPlots){
				index<-(nb-1)*3+i
				name=targetNames[index]
				matplot(timeframe,100*cbind(simul[targetNames[index]]-target[,targetNames[index]])/target[,targetNames[index]],type='l',main=targetNames[index],ylab="% erreur",xlab="")
			}
			if(!is.na(plotFileName)){
				dev.off()
			}
		}
	}
	return(allPars)
}