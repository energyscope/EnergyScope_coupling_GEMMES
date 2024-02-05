# tderivNamesOrdered <- namesordered[namesordered %in% paste(names(SOEM$tderiv),"Dot",sep="")]
y <- SOEM$y0
y <- c(y[-1],y[1])
y0<-y

parms <- SOEM$parms
parms <- c(parms[-1],parms[1])
ydot<- rep(NA,length(y))
x <- rep(NA,length(SOEM$intermediateVar))

source("script.R")
y1<-y0+ydot*0.5*0.1
ydot0<-ydot

y<-y1
ydot<- rep(NA,length(y))
x <- rep(NA,length(SOEM$intermediateVar))
source("script.R")
y2<-y0+ydot*0.5*0.1
ydot1<-ydot

y<-y2
ydot<- rep(NA,length(y))
x <- rep(NA,length(SOEM$intermediateVar))
source("script.R")
y3<-y0+ydot*0.1
ydot2<-ydot


y<-y3
ydot<- rep(NA,length(y))
x <- rep(NA,length(SOEM$intermediateVar))
source("script.R")
ydot3<-ydot

ydotfin<-(ydot0 + 2.0*ydot1 + 2.0*ydot2 + ydot3)/6.0