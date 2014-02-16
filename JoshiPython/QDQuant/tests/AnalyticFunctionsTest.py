'''
Created on Feb 16, 2014

@author: phcostello
'''
import unittest
import QDQuant.AnalyticFunctions as af

class Test(unittest.TestCase):


    def setUp(self):
        #BS analytics
        Spot = 110.
        Strike = 110.
        rate = 0.05
        Vol = 0.2
        dividend = 0.
        Expiry = 1.
        
        self.bs1 = af.BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)



    def tearDown(self):
        pass


    def testAnalyticValues(self):
        
        
        self.assertAlmostEqual(self.bs1.ZCB(), 0.95122942)
        self.assertAlmostEqual(self.bs1.Forward(),5.36476330492)
        self.assertAlmostEqual(self.bs1.CallPrice(),11.49564192)
        self.assertAlmostEqual(self.bs1.PutPrice(),6.13087862)
        self.assertAlmostEqual(self.bs1.DigitalCallPrice(),0.532324815)
        self.assertAlmostEqual(self.bs1.DigitalPutPrice(),0.418904609)
#         self.assertAlmostEqual(self.bs1.CallDelta(),)
#         self.assertAlmostEqual(self.bs1.PutDelta(),)
#         self.assertAlmostEqual(self.bs1.CallPutGamma(,))
#         self.assertAlmostEqual(self.bs1.CallTheta(),)
#         self.assertAlmostEqual(self.bs1.PutTheta(),)
#         self.assertAlmostEqual(self.bs1.CallRho(),)
#         self.assertAlmostEqual(self.bs1.PutRho(),)
#         self.assertAlmostEqual(self.bs1.CallVega(),)
# 
#         


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
#     print "ZCB: ", bs1.ZCB()
#     print "Forward Contract Value: ", bs1.Forward()
#     print "Call Price: ", bs1.CallPrice()
#     print "Put Price: ", bs1.PutPrice()
#     print "Digital Call Price: ", bs1.DigitalCallPrice()
#     print "Digital Put Price: ", bs1.DigitalPutPrice()
#     print "Call Delta: ", bs1.CallDelta()
#     print "Put Delta: ", bs1.PutDelta()
#     print "Call Theta: ", bs1.CallTheta()
#     print "Put Theta: ", bs1.PutTheta()
#     print "Call Rho: ", bs1.CallRho()
#     print "Put Rho: ", bs1.PutRho()
#     print "Call/Put Vega: ", bs1.CallVega()