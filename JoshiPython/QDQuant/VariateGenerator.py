'''
Created on Feb 21, 2014

@author: phcostello
'''

from numpy import random
from numpy.random import normal 


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
        return self

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
        
        
if __name__ == '__main__':
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    #Gen normal path
    ngen = NormalGenerator()
    path = ngen.get_variates(mu=0, sig=1, size=20000)
    plt.hist(x=path, bins=40)
    plt.show()
    
    path1 = ngen.set_seed(seed=0).get_variates(size=4)
    path2 = ngen.set_seed(seed=0).get_variates(size=4)
    print path1
    print path2
    
    
