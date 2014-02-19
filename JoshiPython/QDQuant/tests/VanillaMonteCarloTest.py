'''
Created on Feb 16, 2014

@author: phcostello
'''
import unittest

import AnalyticFunctions as af
from PayOffs import *
from VanillaOptions import VanillaOption
from VanillaMCPricer import VanillaMCPricer
from PathGenerators import GBMGenerator
from Gatherer import MeanGatherer

class VanillaCallTest(unittest.TestCase):

    def setUp(self):
        #BS analytics
        self.Spot = 110.
        self.Strike = 110.
        self.rate = 0.05
        self.Vol = 0.2
        self.dividend = 0.
        self.Expiry = 1.
        
        #Setup analytic prices
        self.bs1 = af.BSAnalyticFormulas(self.Spot,
                                          self.Strike,
                                          self.rate,
                                          self.Vol,
                                          self.Expiry,
                                          self.dividend)
        
        
        #Setup MC pricer
        num_paths = 100000
        times = [self.Expiry]
        generator = GBMGenerator(self.Spot,
                                 self.rate,
                                 self.Vol,
                                 times)
        gatherer = MeanGatherer()
        
        self.van_mc = VanillaMCPricer(spot=self.Spot, 
                                      rate=self.rate, 
                                      Vol=self.Vol, 
                                      generator=generator, 
                                      gatherer=gatherer, 
                                      num_paths=num_paths, 
                                      dividend=0)
            
                                          
                                        

    def test_reprice_vanillaCall(self):
        an_price = self.bs1.CallPrice()
        call_po = VanillaCall(Strike = self.Strike)
        vcall = VanillaOption(Expiry=self.Expiry, PayOff=call_po)
        self.van_mc.do_trade(trade=vcall)
        mc_price = self.van_mc.price
        
        self.assertAlmostEqual(an_price, mc_price, delta=0.1)
         
    def test_reprice_vanillaPut(self):
          
        an_price = self.bs1.PutPrice()
        po = VanillaPut(Strike = self.Strike)
        option = VanillaOption(Expiry=self.Expiry, PayOff=po)
        self.van_mc.do_trade(trade=option)
        mc_price = self.van_mc.price
        
        self.assertAlmostEqual(an_price, mc_price, delta=0.1)
          
    def test_reprice_vanillaDigitalCall(self):
          
        an_price = self.bs1.DigitalCallPrice()
        po = VanillaDigitalCall(Strike = self.Strike)
        option = VanillaOption(Expiry=self.Expiry, PayOff=po)
        self.van_mc.do_trade(trade=option)
        mc_price = self.van_mc.price
        
        self.assertAlmostEqual(an_price, mc_price, delta=0.1)
     
    def test_reprice_vanillaDigitalPut(self):
          
        an_price = self.bs1.DigitalPutPrice()
        po = VanillaDigitalPut(Strike = self.Strike)
        option = VanillaOption(Expiry=self.Expiry, PayOff=po)
        self.van_mc.do_trade(trade=option)
        mc_price = self.van_mc.price
        
        self.assertAlmostEqual(an_price, mc_price, delta=0.1)    
      

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_reprice_vanillaCall']
    unittest.main()