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
num_paths = 5000
Strike = 103.
Spot = 100.
rate = 0.05
dividend = 0.0
Vol = 0.1
Expiry = 1.

bs1 = BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)
print "Analytic Call Price ", bs1.CallPrice()


#Implement Asian exotic

def AsianPrototype(Spot):
    
    #look at times
    look_at_times = list(np.linspace(start=0, stop=Expiry, num=12))
    
    #generate a path
    
    path_gen = GBMGenerator(spot=Spot, rate=rate, vol=Vol, times=look_at_times)
    sum = 0.
    
    for i in range(0,num_paths):
        
        path = path_gen.do_one_path() 
        # plt.plot(look_at_times,path)
        # plt.show()
        
        #Evaluate the payoff for path
        #Average of price - K
        average_price = np.mean(path)
        #Calc payoff
        po = VanillaCall(Strike=Strike)
        this_payoff = po.po(average_price)
        sum += this_payoff
    
    #Average and discount    
    price = math.exp(-rate*Expiry)*sum/num_paths
    
    return price



#Implement down and out call

def UpAndOutCallPrototype(Spot):
    
    #look at times
    look_at_times = list(np.linspace(start=0, stop=Expiry, num=12))
    
    #generate a path
    
    path_gen = GBMGenerator(spot=Spot, rate=rate, vol=Vol, times=look_at_times)
    sum = 0.
    Knockout = 108.
    for i in range(0,num_paths):
        
        path = path_gen.do_one_path() 
        # plt.plot(look_at_times,path)
        # plt.show()
        
        #Evaluate the payoff for path
        #Check if knocks out above barrier
        if any(map(lambda(x): x >= Knockout,path)):
            this_payoff = 0
        else:
            #Calc payoff
            po = VanillaCall(Strike=Strike)
            this_payoff = po.po(path[-1]) #Get last element of path
        
        sum += this_payoff
        
    price = math.exp(-rate*Expiry)*sum/num_paths
    
    return price

def plotUpAndOutProtype():
    
    Spots = np.linspace(start=50., stop=120, num=100)
    Spots = list(Spots)
    
    UandOprices = [UpAndOutCallPrototype(sp) for sp in Spots]
    
    plt.plot(Spots, UandOprices)
    plt.show()

def plotAsianPrototype():
    
    Spots = np.linspace(start=50., stop=120, num=100)
    Spots = list(Spots)
    
    Asian = [AsianPrototype(sp) for sp in Spots]
    call_an = lambda(x): BSAnalyticFormulas(x, Strike, rate, Vol, Expiry, dividend).CallPrice()
    BSanal = [ call_an(x) for x in Spots]
    
    plt.plot(Spots, Asian, Spots, BSanal)
    plt.show()
    
    
if __name__ == "__main__":
    
#     print "Up and Out Call ", UpAndOutCallPrototype(Spot)
#     plotUpAndOutProtype()
    plotAsianPrototype()
    