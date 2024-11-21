#ifndef solverModelR_h
#define solverModelR_h

#include <iostream>
#include <fstream>
#include <math.h>
#include <cstring>
#include <stdio.h>
#include <string.h>



#include "ODE.h"
#include "euler.h"
#include "RK4Fixed.h"
#include "dopri.h"
#include "dopriStiffDetect.h"
#include "modelR.h"

using namespace std;

template<typename T>
class modelREuler: public Euler<T>, public modelR<T>, public virtual ODE<T> {
public:
	// CONSTRUCTOR
	modelREuler(const int nVIn, const int nIVIn, const T tInitIn, const T tEndIn, const int ntIn, exogVar<T>* myExogVarIn = nullptr) :
			ODE<T>{nVIn, nIVIn, tInitIn, tEndIn, ntIn}, myExogVar(myExogVarIn) {}
	// Copy constructor
	modelREuler(const modelREuler<T>& other) : 
		ODE<T>{other.nV, other.nIV, other.tInit, other.tEnd, other.ntIn}, myExogVar(other.myExogVar) {}
protected:
	exogVar<T>* myExogVar;
	T getExogVar(T t, int i) override {
		return myExogVar->getValue(t-this->tInit, i);
	}

};

template<typename T>
class modelRRK4: public RK4Fixed<T>, public modelR<T> {
public:
	// CONSTRUCTOR
	modelRRK4(const int nVIn, const int nIVIn, const T tInitIn, const T tEndIn, const int ntIn, exogVar<T>* myExogVarIn = nullptr) :
			ODE<T>{nVIn, nIVIn, tInitIn, tEndIn, ntIn}, myExogVar(myExogVarIn) {}
	// Copy constructor
	modelRRK4(const modelRRK4<T>& other) : 
		ODE<T>{other.nV, other.nIV, other.tInit, other.tEnd, other.ntIn}, myExogVar(other.myExogVar) {}
protected:
	exogVar<T>* myExogVar;
	T getExogVar(T t, int i) override {
		return myExogVar->getValue(t-this->tInit, i);
	}

};

template<typename T>
class modelRDopri: public dopri<T>, public modelR<T> {
public:
	// CONSTRUCTOR
	modelRDopri(const int nVIn, const int nIVIn, const T tInitIn, const T tEndIn, const int ntIn, 
		    T atolIn, T rtolIn, T facIn, T facMinIn, T facMaxIn, int nStepMaxIn, T hInitIn, T hMinIn, T hMaxIn, exogVar<T>* myExogVarIn = nullptr) :
			ODE<T>{nVIn, nIVIn, tInitIn, tEndIn, ntIn}, 
			dopri<T>{atolIn, rtolIn, facIn, facMinIn, facMaxIn, nStepMaxIn, hInitIn, hMinIn, hMaxIn},
			myExogVar(myExogVarIn) {}

	// Copy constructor
	modelRDopri(const modelRDopri<T>& other) :
		ODE<T>{other.nV, other.nIV, other.tInit, other.tEnd, other.ntIn}, myExogVar(other.myExogVar),
      		dopri<T>{other.atol, other.rtol, other.fac, other.facMin, other.facMax, other.nStepMax, other.hInit, other.hMax} {}
protected:
	exogVar<T>* myExogVar;
	T getExogVar(T t, int i) override {
		return myExogVar->getValue(t-this->tInit, i);
	}

};


template<typename T>
class modelRDopriStiff: public dopriStiff<T>, public modelR<T> {
public:
	// CONSTRUCTOR
	modelRDopriStiff(const int nVIn, const int nIVIn, const T tInitIn, const T tEndIn, const int ntIn,
		    T atolIn, T rtolIn, T facIn, T facMinIn, T facMaxIn, int nStepMaxIn, T hInitIn, T hMinIn, T hMaxIn, int nStiffMaxIn, int nStiffSuccessiveMaxIn, exogVar<T>* myExogVarIn = nullptr) :
			ODE<T>{nVIn, nIVIn, tInitIn, tEndIn, ntIn},
			dopriStiff<T>{atolIn, rtolIn, facIn, facMinIn, facMaxIn, nStepMaxIn, hInitIn, hMinIn, hMaxIn, nStiffMaxIn, nStiffSuccessiveMaxIn},
			myExogVar(myExogVarIn) {}

	// Copy constructor
	modelRDopriStiff(const modelRDopriStiff<T>& other) :
		ODE<T>{other.nV, other.nIV, other.tInit, other.tEnd, other.ntIn}, myExogVar(other.myExogVar),
      		dopri<T>{other.atol, other.rtol, other.fac, other.facMin, other.facMax, other.nStepMax, other.hInit, other.hMax, other.nStiffMax, other.nStiffSuccessiveMax} {}
protected:
	exogVar<T>* myExogVar;
	T getExogVar(T t, int i) override {
		return myExogVar->getValue(t-this->tInit, i);
	}

};

#endif
