// [[Rcpp::depends(RcppArmadillo)]]
#include <RcppArmadillo.h>
#include <omp.h>
#include <iostream>
#include <fstream>
#include<math.h>
#include <Rcpp.h>
using namespace Rcpp; 
using namespace arma; 
using namespace std;

#define dim @AddDim
#define dimIv @AddDimIv
#define dimOut @AddDimOut



/******************************/
/*  Optimization using CMAES  */
/******************************/

template<typename T>
class CMAES
{
public:
  //Constructor
  CMAES(T modelIn,
        const unsigned int lambdaIn,
        double sigmaIn, 
        const unsigned int nIterMaxIn, 
        const double tolIn,
        const bool useParallelIn) : 
  model(modelIn),
  lambda(lambdaIn), sigmaMem(sigmaIn), nIterMax(nIterMaxIn),
  tol(tolIn), tolFitness(1e-3), useParallel(useParallelIn) {}
  
  // Minimizes (minus) the log-likelihood using CMA-ES
  double Optimize(arma::vec& m) {
    const unsigned int n = m.n_elem;
    double sigma = sigmaMem;
    double mu = floor(lambda/2);
    arma::vec w = createw(lambda, n);
    double muEff = pow(accu(w(span(0, mu-1))), 2)/accu(pow(w(span(0, mu-1)), 2)); 
    double EN01 = std::pow(n, 0.5)*(1-1/(4*n)+1/(21*std::pow(n, 2)));
    double csig = (muEff+2)/(n + muEff+5);
    double dsig = 1 + 2*std::max(0.0, std::pow((muEff-1)/(n+1), 0.5)-1) + csig;
    double cc = (4 + muEff/n)/(n + 4 + 2*muEff/n);
    double c1 = 2/(std::pow(n + 1.3, 2) + muEff);
    double cb = 1;
    double cmu = std::min(1-c1, 2*(muEff- 2 + 1/muEff)/(std::pow(2+n, 2) + 2*muEff/2));
    double hsig = 0;
    unsigned int indexPastVal = 0;
    unsigned int maxPastVal = 95 + floor(30*n/lambda);
    unsigned int indexNewestVal = 0;
    arma::vec NewestVal(25);
    arma::vec OldestVal(25);
    
    unsigned int nTrial;
    arma::vec yw(n);
    arma::mat C = eye(n, n);
    arma::mat zlambda(n, lambda);
    arma::mat ylambda(n, lambda);
    arma::mat xlambda(n, lambda);
    arma::vec flambda(lambda);
    arma::vec psig = zeros(n);
    arma::vec pc = zeros(n);
    arma::Col<unsigned int> flambdaIndex(lambda);
    arma::vec D(n);
    arma::mat B(n, n);
    arma::vec tempM;
    arma::vec pastVal(maxPastVal);
    arma::Col<unsigned int> pastAvgResults(n, fill::zeros);
    arma::vec wo = w;
    unsigned int indexPastAvgResults = 0;
    
    // MAIN LOOP //
    for (unsigned int i=0; i<nIterMax; ++i) {
      // GENERATE NEW GENERATION OF CANDIDATES //
      eig_sym(D, B, C);
      D = pow(D, 0.5);
      // We can't have a parallel construct nested in a single construct, need to start a new parallel regin at each iteration of the for loop
#pragma omp parallel for default(shared) private(nTrial, tempM) if(useParallel)
      for (unsigned int j=0; j<lambda; ++j) { //Generate offsprings and compute their fitness
        nTrial = 0;
        do {
          zlambda.col(j) = randn(n);
          ylambda.col(j) = B*diagmat(D)*zlambda.col(j);
          xlambda.col(j) = m + sigma*ylambda.col(j);
          tempM = vec(xlambda.colptr(j), n, false, false);
          flambda(j) = model.Evaluate(tempM);
          nTrial++;
        } while (flambda(j)>=1e50 && nTrial<100); // Re-generate points untill the LLK is successfully computed
      }
      flambdaIndex = arma::sort_index(flambda, "ascend"); // sort points by fitness
      yw = ylambda.cols(flambdaIndex(arma::span(0, mu-1)))*w(span(0, mu-1));
      // SELECTION AND RECOMBINATION
      m = m + cb*sigma*yw; //update m taking the mean of the selected points
      // STEP-SIZE CONTROL
      psig = (1 - csig)*psig + std::pow(csig*(2-csig)*muEff, 0.5)*B*zlambda.cols(flambdaIndex(span(0, mu-1)))*w(span(0, mu-1));
      sigma = sigma*exp(csig/dsig*(norm(psig)/EN01-1));
      //COVARIANCE MATRIX ADAPTATION
      for (unsigned int j=mu;j<lambda; ++j) {
        wo(j)= w(j)*n/pow(norm(B*zlambda.col(flambdaIndex(j)), 2), 2);
      }
      hsig = ((norm(psig)/std::pow(1 - std::pow(1.0-csig, 2.0*(n+1.0)), 0.5)) < ((1.4 + 2/(n+1))*EN01)) ? 1.0 : 0.0;
      pc = (1-cc)*pc + hsig*std::pow(cc*(2-cc)*muEff, 0.5)*ylambda.cols(flambdaIndex(arma::span(0, mu-1)))*w(span(0, mu-1));
      C = (1 + c1*(1-hsig)*cc*(2-cc) - c1 - cmu*accu(wo))*C + c1*pc*pc.t() + cmu*ylambda.cols(flambdaIndex)*diagmat(wo)*ylambda.cols(flambdaIndex).t();
      C = trimatu(C) + trimatl(C, -1); //Enforce symmetry of C
      //if (std::abs((flambda(flambdaIndex(0))-flambda(flambdaIndex(mu-1)))/flambda(flambdaIndex(0)))<tolFitness) { //check for flatness
      //  sigma = sigma*exp(0.2+csig/dsig);
      //  Rcpp::Rcout<<"Warning: Flat fitness function"<<std::endl;
      //}
      //TERMINATION CRITERIA
      if (max(pc)<tol && max(sigma*C.diag())<tol) {
        if (useParallel==true) Rcpp::Rcout<<"Terminating successfully: pc and C's values are below threshold, at iteration: "<<i<<std::endl;
        break;
      }
      if (max(D)>pow(10, 14)*min(D)) {
        if (useParallel==true) Rcpp::Rcout<<"Terminating successfully: Excessive condition number of the covariance matrix, at iteration: "<<i<<std::endl;
        break;
      }
      (indexPastVal<maxPastVal-1) ? indexPastVal++ : indexPastVal = 0;
      (indexNewestVal<25-1) ? indexNewestVal++ : indexNewestVal=0;
      OldestVal(indexNewestVal) = pastVal(indexPastVal);
      pastVal(indexPastVal) = model.Evaluate(m);
      NewestVal(indexNewestVal) = pastVal(indexPastVal);
      if (i>maxPastVal+25 && std::abs(mean(OldestVal) - mean(NewestVal))<tol & std::abs(median(OldestVal) - median(NewestVal))<tol) {
        if (useParallel==true) Rcpp::Rcout<<"Terminating successfully: Stagnation of function value at m, at iteration: "<<i<<std::endl;
        break;
      }
      (indexPastAvgResults<n-1) ? indexPastAvgResults++ : indexPastAvgResults = 0;
      flambda(flambdaIndex(mu-1)) - flambda(flambdaIndex(0))<tol ? pastAvgResults(indexPastAvgResults)=1 : pastAvgResults(indexPastAvgResults) = 0;
      if (accu(pastAvgResults)>n/3) {
        if (useParallel==true) Rcpp::Rcout<<"Terminating successfully: Constant value for all best mu points, at iteration: "<<i<<std::endl;
        break;
      }
      if (norm(0.1*sigma*D(n-1)*B.col(n-1)/m)<tol) {
        if (useParallel==true) Rcpp::Rcout<<"Terminating successfully: A shock on the principal axis of C does not significantly change m, at iteration: "<<i<<std::endl;
        break;
      }
      //Rcpp::Rcout<<"generation: "<<i<<"flambda: "<<flambda(flambdaIndex(0))<<" "<<flambda(flambdaIndex(mu-1))<<" "<<pastVal(indexPastVal)<<" " <<max(abs(m))<<std::endl;
      if (flambda(flambdaIndex(mu-1))>1e45) break;
    }
    
    // generate and return output (best solution m and value at the best solution)
    return pastVal(indexPastVal);
  }
  
  void editModel(T& newModel) {
    model = newModel;
  }
  
private:
  T model; // a class containing a member function double Evaluate(arma::vec) to minimize
  const unsigned int lambda; 
  double sigmaMem; // used to reset sigma between two calls of the function with he genetic algorithm
  const unsigned int nIterMax;
  const double tol;
  const double tolFitness;
  const bool useParallel;
  const bool destroyPointers = false;
  arma::vec createw(const unsigned int LAMBDA, const unsigned int N) { // used to initialize w
    const unsigned int MU = floor(LAMBDA/2);
    arma::vec out(LAMBDA);
    for (unsigned int i=0; i<LAMBDA; ++i) {
      out(i) = log((LAMBDA+1)/2) - log(i+1);
    }
    double MUEFF = pow(accu(out(span(0, MU-1))), 2)/accu(pow(out(span(0, MU-1)), 2));
    double MUEFFminus = pow(accu(out(span(MU, LAMBDA-1))), 2)/accu(pow(out(span(MU, LAMBDA - 1)), 2));
    double C1 = 2/(std::pow(N + 1.3, 2) + MUEFF);
    double CC = (4 + MUEFF/N)/(N + 4 + 2*MUEFF/N);
    double CMU = std::min(1-C1, 2*(MUEFF- 2 + 1/MUEFF)/(std::pow(2+N, 2) + 2*MUEFF/2));
    double ALPHAMUminus = 1 + C1/CMU;
    double ALPHAMUEFFminus = 1 + 2*MUEFFminus/(MUEFF+2);
    double ALPHAPOSDEFminus = (1 - C1 - CMU)/(N*CMU);
    double SUMTEMPplus = accu(out(span(0, MU-1)));
    double SUMTEMPminus = std::abs(accu(out(span(MU, LAMBDA-1))));
    for (unsigned int i = 0; i<MU;++i) {
      out(i) *= 1/SUMTEMPplus;
    }
    for (unsigned int i = MU; i<LAMBDA;++i) {
      out(i) *= std::min(std::min(ALPHAMUminus, ALPHAMUEFFminus), ALPHAPOSDEFminus)/SUMTEMPminus;
    }
    return out;
  }
};


// SYSTEM OF DIFFERENTIAL EQUATION
@AddFunc
	

class minDistRK4
{
  
public:
  // CONSTRUCTOR
  minDistRK4(double* yInitIn,
             unsigned int ntIn,
             double bytIn,
             double** dataExogVarIn, 
             double** exogSamplingTimeIn, 
             int nExogVarIn,
             unsigned int* varMinDistIn,
             unsigned int nVarMinDistIn,
             double** dataMinDistIn,
             double** samplingTimeIn,
             double** pointsWeightIn) :
  yInit(yInitIn),
  nt(ntIn),
  byt(bytIn),
  dataExogVar(dataExogVarIn),
  exogSamplingTime(exogSamplingTimeIn),
  nExogVar(nExogVarIn),
  varMinDist(varMinDistIn), 
  nVarMinDist(nVarMinDistIn),
	dataMinDist(dataMinDistIn),
  samplingTime(samplingTimeIn),
  pointsWeight(pointsWeightIn) {}
	
	// COMPUTES INTERMEDIATE VARIABLES AT T=0	
	void getFullInitialPosition(double t, double* y, double* parms, double* yx, double** dataExogVar, double** exogSamplingTime, int nExogVar) {
		double ydot0[dim];
		for (unsigned int it=0; it<dim; it++) yx[it] = y[it];
		double* yptr = &yx[0];
		double* xptr = &yx[dim];
		int comptExogVar[nExogVar];
		for (unsigned int it=0; it<nExogVar; it++) comptExogVar[it]=1;
		Func(0, yptr, parms, ydot0, xptr, dataExogVar, exogSamplingTime, nExogVar, comptExogVar); // because yptr and xptr are pointers to elements of yx, elements in yx are directly filled by Func without having to do any copy
	}
	
	double EvaluateWithoutTryCatch(double* parms) {
		// INIT
		int it, it1, indexData;
		
		// To store number of points already explored in dataMinDist
		unsigned int arraycomptVarMinDist[nVarMinDist];
		for (it=0; it<nVarMinDist; it++) {
			arraycomptVarMinDist[it] = 1;
		}
		unsigned int* comptVarMinDist = &arraycomptVarMinDist[0];
		
		// Initialize pointer y
		double yy[dim];
		for (it=0; it<dim; ++it) {
			yy[it] = yInit[it];
		}
		double *y = &yy[0];
		double yx[dim+dimIv];
		double y1[dim], y2[dim], y3[dim], ydot0[dim], ydot1[dim], ydot2[dim], ydot3[dim], ydots[dim], x0[dimIv], x1[dimIv], x2[dimIv], x3[dimIv];
		
		double fit = 0;
		
		int comptExogVar[nExogVar];
		for (it=0; it<nExogVar; it++) {
		  comptExogVar[it] = 1;
		}
		// get intermediateVar and compute distance at t=0 //
		getFullInitialPosition(0, y, parms, yx, dataExogVar, exogSamplingTime, nExogVar);
		for (it1=0; it1<nVarMinDist; it1++) { // update fit
			if ( 0 >= samplingTime[it1][0]) {
				fit+=pointsWeight[it1][0]*std::abs((yx[varMinDist[it1]] - dataMinDist[it1][0])/dataMinDist[it1][0]);
			}
		}
		
		// MAIN LOOP (RK4 and compute distance)
		for (it=0; it<(nt-1); it++) {
			@AddEventTime
			@AddEventVar
			
			Func(it*byt, y, parms, ydot0, x0, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			
			for (it1=0; it1<dim; it1++)
				y1[it1] = y[it1] + ydot0[it1]*0.5*byt;
			Func((it + 0.5)*byt, y1, parms, ydot1, x1, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			
			for (it1=0; it1<dim; it1++)
				y2[it1] = y[it1] + ydot1[it1]*0.5*byt;
			Func((it + 0.5)*byt, y2, parms, ydot2, x2, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			
			for (it1=0; it1<dim; it1++)
				y3[it1] = y[it1] + ydot2[it1]*byt;
			Func((it+1)*byt, y3, parms, ydot3, x3, dataExogVar, exogSamplingTime, nExogVar, comptExogVar);
			
			for (it1=0; it1<dim; it1++) {
				ydots[it1] = (ydot0[it1] + 2.0*ydot1[it1] + 2.0*ydot2[it1] + ydot3[it1])/6.0;
				y[it1] = y[it1] + byt*ydots[it1];
				yx[it1] = y[it1];
			}
			
			for (it1=0; it1<dimIv; it1++) {
				yx[dim + it1] = (x0[it1] + 2.0*x1[it1] + 2.0*x2[it1] + x3[it1])/6.0;
			}
			for (it1=0; it1<nVarMinDist; it1++) { // update fit
				if ( (double) (it + 1)*byt>= samplingTime[it1][comptVarMinDist[it1]]) {
					fit+=pointsWeight[it1][comptVarMinDist[it1]]*std::abs((yx[varMinDist[it1]] - dataMinDist[it1][comptVarMinDist[it1]])/dataMinDist[it1][comptVarMinDist[it1]]);
					comptVarMinDist[it1]++;
				}
			}
		}
		return fit;
	}
	
	double Evaluate(double* parms) {
		double out = 0;
		try {
			out = EvaluateWithoutTryCatch(parms);
		}
		catch(...) {
			out = 1e50;
		}
		if (std::isnan(out)) out = 1e50;
		
		return out;
	}
	
private:
	double* yInit;
	unsigned int nt;
	double byt;
	double** dataExogVar; 
	double** exogSamplingTime; 
	int nExogVar;
	unsigned int* varMinDist;
	unsigned int nVarMinDist;
	double** dataMinDist;
	double** samplingTime;
	double** pointsWeight;
};

template<typename RK4>
class fixedMinDistRK4 {
public:
	fixedMinDistRK4(RK4* myRK4In, 
                 const bool* parmsFixedIn, 
                 const double* parmsFullInitIn,
                 const double* parmsLowerIn, 
                 const double* parmsUpperIn, 
                 const unsigned int nEltsParmsFullIn, 
                 const bool standardizeParmsIn) :
			myRK4(myRK4In), 
			parmsFixed(parmsFixedIn),
			parmsFullInit(parmsFullInitIn),
			parmsLower(parmsLowerIn),
			parmsUpper(parmsUpperIn), 
			nEltsParmsFull(nEltsParmsFullIn), 
			standardizeParms(standardizeParmsIn) {}
	
	void completeParms(arma::vec parmsPart, double* parmsFull) {
		unsigned int compt=0;
		for (unsigned int it=0; it<nEltsParmsFull; it++) {
			if (parmsFixed[it]==true) {
				parmsFull[it] = parmsPart[compt];
				compt++;
			} else {
				parmsFull[it] = parmsFullInit[it];
			}
		}
	}
	
	void standardizeParmsPart(arma::vec& parmsPart) {
		unsigned int compt=0;
		for (unsigned int it=0; it<nEltsParmsFull; it++) {
			if (parmsFixed[it]==true) {
				parmsPart[compt]-=parmsLower[it];
				parmsPart[compt]/=(parmsUpper[it]-parmsLower[it]);
				compt++;
			}
		}
	}
	
	void unstandardizeParmsPart(arma::vec& parmsPart) {
		unsigned int compt=0;
		for (unsigned int it=0; it<nEltsParmsFull; it++) {
			if (parmsFixed[it]==true) {
				parmsPart[compt]*=(parmsUpper[it]-parmsLower[it]);
				parmsPart[compt]+=parmsLower[it];
				compt++;
			}
		}
	}
	
	double Evaluate(arma::vec armaParmsPart) {
		if (standardizeParms==true) unstandardizeParmsPart(armaParmsPart);
		double parmsFullArray[nEltsParmsFull];
		double* parmsFull = &parmsFullArray[0];
		completeParms(armaParmsPart, parmsFull);
		double out = myRK4->Evaluate(parmsFull);
		// add penalty
		bool outOfBounds = false;
		for (unsigned int it=0; it<nEltsParmsFull; it++) {
			if (parmsFull[it]<parmsLower[it] || parmsFull[it]>parmsUpper[it]) {
				outOfBounds = true;
			}
		}
		if (outOfBounds==true) { //arbitrary large value added as penalty if outOfBounds
			out+=1e50; 
		}
		return out;
	}

private:
RK4* myRK4;
const bool* parmsFixed;
const double* parmsFullInit;
const double* parmsLower;
const double* parmsUpper;
const unsigned int nEltsParmsFull;
const bool standardizeParms;
};

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

// [[Rcpp::export]]
Rcpp::List minDistOptimForR(std::vector<double> Rparms,
                            std::vector<bool> RparmsFixed,
                            std::vector<double> RparmsLower,
                            std::vector<double> RparmsUpper,
                            std::vector<double> RyInit, 
                            unsigned int nt, 
                            double byt,
                            Rcpp::List RdataExogVar,
                            Rcpp::List RexogSamplingTime,
                            std::vector<unsigned int> RvarMinDist,
                            Rcpp::List RdataMinDist,
                            Rcpp::List RsamplingTime,
                            Rcpp::List RpointsWeight,
                            const unsigned int lambda,
                            double sigma, 
                            const unsigned int nIterMax, 
                            const double tol,
                            const bool standardizeParms,
                            const bool useParallel) {
	// INITIALIZATION //
	arma::vec RparmsInit(Rparms);
	double* parmsInit = &RparmsInit[0];
	double* parms = &Rparms[0];
	bool parmsFixedArray[RparmsFixed.size()];
	for (unsigned int it=0; it<RparmsFixed.size(); it++) {
		parmsFixedArray[it] = RparmsFixed[it];
	}
	bool* parmsFixed = &parmsFixedArray[0];
	double* parmsLower = &RparmsLower[0];
	double* parmsUpper = &RparmsUpper[0];
	unsigned int nEltsParmsPart = 0;
	arma::vec parmsPart(Rparms.size());
	for (unsigned int it=0; it<Rparms.size(); it++) {
		if (parmsFixed[it]==true) {
			parmsPart[nEltsParmsPart] = parms[it];
			nEltsParmsPart++;
		}
	}
	parmsPart.resize(nEltsParmsPart);
	
	double* yInit = &RyInit[0];
	unsigned int* varMinDist = &RvarMinDist[0];
	
	int nExogVar = RdataExogVar.size();
	double** dataExogVar = (double**) malloc(sizeof(double*)*RdataExogVar.size());
	double** exogSamplingTime = (double**) malloc(sizeof(double*)*RexogSamplingTime.size());
	RcppListToPptr(RdataExogVar, dataExogVar);
	RcppListToPptr(RexogSamplingTime, exogSamplingTime);

	double** dataMinDist = (double**) malloc(sizeof(double*)*RdataMinDist.size());
	double** samplingTime = (double**) malloc(sizeof(double*)*RsamplingTime.size());
	double** pointsWeight = (double**) malloc(sizeof(double*)*RpointsWeight.size());
	RcppListToPptr(RdataMinDist, dataMinDist);
	RcppListToPptr(RsamplingTime, samplingTime);
	RcppListToPptr(RpointsWeight, pointsWeight);
	// return Rcpp::List::create();
	minDistRK4 myMinDistRK4(yInit, nt, byt,
                         dataExogVar,
                         exogSamplingTime,
                         nExogVar,
                         varMinDist,
                         RvarMinDist.size(),
                         dataMinDist, 
                         samplingTime,
                         pointsWeight);
	
	fixedMinDistRK4<minDistRK4> myFixedMinDistRK4(&myMinDistRK4, 
										                            parmsFixed, 
										                            parms,
										                            parmsLower, 
										                            parmsUpper, 
										                            Rparms.size(), 
										                            standardizeParms);
	CMAES<fixedMinDistRK4<minDistRK4>> myCMAES(myFixedMinDistRK4,
                                           lambda,
                                           sigma, 
                                           nIterMax, 
                                           tol,
                                           useParallel);
	
	if (standardizeParms==true) myFixedMinDistRK4.standardizeParmsPart(parmsPart);
	double crit = myCMAES.Optimize(parmsPart);
	if (standardizeParms==true) myFixedMinDistRK4.unstandardizeParmsPart(parmsPart);
	// double crit = myFixedMinDistRK4.Evaluate(parmsPart);
	// double crit = 1;
	Rcpp::Rcout<<crit<<std::endl;
	unsigned int compt=0;
	for (unsigned int it=0; it<Rparms.size(); it++) {
		if (parmsFixed[it]==true) {
			Rparms[it]=parmsPart[compt];
			compt++;
		}
	}
	
	// FREE MEMORY
	for (unsigned int it=0; it<RdataMinDist.size(); it++) {
		free(dataMinDist[it]);
		free(samplingTime[it]);
		free(pointsWeight[it]);
	}
	free(dataMinDist);
	free(samplingTime);
	free(pointsWeight);
	
	return Rcpp::List::create(
		Named("criterion") = crit, 
		Named("parms") = Rparms);
}

// [[Rcpp::export]]
double ComputeDistanceForR(std::vector<double> Rparms, 
                          	std::vector<double> RyInit, 
                          	unsigned int nt, 
                          	double byt,
                          	Rcpp::List RdataExogVar,
                          	Rcpp::List RexogSamplingTime,
                          	std::vector<unsigned int> RvarMinDist,
                          	Rcpp::List RdataMinDist,
                          	Rcpp::List RsamplingTime,
                          	Rcpp::List RpointsWeight) {
	// INITIALIZATION //
	arma::vec RparmsInit(Rparms);
	double* parmsInit = &RparmsInit[0];
	double* parms = &Rparms[0];
	double* yInit = &RyInit[0];
	unsigned int* varMinDist = &RvarMinDist[0];
	
	double** dataExogVar = (double**) malloc(sizeof(double*)*RdataExogVar.size());
	double** exogSamplingTime = (double**) malloc(sizeof(double*)*RexogSamplingTime.size());
	RcppListToPptr(RdataExogVar, dataExogVar);
	RcppListToPptr(RexogSamplingTime, exogSamplingTime);
	int nExogVar = RdataExogVar.size();
	
	double** dataMinDist = (double**) malloc(sizeof(double*)*RdataMinDist.size());
	double** samplingTime = (double**) malloc(sizeof(double*)*RsamplingTime.size());
	double** pointsWeight = (double**) malloc(sizeof(double*)*RpointsWeight.size());
	RcppListToPptr(RdataMinDist, dataMinDist);
	RcppListToPptr(RsamplingTime, samplingTime);
	RcppListToPptr(RpointsWeight, pointsWeight);
	
	
	minDistRK4 myMinDistRK4(yInit, nt, byt,
                         dataExogVar,
                         exogSamplingTime,
                         nExogVar,
                         varMinDist,
                         RvarMinDist.size(),
                         dataMinDist, 
                         samplingTime,
                         pointsWeight);
	double out = myMinDistRK4.Evaluate(parms);
	for (unsigned int it=0; it<RdataMinDist.size(); it++) {
		free(dataMinDist[it]);
		free(samplingTime[it]);
		free(pointsWeight[it]);
	}
	free(dataMinDist);
	free(samplingTime);
	free(pointsWeight);
	return out;
}

// [[Rcpp::export]]
std::vector<double> getFulInitialPositionForR(std::vector<double> Rparms, 
                  							        			std::vector<double> Ry, 
                  							        			Rcpp::List RdataExogVar,
                  							        			Rcpp::List RexogSamplingTime) {
	// INITIALIZATION //
	double* parms = &Rparms[0];
	double* y = &Ry[0];
	
	double** dataExogVar = (double**) malloc(sizeof(double*)*RdataExogVar.size());
	double** exogSamplingTime = (double**) malloc(sizeof(double*)*RexogSamplingTime.size());
	RcppListToPptr(RdataExogVar, dataExogVar);
	RcppListToPptr(RexogSamplingTime, exogSamplingTime);
	int nExogVar = RdataExogVar.size();
	
	
	// init empty objects to initialize class (ugly but it works...)
	unsigned int nt;
	double byt;
	double** dataMinDist;
	double** samplingTime;
	double** pointsWeight;
	unsigned int* varMinDist;
	// END OF DATA CONVERSION
	
	minDistRK4 myMinDistRK4(y, nt, byt,
                         dataExogVar,
                         exogSamplingTime,
                         nExogVar,
                         varMinDist,
                         0,
                         dataMinDist, 
                         samplingTime,
                         pointsWeight);
	
	std::vector<double> yx(dim+dimIv);
	myMinDistRK4.getFullInitialPosition(0, y, parms, &yx[0], dataExogVar, exogSamplingTime, nExogVar);
	return yx;
}	

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
				y[it1] = y[it1] + byT*ydots[it1];
				out(it+1, it1) = y[it1];
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