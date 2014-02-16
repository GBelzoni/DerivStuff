'''
Created on Feb 16, 2014

@author: phcostello
'''
import unittest


class VanillaCallTest(unittest.TestCase):


    def test_reprice_vanillaCall(self):
        
        self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)
        
    def test_reprice_vanillaPut(self):
        
        self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)
        
    def test_reprice_vanillaDigitalCall(self):
        
        self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)
    
    
    def test_reprice_vanillaCallDelta(self):
                
        self.assertAlmostEqual(AnalyticCallPrice, MCCallPrice, places=5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_reprice_vanillaCall']
    unittest.main()