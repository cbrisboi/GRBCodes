"""
Author: Chad Brisbois
Date:   4/6/15

This program will take calculate the luminosity distance from a given redshift.

optional arguments will be the 3 density parameters and the hubble parameter:

I am pulling these values from the Planck 2015 results 
"""
##########################
##      PARAMETERS      ##
##########################
M=0.308
L=1-M
h=0.678

H_o=100*h #km/s /Mpc
c=3.0e5 #km/s

##########################
##########################

import sys
import numbers
import math
from scipy.integrate import quad


sys.argv.pop(0)

#Check the arguments, make sure there is only one!
#print sys.argv
if len(sys.argv)==0:
    print "You must give a redshift value"
    exit()
elif len(sys.argv) > 1:
    print "You may only enter ONE redshift"
    exit()
else:
    red=sys.argv[0]
    
#See if its a number, if it's not, yell at user
try:
    red=float(red)
except ValueError:
    print "The redshift MUST be a number and greater than zero"
    exit()

if (red<0.0):
    print "The redshift MUST greater than zero"
    exit()

###############################################
###      USEFUL PART OF PROGRAM BELOW       ###     
###############################################
"""
This is the integral we need to solve

Taken from Distance Measures in Cosmology  Hogg,2000
"""
def zdist(z):
    E=math.sqrt(M*(1.0+z)**3.0+L)
    integ=1.0/E
    return integ

"""To fix units"""
D_h1=3000/h  #Mpc
D_h2=9.257e25/h #m

distMpc=0
distm=0
err=0
how=0
far=0

print ''
print ''
print 'Luminosity Distance to redshift z={0}' .format(red)
print '--------------------------------------------------'



"""
Do the integration (Unitless)
"""
how, err = quad (zdist, 0, red)
"""Scale by redshift"""
far=(1+red)*how

"""Add units, display!"""
distMpc=D_h1*far
distm=D_h2*far

print ' {:>.3e} Mpc' .format(distMpc)
print ' {:>.3e} m'   .format(distm)
print ' {:>.3e} cm'   .format(distm*100.0)
print '--------------------------------------------------'
print ''
print ''
