'''
Created on Feb 16, 2014

@author: phcostello
'''
import math
class Gatherer(object):
    '''
    Base Class for results gatherer
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def reset(self):
        '''
        Reset Gatherer to empty
        '''
        pass
    
    def dump_one_result(self, result):
        '''
        Collect result
        '''
        pass
        
        
   
class MeanGatherer(Gatherer):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.result = {'sum':0.0,
                       'paths_done': 0.0}
        
    def reset(self):
        
        self.result = {'sum':0.0,
                       'paths_done': 0.0}
        
        
    def dump_one_result(self, result):
        
        self.result['sum'] += result
        self.result['paths_done'] +=1.0
        
        
    def mean(self):
        
        return self.result['sum']/self.result['paths_done']
    
class SDGatherer(Gatherer):
    '''
    classdocs
    '''
 
 
    def __init__(self):
        '''
        Constructor
        '''
        self.result = {'sum':0.0, 
                       'sumsquared': 0.0, 
                       'paths_done': 0.0,
                       'mean':0.0,
                       'sd':0.0}
         
    def reset(self):
         
        self.result = {'sum':0.0, 
                       'sumsquared': 0.0, 
                       'paths_done': 0,
                       'mean':0.0,
                       'sd':0.0}
     
    def dump_one_result(self, result):
         
        self.result['sum'] += result
        self.result['sumsquared'] += result*result
        self.result['paths_done'] +=1.0
        self.result['mean'] = self.result['sum']/self.result['paths_done']
        #Calc variance first
        self.result['sd'] = self.result['sumsquared']/self.result['paths_done'] - self.result['mean']*self.result['mean']
        self.result['sd'] = math.sqrt(self.result['sd'])
    
          
    def mean(self):
        
        return self.result['mean']
    
class ConvergenceTable(object):
    
    def __init__(self,gatherer,stopping_point):
        '''
        Add convergence table eleement
        '''
        self.collection_point = 2
        self.paths_done = 0
        self.stopping_point = stopping_point
        self.gatherer = gatherer
        
        #result should be initialised dict that we'll add result to
        gatherer.reset()
        tbinitdata = dict(gatherer.result)
        
        
        self.table = dict()
        for key, val in tbinitdata.items():
            self.table[key] = [val]
            
            
        
    def reset(self):
        '''
        reset to empty results
        '''
        self.gatherer.reset()
        
    def dump_one_result(self, result):
        '''
        dump result, add to sum
        on save paths of power two powers to table 
        '''
        
        self.gatherer.dump_one_result(result)
        self.paths_done +=1.0
        
        
        if self.paths_done == self.collection_point:
            
            self.collection_point *= 2
            for key in self.gatherer.result.keys():
                
                self.table[key] += [self.gatherer.result[key]]
        
        elif self.paths_done == self.stopping_point:
            
            for key in self.gatherer.result.keys():
                
                self.table[key] += [self.gatherer.result[key]]
    
    def mean(self):
        
        return self.gatherer.mean()        
            
if __name__ == '__main__':
    
    
    mg = MeanGatherer()
    
    for i in range(0,100):
        
        mg.dump_one_result(float(i))
        
    print mg.mean()
    mg.reset()
#     print mg.mean() #Should throw division by zero error
    
    num_paths =100000
    mg.reset()
    
    mg_table = ConvergenceTable(mg,stopping_point=num_paths)
    for i in range(0,num_paths):
        
        mg_table.dump_one_result(float(i))
    
    
    import pandas as pd
#     print pd.DataFrame({'a':[1,1], 'b':[2,2]})
    print pd.DataFrame(mg_table.table)
    mg_table.reset()
    print mg_table.table
    
    from numpy.random import normal
    sd = SDGatherer()
    sd.reset()
    sd_table = ConvergenceTable(sd,stopping_point=num_paths)
    for i in range(0,num_paths):
        
        this_res = normal(2,5,1)
        sd_table.dump_one_result(float(this_res))
        
    print pd.DataFrame(sd_table.table)
    

    
        