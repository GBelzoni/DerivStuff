'''
Created on Feb 20, 2014

@author: phcostello
'''

import math

class PathDependentMCPricer(object):
    '''
    classdocs
    '''
    
    def __init__(self, input_parameters = None):
        '''
        Constructor
        '''
        self.input_parameters = input_parameters
        self.market_parameters = self.input_parameters['path_generator'].market_params
    
    
    def do_trade(self,trade):
        
        num_paths = self.input_parameters['num_paths']   
        
        
        #look at times
        look_at_times = trade.parameters['look_at_times']
    
        #generate a path
        path_generator = self.input_parameters['path_generator']
        path_generator.sim_setup(look_at_times)
        
        gatherer = self.input_parameters['gatherer']
        
        
        for i in range(0,num_paths):
            
            path = path_generator.do_one_path() 
            this_payoff = trade.get_cashflows(path)
            gatherer.dump_one_result(this_payoff)
        
        #Average and discount
        rate = self.market_parameters['rate']
        Expiry = trade.parameters['Expiry']
                                  
        
        price = math.exp(-rate*Expiry)*gatherer.mean()
        
        return price
    
    
if __name__ == "__main__":
    
    pass
