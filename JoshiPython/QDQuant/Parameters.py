'''
Created on Feb 21, 2014

@author: phcostello
'''

from scipy.interpolate import interp1d
from bisect import bisect_left

class Parameters(object):
    '''
    classdocs
    '''

    def __init__(self, constant):
        '''
        Constructor
        '''
        pass
    
    def int(self, t1, t2):
        
        pass
        

    def int_sqr(self, t1, t2):
       
        pass


class ParametersConstant(object):
    '''
    classdocs
    '''

    def __init__(self, constant):
        '''
        Constructor
        '''
    
        self.constant = constant
        self.constantSqr = constant**2
        
    def int(self, t1, t2):
        
        return self.constant*(t2-t1)
        
    
    def int_sqr(self, t1, t2):
        
        return self.constantSqr*(t2-t1)

class ParametersPWConstant(object):
    '''
    Uses python bisect class to efficiently look up index for time points
    '''

    def __init__(self, x, y):
        '''
        Inputs:
        x: time poinst
        y: are constants where y[i] is constant over interval [x[i],x[i+1])
        
        Currently not supporting extrapolation beyond endpoints
        '''
    
        self.x = x
        self.y = y
        
    def int(self, t1, t2):
        
        '''
        Does piecwise integral between t1 and t2
        '''
        
        front_index = bisect_left(self.x, t1) 
        back_index = bisect_left(self.x, t2 )
        
        full_interval_integration = [self.y[i]*(self.x[i+1]-self.x[i]) for i in range(front_index, back_index-1)]
        front_stub = self.y[front_index-1]*(self.x[front_index] - t1) 
        back_stub = self.y[back_index-1]*(t2- self.x[back_index -1])
        
        return front_stub + sum(full_interval_integration) + back_stub
    
    def int_sqr(self, t1, t2):
       
        '''
        Does piecwise integral of square between t1 and t2
        ''' 
        front_index = bisect_left(self.x, t1) 
        back_index = bisect_left(self.x, t2 )
        
        full_interval_integration = [(self.y[i]**2)*(self.x[i+1]-self.x[i]) for i in range(front_index, back_index-1)]
        front_stub = (self.y[front_index-1]**2)*(self.x[front_index] - t1) 
        back_stub = (self.y[back_index-1]**2)*(t2- self.x[back_index -1])
        
        return front_stub + sum(full_interval_integration) + back_stub
        
        
    
if __name__ == "__main__":
    
    #uses scipy interpolators
    import numpy as np
    x = np.array([0.0,1.0,3.,7.])
    
    y = np.array([1.,2.,3.,4.])
    t1 = 0.
    t2 = 1.4
    t3 = 5.6
    pw_const = ParametersPWConstant(x,y)
    integral1 = pw_const.int(t1,t2)
    integral2 = pw_const.int(t1,t3)
    integral3 = pw_const.int(t2,t3)
    
    #Manually calc integrals by hand
    calc1 = 1*1. + 0.4*2. 
    calc2 = 1*1. + 2.0*2. + 2.6*3.
    calc3 = 2.0*1.6 + 3.0*2.6
    print integral1, calc1
    print integral2, calc2
    print integral3, calc3
   
    #Do piecwise constants 
    integral1 = pw_const.int_sqr(t1,t2)
    integral2 = pw_const.int_sqr(t1,t3)
    integral3 = pw_const.int_sqr(t2,t3)
    
    #Manually calc integrals by hand
    calc1 = 1*1. + 0.4*2**2. 
    calc2 = 1*1. + 2.0*2**2. + 2.6*3**2.
    calc3 = 2.0**2*1.6 + 3.0**2*2.6
        
    print integral1, calc1
    print integral2, calc2
    print integral3, calc3
 
    
    
    
    
    
    
    
    
    
    
    