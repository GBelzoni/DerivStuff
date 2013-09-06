/*
 * TestingVolStrikePrice.cpp
 *
 *  Created on: Aug 29, 2013
 *      Author: phcostello
 */

#include <iostream>
#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <boost/foreach.hpp>

#include <armadillo>

//Joshi includes
#include <BlackScholesFormulas.h>
#include <Vanilla3.h>
#include "VanillaPayOffs.h"
#include <MCStatistics.h>
#include <ConvergenceTable.h>
#include <AntiThetic.h>
#include <ParkMiller.h>
#include <SimpleMC8.h>

//My project includes
#include "AnalyticFormulas.h"
#include "Utility.h"
#include "MoreStatisticsMC.h"
#include "Utility.h"

using namespace std;
using namespace arma;

int main(){



		double Spot = 90;
		double Strike = 100;
	    double r = 0.05;
	    double d = 0.0;
	    double Vol = 0.1;
	    double Expiry = 1.0;


	    //Vanilla Euro Call
	    PayOffCall thePayOff(Strike);
	    VanillaOption theOption(thePayOff,Expiry);

	    //Calculating functions
	    double BSCprice = BlackScholesCall( Spot,
	                                 Strike,
	                                 r,
	                                 d,
	                                 Vol,
	                                 Expiry);

	//Generate bunch of strikes and spots
	vec strikes = linspace(100,110, 20);
	vec spots = linspace(100,110, 20);
	//Generate vols from 0.01 to 1
	vec vols = linspace( 0.01, 1.0 , 10);
	mat spots_strikes = join_rows(spots, strikes);

	double thisPrice;

	mat ResultTable = ones(4).t();


	for( unsigned int i =0 ; i < spots_strikes.n_rows; i++)
	{
		for( double vol : vols){


			vec this_result;
			mat this_ss(spots_strikes.row(i));
			Spot = this_ss[0];
			Strike = this_ss[1];
			Vol = vol;

			thisPrice = BlackScholesDigitalCall( Spot,
					Strike,
					r,
					d,
					Vol,
					Expiry);

			this_result << Spot << Strike << Vol << thisPrice << endr;
			ResultTable.insert_rows(ResultTable.n_rows,this_result.t());
		}

	}

	//Write to table
	cout << ResultTable;
	ResultTable.save("ResultsTable.csv",csv_ascii);


	return 0;
}





