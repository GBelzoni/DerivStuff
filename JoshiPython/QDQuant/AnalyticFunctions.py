'''
Created on Feb 15, 2014

@author: phcostello
'''
import math


def ZCB(rate, Expiry):
    
    """ 
    Returns price of zero coupon bond
    rate is continuous compounding
    """
    return math.exp(-rate*Expiry)


def Forwar(Spot, Strike, rate, Expiry, dividend=0):
exp(-r * Expiry) * (exp((r - d) * Expiry) * Spot - Strike);