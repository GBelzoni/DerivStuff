'''
Created on Feb 16, 2014

@author: phcostello
'''

#Setup

import pandas as pd
import numpy as np
import math
    
    
#Vanilla Monte Carlo Pricer
from QDQuant.AnalyticFunctions import BSAnalyticFormulas

#For call option do Price

numofpaths = 100000
Strike = 105.
Spot = 100.
rate = 0.05
dividend = 0.0
Vol = 0.05
Expiry = 1.0

market_params = {'spot': Spot, 'vol':Vol,'rate':rate }


bs1 = BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)
# print "Analytic Call Price ", bs1.CallPrice()


def MC_prototype():
    
    #We want a loop that takes average of
    #sum_path( exp(-rt)*max(S - K,0)) where S = S_0*exp(rT - 1/2*sig^2T + sig(sqrt(T)*N(0,1)
    #and discounts
    
    #This is loop for call
    #For path we need to generate random x

    
    randoms = np.random.normal(0,1,numofpaths)
    
    movedSpot = Spot*math.exp(rate*Expiry - 0.5*Vol*Vol*Expiry)
    sum = 0
    for i in range(0,numofpaths):
        #Generate S_t
        thisRand = math.exp(Vol*math.sqrt(Expiry)*randoms[i])
        thisSpot = movedSpot*thisRand
        thisPayOff = max(thisSpot - Strike,0)
        sum +=thisPayOff
        
    price = sum/numofpaths*math.exp(-rate*Expiry)
    
    print "MC Carlo Price", price

    
#This is implementation in lib

from QDQuant.VanillaMCPricer import VanillaMCPricer
from QDQuant.PathGenerators import GeneratorGBM, NormalGenerator
from QDQuant.Gatherer import MeanGatherer, SDGatherer, ConvergenceTable
from QDQuant.PayOffs import VanillaCall, VanillaDigitalPut
from QDQuant.VanillaOptions import VanillaOption

def single_MC_run():
    
#     gatherer = MeanGatherer()
    gatherer = SDGatherer()
    gatherer_ct = ConvergenceTable(gatherer,numofpaths)
    
    
    
    path_gen = GeneratorGBM(market_params=market_params)
    
    pricer_mc= VanillaMCPricer(spot=Spot, 
                               rate=rate, 
                               Vol=Vol, 
                               generator=path_gen, 
                               gatherer=gatherer_ct, 
                               num_paths=numofpaths)
    
    po = VanillaCall(Strike=Strike)
    option = VanillaOption(Expiry=Expiry, PayOff=po)
    
    pricer_mc.do_trade(trade=option)
    
    print "MC price", pricer_mc.price
    
    res_table = pd.DataFrame(gatherer_ct.table)[['mean','sd','paths_done']]
    res_table['smean_sd']= res_table['sd']/res_table['paths_done']
    print res_table

def range_pars_sim(do_plots=True):

    Spots = np.linspace(90, 110, num=40)
    Vols = np.array([0.01,0.05,0.1,0.2,0.5])
    Expiries = np.array([0.1,0,25,0.5,1,5])
    
    vcall_anal = [ BSAnalyticFormulas(thisSpot,Strike,rate,Vol,Expiry,dividend).CallPrice() for thisSpot in Spots]
    
    vcall_mc = []
    #Do MC
    for thisSpot in Spots:
        gatherer = SDGatherer()
        
        ngen = NormalGenerator()
        path_gen = GeneratorGBM(spot=thisSpot, rate=rate, vol=Vol, times=[Expiry])
        pricer_mc= VanillaMCPricer(spot=Spot, 
                               rate=rate, 
                               Vol=Vol, 
                               generator=path_gen, 
                               gatherer=gatherer, 
                               num_paths=numofpaths)
    
        po = VanillaCall(Strike=Strike)
    #     po= VanillaDigitalPut(Strike=Strike)
        option = VanillaOption(Expiry=Expiry, PayOff=po)
    
        pricer_mc.do_trade(trade=option)
        vcall_mc += [pricer_mc.price]
        
    
    print vcall_mc[0:5]
    print Spots[0:5]
    import matplotlib.pyplot as plt
    
    if do_plots:
        plt.plot(Spots,vcall_mc)
        plt.show()

def do_bump_deltas():
    
    from Bumper import bump_delta_central as bd

    print "Anal Call Delta", bs1.CallDelta()
    
    CallDelbmp = lambda( x ): BSAnalyticFormulas(x, Strike, rate, Vol, Expiry, dividend).CallPrice()
    print "Del bump Call 1 ", bd(Spot,CallDelbmp)
    
    def CallMCDelbmp_noSeedReset(x):
        """
        This function for testing bump delta but with NO seed setting
        Should give garbage as seed needs to be reset in MC bump deltas
        
        Note that dependence on spot is actually in the path generator
        """
        
        gatherer = SDGatherer()
        market_params2 = dict(market_params)
        market_params2['spot'] = x
        path_gen = GeneratorGBM(market_params=market_params)
        
        pricer_mc= VanillaMCPricer(spot=x, 
                                   rate=rate, 
                                   Vol=Vol, 
                                   generator=path_gen, 
                                   gatherer=gatherer, 
                                   num_paths=numofpaths)
        
        po = VanillaCall(Strike=Strike)
        option = VanillaOption(Expiry=Expiry, PayOff=po)
        
        pricer_mc.do_trade(trade=option)
    
        return pricer_mc.price
    
    print "MCCall price", CallMCDelbmp_noSeedReset(100)
    print "MCCall Delta without setting seed", bd(100,CallMCDelbmp_noSeedReset)
    
    def CallMCDelbmp_WithSeedReset(x):
        """
        This function for testing bump delta but WITH seed setting
        Should give good result
        
        Note that dependence on spot is actually in the path generator
        """
        
        gatherer = SDGatherer()
        market_params2 = dict(market_params)
        market_params2['spot'] = x
        path_gen = GeneratorGBM(market_params = market_params2)
        path_gen.generator.set_seed(seed=0)
        
        pricer_mc= VanillaMCPricer(spot=x, 
                                   rate=rate, 
                                   Vol=Vol, 
                                   generator=path_gen, 
                                   gatherer=gatherer, 
                                   num_paths=numofpaths)
        
        po = VanillaCall(Strike=Strike)
        option = VanillaOption(Expiry=Expiry, PayOff=po)
        
        pricer_mc.do_trade(trade=option)
    
        return pricer_mc.price
        
    print "MCCall price, seed = 0", CallMCDelbmp_WithSeedReset(100.)
#     print "MCCall price, seed = 0", CallMCDelbmp_WithSeedReset(100.1)
    print "MCCall Delta with setting seed", bd(100.,CallMCDelbmp_WithSeedReset,epsilon = 1e-2)


##TODO

def path_wise_MC():
    
    pass     


def path_wise_MC_Delta():
    
    pass     


def likelyhoodratio_MC_Delta():
    
    pass     


if __name__ == '__main__':
    
    #Functions to test project
    
    do_bump_deltas()
#     single_MC_run()
#     range_pars_sim()
#     pass

