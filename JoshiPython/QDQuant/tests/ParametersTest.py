'''
Created on Mar 15, 2014

@author: phcostello
'''

import unittest
from Parameters import ParametersConstant, ParametersPWConstant

import numpy as np

class Test(unittest.TestCase):


    def test_constant_integral(self):
        
        const_val = 5.
        t1 = 0.1
        t2 = 0.4
        const_par = ParametersConstant(const_val)
        integral = const_par.int(t1,t2)
        calc = const_val*(t2-t1)
        self.assertAlmostEqual(calc, integral)
        

    def test_constant_integral_squared(self):
        
        const_val = 5.
        t1 = 0.1
        t2 = 0.4
        const_par = ParametersConstant(const_val)
        integral = const_par.int_sqr(t1,t2)
        calc = const_val**2*(t2-t1)
        self.assertAlmostEqual(calc, integral)


    def test_piecewise_constant_integral(self):
        
        
        x = np.array([0,1,3,7])
        y = np.array([1,2,3,4])
        t1 = 0.
        t2 = 1.4
        t3 = 5.6
        pw_const = ParametersPWConstant(x,y)
        integral1 = pw_const.int(t1,t2)
        integral2 = pw_const.int(t1,t3)
        integral3 = pw_const.int(t2,t3)
        #Manually calc integrals by hand
        calc1 = 1*1. + 0.4*2. 
        calc2 = 1*1. + 2.0*2. + 2.6*3.
        calc3 = 2.0*1.6 + 3.0*2.6
        self.assertAlmostEqual(first=calc1, second=integral1)
        self.assertAlmostEqual(first=calc2, second=integral2)
        self.assertAlmostEqual(first=calc3, second=integral3)
        
        
    def test_piecewise_constant_integral_squared(self):

        
        x = np.array([0,1,3,7])
        y = np.array([1,2,3,4])
        t1 = 0.
        t2 = 1.4
        t3 = 5.6
        pw_const = ParametersPWConstant(x,y)
        integral1 = pw_const.int_sqr(t1,t2)
        integral2 = pw_const.int_sqr(t1,t3)
        integral3 = pw_const.int_sqr(t2,t3)
        #Manually calc integrals by hand
        calc1 = 1*1. + 0.4*2**2. 
        calc2 = 1*1. + 2.0*2**2. + 2.6*3**2.
        calc3 = 2.0**2*1.6 + 3.0**2*2.6
        self.assertAlmostEqual(first=calc1, second=integral1)
        self.assertAlmostEqual(first=calc2, second=integral2)
        self.assertAlmostEqual(first=calc3, second=integral3)
        
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()