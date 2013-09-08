/*
 * PayOffFRA.h
 *
 *  Created on: Sep 8, 2013
 *      Author: phcostello
 */

#ifndef PAYOFFFRA_H_
#define PAYOFFFRA_H_

#include "PayOff3.h"

class PayOffFRA: public PayOff {
public:
	PayOffFRA( double Strike_);
	virtual ~PayOffFRA();

	virtual double operator()(double Spot) const;
	virtual PayOff* clone() const;

private:

	double Strike;
};

#endif /* PAYOFFFRA_H_ */
