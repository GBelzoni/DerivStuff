/*
 * GeneratePath.h
 *
 *  Created on: Aug 29, 2013
 *      Author: phcostello
 */

#ifndef GENERATEPATH_H_
#define GENERATEPATH_H_

#include <Random2.h>
#include <Parameters.h>


double GeneratePath( const Parameters& r,
		double S0,
		const Parameters& sigma,
		double Expiry,
		int numSteps,
		RandomBase& generator);

//Shortsteps path generation for given interval [0, Expiry] and number of steps
//Takes general paramaters




#endif /* GENERATEPATH_H_ */
