generate.valueMatrix<-function(ds,matrix,pars,time){
  
  # ds=data_col.ts
  # matrix=SAM
  # year=2010
  
  results=matrix(NA,nrow=nrow(matrix),ncol=ncol(matrix),dimnames = dimnames(matrix))
  period=which(ds$time==time)
  attach(ds[period,])
  attach(pars)
  for(r in 1:nrow(matrix)){
    for(c in 1:ncol(matrix)){
      cellVal<-as.character(matrix[r,c])
      if(nchar(cellVal)>0){
        #If there's an entry in the cell
        eq<-eval(parse(text=cellVal))
        results[r,c]=eq
      }
    }
  }
  detach(pars)
  detach(ds[period,])
  return(results)
}

growth<-function(var){
  return(100*(var[-1]/var[-length(var)]-1))
}


mymatplot<-function(dataset,varnames,main=NULL,location="topleft",varLegend=NULL){
  if(is.null(varLegend))
    varLegend<-varnames
  if(is.null(main))
    varLegend<-""
  dstemp=sapply(varnames,function(x) return(eval(parse(text=x),envir=dataset)))
  matplot(dataset$time[1:nrow(dstemp)],dstemp, main=main ,type="l", ylab="", xlab="", lwd=2)
  if(is.numeric(varLegend)){
     if(varLegend!=-1)
        legend(location,legend=varLegend,lty=1:length(varnames),lwd=2,col=1:length(varnames),bty='n')
  }else
    legend(location,legend=varLegend,lty=1:length(varnames),lwd=2,col=1:length(varnames),bty='n')
}

mymatplotcompare<-function(datasets,varnames,main,position=NULL){
  dstemp=sapply(varnames,function(x) return(eval(parse(text=x),envir=datasets[[1]])))
  ltys=rep(1,length(varnames))
  namesScen<-names(datasets)
  if(length(datasets)>1){
    for(i in 2:length(datasets)){
      dstemp=cbind(dstemp,sapply(varnames,function(x) return(eval(parse(text=x),envir=datasets[[i]]))))
      ltys=c(ltys,rep(i,length(varnames)))
    }
  }
  tmp<-datasets[[1]]
  matplot(tmp$time[1:nrow(dstemp)],dstemp, main=main ,type="l", ylab="", xlab="", lwd=2,col=ltys,lty=ltys)
  if(is.null(position))
    position="topleft"
  if(position!=-1)
  legend(position,legend=c(namesScen),lty=ltys,lwd=2,col=c(seq(1,length(namesScen))),bty='y')
}

