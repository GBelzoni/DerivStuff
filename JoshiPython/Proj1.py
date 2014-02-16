'''
Created on Feb 15, 2014

@author: phcostello
'''

# if __name__ == '__main__':
#    pass


#Proj 1
#Implement Analytic formulas for
#Price(TimeToMat, r, dividend, strike, spot, volatility)
#Call option
#Put Option
#Digital Call option

import AnalyticFunctions as af


#BS analytics
Spot = 110.
Strike = 110.
rate = 0.05
Vol = 0.2
dividend = 0.
Expiry = 1.

bs1 = af.BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)

print "ZCB: ", bs1.ZCB()
print "Forward Contract Value: ", bs1.Forward()
print "Call Price: ", bs1.CallPrice()
print "Put Price: ", bs1.PutPrice()
print "Digital Call Price: ", bs1.DigitalCallPrice()
print "Digital Put Price: ", bs1.DigitalPutPrice()
print "Call Delta: ", bs1.CallDelta()
print "Put Delta: ", bs1.PutDelta()
print "Call Theta: ", bs1.CallTheta()
print "Put Theta: ", bs1.PutTheta()
print "Call Rho: ", bs1.CallRho()
print "Put Rho: ", bs1.PutRho()
print "Call/Put Vega: ", bs1.CallVega()


