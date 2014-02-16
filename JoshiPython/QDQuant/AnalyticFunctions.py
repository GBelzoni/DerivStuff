'''
Created on Feb 15, 2014

@author: phcostello
'''
import math
from scipy.stats import norm


def ZCB(rate, Expiry):
    
    """ 
    Returns price of zero coupon bond
    rate is continuous compounding
    """
    return math.exp(-rate*Expiry)


def Forward(Spot, Strike, rate, Expiry, dividend=0):
    """
    Returns Forward price for and Asset paying dividends
    rate = continuous rate
    dividend = continous rate
    """
    
    math.exp(-rate * Expiry) * (math.exp((rate - dividend) * Expiry) * Spot - Strike);
    

class BSAnalyticFormulas(object):
    
    """
    Produces Put/Call prices and delta, rho, theta, Vega
    """
    
    def __init__(self, Spot, Strike, rate, Vol, Expiry, dividend=0.0  ):
    
        """
        Initialise parameters of BlackScholes Formula
        """ 
        
        self.Spot = Spot
        self.Strike = Strike
        self.rate =rate
        self.dividend = 0
        self.Vol = Vol
        self.Expiry = Expiry
        
        self.sd = math.sqrt(Expiry)*Vol
        self.mnyns = math.log(Spot/Strike)
        self.d1 =  (self.mnyns + (rate*Expiry+0.5*self.sd*self.sd ))/(self.sd)
        self.d2 = self.d1 - self.sd
        self.cnd1 = norm.cdf(self.d1)
        self.cnd2 = norm.cdf(self.d2)
        self.pdf1 = norm.pdf(self.d1)
        self.pdf2 = norm.pdf(self.d2)
        
        
    def ZCB(self):
    
        """ 
        Returns price of zero coupon bond
        rate is continuous compounding
        """
        return math.exp(-self.rate*self.Expiry)
    
    
    def Forward(self):
        """
        Returns Forward price for and Asset paying dividends
        rate = continuous rate
        dividend = continous rate
        """
    
        return math.exp(-self.rate * self.Expiry) * \
            (math.exp((self.rate - self.dividend) * \
                      self.Expiry) * self.Spot - self.Strike)

    def CallPrice(self):
        """
        Return BlackScholes Analytic price of call option
        Not sure if working for non-zero dividend
        """   
        
        #believe it or not, below is BS formula
        return self.Spot * self.cnd1 - math.exp(-self.rate*self.Expiry)* self.Strike *self.cnd2
    
    
    def PutPrice(self):
        """
        Return BlackScholes Analytic price of call option
        """   
        #use put/call parity
        return self.CallPrice() - self.Forward()
    
    def DigitalCallPrice(self):
        """
        Return BlackScholes Analytic price of digital call option
        """   
        
        return math.exp(-self.rate*self.Expiry)*self.cnd2;
    
    def DigitalPutPrice(self):
        """
        Return BlackScholes Analytic price of digital call option
        """   
        
        return self.ZCB() - self.DigitalCallPrice()
    
    #Risks
    def CallDelta(self):
        """
        Return Delta of BSCall price with respect to underlying
        """
        return self.cnd1
    
    def PutDelta(self):
        """
        Return Delta of BSCall price with respect to underlying
        """
        return self.cnd1 -1
    
    
    def CallPutGamma(self):
        """
        Return Gamma of BSCall/BSPut price with respect to underlying
        """
        return self.pdf1/(self.Spot*self.sd)
    
    
    def CallTheta(self):
        """
        Return Theta of BSCall price with respect to time
        """
        
        return - self.Spot*self.pdf1*self.Vol/(2*math.sqrt(self.Expiry)) - \
            self.rate*self.Strike*math.exp(-self.rate*self.Expiry)*self.cnd2;
    
    def PutTheta(self):
        """
        Return Theta of BSPut price with respect to time
        """
        
        return - self.Spot*self.pdf1*self.Vol/(2*math.sqrt(self.Expiry)) + \
            self.rate*self.Strike*math.exp(-self.rate*self.Expiry)*(1-self.cnd2);

    def CallRho(self):
        """
        Return Rho of BSCall price with respect to interest rate
        """
        
        return self.Strike*self.Expiry*math.exp(-self.rate*self.Expiry)*self.cnd2

    def PutRho(self):
        """
        Return Rho of BSPut price with respect to interest rate 
        """
        
        return - self.Strike*self.Expiry*math.exp(-self.rate*self.Expiry)*(1-self.cnd2)
    
    def CallVega(self):
        """
        Return Vega of BlackScholesCall
        """
        return self.Spot*self.pdf1*math.sqrt(self.Expiry)
    