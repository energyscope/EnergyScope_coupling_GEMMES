#ifndef exogenousVariables_H
#define exogenousVariables_H

#include <iostream>
#include <fstream>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <armadillo>

using namespace std;

/**************************************************/
// TO DO: MAKE DEEP AND SHALLOW COPY FOR exogVarGeneral
// TO DO: ADD exogVar class with cubic spline interpolation instead of linear interpolation
/**************************************************/
// Virtual class for exogenous variables
template<typename T>
class exogVar {
	public:
	virtual ~exogVar() {};

	virtual T getValue(const T t, const int i) = 0;
};


// Default class for exogenous variables:
// requires both a sampling frequency and a samplingTime
// Tries to guess sampling position based on sampling frequency
// then adjusts sampling position if missplaced due to irregular sampling
// compatible with parallel programming (no need for deep copy), and with irregular sampling frequencies, 
// but not optimal regarding computation time (unnecessary condition tests in case of periodic sampling, and systematic need to adjust position in case of aperiodic sampling).
template<typename T>
class exogVarGeneral: public exogVar<T>{
	public:
		// CONSTRUCTOR
		exogVarGeneral(T* samplesExogVar, T* samplingTimeExogVar, int nVarExogVar, int* nSamplesVarExogVar) : 
				 nVar(nVarExogVar) {
			
			// add one sample at tInit-1 and one sample at tEnd+1 to ensure getValue never goes out of bounds.

			// Define indexVar
			indexVar = new int[nVarExogVar];
			int* indexVarExogVar = new int[nVarExogVar];
			int comptNSamplesVar = 0;
			int comptNSamplesVarExogVar = 0;
			for (int it=0; it<nVar; it++) {
				comptNSamplesVar++; // Add 1 element at tInit-1
				indexVar[it] = comptNSamplesVar;
				indexVarExogVar[it] = comptNSamplesVarExogVar;
				comptNSamplesVar+=nSamplesVarExogVar[it]+1; // Add number of samples + 1 element at tEnd+1
				comptNSamplesVarExogVar+=nSamplesVarExogVar[it];
 			}
			//Define sampleLength
			sampleLength = comptNSamplesVar;
			
			// Define samples
			samples = new T[comptNSamplesVar];
			for (int it=0; it<nVar; it++) {
				samples[indexVar[it]-1] = samplesExogVar[indexVarExogVar[it]]; // add one sample at tInit-1
				for (int it1=0; it1<nSamplesVarExogVar[it]; it1++) samples[indexVar[it]+it1] = samplesExogVar[indexVarExogVar[it]+it1]; // copy from original sampleExogVar to extended sample
				samples[indexVar[it]+nSamplesVarExogVar[it]] = samplesExogVar[indexVar[it]+nSamplesVarExogVar[it]-2]; // add one sample at tEnd+1
			}
			// define samplingTime
			samplingTime = new T[comptNSamplesVar];
			for (int it=0; it<nVar; it++) {
				samplingTime[indexVar[it]-1] = samplingTimeExogVar[indexVarExogVar[it]]-1; // add one sample at tInit-1
				for (int it1=0; it1<nSamplesVarExogVar[it]; it1++) samplingTime[indexVar[it]+it1] = samplingTimeExogVar[indexVarExogVar[it]+it1]; // compy from original samplingTImeExogVar to extended samplingTime
				samplingTime[indexVar[it]+nSamplesVarExogVar[it]] = samplingTimeExogVar[indexVarExogVar[it]+nSamplesVarExogVar[it]-1]+1; // add one sample at tEnd+1
			}
			// Define sampling period hSampling
			hSampling = new T[nVarExogVar];
			for (int it=0; it<nVar; it++) hSampling[it] = samplingTimeExogVar[indexVarExogVar[it] +1] - samplingTimeExogVar[indexVarExogVar[it]];
			delete[] indexVarExogVar;
		}


		// COPY CONSTRUCTOR
		exogVarGeneral(const exogVar<T>& other) :
       				 nVar(other.nVar), sampleLength(other.sampleLength) {
			// Define indexVar
			indexVar = new int[nVar];
			for (int it=0; it<nVar; it++) indexVar[it] = other.indexVar[it];
			// Define samples
			samples = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samples[it] = other.samples[it];
			//Define samplingTime
			samplingTime = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samplingTime[it] = other.samplingTime[it];
			// Define hSampling
			hSampling = new T[nVar];
			for (int it=0; it<nVar; it++) hSampling[it] = other.hSampling[it];
		}		
		// DESTRUCTOR
		~exogVarGeneral() {
			delete[] indexVar;
			delete[] samples;
			delete[] samplingTime;
			delete[] hSampling;
		}
		// ESTIMATES VALUE OF THE Ith INTERMEDIATE VARIABLE AT TIME t USING LINEAR INTERPOLATION
		T getValue(const T t, const int i) {
			// set position at the latest sample for which samplingTime is lower than t
			// tries to guess posSample assuming periodic sampling
			int posSample = indexVar[i] + (int)t/hSampling[i];
			// Adjusts posSample in case of aperiodic sampling
			while (samplingTime[posSample]<t) posSample++;
			while(samplingTime[posSample]>t) posSample--; 
			// Linear interpolation to estimate exogenous variable value at time t
			return samples[posSample] + (samples[posSample + 1] - samples[posSample])*(t - samplingTime[posSample])/(samplingTime[posSample+1] - samplingTime[posSample]);
		}


	private:
		const int nVar;
		T* hSampling;
		T* samples;
		T* samplingTime;
		int sampleLength;
		int* indexVar;
		int* nSamplesVar;
};


// exogVar for periodic sampling time only
// Compatible with parallel programming
// 

template<typename T>
class exogVarPeriodic: public exogVar<T>{
	public:
		// CONSTRUCTOR
		exogVarPeriodic(T tInitIn, T tEndIn, T* samplesExogVar, int nVarExogVar, int* nSamplesVarExogVar) : 
				 nVar(nVarExogVar), tInit(tInitIn), tEnd(tEndIn) {
			
			// add one sample at tInit-1 and one sample at tEnd+1 to ensure getValue never goes out of bounds.

			// Define indexVar
			indexVar = new int[nVarExogVar];
			int* indexVarExogVar = new int[nVarExogVar];
			int comptNSamplesVar = 0;
			int comptNSamplesVarExogVar = 0;
			for (int it=0; it<nVar; it++) {
				comptNSamplesVar++; // Add 1 element at tInit-1
				indexVar[it] = comptNSamplesVar;
				indexVarExogVar[it] = comptNSamplesVarExogVar;
				comptNSamplesVar+=nSamplesVarExogVar[it]+1; // Add number of samples + 1 element at tEnd+1
				comptNSamplesVarExogVar+=nSamplesVarExogVar[it];
 			}
			//Define sampleLength
			sampleLength = comptNSamplesVar;
			
			// Define samples
			samples = new T[comptNSamplesVar];
			for (int it=0; it<nVar; it++) {
				samples[indexVar[it]-1] = samplesExogVar[indexVarExogVar[it]]; // add one sample at tInit-1
				for (int it1=0; it1<nSamplesVarExogVar[it]; it1++) samples[indexVar[it]+it1] = samplesExogVar[indexVarExogVar[it]+it1]; // copy from original sampleExogVar to extended sample
				samples[indexVar[it]+nSamplesVarExogVar[it]] = samplesExogVar[indexVar[it]+nSamplesVarExogVar[it]-2]; // add one sample at tEnd+1
			}
			// Define sampling period hSampling
			hSampling = new T[nVarExogVar];
			for (int it=0; it<nVar; it++) hSampling[it] = (tEndIn-tInitIn)/(nSamplesVarExogVar[it] - 1);
			delete[] indexVarExogVar;
		}


		// COPY CONSTRUCTOR
		exogVarPeriodic(const exogVar<T>& other) :
       				 tInit(other.tInit), tEnd(other.tEnd), nVar(other.nVar), sampleLength(other.sampleLength) {
			// Define indexVar
			indexVar = new int[nVar];
			for (int it=0; it<nVar; it++) indexVar[it] = other.indexVar[it];
			// Define samples
			samples = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samples[it] = other.samples[it];
			// Define hSampling
			hSampling = new T[nVar];
			for (int it=0; it<nVar; it++) hSampling[it] = other.hSampling[it];
		}		
		// DESTRUCTOR
		~exogVarPeriodic() {
			delete[] indexVar;
			delete[] samples;
			delete[] hSampling;
		}
		// ESTIMATES VALUE OF THE Ith INTERMEDIATE VARIABLE AT TIME t USING LINEAR INTERPOLATION
		T getValue(const T t, const int i) {
			// set position at the latest sample for which samplingTime is lower than t
			int posSample = indexVar[i] + (int)t/hSampling[i]; 
			// Linear interpolation to estimate exogenous variable value at time t
			return samples[posSample] + (samples[posSample + 1] - samples[posSample])*(t - (posSample-indexVar[i])*hSampling[i])/(hSampling[i]);
		}


	private:
		const int nVar;
		T tInit;
		T tEnd;
		T* hSampling;
		T* samples;
		int sampleLength;
		int* indexVar;
		int* nSamplesVar;
};

// ExogVar class for non-periodic samplingTime
// getValue uses a local array posSamples to know which sampling time to get, and update it at every call of getValue depending on the value of t.
// WARNING: YOU NEED TO MAKE A HARD COPY OF EXOGVAR TO USE IT IN PARALLEL CODE;
// Because of this, it is no longer used in practice.
template<typename T>
class exogVarAperiodic: public exogVar<T>{
	public:
		// CONSTRUCTOR
		exogVarAperiodic(T* samplesExogVar, T* samplingTimeExogVar, int nVarExogVar, int* nSamplesVarExogVar) : 
				 nVar(nVarExogVar) {
			
			// add one sample at tInit-1 and one sample at tEnd+1 to ensure getValue never goes out of bounds.

			// Define indexVar
			indexVar = new int[nVarExogVar];
			int* indexVarExogVar = new int[nVarExogVar];
			int comptNSamplesVar = 0;
			int comptNSamplesVarExogVar = 0;
			for (int it=0; it<nVar; it++) {
				comptNSamplesVar++; // Add 1 element at tInit-1
				indexVar[it] = comptNSamplesVar;
				indexVarExogVar[it] = comptNSamplesVarExogVar;
				comptNSamplesVar+=nSamplesVarExogVar[it]+1; // Add number of samples + 1 element at tEnd+1
				comptNSamplesVarExogVar+=nSamplesVarExogVar[it];
 			}
			//Define sampleLength
			sampleLength = comptNSamplesVar;
			
			// Define samples
			samples = new T[comptNSamplesVar];
			for (int it=0; it<nVar; it++) {
				samples[indexVar[it]-1] = samplesExogVar[indexVarExogVar[it]]; // add one sample at tInit-1
				for (int it1=0; it1<nSamplesVarExogVar[it]; it1++) samples[indexVar[it]+it1] = samplesExogVar[indexVarExogVar[it]+it1]; // copy from original sampleExogVar to extended sample
				samples[indexVar[it]+nSamplesVarExogVar[it]] = samplesExogVar[indexVar[it]+nSamplesVarExogVar[it]-2]; // add one sample at tEnd+1
			}
			// define samplingTime
			samplingTime = new T[comptNSamplesVar];
			for (int it=0; it<nVar; it++) {
				samplingTime[indexVar[it]-1] = samplingTimeExogVar[indexVarExogVar[it]]-1; // add one sample at tInit-1
				for (int it1=0; it1<nSamplesVarExogVar[it]; it1++) samplingTime[indexVar[it]+it1] = samplingTimeExogVar[indexVarExogVar[it]+it1]; // compy from original samplingTImeExogVar to extended samplingTime
				samplingTime[indexVar[it]+nSamplesVarExogVar[it]] = samplingTimeExogVar[indexVarExogVar[it]+nSamplesVarExogVar[it]-1]+1; // add one sample at tEnd+1
			}
			// Define posSamples
			posSamples = new int[nVarExogVar];
			for (int it=0; it<nVar; it++) posSamples[it] = indexVar[it]+1;
			delete[] indexVarExogVar;
		}


		// COPY CONSTRUCTOR
		exogVarAperiodic(const exogVar<T>& other) :
       				 nVar(other.nVar), sampleLength(other.sampleLength) {
			// Define indexVar
			indexVar = new int[nVar];
			for (int it=0; it<nVar; it++) indexVar[it] = other.indexVar[it];
			//D
			// Define samples
			samples = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samples[it] = other.samples[it];
			//Define samplingTime
			samplingTime = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samplingTime[it] = other.samplingTime[it];
			// Define posSamples
			posSamples = new int[nVar];
			for (int it=0; it<nVar; it++) posSamples[it] = indexVar[it]+1;
		}		
		// DESTRUCTOR
		~exogVarAperiodic() {
			delete[] indexVar;
			delete[] samples;
			delete[] samplingTime;
			delete[] posSamples;
		}
		// ESTIMATES VALUE OF THE Ith INTERMEDIATE VARIABLE AT TIME t USING LINEAR INTERPOLATION
		T getValue(const T t, const int i) {
			// set position at the latest sample for which samplingTime is lower than t
			while (samplingTime[posSamples[i]]<t) posSamples[i]++;
			while(samplingTime[posSamples[i]]>t) posSamples[i]--;
			// Linear interpolation to estimate exogenous variable value at time t
			return samples[posSamples[i]] + (samples[posSamples[i] + 1] - samples[posSamples[i]])*(t - samplingTime[posSamples[i]])/(samplingTime[posSamples[i]+1] - samplingTime[posSamples[i]]);
		}
		void resetPosSample() {
		for (int it=0; it<nVar; it++) posSamples[it] = indexVar[it]+1; 
		}



		int* posSamples;
	private:
		const int nVar;
		T* samples;
		T* samplingTime;
		int sampleLength;
		int* indexVar;
		int* nSamplesVar;
};


// Can't add extra point before/after sample because it would affect the curvature of the polynomial (i.e impose null 1st and second order derivatives of the splines at first/last point)
template<typename T>
class exogVarCubicSplinePeriodic: public exogVar<T>{
	public:
		// CONSTRUCTOR
		exogVarCubicSplinePeriodic(T tInitIn, T tEndIn, T* samplesExogVar, int nVarExogVar, int* nSamplesVarExogVar) :
				 nVar(nVarExogVar), tInit(tInitIn), tEnd(tEndIn), nSamplesVar(nSamplesVarExogVar) {

			// add one sample at tInit-1 and one sample at tEnd+1 to ensure getValue never goes out of bounds.
			// Define indexVar
			indexVar = new int[nVarExogVar];
			int comptNSamplesVar = 0;
			//int comptNSamplesVarExogVar = 0;
			for (int it=0; it<nVar; it++) {
				indexVar[it] = comptNSamplesVar;
				comptNSamplesVar+=nSamplesVarExogVar[it];
 			}
			//Define sampleLength
			sampleLength = comptNSamplesVar;
			// Define samples
			samples = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samples[it] = samplesExogVar[it];
			// Define sampling period hSampling
			hSampling = new T[nVarExogVar];
			for (int it=0; it<nVar; it++) hSampling[it] = (tEndIn-tInitIn)/(nSamplesVarExogVar[it] - 1);
			a = new T[sampleLength - nVar];
			b = new T[sampleLength - nVar];
			c = new T[sampleLength - nVar];
			d = new T[sampleLength - nVar];
			for (int i=0; i<nVar; i++) {
				createSpline(i);
			}
		}

		// DESTRUCTOR
		~exogVarCubicSplinePeriodic() {
			delete[] samples;
			delete[] indexVar;
			delete[] hSampling;
			delete[] a;
			delete[] b;
			delete[] c;
			delete[] d;
		}
		// ESTIMATES VALUE OF THE Ith INTERMEDIATE VARIABLE AT TIME t USING LINEAR INTERPOLATION
		T getValue(const T t, const int i) {
			// set position at the latest sample for which samplingTime is lower than t
			int j = indexVar[i] - i + (int)(t/hSampling[i]); 
			if (j >= indexVar[i] - i + nSamplesVar[i] - 1) {
				j--;
			}
			//Rcpp::Rcout<<"estimating Exogenous Variable: "<<i<<" at time: "<<t<<" value left="<<a[j]*pow(std::floor(t), 3.0) + b[j]*pow(std::floor(t), 2) + c[j]*std::floor(t) + d[j]<<" value right="<<a[j]*pow(std::ceil(t), 3.0) + b[j]*pow(std::ceil(t), 2) + c[j]*std::ceil(t) + d[j]<<endl;
			// Linear interpolation to estimate exogenous variable value at time t
			return a[j]*pow(t, 3.0) + b[j]*pow(t, 2) + c[j]*t + d[j];
		}

//	private:
		void createSpline(int i) {
			int n = nSamplesVar[i]-1; // number of (cubic) splines to define
			arma::mat A(4*n, 4*n, arma::fill::zeros);
			arma::vec B(4*n, arma::fill::zeros);
			int compt = 1;
			T t_i = 0*tInit;
			// 2*n equality conditions: 
			for (int it=0; it<n; it++) { // assuming only one exogenous variable for now
				// f_i(t_i) = y_i
				A(compt + it, (it)*4  ) = pow(t_i, 3.0);
				A(compt + it, (it)*4+1) = pow(t_i, 2.0);
				A(compt + it, (it)*4+2) = t_i;
				A(compt + it, (it)*4+3) = 1;
				B(compt + it) = samples[indexVar[i] + it];
				// f_i(t_i+1) = y_i+1
				A(compt + n + it, (it)*4  ) = pow(t_i + hSampling[i], 3.0);
				A(compt + n + it, (it)*4+1) = pow(t_i + hSampling[i], 2.0);
				A(compt + n + it, (it)*4+2) = t_i + hSampling[i];
				A(compt + n + it, (it)*4+3) = 1;
				B(compt + n + it) = samples[indexVar[i] + it + 1];
				t_i+=hSampling[i];
			}
			t_i = 0*tInit;
			compt+=2*n;
			// n-1 first order derivatives conditions
			for (int it=0; it<n-1; it++) {
				A(compt + it, it*4      ) = 3.0*pow(t_i + hSampling[i], 2.0);
				A(compt + it, it*4+1    ) = 2.0*(t_i + hSampling[i]);
				A(compt + it, it*4+2    ) = 1.0;
				A(compt + it, (it+1)*4  ) = -3.0*pow(t_i + hSampling[i], 2.0);
				A(compt + it, (it+1)*4+1) = -2.0*(t_i + hSampling[i]);
				A(compt + it, (it+1)*4+2) = -1.0;
				B(compt + it) = 0.0;
				t_i+=hSampling[i];
			}
			compt+=n-1;
			t_i = 0*tInit;
			// n-1 second order derivatives conditions
			for (int it=0; it<n-1; it++) {
				A(compt + it, it*4      ) = 6.0*(t_i + hSampling[i]);
				A(compt + it, it*4+1    ) = 2.0;
				A(compt + it, (it+1)*4  ) = -6.0*(t_i + hSampling[i]);
				A(compt + it, (it+1)*4+1) = -2.0;
				B(compt + it            ) = 0.0;
				t_i+=hSampling[i];

			}
			// Two second order derivatives conditions at border
			A(0    , 0          ) = 6.0*(0*tInit);
			A(0    , 1          ) = 2.0;
			B(0                 ) = 0.0; 
			A(4*n-1, 4*(n-1)    ) = 6.0*(tEnd-tInit);
			A(4*n-1, 4*(n-1) + 1) = 2.0;
			B(4*n-1             ) = 0.0;
			arma::vec X = solve(A, B);
			for (int it=0; it<nSamplesVar[i]-1; it++) {
				a[indexVar[i] - i + it] = X[4*it];
				b[indexVar[i] - i + it] = X[4*it + 1];
				c[indexVar[i] - i + it] = X[4*it + 2];
				d[indexVar[i] - i + it] = X[4*it + 3];
			}
			//cout<<"A: "<<A<<endl;
			//cout<<"B: "<<B<<endl;
			//cout<<"X: "<<X<<endl;
		}

		// ptrs storing the polinomial coefficients of the splines.
		const int nVar;
		T tInit;
		T tEnd;
		T* hSampling;
		T* samples;
		int sampleLength;
		int* indexVar;
		int* nSamplesVar;
		T* a;
		T* b;
		T* c;
		T* d;

};


// Same as above but with additional conditions to better behave: 
// (1) We impose that if two successive observations take th same value, the polynomial is constant on this interval
// (2) And that its derivatives at the extremities are equal to zero
template<typename T>
class exogVarCubicSplinePeriodic2: public exogVar<T>{
	public:
		// CONSTRUCTOR
		exogVarCubicSplinePeriodic2(T tInitIn, T tEndIn, T* samplesExogVar, int nVarExogVar, int* nSamplesVarExogVar) :
				 nVar(nVarExogVar), tInit(tInitIn), tEnd(tEndIn), nSamplesVar(nSamplesVarExogVar) {

			// add one sample at tInit-1 and one sample at tEnd+1 to ensure getValue never goes out of bounds.
			// Define indexVar
			indexVar = new int[nVarExogVar];
			int comptNSamplesVar = 0;
			//int comptNSamplesVarExogVar = 0;
			for (int it=0; it<nVar; it++) {
				indexVar[it] = comptNSamplesVar;
				comptNSamplesVar+=nSamplesVarExogVar[it];
 			}
			//Define sampleLength
			sampleLength = comptNSamplesVar;
			// Define samples
			samples = new T[sampleLength];
			for (int it=0; it<sampleLength; it++) samples[it] = samplesExogVar[it];
			// Define sampling period hSampling
			hSampling = new T[nVarExogVar];
			for (int it=0; it<nVar; it++) hSampling[it] = (tEndIn-tInitIn)/(nSamplesVarExogVar[it] - 1);
			a = new T[sampleLength - nVar];
			b = new T[sampleLength - nVar];
			c = new T[sampleLength - nVar];
			d = new T[sampleLength - nVar];
			for (int i=0; i<nVar; i++) {
				createSpline(i);
			}
		}

		// DESTRUCTOR
		~exogVarCubicSplinePeriodic2() {
			delete[] samples;
			delete[] indexVar;
			delete[] hSampling;
			delete[] a;
			delete[] b;
			delete[] c;
			delete[] d;
		}
		// ESTIMATES VALUE OF THE Ith INTERMEDIATE VARIABLE AT TIME t USING LINEAR INTERPOLATION
		T getValue(const T t, const int i) {
			// set position at the latest sample for which samplingTime is lower than t
			int j = indexVar[i] - i + (int)(t/hSampling[i]); 
			if (j >= indexVar[i] - i + nSamplesVar[i] - 1) {
				j--;
			}
			//Rcpp::Rcout<<"estimating Exogenous Variable: "<<i<<" at time: "<<t<<" value left="<<a[j]*pow(std::floor(t), 3.0) + b[j]*pow(std::floor(t), 2) + c[j]*std::floor(t) + d[j]<<" value right="<<a[j]*pow(std::ceil(t), 3.0) + b[j]*pow(std::ceil(t), 2) + c[j]*std::ceil(t) + d[j]<<endl;
			// Linear interpolation to estimate exogenous variable value at time t
			return a[j]*pow(t, 3.0) + b[j]*pow(t, 2) + c[j]*t + d[j];
		}

//	private:
		void createSpline(int i) {
			int n = nSamplesVar[i]-1; // number of (cubic) splines to define
			int sizeSys = 4*n; 
			arma::mat A(sizeSys, sizeSys, arma::fill::zeros);
			arma::vec B(sizeSys, arma::fill::zeros);
			int compt = 1;
			T t_i = 0*tInit;
			// 2*n equality conditions: 
			for (int it=0; it<n; it++) { // assuming only one exogenous variable for now
				if (samples[indexVar[i] + it]== samples[indexVar[i] + it + 1]) { // if y_i = y_i+1
					// d_i = y_i
					A(compt + it, (it)*4  ) = 0;
					A(compt + it, (it)*4+1) = 0;
					A(compt + it, (it)*4+2) = 0;
					A(compt + it, (it)*4+3) = 1;
					B(compt + it) = samples[indexVar[i] + it];
					// c_i = 0
					A(compt + n + it, (it)*4  ) = 0;
					A(compt + n + it, (it)*4+1) = 0;
					A(compt + n + it, (it)*4+2) = 1;
					A(compt + n + it, (it)*4+3) = 0;
					B(compt + n + it) = 0;
				} else { // default case y_i != y_i+1, polynomial condition
					// f_i(t_i) = y_i
					A(compt + it, (it)*4  ) = pow(t_i, 3.0);
					A(compt + it, (it)*4+1) = pow(t_i, 2.0);
					A(compt + it, (it)*4+2) = t_i;
					A(compt + it, (it)*4+3) = 1;
					B(compt + it) = samples[indexVar[i] + it];
					// f_i(t_i+1) = y_i+1
					A(compt + n + it, (it)*4  ) = pow(t_i + hSampling[i], 3.0);
					A(compt + n + it, (it)*4+1) = pow(t_i + hSampling[i], 2.0);
					A(compt + n + it, (it)*4+2) = t_i + hSampling[i];
					A(compt + n + it, (it)*4+3) = 1;
					B(compt + n + it) = samples[indexVar[i] + it + 1];
				}
				t_i+=hSampling[i];
			}
			t_i = 0*tInit;
			compt+=2*n;
			// n-1 first order derivatives conditions
			for (int it=0; it<n-1; it++) {
				if (samples[indexVar[i] + it]== samples[indexVar[i] + it + 1]) { // if y_i = y_i+1
					A(compt + it, it*4      ) = 0;
					A(compt + it, it*4+1    ) = 0;
					A(compt + it, it*4+2    ) = 0;
					A(compt + it, (it+1)*4  ) = -3.0*pow(t_i + hSampling[i], 2.0);
					A(compt + it, (it+1)*4+1) = -2.0*(t_i + hSampling[i]);
					A(compt + it, (it+1)*4+2) = -1.0;
					B(compt + it) = 0.0;				
				} else if (samples[indexVar[i] + it + 1]== samples[indexVar[i] + it + 2]) { // if y_i+1 = y_i+2
					A(compt + it, it*4      ) = 3.0*pow(t_i + hSampling[i], 2.0);
					A(compt + it, it*4+1    ) = 2.0*(t_i + hSampling[i]);
					A(compt + it, it*4+2    ) = 1.0;
					A(compt + it, (it+1)*4  ) = 0;
					A(compt + it, (it+1)*4+1) = 0;
					A(compt + it, (it+1)*4+2) = 0;
					B(compt + it) = 0.0;
				} else { // normal case, polynomial condition
					A(compt + it, it*4      ) = 3.0*pow(t_i + hSampling[i], 2.0);
					A(compt + it, it*4+1    ) = 2.0*(t_i + hSampling[i]);
					A(compt + it, it*4+2    ) = 1.0;
					A(compt + it, (it+1)*4  ) = -3.0*pow(t_i + hSampling[i], 2.0);
					A(compt + it, (it+1)*4+1) = -2.0*(t_i + hSampling[i]);
					A(compt + it, (it+1)*4+2) = -1.0;
					B(compt + it) = 0.0;
				}
				t_i+=hSampling[i];
			}
			compt+=n-1;
			t_i = 0*tInit;
			// n-1 second order derivatives conditions
			for (int it=0; it<n-1; it++) {
				if (samples[indexVar[i] + it]== samples[indexVar[i] + it + 1]) { // if y_i = y_i+1
					// b_i=0
					A(compt + it, it*4      ) = 0;
					A(compt + it, it*4+1    ) = 1.0;
					A(compt + it, (it+1)*4  ) = 0;
					A(compt + it, (it+1)*4+1) = 0;
					B(compt + it            ) = 0.0;
				} else if (samples[indexVar[i] + it + 1]== samples[indexVar[i] + it + 2]) {  // if y_i+1 = y_i+2
					// a_i+1=0
					A(compt + it, it*4      ) = 0.0;
					A(compt + it, it*4+1    ) = 0.0;
					A(compt + it, (it+1)*4  ) = -1;
					A(compt + it, (it+1)*4+1) = 0.0;
					B(compt + it            ) = 0.0;								
				} else {
					A(compt + it, it*4      ) = 6.0*(t_i + hSampling[i]);
					A(compt + it, it*4+1    ) = 2.0;
					A(compt + it, (it+1)*4  ) = -6.0*(t_i + hSampling[i]);
					A(compt + it, (it+1)*4+1) = -2.0;
					B(compt + it            ) = 0.0;
				}
				t_i+=hSampling[i];
			}
			// Two second order derivatives conditions at border
			if (samples[indexVar[i]]==samples[indexVar[i] + 1]) { // y_0 = y_1
				A(0    , 0          ) = 1.0;
				A(0    , 1          ) = 0.0;
				B(0                 ) = 0.0; 			
			} else {
				A(0    , 0          ) = 6.0*(0*tInit);
				A(0    , 1          ) = 2.0;
				B(0                 ) = 0.0; 
			}
			if (samples[indexVar[i] + n]==samples[indexVar[i] + n + 1]) { //y_n==y_n+1
				A(4*n-1, 4*(n-1)    ) = 0.0;
				A(4*n-1, 4*(n-1) + 1) = 1.0;
				B(4*n-1             ) = 0.0;
			} else {
				A(4*n-1, 4*(n-1)    ) = 6.0*(tEnd-tInit);
				A(4*n-1, 4*(n-1) + 1) = 2.0;
				B(4*n-1             ) = 0.0;
			}
			arma::vec X = solve(A, B);
			for (int it=0; it<nSamplesVar[i]-1; it++) {
				a[indexVar[i] - i + it] = X[4*it];
				b[indexVar[i] - i + it] = X[4*it + 1];
				c[indexVar[i] - i + it] = X[4*it + 2];
				d[indexVar[i] - i + it] = X[4*it + 3];
			}
			
			//Rcpp::Rcout<<"A: "<<A<<endl;
			//Rcpp::Rcout<<"B: "<<B<<endl;
			//Rcpp::Rcout<<"X: "<<X<<endl;
		}

		// ptrs storing the polinomial coefficients of the splines.
		const int nVar;
		T tInit;
		T tEnd;
		T* hSampling;
		T* samples;
		int sampleLength;
		int* indexVar;
		int* nSamplesVar;
		T* a;
		T* b;
		T* c;
		T* d;

};

#endif
