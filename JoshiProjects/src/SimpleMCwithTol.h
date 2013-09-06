/*
 * SimpleMCwithTol.cpp
 *
 *  Created on: Aug 29, 2013
 *      Author: phcostello
 */

#ifndef SIMPLEMCTOL	_H
#define SIMPLEMCTOL_H

#include <Vanilla3.h>
#include <Parameters.h>
#include <Random2.h>
#include <MCStatistics.h>
//Currently takes tolerance and target
//Should take tolerance and calc error via 2*sd where sd is estimated via
//running sum of squares - mean^2.

void SimpleMonteCarlo_tol(const VanillaOption& TheOption,
						 double Spot,
						 const Parameters& Vol,
						 const Parameters& r,
                         double tol,
                         double maxLoops,
						 StatisticsMC& gatherer,
                         RandomBase& generator,
                         double target);


void SimpleStepping_tol( const VanillaOption& TheOption,
						 double Spot,
						 const Parameters& Vol,
						 const Parameters& r,
                         double tol,
                         double maxLoops,
                         int numSteps,
						 StatisticsMC& gatherer,
                         RandomBase& generator,
                         double target);


#endif




