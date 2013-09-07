/*
 * SimpleMCwithTol.cpp
 *
 *  Created on: Aug 29, 2013
 *      Author: phcostello
 */
//
//
//                      SimpleMC8.cpp
//
//
#include"SimpleMCwithTol.h"
#include <cmath>
#include <Arrays.h>
#include "GeneratePath.h"
// the basic math functions should be in namespace std but aren't in VCPP6
#if !defined(_MSC_VER)
using namespace std;
#endif

void SimpleMonteCarlo_tol(const VanillaOption& TheOption,
						 double Spot,
						 const Parameters& Vol,
						 const Parameters& r,
                         double tol,
                         double maxLoops,
						 StatisticsMC& gatherer,
                         RandomBase& generator,
                         double target)
{
    generator.ResetDimensionality(1);

    double Expiry = TheOption.GetExpiry();
	double variance = Vol.IntegralSquare(0,Expiry);
	double rootVariance = sqrt(variance);
	double itoCorrection = -0.5*variance;
	double movedSpot = Spot*exp(r.Integral(0,Expiry) +itoCorrection);

	double thisSpot;
    double discounting = exp(-r.Integral(0,Expiry));

    MJArray VariateArray(1);

    double error = 100.0;
    double loops = 0.0;
	double running_sum = 0.0;
    double prev_res = 0.0;

	while( (abs(error) > tol) && (loops < maxLoops))
	{
        generator.GetGaussians(VariateArray);
		thisSpot = movedSpot*exp( rootVariance*VariateArray[0]);
		double thisPayOff = TheOption.OptionPayOff(thisSpot);
        gatherer.DumpOneResult(thisPayOff*discounting);
        if(loops > 0){
        	prev_res = running_sum/loops;
        	running_sum += thisPayOff*discounting;
        	loops++;
        	error = abs(target - running_sum/loops);
        }
        else{
        	running_sum += thisPayOff*discounting;
        	loops++;
        }



	}

    return;
}

void SimpleStepping_tol(const VanillaOption& TheOption,
		double Spot,
		const Parameters& Vol,
		const Parameters& r,
		double tol,
		double maxLoops,
		int numSteps,
		StatisticsMC& gatherer,
		RandomBase& generator,
		double target)
{

	generator.ResetDimensionality(numSteps);

    double Expiry = TheOption.GetExpiry();
	double variance = Vol.IntegralSquare(0,Expiry)/Expiry;
	double rootVariance = sqrt(variance);
	double rr = r.Integral(0,Expiry)/Expiry;
	double discounting = exp(-r.Integral(0,Expiry));

    MJArray VariateArray(numSteps);

    double error = 100.0;
    double loops = 0.0;
	double running_sum = 0.0;
    double prev_res = 0.0;



	while( (abs(error) > tol) && (loops < maxLoops))
	{
        generator.GetGaussians(VariateArray);
        //Very similar to simple MC but generates thisSpot by stepping
        double thisSpot = GeneratePath(r,
        							Spot,
        							Vol,
        							Expiry,
        							numSteps,
        							generator);

        double thisPayOff = TheOption.OptionPayOff(thisSpot);
        gatherer.DumpOneResult(thisPayOff*discounting);
        if(loops > 0){
        	prev_res = running_sum/loops;
        	running_sum += thisPayOff*discounting;
        	loops++;
        	error = abs(target - running_sum/loops);
        }
        else{
        	running_sum += thisPayOff*discounting;
        	loops++;
        }



	}

    return;



}
