'''
Created on Mar 15, 2014

@author: phcostello
'''
import unittest
import numpy as np
import matplotlib.pyplot as plt
from PathGenerators import *
import pandas as pd

class Test(unittest.TestCase):


    def setUp(self):
       
        spot = 100.
        rate = 0.05
        vol = 0.1
        times = list(np.linspace(0.0, stop=1.0, num=3))
        
        self.times = times[1:]
        
        self.market_params = {'spot':spot, 'rate':rate, 'vol':vol}

        self.generator = NormalGenerator() #Make generator out of np normal generator
        self.athetic = Antithetic(self.generator)
        
    def tearDown(self):
        pass

    def testIncrementalPathGenInterface(self):
        
        #Test that interface doesn't throw any errors
        bgmgen = GeneratorGBM(self.market_params)
        bgmgen.sim_setup(self.times)
        path = bgmgen.do_one_path()
        
        self.assertEqual(len(path), len(self.times))

    def testIncrementalPathGenMoments(self):
        
        """
        test mean and variance of path gens against theoretical as given
        in #http://en.wikipedia.org/wiki/Geometric_Brownian_motion
        """
        
        num_paths = 100000
        
        bgmgen = GeneratorGBM(self.market_params)
        bgmgen.generator=self.athetic
        bgmgen.sim_setup(self.times)
        #Change random generator
        spot = self.market_params['spot']
        rate = self.market_params['rate']
        vol = self.market_params['vol']
        
        paths = [ tuple( bgmgen.do_one_path()) for i in range(0,num_paths)]
        
        paths = pd.DataFrame(paths)
        result = pd.concat([pd.DataFrame(paths.mean()),pd.DataFrame(paths.var())],axis=1)
        result.columns= ['mean','var']
        
        #Theoretical mean and variance of GBM 
        #http://en.wikipedia.org/wiki/Geometric_Brownian_motion
        
        result['mean_theo'] = [ spot*exp(rate*t) for t in self.times]
        result['var_theo'] = [ spot**2 *exp(2*rate*t)*(exp(vol*vol*t)-1) for t in self.times]
        
        print "inc result\n", result
        
        mean_theo_error =  (result['mean']- result['mean_theo']).abs().sum()
        var_theo_error =  (result['var']- result['var_theo']).abs().sum()
        
        
        self.assertAlmostEqual(first = mean_theo_error, second= 0.0, delta=0.1)        
        self.assertAlmostEqual(first = var_theo_error, second= 0.0, delta=1.)        

    def testBrownianBridgePathGen(self):

        """
        test mean and variance of path gens for brownian bridge
        against theoretical as given
        in #http://en.wikipedia.org/wiki/Geometric_Brownian_motion
        """
        
        num_paths = 100000
        
        bgmgen = GeneratorGBM(self.market_params, "brownian_bridge")
        bgmgen.generator=self.athetic
        bgmgen.sim_setup(self.times)
        #Change random generator
        spot = self.market_params['spot']
        rate = self.market_params['rate']
        vol = self.market_params['vol']
        
        paths = [ tuple( bgmgen.do_one_path()) for i in range(0,num_paths)]
        
        paths = pd.DataFrame(paths)
        result = pd.concat([pd.DataFrame(paths.mean()),pd.DataFrame(paths.var())],axis=1)
        result.columns= ['mean','var']
        
        #Theoretical mean and variance of GBM 
        #http://en.wikipedia.org/wiki/Geometric_Brownian_motion
        
        
        result['mean_theo'] = [ spot*exp(rate*t) for t in self.times]
        result['var_theo'] = [ spot**2 *exp(2*rate*t)*(exp(vol*vol*t)-1) for t in self.times]
        
        print result
        
        mean_theo_error =  (result['mean']- result['mean_theo']).abs().sum()
        var_theo_error =  (result['var']- result['var_theo']).abs().sum()
        
        self.assertAlmostEqual(first = mean_theo_error, second= 0.0, delta=0.1)        
        self.assertAlmostEqual(first = var_theo_error, second= 0.0, delta=1.)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()