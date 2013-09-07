/*
 * MoreStatisticsMC.h
 *
 *  Created on: Aug 28, 2013
 *      Author: phcostello
 */

#ifndef MORESTATISTICSMC_H_
#define MORESTATISTICSMC_H_

#include <MCStatistics.h>
#include <vector>

class MoreStatisticsMC: public StatisticsMC {

public:
	MoreStatisticsMC();
	virtual ~MoreStatisticsMC();

	virtual void DumpOneResult(double result);
    virtual std::vector<std::vector<double> > GetResultsSoFar() const;
    virtual StatisticsMC* clone() const;


private:

    unsigned long paths_done;
    std::vector<double> running_sum_and_sum2;

};

#endif /* MORESTATISTICSMC_H_ */
