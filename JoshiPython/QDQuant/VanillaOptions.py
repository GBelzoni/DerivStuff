'''
Created on Feb 16, 2014

@author: phcostello
'''


class Trade(object):

    def __init__(self):
        '''
        Constructor
        '''
        self.notional = 1
    
    def price(self):
        
        pass
    
    def value(self):
        
        return self.price()*self.notional
        

class VanillaOption(Trade):
    '''
    classdocs
    '''

    def __init__(self, Expiry, PayOff):
        '''
        Constructor
        '''
        self.Expiry = Expiry
        self.PayOff = PayOff
    
    def pay_off(self, spot):
        
        return self.PayOff.po(spot)
    
    def price(self,model):
        
        return model.price(self)
    
if __name__ == '__main__':
    
    from PayOffs import VanillaCall, VanillaPut
    
    Strike = 110.
    Spot = 100.
    
    vc1 = VanillaCall(Strike)
    vp1 = VanillaPut(Strike)
    
    vo_call = VanillaOption(Expiry=1, PayOff=vc1)
    vo_put = VanillaOption(Expiry=1, PayOff=vp1)
    
    print vo_call.pay_off(Spot)
    print vo_put.pay_off(Spot)
    
    
    