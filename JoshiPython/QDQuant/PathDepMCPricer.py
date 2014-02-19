'''
Created on Feb 20, 2014

@author: phcostello
'''

class PathDependentMCPricer(object):
    '''
    classdocs
    '''
    
    def __init__(self, path_generator, input_parameters = None):
        '''
        Constructor
        '''
        self.path_generator
        self.input_parameters = input_parameters
    
    
    def do_trade(self):
        
        #look at times
        look_at_times = list(np.linspace(start=0, stop=Expiry, num=12))
        
        #generate a path
        
        path_gen = GBMGenerator(spot=Spot, rate=rate, vol=Vol, times=look_at_times)
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
