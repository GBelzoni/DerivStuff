'''
Created on Feb 16, 2014

@author: phcostello
'''

from numpy.random import normal
from math import exp, sqrt


class NormalGenerator(object):
    
    """
    Just a wrapper for generator of normals
    """
    
    def __init__(self, generator):
        
        self.generator = generator
    
    def get_variates(self,mu=0,sig=1,size=1):
        
        """
        based on numpy normal generator
        """
        
        return self.generator(mu,sig,size)
        
class Antithetic(NormalGenerator):
    """
    Decorator for generator that does antithetic sampling
    """
    def __init__(self, generator):
        
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
        self.generator = NormalGenerator(normal)
        
        #Contruct times up to random draw
        self.moved_spots = [ spot*exp(self.rate*(time) - 0.5 * self.vol*self.vol*time) for time in self.times]
        
        
    def do_one_path(self):
        
        randoms = self.generator.get_variates(0,1,len(self.times))
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
    
    #Change random generator
    generator = NormalGenerator(normal) #Make generator out of np normal generator
    athetic = Antithetic(generator)
    
    bgmgen.generator = athetic 
    print athetic.get_variates(0, 1, 1)
    print athetic.get_variates(0, 1, 1)
    
    path = bgmgen.do_one_path()
    print path
    
#     plt.plot(path)
#     plt.show()
    
#     vals = [bgmgen.do_one_path() for i in range(0,3)]
    
#     print vals
#     vals2 = [ v[0] for v in vals]
#     print vals2
#     plt.hist(vals2,50)
#     plt.show()
#     
#     print vals
    
    
    
        