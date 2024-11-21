// cppimport
#include <pybind11/pybind11.h>

namespace py = pybind11;

#include <pybind11/stl.h>
#define UseRCPP 2 		// true if the code is called from R(via RCPP), false if it is directly called from c++


#include <iostream>
#include <fstream>
#include <math.h>
#include <stdio.h>
#include <string.h>

#define ARMA_WARN_LEVEL 1
#include <armadillo>

#include "src/preprocRCPP_R.h"
//#include "src/exogenousVariables.h"
#include "src/solverModelR.h"

namespace py = pybind11;

using namespace std;

int getNt() {
	return ntForPython;
}

double getTInit() {
	return TInitForPython;
}

double getTEnd() {
	return TEndForPython;
}
int getNV() {
	return NVForPython;
}

int getNIV() {
	return NIVForPython;
}


std::vector<std::string> getParmsNames() {
	std::vector<std::string> out = ParmsNamesForPython;
	return out;
}

std::vector<std::string> getVarNames() {
	std::vector<std::string> out = VarNamesForPython;
	return out;
}

std::vector<std::string> getIntermediateVarNames() {
	std::vector<std::string> out = IntermediateVarNamesForPython;
	return out;
}

std::vector<double> getParms() {
	std::vector<double> out = ParmsForPython;
	return out;
}

std::vector<double> getYInit() {
	std::vector<double> out = YInitForPython;
	return out;
}

std::vector<double> getSamplesExogVar() {
	std::vector<double> out = SamplesExogVarForPython ;
	return out;
}

std::vector<int> getNSamplesVarExogVar() {
	std::vector<int> out = NSamplesVarExogVarForPython;
	return out;
}

int getNVarExogVar() {
	int out = NVarExogVarForPython;
	return out;
}

int getReturnType() {
	int out = ReturnRK4;
	return out;
}

std::vector<double>   eulerPy(int nt,
			      double tInit, 
			      double tEnd, 
			      int nV,
			      int nIV,
		              vector<double> y0R,
		              vector<double> parmsR, 
		              vector<double> samplesExogVarR,   
		              vector<int> nSamplesVarExogVarR,
		              int nVarExogVar) {
	// Convert vector to ptrs
	double* y0 = &y0R[0];
	double* parms = &parmsR[0];
	double* samplesExogVar = &samplesExogVarR[0];
	int* nSamplesVarExogVar = &nSamplesVarExogVarR[0];
	
	exogVarCubicSplinePeriodic2<double> myExogVar(tInit, tEnd, samplesExogVar, nVarExogVar, nSamplesVarExogVar);

	modelREuler<double> model(nV, nIV, tInit, tEnd, nt, &myExogVar);
	vector<double> outR(model.getNRowOutSolve());
	double* out = &outR[0];
	model.solve(y0, parms, out);
	return outR;
}

std::vector<double>   RK4FixedPy(int nt,
			         double tInit, 
			         double tEnd, 
			         int nV,
			         int nIV,
		                 vector<double> y0R,
		                 vector<double> parmsR, 
		                 vector<double> samplesExogVarR,   
		                 vector<int> nSamplesVarExogVarR,
		                 int nVarExogVar) {
	// Convert vector to ptrs
	double* y0 = &y0R[0];
	double* parms = &parmsR[0];
	double* samplesExogVar = &samplesExogVarR[0];
	int* nSamplesVarExogVar = &nSamplesVarExogVarR[0];
	
	exogVarCubicSplinePeriodic2<double> myExogVar(tInit, tEnd, samplesExogVar, nVarExogVar, nSamplesVarExogVar);

	modelRRK4<double> model(nV, nIV, tInit, tEnd, nt, &myExogVar);
	vector<double> outR(model.getNRowOutSolve());
	double* out = &outR[0];
	model.solve(y0, parms, out);
	return outR;
}

std::vector<double>   dopriPy(int nt,
			      double tInit, 
			      double tEnd, 
			      int nV,
			      int nIV,
		              vector<double> y0R,
		              vector<double> parmsR, 
		              vector<double> samplesExogVarR,   
		              vector<int> nSamplesVarExogVarR,
		              int nVarExogVar, 
			      double atol,
			      double rtol, 
			      double fac,
			      double facMin, 
			      double facMax,
			      double nStepMax,
			      double hInit, 
			      double hMin, 
			      double hMax) {
	// Convert vector to ptrs
	double* y0 = &y0R[0];
	double* parms = &parmsR[0];
	double* samplesExogVar = &samplesExogVarR[0];
	int* nSamplesVarExogVar = &nSamplesVarExogVarR[0];
	
	exogVarCubicSplinePeriodic2<double> myExogVar(tInit, tEnd, samplesExogVar, nVarExogVar, nSamplesVarExogVar);

	modelRDopri<double> model(nV, nIV, tInit, tEnd, nt, atol, rtol, fac, facMin, facMax, nStepMax, hInit, hMin, hMax, &myExogVar);
	vector<double> outR(model.getNRowOutSolve());
	double* out = &outR[0];
	model.solve(y0, parms, out);
	return outR;
}


PYBIND11_MODULE(functionsForPy, m) {
    m.def("euler", &eulerPy);
    m.def("RK4Fixed", &RK4FixedPy);
    m.def("dopri", &dopriPy);
    m.def("nt", &getNt);
    m.def("tInit", &getTInit);
    m.def("tEnd", &getTEnd);
    m.def("nV", &getNV);
    m.def("nIV", &getNIV);
    m.def("parmsNames", &getParmsNames);
    m.def("varNames", &getVarNames);
    m.def("intermediateVarNames", &getIntermediateVarNames);
    m.def("parms", &getParms);
    m.def("yInit", &getYInit);
    m.def("samplesExogVar", &getSamplesExogVar);
    m.def("nSamplesVarExogVar", &getNSamplesVarExogVar);
    m.def("nVarExogVar", &getNVarExogVar);
    m.def("returnType", &getReturnType);
}
/*
<%
cfg['extra_compile_args'] = ['-std=c++14', '-larmadillo']
cfg['libraries'] = ['armadillo']
cfg['dependencies'] = ['src/preprocRCPP_R.h', 'src/exogenousVariables.h', 'src/solverModelR.h', 'src/ODE.h', 'src/modelR.h', 'src/euler.h', 'src/RK4Fixed.h', 'src/dopri.h']
setup_pybind11(cfg)
%>
*/

