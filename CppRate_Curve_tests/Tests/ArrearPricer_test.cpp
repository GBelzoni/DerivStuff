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


using namespace std;

BOOST_AUTO_TEST_SUITE( ArrearsPricer)


BOOST_AUTO_TEST_CASE( Check_FRA_Arrears_Formula )
{
	//Check that FRA_Arrears_Working
	double Spot_fr = 0.06;
	double Strike = 0.07;
	double tau = 0.5;
	double Vol = 0.2;
	double Expiry = 10.0;
	double ZCB = 0.5;

	double res_anal, res_int, res_mc;
	res_anal = FRA_Arrears( Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCB);

	BOOST_MESSAGE( "Analytic Arrears = " << res_anal);
	//Check we get rates back
	int num_intervals=100;
	VanillaIntPricer vp1;
	res_int = vp1.price(Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCB,
						num_intervals);

	BOOST_MESSAGE( "NumInt Arrears =anal " << res_int);

//	res_int = FRA_Arrears_mc(Spot_fr,
//							Strike,
//							Vol,
//							tau,
//							Expiry,
//							ZCB);



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
