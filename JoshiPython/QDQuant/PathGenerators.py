'''
Created on Feb 16, 2014

@author: phcostello
'''

from numpy import random
from numpy.random import normal 
from math import exp, sqrt



class NormalGenerator(object):
    
    """
    Just a wrapper for generator of normals
    Assumes generator interface same as numpy normals
    Write wrapper for other generators
    """
    
    def __init__(self, generator=normal):
        
        self.generator = generator
    
    def get_variates(self,mu=0,sig=1,size=1):
        
        """
        based on numpy normal generator
        """
        
        return self.generator(mu,sig,size)
    
    def set_seed(self,seed):
        
        """
        Reset seed of random generatr
        """
        random.seed(seed)
        
class Antithetic(NormalGenerator):
    """
    Decorator for generator that does antithetic sampling
    """
    def __init__(self, generator=NormalGenerator()):
        
        super(Antithetic,self).__init__(generator)
        self.even = True
        self.lastsample=0
        
    def get_variates(self,mu=0,sig=1,size=1):
        
        """
        based on numpy normal generator
        note that size of returned samples = 2*size due to antithetic sampling
        """
        
        if self.even:
            self.even = False
            self.lastsample = self.generator.get_variates(mu,sig,size)
            return self.lastsample
        else:
            self.even = True
            return -self.lastsample       

        


class GBMGenerator(object):
    '''
    classdocs
    '''


    def __init__(self, market_params):
        '''
        
        '''
    
 
        self.spot = market_params['spot']
        self.rate = market_params['rate']
        self.vol = vol
        self.times = times
        self.generator = NormalGenerator(normal)
        
        
        aug_times = [0.0]+times
        self.time_diffs = [ aug_times[i] - aug_times[i-1] for i in range(1,len(aug_times))]
        
        #Contruct times up to random draw
        self.drifts = [ exp(self.rate*td - 0.5 * self.vol*self.vol*td) for td in self.time_diffs]
        
        
    def do_one_path(self):
        
        """
        Currently set to use analytice solution to GBM
        Change to be a dispatcher
        """
        
        randoms = self.generator.get_variates(0,1,len(self.time_diffs))
        
        path = []
        prev_spot = self.spot
        
        for i in range(0, len(self.time_diffs)):
            next_spot = prev_spot*self.drifts[i] * exp(self.vol*sqrt(self.time_diffs[i])*randoms[i])
            path += [next_spot]
            prev_spot = next_spot
        
        
        return path
    
    
if __name__ == '__main__':
    
    import numpy as np
    import matplotlib.pyplot as plt
    spot = 100.
    rate = 0.05
    vol = 0.01
    times = list(np.linspace(0.01, stop=1.0, num=200))
#     times = [1.]
    
    bgmgen = GBMGenerator(spot, rate, vol, times)
    
    #Change random generator
    generator = NormalGenerator(normal) #Make generator out of np normal generator
    athetic = Antithetic(generator)
    
    bgmgen.generator = athetic 
#     print athetic.get_variates(0, 1, 3)
#     print athetic.get_variates(0, 1, 3)
    
    path = bgmgen.do_one_path()
    print len(path)
    print list(times)
    plt.plot(times,path)
    plt.show()
    
#     vals = [bgmgen.do_one_path() for i in range(0,3)]
    
#     print vals
#     vals2 = [ v[0] for v in vals]
#     print vals2
#     plt.hist(vals2,50)
#     plt.show()
#     
#     print vals
    
    
    
        