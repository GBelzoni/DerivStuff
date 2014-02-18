'''
Created on Feb 16, 2014

@author: phcostello
'''

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
        self.sum = 0.0
        self.paths_done = 0.0
        
    def reset(self):
        
        self.sum = 0.0
        self.paths_done = 0.0
    
    def dump_one_result(self, result):
        
        self.sum += result
        self.paths_done +=1.0
        
        
    def mean(self):
        
        return self.sum/self.paths_done
    
class ConvergenceTable(MeanGatherer):
    
    def __init__(self,stopping_point):
        '''
        Add convergence table eleement
        '''
        super(ConvergenceTable,self).__init__()
        self.table = { 'sum': [0], 'paths_done': [0]}
        self.collection_point = 2
        self.stopping_point = stopping_point
        
    def reset(self):
        '''
        reset to empty results
        '''
        self.sum = 0.0
        self.paths_done = 0.0
        self.table = { 'sum': [0], 'paths_done': [0] }
    
    def dump_one_result(self, result):
        '''
        dump result, add to sum
        on save paths of power two powers to table 
        '''
        self.sum += result
        self.paths_done +=1.0
        
        if self.paths_done == self.collection_point:
            
            self.table['sum'] += [self.sum]
            self.table['paths_done'] += [self.paths_done] 
            self.collection_point *= 2
        
        elif self.paths_done == self.stopping_point:
            
            self.table['sum'] += [self.sum]
            self.table['paths_done'] += [self.paths_done]
            
            
if __name__ == '__main__':
    
    
    mg = MeanGatherer()
    
    for i in range(0,100):
        
        mg.dump_one_result(float(i))
        
    print mg.mean()
    mg.reset()
#     print mg.mean() #Should throw division by zero error
    
    num_paths =100000
    mg_table = ConvergenceTable(stopping_point=num_paths)
    for i in range(0,num_paths):
        
        mg_table.dump_one_result(float(i))
        
    print mg_table.mean()
    print mg_table.table
    
    import pandas as pd
#     print pd.DataFrame({'a':[1,1], 'b':[2,2]})
    print pd.DataFrame(mg_table.table)
    mg_table.reset()
    print mg_table.table
    

    
        