#Chad Brisbois
#11/3/2014
#
#
#This program will take data from a ascii file for a GRB and then plot the energy of the photons within a given radius after a trigger time
#
#Requires WeekPhotons.txt, GRBRealTime.dat to exist
#
#Plot of photons during MET+/-1000s
#
#
#
#
#Usage: python PhotonPlotter.py 
#
#

import sys


import scipy as sp
from matplotlib import pyplot as p


print sys.argv

#Only burst name given                                                   
if ( len(sys.argv) == 2 ):
    name=sys.argv[1]
else:
    print("You can only plot one GRB at a time.")
    sys.exit()






RealTimes='/home/campus26/cbrisboi/Desktop/GRB_Research/GRBCodes/GRBRealTime.dat'
filename ='/home/campus26/cbrisboi/Desktop/GRB_Research/GRBs/{0}/Photons.grb' .format(name)
output   ='EnergyTimePlot.ps'




#bursts, times, centRa, cent Dec, err = sp.loadtxt(RealTimes, unpack=True, skiprows=1)


#Check if name is a burst we can plot

#for i in range(len(bursts)):
    



En,Ra,Dec,L,B,ti,ed = sp.loadtxt(filename,unpack = True,skiprows=1)


mev=100.0

p.title('GRB141028A above '+str(mev)+'MeV')
p.xlabel('Time (s)')
p.ylabel('Energy (MeV)')

p.yscale('log')

p.scatter(ti, En, s=0.3, marker='.')
