'''
Created on Feb 16, 2014

@author: phcostello
'''

from numpy.random import normal
from math import exp, sqrt

class BGMGenerator(object):
    '''
    classdocs
    '''


    def __init__(self, spot, rate, vol, times):
        '''
        This isn't quite right maybe
        You need to generate each interval step
        does generating a draw form intervals from lognormals give a lognormal path??
        Not sure you might have step it out.
        Will work for one step though
        '''
        self.spot = spot
        self.rate = rate
        self.vol = vol
        self.times = times
        
        #Contruct times up to random draw
        self.moved_spots = [ spot*exp(self.rate*(time) - 0.5 * self.vol*self.vol*time) for time in self.times]
        
        
    def do_one_path(self):
        
        randoms = normal(0,1,len(self.times))
        path = [ self.moved_spots[i]*exp(self.vol*sqrt(self.times[i])*randoms[i]) for i in range(0, len(self.times))]
        
        return path
    
    
if __name__ == '__main__':
    
    import numpy as np
    import matplotlib.pyplot as plt
    spot = 100.
    rate = 0.05
    vol = 0.2
#     times = np.linspace(0.01, stop=1.0, num=200)
    times = [1.]
    
    bgmgen = BGMGenerator(spot, rate, vol, times)
    
    path = bgmgen.do_one_path()
    
#     plt.plot(path)
#     plt.show()
    
    vals = [bgmgen.do_one_path() for i in range(0,10000)]
    
    print vals
    vals2 = [ v[0] for v in vals]
    print vals2
    plt.hist(vals2,50)
    plt.show()
    
#     print vals
    
    
    
        