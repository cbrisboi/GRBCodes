"""
Chad Brisbois
7/31/2015
This is an implementation of Knuth's optBINS algorithm from arxiv:0605197

It is a brute-force method to determine the optimal bin number for a given set of data. 
This allows for a systematic method to determine the bin width for the prompt emission 
    for LAT data during a GRB. Or some other set of data.  

"""

import numpy as np
from scipy.special import gammaln


#from scipy.optimize import fmin
#from matplotlib import pyplot as p

###################
#This is written from the sample code provided in the paper \
#   after I failed to use AstroML's implementation
#
###################

def prob(nk,M):
    N=len(nk)
    
    optbins= N * np.log(M)             \
            + gammaln(0.5 * M)          \
            - M * gammaln(0.5)          \
            - gammaln(N + 0.5 * M)      \
            + np.sum(gammaln(nk + 0.5)) 
    return optbins

def knuthbin(data, maxM):

    if data.ndim != 1:
        raise ValueError("Data needs to be one-dimensional")
    
    data.sort()
    
    ms=range(1,maxM+1)
    #print ms
    maxthing=[prob(data,i) for i in ms]
    

    return ms[np.argmax(maxthing)]
    

    
