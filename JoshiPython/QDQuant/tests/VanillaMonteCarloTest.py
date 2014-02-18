'''
Created on Feb 16, 2014

@author: phcostello
'''
import unittest

import AnalyticFunctions as af
from PayOffs import VanillaCall, VanillaPut
from VanillaOptions import VanillaOption
from VanillaMCPricer import VanillaMCPricer

class VanillaCallTest(unittest.TestCase):

        def setUp(self):
            #BS analytics
            self.Spot = 110.
            self.Strike = 110.
            self.rate = 0.05
            self.Vol = 0.2
            self.dividend = 0.
            self.Expiry = 1.
        
            self.bs1 = af.BSAnalyticFormulas(self.Spot,
                                              self.Strike,
                                              self.rate,
                                              self.Vol,
                                              self.Expiry,
                                              self.dividend)
            
            self.van_mc = VanillaMCPricer()

#     def test_reprice_vanillaCall(self):
#         an_call_price = self.bs1.CallPrice()
#         
#         vcall = 
#         self.assertAlmostEqual(, MCCallPrice, places=5)
#         
#     def test_reprice_vanillaPut(self):
#         
#         self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)
#         
#     def test_reprice_vanillaDigitalCall(self):
#         
#         self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)
#     
#     
#     def test_reprice_vanillaCallDelta(self):
#                 
#         self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_reprice_vanillaCall']
    unittest.main()