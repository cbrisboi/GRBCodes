#Chad Brisbois
#11/3/2014
#
#
#This program will take data from a ascii file for a GRB and then plot the energy of the photons within a given radius after a trigger time
#
#Requires WeekPhotons.txt to exist
#
#produces Photons.grb
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






filename ='Photons.grb'
output   ='EnergyTimePlot.ps'

En,Ra,Dec,L,B,ti,ed = sp.loadtxt(filename,unpack = True,skiprows=1)


trigger=4e9

mev=100.0

p.title('GRB141028A above '+str(mev)+'MeV')
p.xlabel('Time (s)')
p.ylabel('Energy (MeV)')

p.yscale('log')

p.scatter(ti, En, s=0.3, marker='.')
