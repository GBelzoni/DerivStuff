'''
Created on Feb 15, 2014

@author: phcostello
'''

# if __name__ == '__main__':
#    pass


#Proj 1
#Implement Analytic formulas for
#Price(TimeToMat, r, dividend, strike, spot, volatility)
#Call option
#Put Option
#Digital Call option
#ZCB

import AnalyticFunctions as af
reload(af)
af.ZCB(rate=0.05, Expiry=1) 
