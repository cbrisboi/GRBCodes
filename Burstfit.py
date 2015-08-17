# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 03:34:57 2015

Chad Brisbois

This module contains a class to model an arbitrary number of Norris pulses of the form:

            A * exp(Rise / (t - time0) + (t - time0) / Decay)

This is of the same form as the gtburstfit tool provided in Fermi-Tools

However, this will (hopefully) not contain the same hurdles which hinder its use.

"""

import numpy as np
from scipy.optimize import curve_fit as fit


def burstfit(N=1, bins, counts, params, method="chi2"):
    if method=="chi2":
        return modelfit(N, bins, counts, params)
    elif method=="bayesian":
        print("This functionality has not yet been added")
        return 42.0
    else:
        raise NameError("Must enter fitting method: chi2 or bayesian")



def modelfit(N, bins, count, params):


    burst=PulseModel(N, bins, counts)
    
    final_param=fit(burst, bins, count, p0=param)
    
    return final_param
    
    
def convert_params(params):
    #################################
    #This is relatively esoteric. curve_fit requires a list of parameters
    #Syntax for those parameters are 
    #[amp1, rise1, decay1, pulse1, amp2, rise2, ... , background]
    #
    #This function converts that list (using modular arithmetic) into 4 lists + background value
    #
    #This is an effort to keep the rest of this module readable by separating the parameters from each other  
    #Because python does not have a switch case statement, I used dictionary mapping, after popping off the
    #       background value. Since i % 4 will only result in integers 0-3 it is a simple matter to write a 
    #       dictionary to map the position in the sequence required by curve_fit to that required by this 
    #       module while maintaining readability
    #
    #This technique for mapping rather than switch is very powerful, but only if you dont need an else case
    #       otherwise, use if, elif, else. 
    #################################

    bkg = params.pop(-1)


    Amp=[]
    Rise=[]
    Decay=[]
    Pulse=[]
    
    load_lists = {0 : lambda x: Amp.append(x)   , \ 
                  1 : lambda x: Rise.append(x)  , \
                  2 : lambda x: Decay.append(x) , \
                  3 : lambda x: Pulse.append(x) }
    
    for i in range(len(params)):
        which = i % 4
        
        val=params[i]
        
        load_lists[which](val)

    return Amp, Rise, Decay, Pulse, bkg

def deconvert_params(A, R, D, P, bkg):
    n = len(A)
    
    length = 4 * n + 1
    
    params=[]

    wrap_lists = {0 : params.append(A.pop(0)), \ 
                  1 : params.append(R.pop(0)), \
                  2 : params.append(D.pop(0)), \
                  3 : params.append(P.pop(0)) }

    for i in range(length):
        which = i % 4
        wrap_lists[which]

    params.append(bkg)
    
    return params


class PulseModel(object):
    
    def __init__(self, N, bins, counts):
        
        
        if isinstance(N, int):
            self.N=N
        else:
            raise TypeError("N must be an integer")
            
        if isinstance(bins, list):
            self.bins=bins
        else:
            raise TypeError("Bins must be a list")
            
        if isinstance(counts, list):
            self.counts=counts
        else:
            raise TypeError("Counts must be a list")
        
        
    def __call__(self, t, params):
               
        Amp, Rise, Decay, Pulse, Back = convert_params(params)
        
        bkg=Back

        check=Pulse.sort()

        if self.N != len(Amp):
            raise ValueError("Model Constructed for N={0} terms, Given {1} terms in parameter array" .format(self.N, len(Amp)))

        if Pulse[0]< 239557417.0:
            raise ValueError("Pulse cannot start before Fermi launched")

        for i in Decay:
            if i==0.0:
                raise ZeroDivisionError("No Decay constants may be zero")

            
        return self.eval(Amp, Rise, Decay, Pulse, bkg, t)
        

    def eval(self, Amp, Rise, Decay, Pulse, bkg, t):
        return _Model(t, bkg, Amp, Rise, Decay, Pulse) 

    def _Model(self, time, bkg, Amp, Rise, Decay, Pulse):
        t=[time]
        
        val= np.sum( Amp * np.exp(Rise / (t[0] - Pulse) + (t[0] - Pulse) / Decay) ) + bkg

        return val

    
