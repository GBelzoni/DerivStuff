'''
Created on Mar 15, 2014

@author: phcostello
'''
import unittest
import pandas as pd
import numpy as np
import math

from PathGenerators import GeneratorGBM   
from PathDependentOption import AsianArithmeticOption, UpAndOutCall
from PathDepMCPricer import PathDependentMCPricer
from Gatherer import SDGatherer

#Vanilla Monte Carlo Pricer
from QDQuant.AnalyticFunctions import BSAnalyticFormulas


class Test(unittest.TestCase):


    def setUp(self):
        #For call option do Price
        
        self.Strike = 103.
        self.Spot = 100.
        self.rate = 0.05
        self.dividend = 0.0
        self.Vol = 0.1
        self.Expiry = 1.

        self.bs1 = BSAnalyticFormulas(self.Spot, 
                                      self.Strike, 
                                      self.rate, 
                                      self.Vol, 
                                      self.Expiry, 
                                      self.dividend)
        pass


    def tearDown(self):
        pass


    def test_AsianArithmetic_pricer(self):
        
        """
        test that asian arithmetic option pricer works
        """
        
        num_paths = 500000
        
        payoff = VanillaCall(Strike=self.Strike)
    
        #look at times
        look_at_times = list(np.linspace(start=0, stop=self.Expiry, num=12))
        
        #Contruct Option
        option_parameters = {'payoff': payoff, 
                             'look_at_times':look_at_times,
                             'Expiry':self.Expiry}
        
        ao = AsianArithmeticOption(option_parameters)
        
        #Construct market parameters for path generation
        market_params = {'spot':self.Spot, 'rate':self.rate, 'vol':self.Vol}
        path_generator = GeneratorGBM(market_params)
        
        #Construct Pricer parameters
        #Note includes path generator
        gatherer = SDGatherer()
        pricer_parameters = {'path_generator':path_generator,
                             'num_paths': num_paths,
                             'gatherer': gatherer}
        
        #Contruct pricer 
        pd_pricer = PathDependentMCPricer(pricer_parameters)
        
        #Do trade
        price = pd_pricer.do_trade(ao)
        
        print "MC Asian opt price ", price
        self.assertAlmostEqual( first =   2.015, second= price, places=2)#, msg, delta)

    def test_UpAndOut_pricer(self):

        """
        test that path dependent pricer works for up and out option
        with discrete barrier data
        """
        
        num_paths = 500000            
        
        #Construct option
        barrier = 108.
        payoff = VanillaCall(Strike=self.Strike)
    
        #look at times
        look_at_times = list(np.linspace(start=0, stop=self.Expiry, num=12))
        
        option_parameters = {'payoff': payoff, 
                             'look_at_times':look_at_times,
                             'Expiry':self.Expiry,
                             'Barrier': barrier}
    
        ao = UpAndOutCall(option_parameters)
    
        #Construct market parameters for path generation
        market_params = {'spot':self.Spot, 'rate':self.rate, 'vol':self.Vol}
        path_generator = GeneratorGBM(market_params)
        
        
        
        
        #Construct Pricer parameters
        #Note includes path generator
        gatherer = SDGatherer()
        pricer_parameters = {'path_generator':path_generator,
                             'num_paths': num_paths,
                             'gatherer': gatherer}
        
        #Contruct pricer 
        pd_pricer = PathDependentMCPricer(pricer_parameters)
        
        #Do trade
        price = pd_pricer.do_trade(ao)
        
        print "MC up and out call price ", price
        self.assertAlmostEqual( first =  0.2096, second= price, places=2)#, msg, delta)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()