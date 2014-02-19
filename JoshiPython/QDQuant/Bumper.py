'''
Created on Feb 19, 2014

@author: phcostello
'''


def bump_delta_central( x, function, epsilon= 1e-5 ):
    """
    Use central diff to get bump delta
    """
    
    return (function(x + epsilon) -function(x - epsilon))/(2.*epsilon)
    

if __name__ == "__main__":
    
    linear = lambda(x): 3*x
    
    from math import sin
    
    print linear(4)
    
    print bump_delta_central(4, function=linear)
    
    import matplotlib.pyplot as plt
    import numpy as np
    
    xrange = np.linspace(0, 10, num=50)
    ysin = [ sin(x) for x in xrange]
    ycos = [ bump_delta_central(x, sin) for x in xrange ]
    
    plt.plot(xrange,ycos)
    plt.show()
    
    
    