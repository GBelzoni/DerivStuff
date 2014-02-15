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
		thisPayOff = tau*max(thisSpot-Strike,0.0)*(1.0 + tau*thisSpot);
//		thisPayOff = tau*(thisSpot-Strike)*(1.0 + tau*thisSpot);
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
		thisPayOff = tau*max(thisSpot-Strike,0.0)*(1.0 + tau*thisSpot);
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
			thisSpot += ((tau*thisSpot*thisSpot)/(1.0+tau*thisSpot))*Vol*Vol*dt + discVol*thisSpot*VariateArray[j]; //Drift evolution

		}

		//Do one path
		thisPayOff = tau*max(thisSpot-Strike,0.0); //CalcPayOff
//		thisPayOff = tau*(thisSpot-Strike); //CalcPayOff
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
		int discretization,
		RandomBase& theGenerator,
		StatisticsMC& theGatherer)
{

	//Do loop
	double thisSpot;
	double initDrift;
	double predSpot;
	double predDrift;
	double averageDrift;
	double thisPayOff;
	double thisResult;

	//For stepping
	//For stepping
	double dt = Expiry/discretization;

	MJArray VariateArray(discretization);
	theGenerator.ResetDimensionality(discretization);

	for( int i=0; i<num_paths; i++){


		//Prediction Correction
		//Generate one path
		//Draw a random gaussians
		theGenerator.GetGaussians(VariateArray);
		//CalcSpot

		double discVol = Vol*sqrt(dt); //make sure to get vol over step

		thisSpot = Spot;

		for( int j=0 ; j<discretization; j++)
		{
			initDrift = (tau*thisSpot*thisSpot)/(1.0+tau*thisSpot)*Vol*Vol*dt;
			predSpot = thisSpot + initDrift + Vol*sqrt(dt)*thisSpot*VariateArray[j];
			predDrift = (tau*predSpot*predSpot)/(1.0+tau*predSpot)*Vol*Vol*dt;
			averageDrift = (initDrift + predDrift)/2.0;
			thisSpot = thisSpot + averageDrift + Vol*sqrt(dt)*thisSpot*VariateArray[j];

		}




		//Do one path
		thisPayOff = tau*max(thisSpot-Strike,0.0); //CalcPayOff
		thisResult = thisPayOff*ZCB; //Mult by numeraire
		theGatherer.DumpOneResult(thisResult);

	}

}



