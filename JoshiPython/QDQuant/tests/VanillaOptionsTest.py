'''
Created on Feb 18, 2014

@author: phcostello
'''
import unittest

from PayOffs import VanillaCall, VanillaPut
from VanillaOptions import VanillaOption

class Test(unittest.TestCase):

    
   
    def setUp(self):
        
        self.StrikeHigher = 110.
        self.StrikeLower = 90.
        self.Spot = 100.
    
    

    def tearDown(self):
        pass


    def test_PutCallPayOffs(self):
        
        vc_higher = VanillaCall(self.StrikeHigher)
        vc_lower= VanillaCall(self.StrikeLower)
        vp_higher = VanillaPut(self.StrikeHigher)
        vp_lower= VanillaPut(self.StrikeLower)
            
        vo_callhigher = VanillaOption(Expiry=1, PayOff=vc_higher)
        vo_calllower= VanillaOption(Expiry=1, PayOff=vc_lower)
        vo_puthigher = VanillaOption(Expiry=1, PayOff=vp_higher)
        vo_putlower= VanillaOption(Expiry=1, PayOff=vp_lower)
        
        self.assertAlmostEqual(vo_callhigher.pay_off(self.Spot),0.)
        self.assertAlmostEqual(vo_calllower.pay_off(self.Spot),10.)
        self.assertAlmostEqual(vo_puthigher.pay_off(self.Spot),10.)
        self.assertAlmostEqual(vo_putlower.pay_off(self.Spot),0.)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()