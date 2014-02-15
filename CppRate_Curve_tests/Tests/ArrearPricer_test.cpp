/*
 * ArrearPricer_test.cpp
 *
 *  Created on: Sep 7, 2013
 *      Author: phcostello
 */
// analytic pricer

#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>
#include <vector>
#include <AnalyticFormulas.h>
#include <VanillaIntPricer.h>
#include <ParkMiller.h>
#include <AntiThetic.h>
#include <ConvergenceTable.h>
//#include <armadillo>


using namespace std;

BOOST_AUTO_TEST_SUITE( ArrearsPricer)

BOOST_AUTO_TEST_CASE( Check_FRA_Arrears_Formula )
{
	//Check that FRA_Arrears_Working
	double Spot_fr = 0.07;
	double Strike = 0.05;
	double tau = 0.5;
	double Vol = 0.20;
	double Expiry = 5.0;
	double ZCB = 0.65;

	//I think ZCBT2 should be in formulas with T2 numeraire and ZCB when using T1

	double ZCBT2 = ZCB/(1+Spot_fr*tau);

	double res_anal, res_int, res_mc;
	res_anal = FRA_Arrears( Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCBT2);

	BOOST_MESSAGE( "Analytic Arrears = " << res_anal);
	//Check we get rates back
	int num_intervals=100;
	VanillaIntPricer vp1;
	res_int = vp1.price(Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCBT2,
						num_intervals);



	BOOST_MESSAGE( "NumInt Arrears = " << res_int);

	int num_paths =10000;
	RandomParkMiller generator(1);
	AntiThetic genTwo(generator);

	res_mc = vp1.MCprice(Spot_fr,
							Strike,
							Vol,
							tau,
							Expiry,
							ZCBT2,
							num_paths,
							genTwo);

	BOOST_MESSAGE( "MC Arrears = " << res_mc);

	StatisticsMean theGatherer;
	ConvergenceTable CT(theGatherer);

	RandomParkMiller generator3(1);
	AntiThetic gen4(generator3);

	int discretization = 50;

	vp1.MCprice_stepper(Spot_fr,
			Strike,
			Vol,
			tau,
			Expiry,
			ZCB,
			num_paths,
			discretization,
			gen4,
			CT);

	vector<vector<double > > res_mc_stepper = CT.GetResultsSoFar();
	BOOST_MESSAGE( "MC Arrears stepper = " << res_mc_stepper[res_mc_stepper.size()-1][0]<< " " <<
			res_mc_stepper[res_mc_stepper.size()-1][1]);


	StatisticsMean theGatherer2;
	ConvergenceTable CT2(theGatherer2);
	RandomParkMiller generator5(1);
	AntiThetic gen6(generator5);
	int disc = 50;

	vp1.MCprice_predCor(Spot_fr,
				Strike,
				Vol,
				tau,
				Expiry,
				ZCB,
				num_paths,
				disc,
				gen6,
				CT2);

		vector<vector<double > > res_mc_predCor = CT2.GetResultsSoFar();
		BOOST_MESSAGE( "MC Arrears predCor = " << res_mc_predCor[res_mc_predCor.size()-1][0]<< " " <<
				res_mc_predCor[res_mc_predCor.size()-1][1]);

}

BOOST_AUTO_TEST_SUITE_END()

//product - NPV member

// in arrears fra

// in arrears caplet

// numerical integrator

// model 1 rate

//Classes
// product - base
// - eval method

// fra
// * payoff - forward - strike
// * rate time = T_1 - T_2
// * evolution time, T_2

// arrears fra

//etc

//arrears_pricing_engine(curve, vol , random_gen, stepping_method)

//test price in analytic price of in arrears fra

//test in arrears fra, caplet

//test model - model( curve, vol)
// model.fit(T_1, T_2)

// product(Pay off, Evolution)

// random_gen = random_generator

// mc_pricing_engine(model, random_generator, stepping_method,max_num_path,tol)
// * stop tol ?
// * pricing_engine.eval(results)

// product.eval(pe, statistics)

//fra.eval(analytic, result) /
//fra.eval(mc_bgm, result)

// functional
//fra_anal_price( Strike, Spot, T_1, T_2)
//fra_anal_arr( Strike, Spot, T_1, T_2, vol)
//caption_anal_price( Strike, Spot, T_2, T_2, vol)
//fra_numerical_int( Strike, Spot, T_1, T_2)
//fra_arrears_int( Strike, Spot, vol, T_1, T_2)
//caption_numerical_int( Strike, Spot, vol, T_1, T_2)
//fra_mc_price( Strike, T_1, T_2, vol, random_gen_stepping, max_num, tol, use_tol, results)
//fra_mc_arrears( Strike, T_1, T_2, vol, random_gen_stepping, max_num, tol, use_tol, results)
//caption_mc_arrears( Strike, T_1, T_2, vol, random_gen_stepping, max_num, tol, use_tol, results)

// define loop num_path
// stepping num
