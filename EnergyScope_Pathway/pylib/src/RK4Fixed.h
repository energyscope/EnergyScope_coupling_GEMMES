#ifndef RK4Fixed_h
#define RK4Fixed_h


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
#include "ODE.h"

using namespace std;

template<typename T>
class RK4Fixed: virtual public ODE<T> {
	using ODE<T>::Func;
	using ODE<T>::makeEventVar;
	using ODE<T>::makeEventTime;
	using ODE<T>::completeOut;
	using ODE<T>::getNV;
	using ODE<T>::getNIV;
	using ODE<T>::getNt;
	using ODE<T>::getNRowOut;
	using ODE<T>::getTInit;
	using ODE<T>::getTEnd;
	using ODE<T>::getHOut;
public:	

	// Main solver, overrides the virtual one from base ODE class
	void solve(const T* yInit, T* parms, T* out) override {
		//Init
		int nV = getNV();
		int nIV = getNIV();
		int nt = getNt();
		double t=getTInit();
		int nRowOut = getNRowOut();
		T k1[nV], k2[nV], k3[nV], k4[nV];
		T x[nIV];
		for (int it=0; it<nV; it++) out[it] = yInit[it]; 
		//Main Loop
		for (int it=1; it<nt; it++) {
			// Run events (if needed)
			#if UseEventTime
				makeEventTime(t, parms, &out[(it-1)*getNRowOut()], x, getHOut());
			#endif
			#if UseEventVar
				makeEventVar(t, parms, &out[(it-1)*getNRowOut()], x, getHOut());
			#endif

			// Use RK4 to estimate y at t+h
			RK4OneStep(t, &out[(it-1)*nRowOut], parms, k1, k2, k3, k4, x, &out[it*nRowOut]);
			// complete output with ydot and x at t
			completeOut(k1, x, &out[(it-1)*nRowOut]); // THIS IS NOT A TYPO: "(it-1)" is what we want here (because ydot and x are computed at t and not at t+h)
			t+=getHOut(); //increment time
			}
		// Complete out at last point
		Func(t, &out[(nt-1)*nRowOut], parms, k1, x);
		completeOut(k1, x, &out[(nt-1)*nRowOut]);
		}	
	


	// Same as solve, but only returns last point of trajectory
	void solveLastPoint(const T* yInit, T* parms, T* out) override {
		//Init
		int nV = getNV();
		int nIV = getNIV();
		int nt = getNt();
		double t=getTInit();
		T k1[nV], k2[nV], k3[nV], k4[nV];
		T x[nIV];
		T yIn[nV], yOut[nV];
		for (int it=0; it<nV; it++) yIn[it] = yInit[it]; 
		//Main Loop
		for (int it=1; it<nt; it++) {
			// Run events (if needed)
			#if UseEventTime
				makeEventTime(t, parms, yIn, x, getHOut());
			#endif
			#if UseEventVar
				makeEventVar(t, parms, yIn, x, getHOut());
			#endif
				// Use RK4 to estimate y at t+h
			RK4OneStep(t, yIn, parms, k1, k2, k3, k4, x, yOut);
			for (int it=0; it<getNV(); it++) yIn[it] = yOut[it]; // update yIn for next step
			t+=getHOut(); //increment time
		}
		// Complete out at last point
		for (int it=0; it<nV; it++) out[it] = yOut[it];
		Func(t, yOut, parms, k1, x);
		completeOut(k1, x, out);
	}	
protected:
	void RK4OneStep(const T t, const T* y, const T* parms, T* k1, T* k2, T* k3, T* k4, T* x, T* out) {
		T xTrash[getNIV()];
		Func(t, y, parms, k1, x);
		for (int it=0; it<getNV(); it++) out[it] = y[it] + a21*getHOut()*k1[it];
		Func(t+c2*getHOut(), out, parms, k2, xTrash);
		for (int it=0; it<getNV(); it++) out[it] = y[it] + a32*getHOut()*k2[it];
		Func(t+c3*getHOut(), out, parms, k3, xTrash);
		for (int it=0; it<getNV(); it++) out[it] = y[it] + a43*getHOut()*k3[it];
		Func(t+c4*getHOut(), out, parms, k4, xTrash);
		for (int it=0; it<getNV(); it++) out[it] = y[it] + getHOut()*(b1*k1[it] + b2*k2[it] + b3*k3[it] + b4*k4[it]);
	}

	// parameters for RK
	// In practice, terms including parameters set to zero are removed from code above for performances,
	// but the parameters are explicitely defined here for clarity.
	const T c2 = 0.5;
	const T c3 = 0.5;
	const T c4 = 1.0;
	const T a21 = 0.5;
        const T a31 = 0.0;
	const T a32 = 0.5;
	const T a41 = 0.0;
	const T a42 = 0.0;
	const T a43 = 1.0;
	const T b1 = 1.0/6.0;
	const T b2 = 1.0/3.0;
	const T b3 = 1.0/3.0;
	const T b4 = 1.0/6.0;
};


#endif
