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
#include <Arrays.h>


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
		thisSpot = Spot*exp( -0.5*Vol*Vol*(Expiry) + Vol*sqrt(Expiry)*x_n);
		//CalcPayOff
		thisPayOff = tau*(thisSpot-Strike)*(1.0 + tau*thisSpot);
		thisScaledPayOff = thisPayOff*(1.0/sqrt(2 * M_PI))*exp(-0.5*x_n*x_n);
		total += thisScaledPayOff*interval_size;

	}

	total = total*ZCB;

	return total;


}

//This function is for testing MC arrears pricing with P1 numeraire
double VanillaIntPricer::MCprice(double Spot,
		double Strike,
		double Vol,
		double tau,
		double Expiry,
		double ZCB,
		int num_paths,
		RandomBase& theGenerator)
{


	//Do loop
	double total = 0;

	double thisSpot;
	double thisPayOff;
	double x_n;
	MJArray VariateArray(1);
	theGenerator.ResetDimensionality(1);

	for( int i=0; i<num_paths; i++){

		//Draw a random gaussian
		theGenerator.GetGaussians(VariateArray);
		x_n = VariateArray[0];
		//CalcSpot
		thisSpot = Spot*exp( -0.5*Vol*Vol*(Expiry) + Vol*sqrt(Expiry)*x_n);
		//CalcPayOff
		thisPayOff = tau*(thisSpot-Strike)*(1.0 + tau*thisSpot);
		total += thisPayOff;

	}

	total = total*ZCB/num_paths;

	return total;


}

//This function is for testing MC arrears pricing with P0 numeraire
void VanillaIntPricer::MCprice_stepper(double Spot,
		double Strike,
		double Vol,
		double tau,
		double Expiry,
		double ZCB,
		int num_paths,
		int discretization,
		RandomBase& theGenerator,
		StatisticsMC& theGatherer)
{

	//Do loop
	double thisSpot;
	double thisPayOff;
	double thisResult;

	//For stepping
	double dt = Expiry/discretization;

	MJArray VariateArray(discretization);
	theGenerator.ResetDimensionality(discretization);

	double discVol = Vol*sqrt(dt); //make sure to get vol over step

	for( int i=0; i<num_paths; i++){

		//Generate one path
		//Draw a random gaussians
		theGenerator.GetGaussians(VariateArray);
		//CalcSpot
		thisSpot = Spot;
		//Stepping loop - use f(t,T0,T1) path in P(t,T0) numeraire as in Joshi (14.14) p331
		for( int j=0 ; j<discretization; j++)
		{
			thisSpot += ((tau*thisSpot*thisSpot)/(1.0+tau*thisSpot))*Vol*Vol*dt*dt + discVol*thisSpot*VariateArray[j]; //Drift evolution

		}

		//Do one path
		thisPayOff = tau*(thisSpot-Strike); //CalcPayOff
		thisResult = thisPayOff*ZCB; //Mult by numeraire
		theGatherer.DumpOneResult(thisResult);

	}

}



//This function is for testing MC arrears pricing with P0 numeraire
void VanillaIntPricer::MCprice_predCor(double Spot,
		double Strike,
		double Vol,
		double tau,
		double Expiry,
		double ZCB,
		int num_paths,
		RandomBase& theGenerator,
		StatisticsMC& theGatherer)
{

	//Do loop
	double initDrift;
	double predSpot;
	double predDrift;
	double averageDrift;
	double correctedSpot;
	double thisPayOff;
	double thisResult;

	//For stepping


	MJArray VariateArray(1);
	theGenerator.ResetDimensionality(1);

	for( int i=0; i<num_paths; i++){


		//Prediction Correction
		//Generate one path
		//Draw a random gaussians
		theGenerator.GetGaussians(VariateArray);
		//CalcSpot

		initDrift = (tau*Spot*Spot)/(1.0+tau*Spot)*Vol*Vol*Expiry*Expiry;

		predSpot = Spot + initDrift + Vol*sqrt(Expiry)*Spot*VariateArray[0];

		predDrift = (tau*predSpot*predSpot)/(1.0+tau*predSpot)*Vol*Vol*Expiry*Expiry;

		averageDrift = (initDrift + predDrift)/2.0;

		correctedSpot = Spot + averageDrift + Vol*sqrt(Expiry)*Spot*VariateArray[0];



		//Do one path
		thisPayOff = tau*(correctedSpot-Strike); //CalcPayOff
		thisResult = thisPayOff*ZCB; //Mult by numeraire
		theGatherer.DumpOneResult(thisResult);

	}

}



