#include <iostream>
#include <fstream>
#include<math.h>
#include <Rcpp.h>
using namespace Rcpp; 

#define dim @AddDim
#define dimIv @AddDimIv
#define dimOut @AddDimOut

//Note: All pieces of code beginning with a @ will be replaced by the required code by R before compiling
//For instance @AddDim will be replaced by the dimension of the model

// utility function that converts a Rcpp::List to a double**
// WARNING: do not forget to free the double** after use!
template<typename T>
void RcppListToPptr(Rcpp::List L, T**& pptr) {
	for (unsigned int it=0; it<L.size(); it++) {
		std::vector<double> tempVec = L[it];
		pptr[it] = (double*) malloc(sizeof(*pptr[it]) * tempVec.size());
		for (unsigned int it2=0; it2<tempVec.size(); it2++) {
			pptr[it][it2] = tempVec[it2];
		}
	}
}

@AddFunc
	
Rcpp::NumericMatrix RK4(int nt, 
                      double byT,
                      std::vector<double> Ry0,
                      std::vector<double> Rparms, 
                      double** dataExogVar,
                      double** exogSamplingTime, 
                      int nExogVar) {
	int it, it1;
	double *y = &Ry0[0];
	double *parms = &Rparms[0];
	double y1[dim], y2[dim], y3[dim], ydot0[dim], ydot1[dim], ydot2[dim], ydot3[dim], ydots[dim], x0[dimIv], x1[dimIv], x2[dimIv], x3[dimIv];
	Rcpp::NumericMatrix out(nt, dimOut);

	for (it=0; it<dim;it++) { //init out vector
		out(0, it)=y[it];
	}
	int comptExogVar[nExogVar];
	for (it=0; it<nExogVar; it++) comptExogVar[it]=1;

	// get intermediateVar and compute distance at t=0 //
	@AddReportingVarsInit
	
	for (it=0; it<nExogVar; it++) comptExogVar[it]=1;
	
	for (it=0; it<(nt-1); it++) {

			@AddEventTime
			@AddEventVar

			Func(it*byT, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);

			for (it1=0; it1<dim; it1++)
				y1[it1] = y[it1] + ydot0[it1]*0.5*byT;
			Func((it + 0.5)*byT, y1, parms, ydot1, x1, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			for (it1=0; it1<dim; it1++)
				y2[it1] = y[it1] + ydot1[it1]*0.5*byT;
			Func((it + 0.5)*byT, y2, parms, ydot2, x2, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			for (it1=0; it1<dim; it1++)
				y3[it1] = y[it1] + ydot2[it1]*byT;
			Func((it+1)*byT, y3, parms, ydot3, x3, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			for (it1=0; it1<dim; it1++) {
				ydots[it1] = (ydot0[it1] + 2.0*ydot1[it1] + 2.0*ydot2[it1] + ydot3[it1])/6.0;
			  out(it+1, it1) = y[it1];
				y[it1] = y[it1] + byT*ydots[it1];
				
			}
			
			@AddReportingVars
				
	}
	return out;
}

// [[Rcpp::export]]
Rcpp::NumericMatrix RK4(int nt, 
                        double byT,
                        std::vector<double> Ry0,
                        std::vector<double> Rparms, 
                        Rcpp::List RdataExogVar,
                        Rcpp::List RexogSamplingTime) {
	double** dataExogVar = (double**) malloc(sizeof(double*)*RdataExogVar.size());
	RcppListToPptr(RdataExogVar, dataExogVar);
	double** exogSamplingTime = (double**) malloc(sizeof(double*)*RexogSamplingTime.size());
	RcppListToPptr(RexogSamplingTime, exogSamplingTime);
	int nExogVar = RdataExogVar.size();
	Rcpp::NumericMatrix out = RK4(nt, byT, Ry0, Rparms, dataExogVar, exogSamplingTime, nExogVar);
	for (unsigned int it=0; it<RdataExogVar.size(); it++) {
		free(dataExogVar[it]);
		free(exogSamplingTime[it]);
	}
	free(dataExogVar);
	free(exogSamplingTime);
	
	return out;
}
