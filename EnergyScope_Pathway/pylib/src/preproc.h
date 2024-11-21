#ifndef PREPROC_H
#define PREPROC_H

// parameters to define prior to compile time

#define UseRCPP 0 		// true if the code is called from R(via RCPP), false if it is directly called from c++
#define UseParallel 1		// CPU-parallelized algorithm (1), or sequential algorithm (0). 
#define UseEventTime 0		// Use time events (1) or ignore them (0)
#define UseEventVar 0		// Use variables events (1) or ignore them (0)
#define ReturnRK4 3		// Define what to store and return with RK4: 0 for variables only, 1 for variables and time derivatives, 2 for variables and intermediate variables and 3 for variables, time derivatives and intermediate variables
#define VerboseCMAES 0
#endif
