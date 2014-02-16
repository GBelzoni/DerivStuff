'''
Created on Feb 16, 2014

@author: phcostello
'''
import math
 

class VanillaMCPricer(object):
    '''
    classdocs
    '''


    def __init__(self, spot, rate, Vol, generator, gatherer, num_paths, dividend=0):
        '''
        Currently dividend not implement
        '''
        self.spot = spot
        self.rate = rate
        self.Vol = Vol
        self.generator = generator
        self.gatherer = gatherer
        self.num_paths = num_paths
        self.dividend = dividend
        self.price = "Not price yet"
        
    def do_trade(self,trade):
        
        #Setup sim wide pars
        df = math.exp(-rate*trade.Expiry) 
        gatherer.reset()
        generator.times = [Expiry]
        
        for i in range(0,self.num_paths):
            #Generate S_t
            thisSpot = generator.do_one_path()[0]
            thisPayOff = trade.pay_off(thisSpot)
            gatherer.dump_one_result(thisPayOff)
        
        
        self.price = df*gatherer.mean()
            
    
    
if __name__ == '__main__':
    
    from PayOffs import VanillaCall, VanillaPut
    from VanillaOptions import VanillaOption
    from Gatherer import MeanGatherer
    from PathGenerators import BGMGenerator
    
    from AnalyticFunctions import BSAnalyticFormulas
    
    #Option params
    Strike = 110.
    Expiry = 1.
    
    vc1 = VanillaCall(Strike)
    vp1 = VanillaPut(Strike)
    
    vo_call = VanillaOption(Expiry, PayOff=vc1)
    vo_put = VanillaOption(Expiry, PayOff=vp1)
    
    #Model/Market parameters
    Spot = 100.
    rate = 0.05
    Vol = 0.2
    dividend = 0.0 #not included in pricing yet
    
    #Model parameters
    times = [1.]
    num_paths = 500000
    generator = BGMGenerator(Spot,rate,Vol,times)
    gatherer = MeanGatherer()
    
    #Do sim
    mc_pricer = VanillaMCPricer(Spot, rate, Vol, generator, gatherer, num_paths, dividend)
    mc_pricer.do_trade(vo_put)
    price_put = mc_pricer.price
    mc_pricer.do_trade(vo_call)
    price_call = mc_pricer.price
    
    #Compare to Analytic Pricer
    
    bsan = BSAnalyticFormulas(Spot, Strike, rate, Vol, Expiry, dividend)
    print "MC price Put: ", price_put
    print "Analytic Put price: ", bsan.PutPrice()
    print "MC price Call: ", price_call
    print "Analytic Call price: ", bsan.CallPrice()
    
    
    