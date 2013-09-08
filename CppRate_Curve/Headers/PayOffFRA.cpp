/*
 * PayOffFRA.cpp
 *
 *  Created on: Sep 8, 2013
 *      Author: phcostello
 */

#include "PayOffFRA.h"

PayOffFRA::PayOffFRA( double Strike_): Strike(Strike_)
{
}

PayOffFRA::~PayOffFRA() {
	// TODO Auto-generated destructor stub
}

PayOff* PayOffFRA::clone() const
{
	return new PayOffFRA( *this);
}

double PayOffFRA::operator ()(double Spot) const {

	return Spot-Strike;
}
