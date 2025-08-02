#ifndef EULER_h
#define EULER_h


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
class Euler: virtual public ODE<T> {
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
		double t=getTInit();
		T yDot[getNV()];
		T x[getNIV()];
		for (int it=0; it<getNV(); it++) out[it] = yInit[it]; 
		//Main Loop
		for (int it=1; it<getNt(); it++) {
			// Run events (if needed)
			#if UseEventTime
				makeEventTime(t, parms, &out[(it-1)*getNRowOut()], x, getHOut());
			#endif
			#if UseEventVar
				makeEventVar(t, parms, &out[(it-1)*getNRowOut()], x, getHOut());
			#endif

			// Use Euler's method to estimate y at t+h
			EulerOneStep(t, &out[(it-1)*getNRowOut()], parms, yDot, x, &out[it*getNRowOut()]);
			// complete output with ydot and x at t
			completeOut(yDot, x, &out[(it-1)*getNRowOut()]); // THIS IS NOT A TYPO: "(it-1)" is what we want here (because ydot and x are computed at t and not at t+h)
			t+=getHOut(); //increment time
			}
		// Complete out at last point
		Func(t, &out[(getNt()-1)*getNRowOut()], parms, yDot, x); //Run Func to estimate yDot and x at t=tEnd
		completeOut(yDot, x, &out[(getNt()-1)*getNRowOut()]);
		}	
	


	// Same as solve, but only returns last point of trajectory
	void solveLastPoint(const T* yInit, T* parms, T* out) override {
		//Init
		double t=getTInit();
		T yDot[getNV()];
		T x[getNIV()];
		T y[getNV()];
		for (int it=0; it<getNV(); it++) y[it] = yInit[it]; 
		// Main Loop
		for (int it=1; it<getNt(); it++) {
			// Run events (if needed)
			#if UseEventTime
				makeEventTime(t, parms, y, x, getHOut());
			#endif
			#if UseEventVar
				makeEventVar(t, parms, y, x, getHOut());
			#endif
				// Use Euler's method to estimate y at t+h
			EulerOneStep(t, y, parms, yDot, x, y); // y appears twice as an argument (one tells EulerOneStep where to take initial estimate of y and the other where to write the new value of y) because we do not need to store the full trajectory here.
			t+=getHOut(); //increment time
		}
		// Complete out at last point

		// Complete out at last point
		for (int it=0; it<getNV(); it++) out[it] = y[it];
		Func(t, y, parms, yDot, x); //Run Func to estimate yDot and x at t=tEnd
		completeOut(yDot, x, out);
	}	
protected:
	void EulerOneStep(const T t, const T* y, const T* parms, T* yDot, T* x, T* out) {
		Func(t, y, parms, yDot, x);
		for (int it=0; it<getNV(); it++) {
			out[it] = y[it] + getHOut()*yDot[it];
		}
	}

};


#endif
