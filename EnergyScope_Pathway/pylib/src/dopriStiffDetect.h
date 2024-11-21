#ifndef dopriStiff_h
#define dopriStiff_h


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

// TO DO: ADD CONSTRUCTOR TO DEFINE ATOL, RTOL, NSTEPMAX, ETC
// TO DO: replace nVs by betNV()s
// TO DO: recycle k7 into k1 from one call to dopriOneStep to another instead of only within dopriOneStep
// TO DO: improve events management (especially eventVar)
// TO DO: make a solveLastPointNoEvents that only make one call to dopriOneIter for performance
using namespace std;

template<typename T>
class dopriStiff: virtual public ODE<T> {

public:
	//CONSTRUCTOR
	//default constructor
	dopriStiff() :
			atol(1e-4), rtol(0),
        	  	fac(0.85), facMin(0.1), facMax(3),
        	  	nStepMax(1000),
        	  	hInit(0.01), hMin(1e-4), hMax(0.1), nStiffMax(999999), nStiffSuccessiveMax(5) {}

	// only sets h
		dopriStiff(T hInitIn, T hMinIn, T hMaxIn) :
			atol(1e-4), rtol(0),
        	  	fac(0.85), facMin(0.1), facMax(3),
        	  	nStepMax(1000),
        	  	hInit(hInitIn), hMin(hMinIn), hMax(hMaxIn), nStiffMax(999999), nStiffSuccessiveMax(5) {}
	// sets all parameters
		dopriStiff(T atolIn, T rtolIn, T facIn, T facMinIn, T facMaxIn, int nStepMaxIn, T hInitIn, T hMinIn, T hMaxIn, int nStiffMaxIn, int nStiffSuccessiveMaxIn) :
			atol(atolIn), rtol(rtolIn),
			fac(facIn), facMin(facMinIn), facMax(facMaxIn),
			nStepMax(nStepMaxIn),
			hInit(hInitIn), hMin(hMinIn), hMax(hMaxIn),
			nStiffMax(nStiffMaxIn), nStiffSuccessiveMax(nStiffSuccessiveMaxIn) {}

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

	// Main solver, overrides the virtual one from base ODE class
	void solve(const T* yInit, T* parms, T* out) override {
		//Init
		// Note that below variables needs to be defined locally, rather than as class members to ensure the solve function is thread safe.
		const int nV = getNV();
		const int nIV = getNIV();
		const int nt = getNt();
		const int nRowOut = getNRowOut();
		int stiffCompt[2] = {0, 0};
		T t=getTInit();
		T k0[nV], k1[nV], k2[nV], k3[nV], k4[nV], k5[nV], k6[nV], k7[nV];
		T x[nIV];
		T yTemp[nV], y0[nV], y4thOrder[nV];
		T h = hInit;
		T tol[nV];
		for (int it=0; it<nV; it++) out[it] = yInit[it];
		//Main Loop
		for (int it=1; it<nt; it++) {
			// Run events
			#if UseEventTime
				makeEventTime(t, parms, &out[(it-1)*getNRowOut()], x, hInit);
			#endif
			#if UseEventVar
				makeEventVar(t, parms, &out[(it-1)*getNRowOut()], x, hInit);
			#endif

			// Use dopri method to estimate y at t+h
			dopriOneStep(t, &out[(it-1)*nRowOut], parms, k0, k1, k2, k3, k4, k5, k6, k7, x, &out[it*nRowOut],
			             h, tol, yTemp, y0, y4thOrder, stiffCompt);
			// complete output with ydot and x at t
			completeOut(k0, x, &out[(it-1)*nRowOut]); // THIS IS NOT A TYPO: "(it-1)" is what we want here (because ydot and x are computed at t and not at t+h)
		}
		// Complete out at last point
		Func(t, &out[(nt-1)*nRowOut], parms, k0, x);
		completeOut(k0, x, &out[(nt-1)*nRowOut]);
		}

	// Same as solve, but only returns last point of trajectory
	void solveLastPoint(const T* yInit, T* parms, T* out) override {
		//Init
		int nV = getNV();
		int nIV = getNIV();
		int nt = getNt();
		T t=getTInit();
		T k0[nV], k1[nV], k2[nV], k3[nV], k4[nV], k5[nV], k6[nV], k7[nV];
		T x[nIV];
		T y[nV], yTemp[nV], y0[nV], y4thOrder[nV];
		T h = hInit;
		T tol[nV];
		int stiffCompt[2] = {0, 0};

		for (int it=0; it<nV; it++) y[it] = yInit[it];
		//Main Loop
		for (int it=1; it<nt; it++) { // it would be possible to get rid of this loop if we were not using events to make this function even faster
			// Run events (if needed)
			#if UseEventTime
				makeEventTime(t, parms, y, x, hInit);
			#endif
			#if UseEventVar
				makeEventVar(t, parms, y, x, hInit);
			#endif
			// Use dopri method to estimate y at t+h
			dopriOneStep(t, y, parms, k0, k1, k2, k3, k4, k5, k6, k7, x, y, h, tol, yTemp, y0, y4thOrder, stiffCompt); // y appears twice as an argument (one tells EulerOneStep where to take initial estimate of y and the other where to write the new value of y) because we do not need to store the full trajectory here.
		}
		// Complete out at last point
		for (int it=0; it<nV; it++) out[it] = y[it];
		Func(t, y, parms, k0, x);
		completeOut(k0, x, out);
	}
protected:
	//use of yTemp in dopriOneStep needed in case of step rejection !
	void dopriOneStep(T& t, const T* y, const T* parms, T* k0, T* k1, T* k2, T* k3, T* k4, T* k5, T* k6, T* k7, T* x, T* out,
			  T& h, T* tol, T* yTemp, T* y0, T* y4thOrder, int* stiffCompt) {
		// INITIALIZATION
		T tEndOneStep = t + getHOut();
		int nStep=0;
		T error = 0.0;
		T alpha = 0.0;
		T hMem = 0.0;
		T lambda;
		T lambdaNum;
		T lambdaDenom;
		T g6[getNV()];
		bool justRejected = false;
		bool truncatedH = false;
		for (int it=0; it<getNV(); it++) y0[it] = y[it];
		Func(t, y0, parms, k0, x);
		for (int it=0; it<getNV(); it++) k1[it] = k0[it];
		//MAIN LOOP
		while(t<tEndOneStep-1e-14 && nStep<nStepMax) { // -1e-14 due to rounding errors when computing t+h
			for (int it=0; it<getNV(); it++) yTemp[it]     = y0[it] + h*(a21*k1[it]                                                                );
			Func(t+c2*h, yTemp, parms, k2, x);
			for (int it=0; it<getNV(); it++) yTemp[it]     = y0[it] + h*(a31*k1[it] + a32*k2[it]                                                   );
			Func(t+c3*h, yTemp, parms, k3, x);
			for (int it=0; it<getNV(); it++) yTemp[it]     = y0[it] + h*(a41*k1[it] + a42*k2[it] + a43*k3[it]                                      );
			Func(t+c4*h, yTemp, parms, k4, x);
			for (int it=0; it<getNV(); it++) yTemp[it]     = y0[it] + h*(a51*k1[it] + a52*k2[it] + a53*k3[it] + a54*k4[it]                         );
			Func(t+c5*h, yTemp, parms, k5, x);
			for (int it=0; it<getNV(); it++) g6[it]     = y0[it] + h*(a61*k1[it] + a62*k2[it] + a63*k3[it] + a64*k4[it] + a65*k5[it]            );
			Func(t+c6*h, g6, parms, k6, x);
			for (int it=0; it<getNV(); it++) yTemp[it]     = y0[it] + h*(a71*k1[it]              + a73*k3[it] + a74*k4[it] + a75*k5[it] +a76*k6[it]);
			Func(t+c7*h, yTemp, parms, k7, x);
			// estimate 4th order solution for error estimation
			for (int it=0; it<getNV(); it++) y4thOrder[it] = y0[it] + h*(b1p*k1[it]               + b3p*k3[it] + b4p*k4[it] + b5p*k5[it] + b6p*k6[it] + b7p*k7[it]);

			// STIFFNESS DETECTION
			lambdaDenom=0.0;
			lambdaNum=0.0;
			for (int it=0; it<getNV(); it++) {
				lambdaNum+=pow(k7[it] - k6[it], 2.0);
				lambdaDenom+=pow(yTemp[it] - g6[it], 2.0);
			}

			lambda=pow(lambdaNum, 0.5)/max(pow(lambdaDenom, 0.5), 1e-7); // add max to avoid numerical precision issues
			if (lambda*h>3.3) {
//				cout<<"at t="<<t<<", h="<<h<<", y0 = "<<y4thOrder[2]<<", lambda = "<<lambda<<endl;
				stiffCompt[0]++;
				stiffCompt[1]++;
				if (stiffCompt[0]>=nStiffMax | stiffCompt[1]>=nStiffSuccessiveMax) {
				  cout<<"at t="<<t<<endl;
					throw std::runtime_error("Stiffness detected, use a stiff solver or reduce the tolerance.");
				}
			} else {
				stiffCompt[1]= 0;
			}

			// Stepsize selection for next iteration, and validation of current step
			error = 0.0;
			for (int it=0; it<getNV(); it++) tol[it] = atol + rtol*max(abs(yTemp[it]), abs(y4thOrder[it]));
			for (int it=0; it<getNV(); it++) error+= pow((yTemp[it] - y4thOrder[it])/tol[it], 2.0);
			error = pow(error/getNV(), 0.5);
			alpha = fac*pow((1/error), 1.0/5.0);
			if (error<=1) { // Error is small enough, go to next step at t=t+h. Else, restart step with the new time step h
				justRejected = false;
				t+=h; //Set init time for next iteration before updating the time step h
				for (int it=0; it<getNV(); it++) {
					k1[it] = k7[it]; // recycle last observation of last step as first observation of next step
					y0[it] = yTemp[it];
				}
			} else {
				justRejected = true;
			}
			if (alpha<facMin || alpha!=alpha) {
				h*=facMin;
			} else if (justRejected==true && alpha>1.0) {
				// do not increase h right after a step rejection (idk why but apparently this is recommended)
			} else if(alpha>facMax) {
				h*=facMax;
			} else {
				h*=alpha;
			}

			if (h>hMax) {
				h = hMax;
			} else if (h<hMin) {
				h=hMin;
			}
			if (t+h>tEndOneStep && t<tEndOneStep) {
				hMem = h;
				h = tEndOneStep-t;
				truncatedH=true;
			}
			nStep++;
		}
		if (truncatedH) h = hMem;
		for (int it=0; it<getNV(); it++) out[it] = yTemp[it];
		if (nStep>=nStepMax-1) throw std::runtime_error("Maximum number of steps reached. This MIGHT be due to stiffness. Reduce time step, increase maximum number of steps or use a stiff solver.");
	}

	T atol;
	T rtol;
	T fac;
	T facMin;
	T facMax;
	T nStepMax;
	T hInit;
	T hMin;
	T hMax;

	// Parms for stiffness detection
	int nStiffMax;
	int nStiffSuccessiveMax;
	// parameters for RK
	// In practice, terms including parameters set to zero are removed from code above to save computation time,
	// but the parameters are explicitely defined here for clarity.
	const T a21  = (1.0/5.0);
	const T a31  = (3.0/40.0);
	const T a32  = (9.0/40.0);
	const T a41  = (44.0/45.0);
	const T a42  = (-56.0/15.0);
	const T a43  = (32.0/9.0);
	const T a51  = (19372.0/6561.0);
	const T a52  = (-25360.0/2187.0);
	const T a53  = (64448.0/6561.0);
	const T a54  = (-212.0/729.0);
	const T a61  = (9017.0/3168.0);
	const T a62  = (-355.0/33.0);
	const T a63  = (46732.0/5247.0);
	const T a64  = (49.0/176.0);
	const T a65  = (-5103.0/18656.0);
	const T a71  = (35.0/384.0);
	const T a72  = (0.0);
	const T a73  = (500.0/1113.0);
	const T a74  = (125.0/192.0);
	const T a75  = (-2187.0/6784.0);
	const T a76  = (11.0/84.0);

	const T c2   = (1.0 / 5.0);
	const T c3   = (3.0 / 10.0);
	const T c4   = (4.0 / 5.0);
	const T c5   = (8.0 / 9.0);
	const T c6   = (1.0);
	const T c7   = (1.0);

// b1...b7 not used in practice (as these are equal to a71...a76), but showed here for clarity
	const T b1   = (35.0/384.0);
	const T b2   = (0.0);
	const T b3   = (500.0/1113.0);
	const T b4   = (125.0/192.0);
	const T b5   = (-2187.0/6784.0);
	const T b6   = (11.0/84.0);
	const T b7   = (0.0);

	const T b1p  = (5179.0/57600.0);
	const T b2p  = (0.0);
	const T b3p  = (7571.0/16695.0);
	const T b4p  = (393.0/640.0);
	const T b5p  = (-92097.0/339200.0);
	const T b6p  = (187.0/2100.0);
	const T b7p  = (1.0/40.0);
};


#endif
