'''
Created on Apr 17, 2014

@author: phcostello
'''

from math import exp, fabs
import numpy as np


class CovarianceStructure(object):
    '''
    Base Class for Covariance Structure
    '''
    
    def __init__(self, *args, **kwargs):
        
        pass
    
    def vol(self, t, T):
        
        pass
    
    def cov(self,t,Tk, Tn):
        
        pass


class CovariantStructure_abcd(object):
    '''
    classdocs
    '''


    def __init__(self, a, b, c, d, beta):
        '''
        Constructor
        Parameterizes instantaneous vol
        inst_vol = (a+b(T-t))*exp(-c*(T-t)) + d
        '''
        self.a = a
        self.b = b        
        self.c = c
        self.d = d
        self.beta = beta
        
    def vol(self,t,Tn):
        '''
        Integral of instantaneous vol between t to Tn
        '''
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        
        if t < Tn:
            #Did this integration with sympy
            return Tn*d**2 - d**2*t + (2*a**2*c**2 + 2*a*b*c + 8*a*c**2*d + b**2 + 8*b*c*d)/(4*c**3) + \
                (-2*Tn**2*b**2*c**2 - 4*Tn*a*b*c**2 + 4*Tn*b**2*c**2*t - 2*Tn*b**2*c - 2*a**2*c**2 +\
                 4*a*b*c**2*t - 2*a*b*c - 2*b**2*c**2*t**2 + 2*b**2*c*t - b**2 - 8*c*d*(Tn*b*c + a*c - b*c*t + b)*exp(c*(Tn - t)))*exp(-2*c*(Tn - t))/(4*c**3)
        else:
            return 0.0


    def d_coeff(self,t,T1, T2):
        '''
        Decorrelation of covariance coefficient for t<Tn<Tk
        '''
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        
        Tn, Tk = min(T1,T2), max(T1,T2)
        
        if t < Tn:
            #Did this integration with sympy
        
            return Tn*d**2 - d**2*t + \
                (4*c*d*(Tk*b*c*exp(Tn*c) - Tn*b*c*exp(Tn*c) + a*c*exp(Tk*c) + a*c*exp(Tn*c) + b*exp(Tk*c) + b*exp(Tn*c))*exp(c*(Tk - Tn)) + (2*Tk*a*b*c**2 + Tk*b**2*c - 2*Tn*a*b*c**2 - Tn*b**2*c + 2*a**2*c**2 + 2*a*b*c + b**2)*exp(Tk*c))*exp(-c*(2*Tk - Tn))/(4*c**3) + (-4*c*d*(Tk*b*c*exp(Tn*c) + Tn*b*c*exp(Tk*c) + a*c*exp(Tk*c) + a*c*exp(Tn*c) - b*c*t*exp(Tk*c) - b*c*t*exp(Tn*c) + b*exp(Tk*c) + b*exp(Tn*c))*exp(c*(Tk - t)) - (2*Tk*Tn*b**2*c**2 + 2*Tk*a*b*c**2 - 2*Tk*b**2*c**2*t + Tk*b**2*c + 2*Tn*a*b*c**2 - 2*Tn*b**2*c**2*t + Tn*b**2*c + 2*a**2*c**2 - 4*a*b*c**2*t + 2*a*b*c + 2*b**2*c**2*t**2 - 2*b**2*c*t + b**2)*exp(Tk*c))*exp(-c*(2*Tk + Tn - 2*t))/(4*c**3)        
        else:
            return 0.0
        
    def cov_matrix(self,t, times):
        '''
        Generate matrix at t for times        
        '''
        
        cov_matrix = []
        for t1 in times:
            this_row = [ self.d_coeff(t, t1, t2) for t2 in times]
            cov_matrix.append(this_row)
        
        cov_matrix = np.matrix(cov_matrix)
        
        cov_coeff = []
        for t1 in times:
            this_row = [ exp(-self.beta*fabs(t1-t2)) for t2 in times]
            cov_coeff.append(this_row)
        
        cov_coeff = np.matrix(cov_coeff)
        
#         cov_matrix = cov_matrix * cov_coeff

#         return cov_matrix
        return np.multiply(cov_coeff,cov_matrix)


if __name__ == "__main__":
    
    cd = CovariantStructure_abcd(a=0.5,b=0.09,c=0.44,d=0.11,beta=0.1)
    
    print cd.vol(t=0.2, Tn=0.5)
    print cd.vol(t=0.0, Tn=0.3)
    
    times = [ 0.05, 0.1, 0.4, 0.7, 1.0]
    
    
    print cd.d_coeff(t=0.0, T1=0.1, T2=0.5)
    print cd.d_coeff(t=0.0, T1=0.5, T2=0.1)
    print cd.d_coeff(t=0.0, T1=0.3, T2=0.3)
    
    print cd.cov_matrix(t=0.0, times=times)
    
    
    
    
            