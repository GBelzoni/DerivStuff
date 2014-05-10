'''
Created on Apr 16, 2014

@author: phcostello
'''
import math
import pandas as pd
import numpy as np

from BGM.CovarianceStructure import CovariantStructure_abcd

#Project 10 already done in cpp CppRate_Curve_tests

def prototyp_caplet_bgm():
    
    '''
    Do initial concrete implementation of class structure suggested
    in Joshi p452
    '''
    
    
    
    #The product - caplet  
    Spot_fr = 0.07;
    Strike = 0.05;
    tau = 0.5;
    Vol = 0.20;
    Expiry = 5.0;
    ZCB = 0.65;
    
    #underlying times
    u_times = [ 5.0, 5.5]
    
    #evolution times
    e_times = [5.0]
    
    #The covariance structure (a,b,c,d)
    cs = CovariantStructure_abcd(a=0.05, b=0.09, c=0.44, d=0.11, beta=0.1)
    
    #num paths
    
    #number generator
    
    #amount of substepping to be carried out
    
    #method of approximating drift, Euler stepping or predictor-corrector
    
    #intial values of forward rates
    
    #what numeriaire to use and it's initial value


if __name__ == '__main__':
    
    
    print prototyp_caplet_bgm()