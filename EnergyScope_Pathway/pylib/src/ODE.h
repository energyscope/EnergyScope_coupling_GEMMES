#ifndef ODE_h
#define ODE_h

#include <iostream>
#include <fstream>
#include <math.h>
#include <cstring>
#include <stdio.h>
#include <string.h>

#if UseRCPP==1
        #include "preprocRCPP_R.h"
#else
        #include "preproc.h"    
#endif
#include "exogenousVariables.h"

using namespace std;

template<typename T>
class ODE {
public:
	//Constructor
	ODE(const int nVIn, const int nIVIn, T tInitIn, T tEndIn, int ntIn) : 
			nV(nVIn), nIV(nIVIn),
			tInit(tInitIn), tEnd(tEndIn), nt(ntIn), hOut((tEndIn-tInitIn)/(ntIn-1.0)), nRowOutSolve(getNRowOut()*ntIn) {}
	//VIRTUAL DESTRUCTOR
	virtual ~ODE() {}

	//Virtual functions
	virtual void solve(const T* y, T* parms, T* out) = 0;
	virtual void solveLastPoint(const T* y, T* parms, T* out) = 0;
	virtual void Func(const T t, const T* y, const T* parms, T* ydot, T* x) = 0;
	
	
	// Non virtual function to get model characteristics
	int getNRowOut() {
		#if ReturnRK4==0
			return nV;
		#elif ReturnRK4==1
			return 2*nV;
		#elif ReturnRK4==2
			return nV+nIV;
		#elif ReturnRK4==3
			return 2*nV+nIV;
		#endif
	}
	int getNV() {return nV;}
	int getNIV() {return nIV;}
	T getTInit() {return tInit;}
	T getTEnd() {return tEnd;}
	T getHOut() {return hOut;}
	int getNt() {return nt;}
	int getNRowOutSolve() {return nRowOutSolve;}
	void changeNt(int newNt) {nt = newNt;}
	void changeTInit(T newTInit) {tInit=newTInit;}
	void changeTEnd(T newTEnd) {tEnd=newTEnd;}
protected:
	virtual void makeEventTime(const T t, T* parms, T* y, T* x, T h) = 0; 
	virtual void makeEventVar(const T t, T* parms, T* y, T* x, T h) = 0; 
	void completeOut(T* ydot, T* x, T* out) {
		int it1;
		#if ReturnRK4==1
			for(it1=0;it1<nV;it1++){
				out[nV+it1] = ydot[it1];
			}
		#elif ReturnRK4==2
			for(it1=0;it1<nIV;it1++){
				out[nV+it1] = x[it1];
			}
		#elif ReturnRK4==3
			for(it1=0;it1<nV;it1++){
				out[nV+it1] = ydot[it1];
			}
			for(it1=0;it1<nIV;it1++){
				out[2*nV+it1] = x[it1];
			}
		#endif	
	}

	virtual T getExogVar(T t, int i) {return 0;}
	const int nV;
	const int nIV;
	T tInit;
	T tEnd;
	int nt;
	T hOut;
	int nRowOutSolve;
};




#endif
