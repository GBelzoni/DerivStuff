/*
 * VanillaIntPricer.cpp
 *
 *  Created on: Sep 8, 2013
 *      Author: phcostello
 */

#include "VanillaIntPricer.h"//x_n = lower_limit = -4
#include "Utility.h"
#include <vector>
#include <math.h>

VanillaIntPricer::VanillaIntPricer() {
	// TODO Auto-generated constructor stub

}

VanillaIntPricer::~VanillaIntPricer() {
	// TODO Auto-generated destructor stub
}

double VanillaIntPricer::price(double Spot,
		double Strike,
		double Vol,
		double tau,
		double Expiry,
		double ZCB,
		int num_intervals)
{
	//take interval and slice into range

	double steps = num_intervals;
	double interval_size = 40.0/steps;

	std::vector<double> range = vecseq(-20.0,20.0, steps );
	range.pop_back();
	double total = 0;

	double thisSpot;
	double thisPayOff;
	double thisScaledPayOff;

	for( double x_n : range){

		//CalcSpot
		thisSpot = Spot*exp( -0.5*Vol*Vol*(Expiry-tau) + Vol*sqrt(Expiry-tau)*x_n);
		//CalcPayOff
		thisPayOff = tau*(thisSpot-Strike)*(1.0 + tau*thisSpot);
		thisScaledPayOff = thisPayOff*(1.0/sqrt(2 * M_PI))*exp(-0.5*x_n*x_n);
		total += thisScaledPayOff*interval_size;

	}

	total = total*ZCB;

	return total;


}
