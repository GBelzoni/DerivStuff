'''
Created on Feb 16, 2014

@author: phcostello
'''

# if __name__ == '__main__':
#     pass


#Vanilla Monte Carlo Pricer
from QDQuant.AnalyticFunctions import BSAnalyticFormulas

#For call option do Price

numofpaths = 1000000
Strike = 110.
Spot = 100.
rate = 0.05
dividend = 0.0
Vol = 0.15
Expiry = 1.0


bs1 = BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)
print "Analytic Call Price ", bs1.CallPrice()

#We want a loop that takes average of
#sum_path( exp(-rt)*max(S - K,0)) where S = S_0*exp(rT - 1/2*sig^2T + sig(sqrt(T)*N(0,1)
#and discounts

#For path we need to generate random x
import numpy as np
import math
randoms = np.random.normal(0,1,numofpaths)

movedSpot = Spot*math.exp(rate*Expiry - 0.5*Vol*Vol*Expiry)
sum = 0
for i in range(0,numofpaths):
    #Generate S_t
    thisRand = math.exp(Vol*math.sqrt(Expiry)*randoms[i])
    thisSpot = movedSpot*thisRand
    thisPayOff = max(thisSpot - Strike,0)
    sum +=thisPayOff
    
price = sum/numofpaths*math.exp(-rate*Expiry)

print "MC Carlo Price", price

    
    
#vcall1 = VanillaCall(Strike,Expiry)
#mc1 = VanillaMonteCarlo(rate, Vol, path_generator, result_collector)
#mc1.fitTrade(vcall1)
#mc1.price() 






