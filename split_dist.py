"""

Chad Brisbois
11/16/2015

This module will implement a split normal distribution, and allow for picking random values from that distribution

splitnorm(x, mu, sig1, sig2) gives value of the distribution at x

splitrand(mu, sig1, sig2, s=1) gives s random values distributed according to the distribution

This allows the estimation of error in the general case for values described as  F^+a_-b where a and b are sig1 and sig2. 

"""

import numpy as np


def splitnorm(x, mu, sig1, sig2):

    const=np.sqrt( 2.0 / np.pi) / (sig1 + sig2)

    """
    if x is below the mean value, return left part, otherwise, return right
    """
    if x < mu :
        final = const * np.exp( (x-mu)**2 / (2 * sig1**2 ))
    else:
        final = const * np.exp( (x-mu)**2 / (2 * sig2**2 ))

    return final

    
def splitrand(mu, sig1, sig2, s=1):
    
    const=np.sqrt( 2.0 / np.pi) / (sig1 + sig2)
    
    bigsig = max([sig1, sig2])
    print(bigsig)
    #endless loop stopper
    t=0
    total=[]
    i = 0
    while i < s:
        """
        set up acceptance rejection process

        using the biggest sigma essentially says that there is reduced chance for the other side, so we have to reject those values. 
        """
        amp = np.random.uniform(0, const)
        x = np.random.normal(loc=mu, scale=bigsig)


        if amp <= splitnorm(x, mu, sig1, sig2):
            i+=1
            total.append(x)
            

        if t ==100*s:
            print("Loop went on too long, random number generation terminated")
            break
    
        
    print i
    return total
