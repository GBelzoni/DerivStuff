'''
Created on Feb 21, 2014

@author: phcostello
'''


class Parameters(object):
    '''
    classdocs
    '''

    def __init__(self, constant):
        '''
        Constructor
        '''
        pass
    
    def int(self, t1, t2):
        
        pass
        

    def int_sqr(self, t1, t2):
       
        pass


class ParametersConstant(object):
    '''
    classdocs
    '''

    def __init__(self, constant):
        '''
        Constructor
        '''
    
        self.constant = constant
        
    def int(self, t1, t2):
        
        return self.constant*(t2-t1)
        
    
    def int_sqr(self, t1, t2):
        
        return self.constant**2/2.*(t2-t1)
    