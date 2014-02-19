'''
Created on Feb 20, 2014

@author: phcostello
'''

class PathDependentOption(object):
    '''
    Path dependent options will start modelling Asian and discrete barrier
    type options
    
    Early exerices not considered yet
    '''


    def __init__(self, parameters):
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
        
    def calc_cashflows(self, path):
        
        pass
    
    
class AsianArithmeticOption(PathDependentOption):
    '''
    Path dependent options will start modelling Asian and discrete barrier
    type options
    
    Early exerices not considered yet
    '''


    def list_parameter_info(self):
        
        print "Paramters are:"
        print "Vanilla payoff"
        print "look_at_times - list of times that will be avd over"
        print "Expiry - single time of expiry"
        print "path_generator - Path generator"
        print "num_paths - Number of MC paths"
            
    def calc_cashflows(self, path):
        
        num_paths = self.parameters['num_paths']   
        payoff = self.parameters['payoff']
        
        #look at times
        look_at_times = self.parameters['look_at_times']
    
        #generate a path
        path_generator = self.path_generator
        path_generator.setup()
        
        
        sum = 0.
        
        for i in range(0,num_paths):
            
            path = path_gen.do_one_path() 
            # plt.plot(look_at_times,path)
            # plt.show()
            
            #Evaluate the payoff for path
            #Average of price - K
            average_price = np.mean(path)
            #Calc payoff
            po = VanillaCall(Strike=Strike)
            this_payoff = po.po(average_price)
            sum += this_payoff
        
        #Average and discount    
        price = math.exp(-rate*Expiry)*sum/num_paths
        
        return price
        
        
        
        