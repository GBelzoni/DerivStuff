'''
Created on Feb 20, 2014

@author: phcostello
'''

import numpy as np


class PathDependentOption(object):
    '''
    Path dependent options will start modelling Asian and discrete barrier
    type options
    
    Early exerices not considered yet
    '''


    def __init__(self, parameters=None):
        '''
        Constructor
        parameters should have look_at_times
        Expiry
        Cashflow times - probably expiry, but maybe not, e.g cliquet
        PayOff
        path_generator
        '''
        self.parameters = parameters
        
    def list_parameter_info(self):
        pass
        
    def get_cashflows(self, path):
        
        pass
    
    
class AsianArithmeticOption(PathDependentOption):
    '''
    Path dependent options will start modelling Asian and discrete barrier
    type options
    
    Early exerices not considered yet
    '''
        
    def make_parameter_template(self):
        
        """
        Creates a dict of input paramters to fill in"
        payoff - vanilla payoff against average"
        look_at_times - list of times that will be avd over"
        Expiry - single time of expiry"
        """
        
        parameters = {'payoff':None, 'look_at_times':None, 'Expiry':None}
        
        return parameters
            
    def get_cashflows(self, path):
        
        #Evaluate the payoff for path
        #Average of price - K
        average_price = np.mean(path)
        #Calc payoff
        po = self.parameters['payoff']
        this_payoff = po.po(average_price)
        
        return this_payoff

class UpAndOutCall(PathDependentOption):
    '''
    Path dependent options will start modelling Asian and discrete barrier
    type options
    
    Early exerices not considered yet
    '''
        
    def make_parameter_template(self):
        
        """
        Creates a dict of input paramters to fill in"
        payoff - vanilla payoff against average"
        look_at_times - list of times that will be avd over"
        Expiry - single time of expiry"
        """
        
        parameters = {'payoff':None, 
                      'look_at_times':None, 
                      'Expiry':None, 
                      'Barrier':None}
        
        return parameters
            
    def get_cashflows(self, path):
        
        #Evaluate the payoff for path
        #Calc payoff
        payoff = self.parameters['payoff']
        barrier = self.parameters['Barrier']
        if any(map(lambda(x): x >= barrier,path)):
            this_payoff = 0.0
        else:
            #Calc payoff
            this_payoff = payoff.po(path[-1]) #Get last element of path
        
        
        return this_payoff


        
if __name__ == "__main__":
    
    from QDQuant.PayOffs import VanillaCall
    
    payoff = VanillaCall(Strike=100.)
    parameters = {'payoff': payoff, 'look_at_times':[0.5,1.0],'Expiry':1.0}
    
    ao = AsianArithmeticOption(parameters)
    
    path = [110.,120.]
    
    print "Cash Flows for path", ao.get_cashflows(path)
    
        
        