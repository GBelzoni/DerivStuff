'''
Created on Feb 16, 2014

@author: phcostello
'''



class PayOff(object):
    '''
    Base Class for vanilla payoffs
    Not much to do here, just define po function that gives payoff
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def po(self, Spot):
        
        '''
        PayOff given underlying Spot
        '''
        pass
    
class VanillaPut(PayOff):
    '''
    PayOff of Vanilla Call
    '''


    def __init__(self, Strike):
        '''
        Constructor
        '''
        self.Strike = Strike
    
    def po(self, Spot):
        
        '''
        PayOff of Call given underlying Spot
        '''
        return max(self.Strike - Spot, 0.0 )

class VanillaCall(PayOff):
    '''
    PayOff of Vanilla Call
    '''


    def __init__(self, Strike):
        '''
        Constructor
        '''
        self.Strike = Strike
    
    def po(self, Spot):
        
        '''
        PayOff of Call given underlying Spot
        '''
        return max(Spot - self.Strike , 0.0 )
    

    
    
if __name__ == '__main__':
    
    Strike = 110.
    Spot = 100.
    
    vc1 = VanillaCall(Strike)
    vp1 = VanillaPut(Strike)
    print vc1.po(Spot)
    print vp1.po(Spot)
    