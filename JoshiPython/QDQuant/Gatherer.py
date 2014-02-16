'''
Created on Feb 16, 2014

@author: phcostello
'''

class MeanGatherer(object):
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
    
    
if __name__ == '__main__':
    
    
    mg = MeanGatherer()
    
    for i in range(0,100):
        
        mg.dump_one_result(float(i))
        
    print mg.mean()
    mg.reset()
    print mg.mean() #Should throw division by zero error
    
        