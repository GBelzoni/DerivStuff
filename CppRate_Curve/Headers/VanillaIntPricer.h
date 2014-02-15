/*
 * VanillaIntPricer.h
 *
 *  Created on: Sep 8, 2013
 *      Author: phcostello
 */

#ifndef VANILLAINTPRICER_H_
#define VANILLAINTPRICER_H_

#include <nr3.h>
#include <quadrature.h>
#include <PayOffFRA.h>
#include <VanillaPayOffs.h>
#include <Random2.h>
#include <MCStatistics.h>

class VanillaIntPricer {
public:
	VanillaIntPricer();
	virtual ~VanillaIntPricer();

	double price(double Spot,
					double Strike,
					double Vol,
					double tau,
					double Expiry,
					double ZCB,
					int num_intervals);

	double MCprice(double Spot,
					double Strike,
					double Vol,
					double tau,
					double Expiry,
					double ZCB,
					int num_paths,
					RandomBase& theGenerator);

	void MCprice_stepper(double Spot,
						double Strike,
						double Vol,
						double tau,
						double Expiry,
						double ZCB,
						int num_paths,
						int discretization,
						RandomBase& theGenerator,
						StatisticsMC& theGatherer);

	void MCprice_predCor(double Spot,
							double Strike,
							double Vol,
							double tau,
							double Expiry,
							double ZCB,
							int num_paths,
							int discretization,
							RandomBase& theGenerator,
							StatisticsMC& theGatherer);
};

#endif /* VANILLAINTPRICER_H_ */
