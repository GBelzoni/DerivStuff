#Implementing and exotic pricer



import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from PathGenerators import GBMGenerator    
from VanillaOptions import VanillaOption
from PayOffs import VanillaCall
    
#Vanilla Monte Carlo Pricer
from QDQuant.AnalyticFunctions import BSAnalyticFormulas

#For call option do Price

numofpaths = 10000
Strike = 103.
Spot = 100.
rate = 0.05
dividend = 0.0
Vol = 0.1
Expiry = 0.05

bs1 = BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)
# print "Analytic Call Price ", bs1.CallPrice()


#Implement Asian exotic

#look at times
look_at_times = list(np.linspace(start=0, stop=1, num=12))
print look_at_times
#generate a path

path_gen = GBMGenerator(spot=Spot, rate=rate, vol=Vol, times=look_at_times)
path = path_gen.do_one_path() 
# plt.plot(look_at_times,path)
# plt.show()




#Evaluate the payoff for path
    #Average of price - K
    average_price = np.mean(path)
    po = VanillaCall(Strike=Strike)

#Accumulate

#Average and discount


#Implement down and out call

