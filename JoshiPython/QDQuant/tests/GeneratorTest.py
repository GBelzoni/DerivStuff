'''
Created on Feb 19, 2014

@author: phcostello
'''
import unittest
from PathGenerators import *
import numpy as np
import matplotlib.pyplot as plt


class Test(unittest.TestCase):


    def setUp(self):
        pass
     
#         spot = 100.
#         rate = 0.05
#         vol = 0.2
#     #     times = np.linspace(0.01, stop=1.0, num=200)
#         times = [1.]
#         
#         bgmgen = BGMGenerator(spot, rate, vol, times)
#         
#         #Change random generator
#         athetic = Antithetic(generator)
#         
#         bgmgen.generator = athetic 
#         print athetic.get_variates(0, 1, 3)
#         print athetic.get_variates(0, 1, 3)
#         
#         path = bgmgen.do_one_path()
#         print path
#     

    def tearDown(self):
        pass


    def testSetSeed(self):
        """
        test settig seed 
        """
        generator = NormalGenerator() #Make generator out of np normal generator
        generator.set_seed(seed=0)
        res1 = generator.get_variates(mu=0, sig=1, size=1)[0]
        generator.set_seed(seed=0)
        res2 = generator.get_variates(mu=0, sig=1, size=1)[0]
       
        self.assertAlmostEqual(first=res1, second=res2)
        
    def testAntiThetic(self):
        """
        test antithetic sampling
        """
        generator = NormalGenerator() #Make generator out of np normal generator
        antithetic_gen = Antithetic(generator)
        res1 = antithetic_gen.get_variates(mu=0, sig=1, size=1)
        res2 = antithetic_gen.get_variates(mu=0, sig=1, size=1)
        
        self.assertAlmostEqual(first=res1[0], second=-res2[0])

    def testGBMgeneration(self):
        """
        Haven't figured out how to do this one yet
        """
        pass
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()