list.of.packages <- c("Rcpp")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)
library(list.of.packages,character.only = T)

#############################################################
## Create the Cpp function from tderiv and intermediateVar ##
## And compile (if compile==TRUE) the cpp code for RK4     ##
#############################################################
cppMakeSys <- function(fileName=NULL, tderiv=NULL, parms=NULL, times=NULL, 
                       y0=NULL, intermediateVar=NULL, eventTime=NULL,
                       dataExogVar = NULL, exogSamplingTime=NULL,
                       eventVar=NULL, compile=TRUE, reportVars=NULL) {
  if (!is.null(fileName)) {
    sys <- loadModel(fileName)
  }
  sys <- completeSys(c("tderiv", "parms",  "times",
                       "y0", "intermediateVar", "eventTime",
                       "eventVar","reportVars", 
                       "dataExogVar", "exogSamplingTime"), 
                     sys, envir=environment())
  missingArguments(c("tderiv", "parms", "times"), sys,envir=environment())
  initScipen <- getOption("scipen")
  options(scipen=999) #avoid scientific notation, that can cause issues with the different conversions from R to cpp
  #Initialization
  sys$dim <- length(sys$tderiv)
  sys$nT <- length(sys$times)
  sys$byT <- sys$times[2] - sys$times[1]
  
  #Define strings for the cpp function and the options to pass to the openCL Kernel
  allEquations <- unloopEquations(sys$tderiv, sys$intermediateVar)
  
  #########" OK exogVar ###################
  
  sys$strFunc <- makeCppFunc(allEquations, sys$parms, sys$tderiv,sys$intermediateVar, exogVar = !is.null(sys$dataExogVar))
  if (compile==TRUE)
    cppCompileRK4(NULL, sys$dim, sys$strFunc, sys$eventTime, sys$eventVar, sys$parms, sys$tderiv, sys$intermediateVar,sys$reportVars)
  options(scipen=initScipen)
  sys
}

#############################################################
## Create the Cpp function from tderiv and intermediateVar ##
## And compile (if compile==TRUE) the cpp code for MinDist ##
#############################################################
cppMakeMinDist <- function(fileName=NULL, tderiv=NULL, parms=NULL, times=NULL, y0=NULL,
                           dataExogVar = NULL, exogSamplingTime=NULL,
                           fixedParms=NULL, lowerParms=NULL, upperParms=NULL, dataMinDist=NULL, 
                           samplingTime=NULL, pointsWeight=NULL, intermediateVar=NULL, eventTime=NULL, 
                           eventVar=NULL, compile=TRUE, reportVars=2) {
  if (!is.null(fileName)) {
    sys <- loadModel(fileName)
  }
  sys <- completeSys(c("tderiv", "parms", "times", "y0", "intermediateVar", "fixedParms",
                       "dataExogVar", "exogSamplingTime",
                       "lowerParms", "upperParms", "dataMinDist", "samplingTime",
                       "pointsWeight", "eventTime", "eventVar","reportVars"), 
                     sys, envir=environment())
  missingArguments(c("tderiv", "parms", "times"), sys, envir=environment())
  initScipen <- getOption("scipen")
  options(scipen=999) #avoid scientific notation, that can cause issues with the different conversions from R to cpp
  #Initialization
  sys$dim <- length(sys$tderiv)
  sys$nT <- length(sys$times)
  sys$byT <- sys$times[2] - sys$times[1]
  
  #Define strings for the cpp function and the options to pass to the openCL Kernel
  allEquations <- unloopEquations(sys$tderiv, sys$intermediateVar)
  # write.csv(allEquations,file="equations.csv")
  sys$strFunc <- makeCppFunc(allEquations, sys$parms, sys$tderiv,sys$intermediateVar, exogVar = !is.null(sys$dataExogVar))
  
  #Use double not Float in R, for accuracy
  sys$strFunc <- gsub("float", "double", sys$strFunc)
  strEventTime <- ifelse(is.null(eventTime), "", makeEventTime(sys))
  strEventVar <- ifelse(is.null(eventVar), "", makeEventVar(sys))
  if (reportVars==0) {
    strReportingVars <- c("", "")
  } else {
    strReportingVars <- makeReportingVariables(sys)
  }
  
  #Load Raw Cpp Code, add dim and options definitions and save
  cppCode <- readChar("RawCppCodeMinDist.cpp", file.info("RawCppCodeMinDist.cpp")$size)
  cppCode <- sub("@AddDim", as.character(sys$dim), cppCode)
  cppCode <- sub("@AddDimIv", as.character(length(sys$intermediateVar)), cppCode)
  cppCode <- sub("@AddDimOut", ifelse(sys$reportVars==3,
                                      as.character(2*sys$dim+length(sys$intermediateVar)),
                                      ifelse(sys$reportVars==2,
                                             as.character(2*sys$dim),
                                             ifelse(sys$reportVars==1,
                                                    as.character(sys$dim+length(sys$intermediateVar)),
                                                    as.character(sys$dim)))), cppCode)
  cppCode <- gsub("@AddReportingVarsInit", strReportingVars[2], cppCode)
  cppCode <- gsub("@AddReportingVars", strReportingVars[1], cppCode)
  cppCode <- gsub("@AddFunc", sys$strFunc, cppCode)
  cppCode <- gsub("@AddEventTime", strEventTime, cppCode)
  cppCode <- gsub("@AddEventVar", strEventVar, cppCode)
  
  # Final formatting
  cppCode <- gsub("intToFloat", ".0", cppCode) #double not float
  cppCode <- gsub("doubleToFloat", "", cppCode) #double not float
  cppCode <- gsub("somethingToRemoveLater", "", cppCode)
  cppCode <- gsub(", MakeThisAndCommaAnInterrogationMark,", " ? ", cppCode)
  cppCode <- gsub(", MakeThisAndCommaAColon,", " : ", cppCode)
  cppCode <- gsub("makeThisAnSTDAndDoubleColon", "std::", cppCode)
  cppCode <- gsub("thisIsAnInt", "", cppCode)
  
  writeChar(object=cppCode, "CppCodeMinDist.cpp", nchars=nchar(cppCode), eos=NULL)
  
  # Sys.setenv(PKG_LIBS = "-lOpenCL")
  sourceCpp("CppCodeMinDist.cpp")
  options(scipen=initScipen)
  sys
}

cppMinDist <- function(sys=NULL, times=NULL, parms=NULL, fixedParms=NULL,
                       dataExogVar=NULL, exogSamplingTime=NULL,
                       lowerParms=NULL, upperParms=NULL, y0=NULL,
                       eventTime=NULL, eventVar=NULL, 
                       dataMinDist, samplingTime, pointsWeight, 
                       lambda,
                       sigma=1,
                       nIterMax,
                       tol=1e-9,
                       standardizeParms=TRUE,
                       useParallel=TRUE) {
  if(is.null(sys)) sys <- list()
  if(!is.null(sys$dataExogVar) && !is.null(dataExogVar)) dataExogVar <- dataExogVar[names(sys$dataExogVar)]
  sys <- completeSys(c("parms", "fixedParms", "lowerParms", "upperParms", "times", "y0",
                       "dataExogVar", "exogSamplingTime",
                       "eventTime", "eventVar",
                       "dataMinDist", "samplingTime", "pointsWeight"), sys, envir=environment())
  if (is.null(sys$fixedParms)) sys$fixedParms <- rep(0, length(sys$parms))
  if (is.null(sys$samplingTime)) sys$samplingTime <- lapply(sys$dataMinDist, function(x) 1:length(x))
  
  if (is.null(sys$dataExogVar)) sys$dataExogVar <- list()
  if (is.null(sys$exogSamplingTime)) sys$exogSamplingTime <- list()
  
  sys$samplingTime <- lapply(sys$samplingTime, function(x) c(x, +Inf))
  sys$exogSamplingTime <- lapply(sys$exogSamplingTime, function(x) c(x, +Inf))
  
  if (is.null(sys$pointsWeight)) sys$pointsWeight <- lapply(sys$dataMinDist, function(x) rep(1, length(x)))
  
  if(!is.list(sys$dataMinDist)) stop("dataMinDist must be a list of (named) vectors")
  if(!is.list(sys$samplingTime)) stop("samplingTime must be a list of (named) vectors")
  if(!is.list(sys$pointsWeight)) stop("pointsWeight must be a list of (named) vectors")
  
  
  if (is.null(sys$lowerParms)) {
    sys$lowerParms <- rep(-Inf, length(sys$parms))
  }
  if (is.null(sys$upperParms)) {
    sys$upperParms <- rep(+Inf, length(sys$parms))
  }
  
  missingArguments(c("parms", "times", "y0", "dataMinDist"), sys, envir=environment())
  sys$nT <- length(sys$times)
  sys$byT <- sys$times[2] - sys$times[1]
  
  if(!exists("minDistOptimForR"))
    stop("No Compiled C++ code found. Use the function cppMakeMinDist with the argument compile=TRUE to compile.")
  
  varMinDist <- c(which(names(sys$tderiv) %in% names(sys$dataMinDist)),
                  length(sys$y0) + which(names(sys$intermediateVar) %in% names(sys$dataMinDist))) - 1   # -1 as indices start at zero in c++
  sys$dataMinDist <- sys$dataMinDist[c(names(sys$tderiv), names(sys$intermediateVar))[varMinDist+1]]
  sys$samplingTime <- sys$samplingTime[c(names(sys$tderiv), names(sys$intermediateVar))[varMinDist+1]]
  sys$pointsWeight <- sys$pointsWeight[c(names(sys$tderiv), names(sys$intermediateVar))[varMinDist+1]]
  if (standardizeParms==TRUE) {
    for (i in 1:length(sys$parms)) {
      if (sys$fixedParms[i]==TRUE && (sys$lowerParms[i]==-Inf || sys$upperParms[i]==+Inf)) {
        stop("Can't standardize parameters when having infinite lower/upper bounds for non fixed parameters")
      }
    }
  }
  
  minDistOptimForR(sys$parms, 
                   sys$fixedParms, 
                   sys$lowerParms, 
                   sys$upperParms,
                   sys$y0, 
                   sys$nT, 
                   sys$byT, 
                   sys$dataExogVar,
                   sys$exogSamplingTime,
                   varMinDist,
                   sys$dataMinDist, 
                   sys$samplingTime,
                   sys$pointsWeight,
                   lambda, sigma, nIterMax, tol, standardizeParms, useParallel)
}

########################################################################
## Compute the distance criterion for a given value of the parameters ##
########################################################################
cppComputeOneDist <- function(sys=NULL, times=NULL, parms=NULL, y0=NULL,
                              dataExogVar=NULL, exogSamplingTime=NULL,
                              eventTime=NULL, eventVar=NULL,
                              dataMinDist = NULL, samplingTime = NULL, pointsWeight = NULL) {
  if(is.null(sys)) sys <- list()
  if(!is.null(sys$dataExogVar) && !is.null(dataExogVar)) dataExogVar <- dataExogVar[names(sys$dataExogVar)]
  sys <- completeSys(c("parms", "times", "y0",
                       "dataExogVar", "exogSamplingTime",
                       "eventTime", "eventVar",
                       "dataMinDist", "samplingTime", "pointsWeight"), sys, envir=environment())
  missingArguments(c("parms", "times", "y0", "dataMinDist"), sys, envir=environment())
  if (is.null(sys$dataExogVar)) sys$dataExogVar <- list()
  if (is.null(sys$exogSamplingTime)) sys$exogSamplingTime <- list()
  
  if (is.null(sys$samplingTime)) sys$samplingTime <- lapply(sys$dataMinDist, function(x) 1:length(x))
  if (is.null(sys$pointsWeight)) sys$pointsWeight <- lapply(sys$dataMinDist, function(x) rep(1, length(x)))
  
  sys$exogSamplingTime <- lapply(sys$exogSamplingTime, function(x) c(x, +Inf))
  sys$samplingTime <- lapply(sys$samplingTime, function(x) c(x, +Inf))
  
  sys$nT <- length(sys$times)
  sys$byT <- sys$times[2] - sys$times[1]
  
  if(!exists("ComputeDistanceForR"))
    stop("No Compiled C++ code found. Use the function cppMakeMinDist with the argument compile=TRUE to compile.")
  
  varMinDist <- c(which(names(sys$tderiv) %in% names(sys$dataMinDist)),
                  length(sys$y0) + which(names(sys$intermediateVar) %in% names(sys$dataMinDist))) - 1   # -1 as indices start at zero in c++
  sys$dataMinDist <- sys$dataMinDist[c(names(sys$tderiv), names(sys$intermediateVar))[varMinDist+1]]
  sys$samplingTime <- sys$samplingTime[c(names(sys$tderiv), names(sys$intermediateVar))[varMinDist+1]]
  sys$pointsWeight <- sys$pointsWeight[c(names(sys$tderiv), names(sys$intermediateVar))[varMinDist+1]]
  
  # cat("length",length(sys$parms),"type:",typeof(sys$parms),"\n")
  # cat("length",length(sys$y0),"type:",typeof(sys$y0),"\n")
  # cat("length",length(sys$nT),"type:",typeof(sys$nT),"\n")
  # cat("length",length(sys$byT),"type:",typeof(sys$byT),"\n")
  # cat("length",length(dataMinDist),"type:",typeof(dataMinDist),"\n")
  ComputeDistanceForR(sys$parms, 
                      sys$y0, 
                      sys$nT, 
                      sys$byT,
                      sys$dataExogVar, 
                      sys$exogSamplingTime,
                      varMinDist,
                      sys$dataMinDist, 
                      sys$samplingTime, 
                      sys$pointsWeight)
}


###########################################################################
##                           Internal function (Is it really?)           ##
## Load the model from an external file and create an object sys with it ##
###########################################################################
loadModel <- function(fileName) {
  options(warn=-1)
  modelFile <- file(fileName)
  modelText <- readLines(modelFile, n = -1)
  close(modelFile)
  firstEquation=TRUE
  equations = NULL
  out <- list()
  
  #Exogenous Variables
  beginExogenousVar <- which(grepl("##exogenous variables", modelText))[1]
  if (!is.na(beginExogenousVar)) {
    endExogenousVar <- min(which(regexpr("##", modelText[-(1:beginExogenousVar)])==1)) # search next row beginning by a "##"
    
    if (length(endExogenousVar)>0 && endExogenousVar>1) {
      ExogenousVarText <- modelText[beginExogenousVar+1:(endExogenousVar-1)]
      out$dataExogVar <- lapply(createEquations(ExogenousVarText), function(x) eval(parse(text=x)))
      out$intermediateVar <- createExogVar(names(out$dataExogVar))
      # out$exogVarOrder <- 
    }
  }				
  #Sampling time
  beginSamplingTime <- which(grepl("##sampling time", modelText))[1]
  if (!is.na(beginSamplingTime)) {
    endSamplingTime <- min(which(regexpr("##", modelText[-(1:beginSamplingTime)])==1), length(modelText)-beginSamplingTime+1) # search next row beginning by a "##"
    
    if (length(endSamplingTime)>0 && endSamplingTime>1) {
      samplingTimeText <- modelText[beginSamplingTime+1:(endSamplingTime-1)]
      out$exogSamplingTime <- lapply(createEquations(samplingTimeText), function(x) eval(parse(text=x)))
    }
  }
  
  #Intermediate Variables
  beginIntermediateVar <- which(grepl("##intermediate variables", modelText))[1]
  if (!is.na(beginIntermediateVar)) {
    endIntermediateVar <- min(which(regexpr("##", modelText[-(1:beginIntermediateVar)])==1), length(modelText)-beginIntermediateVar+1) # search next row beginning by a "##"
    
    if (length(endIntermediateVar)>0 && endIntermediateVar>1) {
      intermediateVarText <- modelText[beginIntermediateVar+1:(endIntermediateVar-1)]
      # print(intermediateVarText)
      out$intermediateVar <- c(out$intermediateVar, createEquations(intermediateVarText))
    }
  }
  
  #times derivatives
  beginTderiv <- which(grepl("##time derivatives", modelText))[1]
  if (is.na(beginTderiv)) {
    stop("Missing time derivatives")
  }
  endTderiv <- min(c(which(regexpr("##", modelText[-(1:beginTderiv)])==1), length(modelText)-beginTderiv+1)) # search next row beginning by a "#"
  if (length(endTderiv)!=0 && endTderiv>1) {
    tderivText <- modelText[beginTderiv+1:(endTderiv-1)]
    out$tderiv <- createEquations(tderivText)
  } else {
    stop("Missing time derivatives")
  }
  
  #Parameters
  beginParms <- which(grepl("##parameters", modelText))[1]
  if(!is.na(beginParms)) {
    endParms <- min(c(which(regexpr("##", modelText[-(1:beginParms)])==1), length(modelText)-beginParms+1)) # search next row beginning by a "#"
    if (length(endParms)!=0 && endParms>1) {
      parmsText <- modelText[beginParms+1:(endParms-1)]
      out$parms <- sapply(createEquations(parmsText), function(x) eval(parse(text=x)))
      sapply(1:length(out$parms), function(i) eval(call("=", names(out$parms)[i], out$parms[i]), envir=parent.env(environment())))
    }
  }
  
  #Initial Values
  beginInitialValues <- which(grepl("##initial values", modelText))[1]
  if(!is.na(beginInitialValues)) {
    endInitialValues <- min(c(which(regexpr("##", modelText[-(1:beginInitialValues)])==1), length(modelText)-beginInitialValues+1)) # search next row beginning by a "#"
    if (length(endInitialValues)!=0 && endInitialValues>1) {
      y0Text <- modelText[beginInitialValues+1:(endInitialValues-1)]
      out$y0 <- sapply(createEquations(y0Text), function(x) eval(parse(text=x)))
    }
  }
  
  #Time Sequence
  beginTime <- which(modelText=="##time")[1]
  if(!is.na(beginTime)) {
    endTime <- min(c(which(regexpr("##", modelText[-(1:beginTime)])==1), length(modelText)-beginTime+1)) # search next row beginning by a "#"
    if (length(endTime)!=0 && endTime>1) {
      timeText <- modelText[beginTime+1:(endTime-1)]
      out$times <- sapply(createEquations(timeText), function(x) eval(parse(text=x)))
      out$times <- seq(out$times["begin"], out$times["end"], out$times["by"])
    }
  }
  
  #Events Time
  beginEventTime <- which(grepl("##events time", modelText))[1]
  if(!is.na(beginEventTime)) {
    endEventTime <- min(c(which(regexpr("##", modelText[-(1:beginEventTime)])==1), length(modelText)-beginEventTime+1)) # search next row beginning by a "#"
    if (length(endEventTime)!=0 && endEventTime>1) {
      out$eventTime <- lapply(1:(endEventTime-1), function(i) eval(parse(text=modelText[beginEventTime+1:(endEventTime-1)][i])[[1]]))
    }
  }
  
  #Events Var
  beginEventVar <- which(grepl("##events variable", modelText))[1]
  if(!is.na(beginEventVar)) {
    endEventVar <- min(c(which(regexpr("##", modelText[-(1:beginEventVar)])==1), length(modelText)-beginEventVar+1)) # search next row beginning by a "#"
    if (length(endEventVar)!=0 && endEventVar>1) {
      out$eventVar <- lapply(1:(endEventVar-1), function(i) eval(parse(text=modelText[beginEventVar+1:(endEventVar-1)][i])[[1]]))
    }
  }
  
  options(warn=0)
  out
}


##########################################################################
##                           Internal function                          ##
## Used by load model to turn str in equations for sys                  ##
##########################################################################
## I included (pre) formatting on data here for simplicity. I might move it somewhere else later.
## the problem is that it makes some of the formatting visible in the R object sys(in sys$intermediateVar)...
createExogVar <- function(strExogVarNames) {
  out <- c()
  for (i in 1:length(strExogVarNames)) {
    lineText <- paste0("dataExogVar[indexVar][comptExogVar[indexVar]]", 
                       "+",
                       paste0("(", "dataExogVar[indexVar][comptExogVar[indexVar]+somethingToRemoveLater1thisIsAnInt]", 
                              "-",
                              "dataExogVar[indexVar][comptExogVar[indexVar]]", ")"), 
                       "*",
                       paste0(paste0("(", "t",
                                     " - ",
                                     "exogSamplingTime[indexVar][comptExogVar[indexVar]])"),
                              "/", 
                              paste0("(", "exogSamplingTime[indexVar][comptExogVar[indexVar]+somethingToRemoveLater1thisIsAnInt]",
                                     " - ",
                                     "exogSamplingTime[indexVar][comptExogVar[indexVar]])")))
    lineText <- gsub("indexVarPlusOne",
                     paste0("somethingToRemoveLater",
                            as.character(i),
                            "thisIsAnInt"),
                     lineText)
    
    lineText <- gsub("indexVar",
                     paste0("somethingToRemoveLater",
                            as.character(i-1),
                            "thisIsAnInt"),
                     lineText)
    
    
    out <- c(out, lineText)
    names(out)[length(out)] <- strExogVarNames[i]
  }
  out
}

##########################################################################
##                           Internal function                          ##
## Used by load model to turn str in equations for sys                  ##
##########################################################################
createEquations <- function(strEquations) {
  out <- c()
  for (i in 1:length(strEquations)) {
    lineText <- strEquations[i]
    lineText <- sub("#.*", "", lineText) ## Remove any trailing comment
    if (!grepl("^[[:blank:]]*$", lineText)) { ## Skip empty lines or lines containing only spaces
      tempStr1Line = strsplit(lineText, "=")[[1]]
      
      #This is to manage the case when there are other = in the equation (use of logical operators)
      if(length(tempStr1Line)>2){
        tempStr <- tempStr1Line[2]
        for(iter in 3:length(tempStr1Line)){
          tempStr <- paste(tempStr,tempStr1Line[3],sep="=")
          tempStr1Line <- tempStr1Line[-3]
        }
        tempStr1Line[2] <- tempStr
      }
      #Replacing all reseverved words, for now only in-> inv
      
      tempStr1Line[1] <- gsub("[[:space:]]","",tempStr1Line[1])
      tempStr1Line[2] <- gsub("[[:space:]]","",tempStr1Line[2])
      out <- c(out, tempStr1Line[2])
      names(out)[length(out)] <- tempStr1Line[1]
    }
  }
  out
}


################################################################
##                    Internal function                       ##
## Complete the object sys with other inputs if required      ##
################################################################
completeSys <- function(allNames, sys=NULL, envir=environment()) {
  if (is.null(sys))
    sys <- list()
  for (i in 1:length(allNames)) {
    if(!is.null(eval(as.name(allNames[i]), envir=envir))) {
      if (identical(eval(as.name(allNames[i]), envir=envir), FALSE)) {
        sys[allNames[[i]]] <- list(NULL)
      } else {
        sys[[allNames[i]]] <- eval(as.name(allNames[i]), envir=envir)
      }
    }
  }
  sys
}

################################################################
##                    Internal function                       ##
## Test if there is any missing input when calling a function ##
################################################################
missingArguments <- function(allNames, sys=NULL, envir=environment()) {
  if (is.null(sys)) {
    missingArguments <-(sapply(allNames, function(x) is.null(eval(as.name(x),
                                                                  envir=envir))))
    if (any(missingArguments)) {
      stop("Missing arguments: ", paste(allNames[missingArguments], collapse=", "))
    }
  } else {
    missingArguments <-(sapply(allNames, function(x) is.null(eval(call("$", quote(sys), as.name(x)),
                                                                  envir=envir))))
    if (any(missingArguments)) {
      stop("Missing elements in sys: ", paste(paste0("sys$", allNames[missingArguments]), collapse=", "))
    }
  }
}

##########################################################################
##                           Internal function                          ##
## Reorder equations (both intermediate variables and time derivatives) ##
## And detect circularities (which cause an error and stop the code)    ##
##########################################################################
unloopEquations <- function(tderiv, intermediateVar = NULL) {
  allEquations <- tderiv
  names(allEquations) <- paste0(names(allEquations), "Dot")
  if (!is.null(intermediateVar))
    allEquations <- c(allEquations, intermediateVar)
  adjency <- createAdjencies(allEquations)
  variablesRemaining <- rep(TRUE, length(allEquations))
  unloopedOrder <- c()
  while (any(variablesRemaining==TRUE)) {
    tempSum <- colSums(as.matrix(adjency[variablesRemaining, variablesRemaining]))
    newUnloopedVariables <- (1:length(allEquations))[variablesRemaining][which(tempSum==0)]
    if (length(newUnloopedVariables)==0 || is.null(newUnloopedVariables)) {
      stop("There is a circularity with the variables: ", paste(names(allEquations)[variablesRemaining], collapse=" "))
    }
    unloopedOrder <- c(unloopedOrder, newUnloopedVariables)
    variablesRemaining[unloopedOrder] <- FALSE
  }
  return(allEquations[unloopedOrder])
}

##########################################################################
##                           Internal function                          ##
## Create Adjency tables for the different variables                    ##
##########################################################################
createAdjencies <- function(equations) {
  equations <- cbind(names(equations), equations)
  adjacency = matrix(0, nrow = nrow(equations), ncol = nrow(equations), dimnames=list(c(equations[,1]) , c(equations[,1])))
  for (j in 1:nrow(equations)) {
    temp <- gsub("[\\^ \t\n\r\f\v()/\\+\\<\\>\\*\\=\\!|\\,\\&\\-]+", " ", equations[j, 2])
    for (i in 1:nrow(equations)) {
      ind <- grep(paste("([ \t\n\r\f\v]|^)", equations[i, 1], "([ \t\n\r\f\v]|$)", sep = ""), temp)
      if (length(ind)>0 && ind > -1) {
        adjacency[j, i] = 1
      }
    }
  }
  t(adjacency)
}

##################################################
##            Internal function                 ##
## Create str for the cpp function of the model ##
##################################################

# need to specialise if there are exogVar or not for initialization/function structure definition
# otherwise, exogVar treated as intermediate variables, and (pre) formating is already done, so nothing more
# than a true/false is required here.
makeCppFunc <- function(allEquations, parms, tderiv, intermediateVar, exogVar=FALSE) { # Create the cpp function defining differential equations for the kernel
  # init the string with inputs
  strCppFunc <- 'void Func(float t, float* y, float* parms, float* ydot, float* x, float** dataExogVar, float** exogSamplingTime, int nExogVar, int* comptExogVar) {'
  strCppFunc <- paste0(strCppFunc, "\n")
  if (exogVar) {
    strCppFunc <- paste0(strCppFunc, '
		for (unsigned int it=0;it<nExogVar; it++) {
			while (t>exogSamplingTime[it][comptExogVar[it]]) comptExogVar[it]++;
			comptExogVar[it]--;
		}')
  }
  
  # (Pre)Format the equations
  allEquations <- sapply(allEquations,
                         function(x) {
                           funcFormatEquation(Eq=parse(text=x)[[1]], parmsNames=names(parms), yNames=names(tderiv),ivNames = names(intermediateVar))
                         }
  )
  # Include the equations to the str
  for(i in 1:length(allEquations)) {     # add one line with "varName = varExpression"
    if(any(paste0(names(tderiv), "Dot")==names(allEquations[i]))==TRUE) { # if it is a time derivative
      indiceVar <- which(paste0(names(tderiv), "Dot")==names(allEquations[i]))
      strCppFunc <- paste(strCppFunc, 
                          paste0(paste0("ydot[", indiceVar-1, "]"),
                                 ' = ', 
                                 allEquations[i], 
                                 ';'),
                          sep="\n")
    } else { # If it is an intermediate variable
      indiceVar <- which(names(intermediateVar)==names(allEquations[i]))
      strCppFunc <- paste(strCppFunc, 
                          paste0(paste0("x[", indiceVar-1, "]"),
                                 ' = ', 
                                 allEquations[i], 
                                 ';'),
                          sep="\n")
    }
  }
  strCppFunc <- paste(strCppFunc, '}', sep="\n")
}

######################################################
##                  Internal function               ##
## Format the equations to translate them in C code ##
######################################################
funcFormatEquation <- function(Eq, parmsNames, yNames, ivNames) {
  
  
  if (length(Eq)>1) { #Eq is a call with multiple elements
    for (i in 1:length(Eq)) { #apply the function to all the elements
      Eq[[i]] <- funcFormatEquation(Eq[[i]], parmsNames, yNames,ivNames)
    }
    if (Eq[[1]]==quote(ifelse)) { # Handle ifelse statement, use temporary code that is translated during the last step
      newEq <- call("somethingToRemoveLater")
      newEq[[2]] <- call("(", Eq[[2]])
      newEq[[3]] <- quote(MakeThisAndCommaAnInterrogationMark)
      newEq[[4]] <- Eq[[3]]
      newEq[[5]] <- quote(MakeThisAndCommaAColon)
      newEq[[6]] <- Eq[[4]]
      Eq <- newEq
    }
    else if (Eq[[1]]==quote(max)) {
      Eq[[1]] <- quote(makeThisAnSTDAndDoubleColonmax)
    }
    else if (Eq[[1]]==quote(min)) {
      Eq[[1]] <- quote(makeThisAnSTDAndDoubleColonmin)
    }
  } else { #Single element
    if (any(parmsNames==as.character(Eq))) { # Eq is a parameter, replace it by its position in the vector parms
      parmsIndice <- which(parmsNames==rep(as.character(Eq), length(parmsNames))) - 1 
      Eq <- paste0("parms[", as.character(parmsIndice), "]")
      Eq <- parse(text=Eq)[[1]]
    } else if (any(yNames==as.character(Eq))) { # Eq is a variable, replace it by its position in the vector y
      yIndice <- which(yNames==as.character(Eq)) - 1
      Eq <- paste0("y[", as.character(yIndice), "]")
      Eq <- parse(text=Eq)[[1]]
    } else if (any(paste0(yNames, "Dot")==as.character(Eq))) { # Eq is a time derivative, repace it by its position in the vector ydot
      yIndice <- which(paste0(yNames, "Dot")==as.character(Eq)) - 1
      Eq <- paste0("ydot[", as.character(yIndice), "]")
      Eq <- parse(text=Eq)[[1]]
    } else if (any(ivNames==as.character(Eq))) { # Eq is a variable, replace it by its position in the vector y
      ivIndice <- which(ivNames==as.character(Eq)) - 1
      Eq <- paste0("x[", as.character(ivIndice), "]")
      Eq <- parse(text=Eq)[[1]]
    } else if(is.numeric(Eq)) { # Numeric value, need to make it a float! Mark it and make it a float in the final step
      tempEq <- Eq
      if (as.integer(Eq)==Eq) { #if it is an int
        Eq <- as.name(paste0("somethingToRemoveLater", as.character(abs(Eq)), "intToFloat"))
      } else { # if it is a double
        Eq <- as.name(paste0("somethingToRemoveLater", as.character(abs(Eq)), "doubleToFloat"))
      }
      if (tempEq<0) { #Negative value, add a "-"
        Eq <- call("-", Eq)
      }
    } else if (Eq=="^" || Eq=="**") { #Exponent, need to use pow, directly replace it here
      Eq <- quote(pow)
    }
  }
  return(Eq)
}

#################################
##      internal function      ##
## Compile the code for RK4    ##
#################################
cppCompileRK4 <- function(sys=NULL, dim=sys$dim, strFunc=sys$strFunc, eventTime=sys$eventTime,
                          eventVar=sys$eventVar, parms=sys$parms, tderiv=sys$tderiv, 
                          intermediateVars=sys$intermediateVars, reportVars=sys$reportVars) {
  
  if (is.null(sys))
    sys <-list()
  sys <- completeSys(c("dim", "strFunc", "eventTime", "eventVar",
                       "parms", "tderiv", "intermediateVars", "reportVars"),
                     sys, envir=environment())
  missingArguments(c("dim", "strFunc", "parms", "tderiv"), sys, envir=environment())
  
  initScipen <- getOption("scipen")
  options(scipen=999) #avoid scientific notation, that ca cause issues with the different conversions from R to cpp
  
  #Use double not Float in R, for accuracy
  sys$strFunc <- gsub("float", "double", sys$strFunc)
  strEventTime <- ifelse(is.null(eventTime), "", makeEventTime(sys))
  strEventVar <- ifelse(is.null(eventVar), "", makeEventVar(sys))
  if (reportVars==0) {
    strReportingVars <- c("", "")
  } else {
    strReportingVars <- makeReportingVariables(sys)
  }
  
  #Load Raw Cpp Code, add dim and options definitions and save
  cppCode <- readChar("RawCppCodeRK4.cpp", file.info("RawCppCodeRK4.cpp")$size)
  cppCode <- sub("@AddDim", as.character(sys$dim), cppCode)
  cppCode <- sub("@AddDimIv", as.character(length(sys$intermediateVar)), cppCode)
  cppCode <- sub("@AddDimOut", ifelse(sys$reportVars==3,
                                      as.character(2*sys$dim+length(sys$intermediateVar)),
                                      ifelse(sys$reportVars==2,
                                             as.character(2*sys$dim),
                                             ifelse(sys$reportVars==1,
                                                    as.character(sys$dim+length(sys$intermediateVar)),
                                                    as.character(sys$dim)))), cppCode)
  cppCode <- gsub("@AddFunc", sys$strFunc, cppCode)
  cppCode <- gsub("@AddEventTime", strEventTime, cppCode)
  cppCode <- gsub("@AddEventVar", strEventVar, cppCode)
  cppCode <- gsub("@AddReportingVarsInit", strReportingVars[2], cppCode)
  cppCode <- gsub("@AddReportingVars", strReportingVars[1], cppCode)
  
  # Final formatting
  cppCode <- gsub("intToFloat", ".0", cppCode) #double not float
  cppCode <- gsub("doubleToFloat", "", cppCode) #double not float
  cppCode <- gsub("somethingToRemoveLater", "", cppCode)
  cppCode <- gsub("thisIsAnInt", "", cppCode)
  cppCode <- gsub(", MakeThisAndCommaAnInterrogationMark,", " ? ", cppCode)
  cppCode <- gsub(", MakeThisAndCommaAColon,", " : ", cppCode)
  cppCode <- gsub("makeThisAnSTDAndDoubleColon", "std::", cppCode)
  
  writeChar(object=cppCode, "CppCodeRK4.cpp", nchars=nchar(cppCode), eos=NULL)
  
  # Sys.setenv(PKG_LIBS = "-lOpenCL")
  sourceCpp("CppCodeRK4.cpp")
  options(scipen=initScipen)
}

################################################################
##                           Internal function                ##
## Create str for the variables to be reported as output      ##
################################################################
makeReportingVariables <- function(sys=NULL, strFunc=sys$strFunc, eventVar=sys$eventVar, 
                                   parmsNames=names(sys$parms), yNames = names(sys$tderiv), reportVars=sys$reportVars) {
  if(reportVars==3){
    out <- c("for(it1=0;it1<dim;it1++){
							out(it+1, dim+it1) = ydots[it1];
						}
						for(it1=0;it1<dimIv;it1++){
							out(it+1, 2*dim+it1) = (x0[it1] + 2.0*x1[it1] + 2.0*x2[it1] + x3[it1])/6.0;
						}",
             "Func(0, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar); 
						for (it1=0; it1<dim; it1++) {
							out(0, dim+it1) = ydot0[it1];
						}
						for (it1=0; it1<dimIv; it1++) {
							out(0, 2*dim+it1) = x0[it1];
						}
						 ")
  }else if(reportVars==2){
    out <- c("for(it1=0;it1<dim;it1++){
							out(it+1, dim+it1) = ydots[it1];
						}", 
             "Func(0, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar); 
						for (it1=0; it1<dim; it1++) {
							out(0, dim+it1) = ydot0[it1];
						}")
  }else if(reportVars==1){
    out <- c("for(it1=0;it1<dimIv;it1++){
							out(it+1, dim+it1) = (x0[it1] + 2.0*x1[it1] + 2.0*x2[it1] + x3[it1])/6.0;
						}",
             "Func(0, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar); 
						for (it1=0; it1<dimIv; it1++) {
							out(0, dim+it1) = x0[it1];
						}")
  }
  out
}

################################################
## Run RK4 for the previously compiled system ##
################################################
cppRK4 <- function(sys=NULL, times=NULL, parms=NULL, y0=NULL, eventTime=NULL, eventVar=NULL, 
                   dataExogVar = NULL, exogSamplingTime=NULL) {
  if(is.null(sys)) sys <- list()
  if(!is.null(sys$dataExogVar) && !is.null(dataExogVar)) dataExogVar <- dataExogVar[names(sys$dataExogVar)]
  if(is.null(sys$reportVars)) stop("sys$reportVars not defined, use cppMakeSys or cppMakeMinDist to define sys before calling cppRK4")
  sys <- completeSys(c("parms", "times", "y0", "eventTime", "dataExogVar", "exogSamplingTime"), sys, envir=environment())
  if (is.null(sys$dataExogVar)) sys$dataExogVar <- list()
  if (is.null(sys$exogSamplingTime)) sys$exogSamplingTime <- list()
  sys$exogSamplingTime <- lapply(sys$exogSamplingTime, function(x) c(x, +Inf))
  missingArguments(c("parms", "times", "y0", "reportVars"), sys, envir=environment())
  sys$nT <- length(sys$times)
  sys$byT <- sys$times[2] - sys$times[1]
  if(!exists("RK4"))
    stop("No Compiled C++ code found. Use the function cppMakeSys with the argument compile=TRUE to compile.")
  solution = RK4(sys$nT, sys$byT, sys$y0, sys$parms,matrix(as.double(unlist(eventTime,recursive=T)),ncol=2, byrow=T)[,2], sys$dataExogVar, sys$exogSamplingTime)
  solution = cbind(sys$times,solution)
  if(sys$reportVars==3)
    colnames(solution) <- c("time", names(sys$tderiv), paste0(names(sys$tderiv),"Dot"), names(sys$intermediateVar))
  else if(sys$reportVars==2)
    colnames(solution) <- c("time", names(sys$tderiv), paste0(names(sys$tderiv),"Dot"))
  else if(sys$reportVars==1)
    colnames(solution) <- c("time", names(sys$tderiv), names(sys$intermediateVar))
  else 
    colnames(solution) <- c("time",names(sys$tderiv))
  solution <- as.data.frame(solution) # That's considered as a (very) bad coding practice to change the nature of the output of a function written by someone else (here convert a matrix into a data.frame).
  return(solution)
}

##########################################################################
##                           Internal function                          ##
## Create str for the events triggered by a condition on time           ##
##########################################################################
makeEventTime <- function(sys=NULL, eventTime=sys$eventTime,
                          parmsNames=names(sys$parms), yNames = names(sys$tderiv), ivNames=names(sys$intermediateVar)) {
  
  allNames <- c("eventTime", "parmsNames", "yNames")
  missingArguments(allNames, envir=environment())
  
  out <- ""
  for (i in 1:length(eventTime)) {
    newEventTime <- paste0("if(it*byT>=",
                           as.character(eventTime[[i]][[1]]),
                           " && it*byT - ", 
                           as.character(eventTime[[i]][[1]]), "<byT) { \n")
    for (j in 2:length(eventTime[[i]])) {
      
      newEventTime <- paste0(newEventTime,#"std:: cout << RparmsEvent[0];\n",
                             paste0(
        deparse(funcFormatEquation(Eq=parse(text=names(eventTime[[i]])[j])[[1]],
                                            parmsNames=parmsNames,
                                            yNames=yNames,ivNames=ivNames))
        ,"=RparmsEvent[",i-1,"]; \n"))
    }
    out <- paste0(out, newEventTime, "} \n")
  }
  out
}

changeParameters<-function(sys,to.change){
  pars = sys$parms
  for(i in 1:length(to.change))
    pars[which(names(pars)==names(to.change)[i])]=as.numeric(to.change[i])
  return(pars)
}

#############################################################
## Create the Cpp function from tderiv and intermediateVar ##
## And compile (if compile==TRUE) the cpp code for RK4     ##
#############################################################
cppMakeSSSys <- function(fileName=NULL, tderiv=NULL, parms=NULL, intermediateVar=NULL, compile=TRUE) {
  if (!is.null(fileName)) {
    sys <- loadSSModel(fileName)
  }
  sys <- completeSys(c("tderiv", "parms", "intermediateVar"), 
                     sys, envir=environment())
  missingArguments(c("tderiv", "parms"), sys,envir=environment())
  initScipen <- getOption("scipen")
  options(scipen=999) #avoid scientific notation, that can cause issues with the different conversions from R to cpp
  #Initialization
  sys$dim <- length(sys$tderiv)
  
  #Define strings for the cpp function and the options to pass to the openCL Kernel
  allEquations <- unloopEquations(sys$tderiv, sys$intermediateVar)
  sys$strFunc <- makeCppFuncSS(allEquations, sys$parms,sys$tderiv,sys$intermediateVar)
  if (compile==TRUE)
    cppCompileSS(NULL, sys$dim, sys$strFunc, sys$parms, sys$tderiv, sys$intermediateVar)
  options(scipen=initScipen)
  sys
}

###########################################################################
##                           Internal function (Is it really?)           ##
## Load the model from an external file and create an object sys with it ##
###########################################################################
loadSSModel <- function(fileName) {
  options(warn=-1)
  modelFile <- file(fileName)
  modelText <- readLines(modelFile, n = -1)
  close(modelFile)
  firstEquation=TRUE
  equations = NULL
  out <- list()
  #Intermediate Variables
  beginIntermediateVar <- which(grepl("##intermediate variables", modelText))[1]
  if (!is.na(beginIntermediateVar)) {
    endIntermediateVar <- min(which(regexpr("##", modelText[-(1:beginIntermediateVar)])==1)) # search next row beginning by a "#"
    
    if (length(endIntermediateVar)>0 && endIntermediateVar-beginIntermediateVar>1) {
      intermediateVarText <- modelText[beginIntermediateVar:(endIntermediateVar)]
      out$intermediateVar <- createEquations(intermediateVarText)
    }
  }
  
  #times derivatives
  beginTderiv <- which(grepl("##time derivatives", modelText))[1]
  if (is.na(beginTderiv)) {
    stop("Missing time derivatives")
  }
  endTderiv <- min(c(which(regexpr("##", modelText[-(1:beginTderiv)])==1), length(modelText)-beginTderiv+1)) # search next row beginning by a "#"
  if (length(endTderiv)!=0 && endTderiv>1) {
    tderivText <- modelText[beginTderiv+1:(endTderiv-1)]
    out$tderiv <- createEquations(tderivText)
  } else {
    stop("Missing time derivatives")
  }
  
  #Parameters
  beginParms <- which(grepl("##parameters", modelText))[1]
  if(!is.na(beginParms)) {
    endParms <- min(c(which(regexpr("##", modelText[-(1:beginParms)])==1), length(modelText)-beginParms+1)) # search next row beginning by a "#"
    if (length(endParms)!=0 && endParms>1) {
      parmsText <- modelText[beginParms+1:(endParms-1)]
      out$parms <- sapply(createEquations(parmsText), function(x) eval(parse(text=x)))
      sapply(1:length(out$parms), function(i) eval(call("=", names(out$parms)[i], out$parms[i]), envir=parent.env(environment())))
    }
  }
  
  options(warn=0)
  out
}

##################################################
##            Internal function                 ##
## Create str for the cpp function of the model ##
##################################################
makeCppFuncSS <- function(allEquations,parms, tderiv,ivvars) { # Create the cpp function defining differential equations for the kernel
  
  # init the string with inputs
  strCppFunc <- ''
  # (Pre)Format the equations
  allEquations <- sapply(allEquations,
                         function(x) {
                           funcFormatEquation(Eq=parse(text=x)[[1]], parmsNames=names(parms), yNames=names(tderiv),ivNames = names(ivvars))
                         }
  )
  # Include the equations to the str
  for(i in 1:length(allEquations)) {     # add one line with "varName = varExpression"
    if(any(paste0(names(tderiv), "Dot")==names(allEquations[i]))==TRUE) { # if it is a time derivative
      indiceVar <- which(paste0(names(tderiv), "Dot")==names(allEquations[i]))
      strCppFunc <- paste(strCppFunc, 
                          paste0(paste0("ydot[", indiceVar-1, "]"),
                                 ' = ', 
                                 allEquations[i], 
                                 ';'),
                          sep="\n")
    } else { # If it is an intermediate variable
      indiceVar <- which(names(ivvars)==names(allEquations[i]))
      strCppFunc <- paste(strCppFunc, 
                          paste0(paste0("x[", indiceVar-1, "]"),
                                 ' = ', 
                                 allEquations[i], 
                                 ';'),
                          sep="\n")
    }
  }
  strCppFunc
}

#################################
##      internal function      ##
## Compile the code for RK4    ##
#################################
cppCompileSS <- function(sys=NULL, dim=sys$dim, strFunc=sys$strFunc, parms=sys$parms, tderiv=sys$tderiv, intermediateVars=sys$intermediateVars) {
  
  if (is.null(sys))
    sys <-list()
  
  sys <- completeSys(c("dim", "strFunc", "parms", "tderiv", "intermediateVars"), sys, envir=environment())
  missingArguments(c("dim", "strFunc", "parms", "tderiv"), sys, envir=environment())
  
  initScipen <- getOption("scipen")
  options(scipen=999) #avoid scientific notation, that ca cause issues with the different conversions from R to cpp
  
  #Use double not Float in R, for accuracy
  sys$strFunc <- gsub("float", "double", sys$strFunc)
  
  #Load Raw Cpp Code, add dim and options definitions and save
  cppCode <- readChar("RawCppCodeSS.cpp", file.info("RawCppCodeSS.cpp")$size)
  cppCode <- sub("@AddDim", as.character(sys$dim), cppCode)
  cppCode <- sub("@AddDimIv", as.character(length(sys$intermediateVar)), cppCode)
  cppCode <- sub("@AddSys", sys$strFunc, cppCode)
  
  # Final formatting
  cppCode <- gsub("intToFloat", ".0", cppCode) #double not float
  cppCode <- gsub("doubleToFloat", "", cppCode) #double not float
  cppCode <- gsub("somethingToRemoveLater", "", cppCode)
  cppCode <- gsub(", MakeThisAndCommaAnInterrogationMark,", " ? ", cppCode)
  cppCode <- gsub(", MakeThisAndCommaAColon,", " : ", cppCode)
  cppCode <- gsub("makeThisAnSTDAndDoubleColon", "std::", cppCode)
  
  writeChar(object=cppCode, "CppCodeSS.cpp", nchars=nchar(cppCode), eos=NULL)
  
  # Sys.setenv(PKG_LIBS = "-lOpenCL")
  sourceCpp("CppCodeSS.cpp")
  options(scipen=initScipen)
}


################################################
## Run RK4 for the previously compiled system ##
################################################
cppSSmultiroot <- function(sys=NULL, parms=NULL, start=NULL,positive=F) {
  if(is.null(sys))
    sys <- list()
  sys <- completeSys(c("parms" ), sys, envir=environment())
  missingArguments(c("parms"), sys, envir=environment())
  if(!exists("SS"))
    stop("No Compiled C++ code found. Use the function cppMakeSSSys with the argument compile=TRUE to compile.")
  
  demand<-function(y){
    SS(parms,y)
  }
  solution = multiroot(f = demand, start = start,positive = positive)
  
  return(solution)
}

