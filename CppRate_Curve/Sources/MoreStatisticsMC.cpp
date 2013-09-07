/*
 * MoreStatisticsMC.cpp
 *
 *  Created on: Aug 28, 2013
 *      Author: phcostello
 */

#include "MoreStatisticsMC.h"
#include <math.h>


MoreStatisticsMC::MoreStatisticsMC():
				paths_done(0UL) , running_sum_and_sum2({0.0,0.0}) {
}

MoreStatisticsMC::~MoreStatisticsMC() {

}

void MoreStatisticsMC::DumpOneResult(double result){

	running_sum_and_sum2[0]+= result;
	running_sum_and_sum2[1]+= result*result;
	paths_done += 1;

}

std::vector<std::vector<double> > MoreStatisticsMC::GetResultsSoFar() const{

	std::vector<std::vector<double> > Result;


	double mean = running_sum_and_sum2[0]/paths_done;
	//Get running variance estimate of sample mean. This can be used derive
	//CI for how close estimate is to mean.
	//This is as sample_mean - mean is approximately distributed as normal
	// N(0, sigma/n) where sigma is variate mean and n is number of vars in sum

	double var_variate = running_sum_and_sum2[1]/(paths_done-1) ;
	double var_sum = var_variate/paths_done;
	double sd_sum = sqrt(var_sum);
	std::vector<double> thisRes = {mean, var_variate, var_sum, sd_sum};

	Result.push_back(thisRes);

	return Result;

}

StatisticsMC* MoreStatisticsMC::clone() const {

	return new MoreStatisticsMC(*this);
}

