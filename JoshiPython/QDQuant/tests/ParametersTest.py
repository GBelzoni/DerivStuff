'''
Created on Mar 15, 2014

@author: phcostello
'''
import unittest
from Parameters import ParametersConstant

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
        integral = const_par.int(t1,t2)
        calc = const_val*(t2-t1)
        self.assertAlmostEqual(calc, integral)


    def test_piecewise_constant_integral(self):
        pass
    
    def test_piecewise_constant_integral_squared(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()