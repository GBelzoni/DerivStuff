/*
 * GeneratePath.cpp
 *
 *  Created on: Aug 29, 2013
 *      Author: phcostello
 */

#include "GeneratePath.h"
#include "Arrays.h"
#include <cmath>
#include <vector>


double GeneratePath(const Parameters& r,
						double S0,
						const Parameters& sigma,
						double Expiry,
						int numSteps,
						RandomBase& generator) {

	//Gen final draw given steps, expiry, r, vol, generator, so
	//S = S + r*S*delT + S*sigma*sqrt*delT*normal_val[i]

	MJArray nvariates(numSteps);
	//Next line resets seed so keeps generating same randoms
//	generator.ResetDimensionality(numSteps);

	generator.GetGaussians(nvariates);

	double S = S0;
	double delT = Expiry/ numSteps;
	std::vector<double> times_v;

	for(int i = 0 ; i <= numSteps; i++ )
	{
		times_v.push_back( i*delT);
	}

	for( int i =0 ; i<numSteps; i++){

		double thisR = r.Integral(times_v[i],times_v[i+1]);
		double thisVol = sqrt(sigma.IntegralSquare(times_v[i],times_v[i+1]));
		S = S + thisR*S + S*thisVol*nvariates[i];

	}

	return S;
}


