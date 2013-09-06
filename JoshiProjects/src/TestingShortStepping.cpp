/*
 * TestingShortStepping.cpp
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
#include "SimpleMCwithTol.h"
#include "GeneratePath.h"

using namespace std;
using namespace arma;

int main(){

//	Set tolerance for pricing.

// Price by usual monte-carlo
	double Spot = 100;
	double Strike = 110;
    double r = 0.05;
    double d = 0.0;
    double Vol = 0.05;
    double Expiry = 1.0;

    //Calculating functions
    double BSCprice = BlackScholesDigitalCall( Spot,
                                     Strike,
                                     r,
                                     d,
                                     Vol,
                                     Expiry);
    cout << "Analytic Price"<< BSCprice << endl;

    //Monte Carlo Engine from Joshi

    ParametersConstant VolParam(Vol);
    ParametersConstant rParam(r);

    StatisticsMean gatherer;
    MoreStatisticsMC gathererMore;
    ConvergenceTable gathererTwo(gatherer);

    RandomParkMiller generator(1);
    AntiThetic GenTwo(generator);


    vector<vector<double> > results;

    //Vanilla Euro Call
    PayOffDigitalCall thePayOff(Strike);
    VanillaOption theOption(thePayOff,Expiry);

    double tol = 1e-5;
    double maxLoops = 5e7;
    SimpleMonteCarlo_tol(theOption,
    							Spot,
    							VolParam,
    							rParam,
    							tol,
    							maxLoops,
    							gathererTwo,
    							GenTwo,
    							BSCprice);

    results= gathererTwo.GetResultsSoFar();

    vec vres(results[results.size()-1]);
    cout << vres.t();

//    for(auto itm: results)
//    {
//    	vec thisRow(itm);
//    	cout << thisRow.t();
//    }



    int steps = 50;
    StatisticsMean gatherer_stepper;
    ConvergenceTable CT_stepper(gatherer_stepper);

    RandomParkMiller gen_stepper(steps);

    SimpleStepping_tol(theOption,
    					Spot,
    					VolParam,
    					rParam,
    					tol,
    					maxLoops,
    					steps,
    					CT_stepper,
    					gen_stepper,
    					BSCprice);

    results = CT_stepper.GetResultsSoFar();

    vec vres2(results[results.size()-1]);
        cout << vres2.t();

//    for(auto itm: results)
//    {
//    	vec thisRow(itm);
//    	cout << thisRow.t();
//    }


//Price by shortstepping

// Test path generation working
//	double r2 = 0.15;
//	double S0= 100.0;
//	double sigma = 0.20;
//	double Expiry2 = 1.0;
//	int numSteps = 100;
//	RandomParkMiller generator2(numSteps);
//
//	double thisPath;
//
//	vector<double> Result;
//
//	for( int i = 0; i<100000 ; i++){
//
//		thisPath = GeneratePath(r2,
//											S0,
//											sigma,
//											Expiry2,
//											numSteps,
//											generator2);
//
//		Result.push_back(thisPath);
//
//	}
//
//	mat Res2(Result);
//	Res2.save("Path.csv",csv_ascii);
//

return 0;
}


