/*
 * PythonHelpers_test.cpp
 *
 *  Created on: Jun 10, 2013
 *      Author: phcostello
 */






#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>


#include <SimpleBootStrap.h>
#include <LinearZeroesInnerCurve.h>
#include <InstrumentDF.h>
#include <GeneralCurveInstrument.h>
#include <PythonHelpers.h>


using namespace std;

BOOST_AUTO_TEST_SUITE( PythonHelpersSuite)

BOOST_AUTO_TEST_CASE( curve_construction )
{
	SimpleBootStrap curve = CurveBootStrapLZ();
	DepoInstrument depo1( 0.05, 1.0 );
	curve.addInstrument(depo1);
	curve.fit();
	double df = curve.getDF(0.5);
	BOOST_MESSAGE("The df is " << df << '\n');

}

BOOST_AUTO_TEST_SUITE_END()

