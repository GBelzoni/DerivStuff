/*
 * AnalyticFormulas.cpp
 *
 *  Created on: Feb 14, 2013
 *      Author: phcostello
 */

#include <cmath>
#include <Normals.h>
#include "AnalyticFormulas.h"
#include <BlackScholesFormulas.h>


#if !defined(_MSC_VER)
using namespace std;
#endif

double ZCB(double r, double Expiry) {
	return exp(-r * Expiry);

}

double ForwardContract(double r, double d, double Spot, double Strike,
		double Expiry) {
	return exp(-r * Expiry) * (exp((r - d) * Expiry) * Spot - Strike);
}


double BlackScholesCallDelta(double Spot, double Strike, double r, double d,
		double Vol, double Expiry) {

	double standardDeviation = Vol * sqrt(Expiry);
	double moneyness = log(Spot / Strike);
	double d1 = (moneyness + (r - d) * Expiry
			+ 0.5 * standardDeviation * standardDeviation) / standardDeviation;
	return CumulativeNormal(d1);

}


double BlackScholesPutDelta(double Spot, double Strike, double r, double d,
		double Vol, double Expiry) {

	double standardDeviation = Vol * sqrt(Expiry);
	double moneyness = log(Spot / Strike);
	double d1 = (moneyness + (r - d) * Expiry
			+ 0.5 * standardDeviation * standardDeviation) / standardDeviation;
	return CumulativeNormal(d1)-1;

}


double BlackScholesCallTheta(double Spot, double Strike, double r, double d,
		double Vol, double Expiry) {

	double standardDeviation = Vol * sqrt(Expiry);
	double moneyness = log(Spot / Strike);
	double d1 = (moneyness + (r - d) * Expiry
			+ 0.5 * standardDeviation * standardDeviation) / standardDeviation;
	double d2 = d1 - standardDeviation;
	return Spot*NormalDensity(d1)*standardDeviation/(2*sqrt(Expiry)) - r*Strike*exp(-r*Expiry)*CumulativeNormal(d2);

}

double BlackScholesPutTheta(double Spot, double Strike, double r, double d,
	double Vol, double Expiry) {

	double standardDeviation = Vol * sqrt(Expiry);
	double moneyness = log(Spot / Strike);
	double d1 = (moneyness + (r - d) * Expiry
			+ 0.5 * standardDeviation * standardDeviation) / standardDeviation;
	double d2 = d1 - standardDeviation;
	return Spot*NormalDensity(d1)*standardDeviation/(2*sqrt(Expiry)) + r*Strike*exp(-r*Expiry)*CumulativeNormal(-d2);


}

double BlackScholesCallRho(double Spot, double Strike, double r, double d,
	double Vol, double Expiry) {

	double standardDeviation = Vol * sqrt(Expiry);
	double moneyness = log(Spot / Strike);
	double d1 = (moneyness + (r - d) * Expiry
			+ 0.5 * standardDeviation * standardDeviation) / standardDeviation;
	double d2 = d1 - standardDeviation;
	return Strike*Expiry*exp(-r*Expiry)*CumulativeNormal(d2);

}

double BlackScholesPutRho(double Spot, double Strike, double r, double d,
	double Vol, double Expiry) {

	double standardDeviation = Vol * sqrt(Expiry);
	double moneyness = log(Spot / Strike);
	double d1 = (moneyness + (r - d) * Expiry
			+ 0.5 * standardDeviation * standardDeviation) / standardDeviation;
	double d2 = d1 - standardDeviation;
	return -Strike*Expiry*exp(-r*Expiry)*CumulativeNormal(-d2);
}

double BlackCaplet(double Spot_fr, double Strike, double Vol, double Tau,
		double Expiry, double ZCB) {
		/**
		 * Prices Caplet using Black formula.
		 * Expiry is expiry of caplet, ie start of cap
		 * ZCB is price for ZCB ending at end of cap period, ie Expiry + tau
		 */

		///Can price using usual BSF with zero rates
		double BS_res = BlackScholesCall( Spot_fr,
									Strike,
									0.0,
									0.0,
									Vol,
									Expiry);

		return ZCB*Tau*BS_res;
}

double FRA_Arrears(double Spot_fr, double Strike, double Vol, double Tau,
		double Expiry, double ZCB) {

	/**
	 * The formula for arrears cap can be done by avaluating in T_2 numerair to ge
	 * I did this in sympy and used to solve fair rate as well
	 *
	 * fair rate  = f_0*(f_0*tau*exp(sig^2*(Expiry-Tau) +1)/(1+tau*f_0)
	 * if you exand first to terms of exp term then you get
	 * fair rate approx = f_0 + f_0^2*sig^2*tau*(Expiry-Tau)/(1+tau*f_0)
	 * = f_0 + usual_convexity_adjustment
	 */

	double sig2 = Vol*Vol;
	double Spot2 = Spot_fr*Spot_fr;
	double Time1 = Expiry;
//	return Tau*ZCB*((Spot_fr - Strike) +
//					(Spot2*Tau*(std::exp(sig2*Time1))-Strike*Spot_fr*Tau)
//					);
	return Tau*ZCB*((Spot_fr - Strike) +
					(Spot2*Tau*(std::exp(sig2*Time1))-Strike*Spot_fr*Tau)
					);

}
