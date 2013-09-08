/*
 * SimpleBootStrap_test.cpp
 *
 *  Created on: Jun 6, 2013
 *      Author: phcostello
 */




#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>
#include <vector>
#include <AnalyticFormulas.h>

using namespace std;

BOOST_AUTO_TEST_SUITE( AnalyticFormulas)


BOOST_AUTO_TEST_CASE( Check_FRA_Arrears_Formula )
{
	//Check that FRA_Arrears_Working
	double Spot_fr = 0.06;
	double Strike = 0.07;
	double tau = 0.5;
	double Vol = 0.2;
	double Expiry = 10.0;
	double ZCB = 0.5;

	double res;
	res = FRA_Arrears( Spot_fr,
						Strike,
						Vol,
						tau,
						Expiry,
						ZCB);

	//Check we get rates back

	BOOST_CHECK_CLOSE(res,-0.0023536,0.01);

}

BOOST_AUTO_TEST_SUITE_END()
