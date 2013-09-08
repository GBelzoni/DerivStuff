/*
 * ArrearPricer_test.cpp
 *
 *  Created on: Sep 7, 2013
 *      Author: phcostello
 */
// analytic pricer

#include <vector>
#include <AnalyticFormulas.h>
#include <VanillaIntPricer.h>


using namespace std;


int main()
{
	//Check that FRA_Arrears_Working
	double Spot_fr = 0.06;
	double Strike = 0.07;
	double tau = 0.5;
	double Vol = 0.20;
	double Expiry = 10.0;
	double ZCB = 0.5;

	double res_anal, res_int, res_mc;
	res_anal = FRA_Arrears( Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCB);

	cout << res_anal << endl;
	//Check we get rates back
	int num_intervals=100000;
	VanillaIntPricer vp1;
	res_int = vp1.price(Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCB,
						num_intervals);

	cout << res_int << endl;
//	res_int = FRA_Arrears_mc(Spot_fr,
//							Strike,
//							Vol,
//							tau,
//							Expiry,
//							ZCB);

	return 0;

}

