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
from os.path import isfile

import scipy as sp
from matplotlib import pyplot as p


#print sys.argv

#Only burst name given                                                   
if ( len(sys.argv) > 3):
    print("You can only parse data for One burst at a time")
    sys.exit()

#Only burst name given, use default 100MeV limit
elif ( len(sys.argv) == 2 ):
    mev=100.0
    name=sys.argv[1]
    print("GRB{0}, Default: Plotting All Photons >100MeV" .format(name))

#Everything is good, set it up
else:
    name=sys.argv[1]
    mev=sys.argv[2]
    print("GRB{0}, Plotting All Photons >{1}MeV" .format(name,lim))



filename ='/home/campus26/cbrisboi/Desktop/GRB_Research/GRBs/{0}/Photons.grb' .format(name)
output   ='/home/campus26/cbrisboi/Desktop/GRB_Research/GRBs/{0}/EvTGRB{0}.ps'.format(name)


if not(isfile(filename)):
    print("The file {0} does not exist. Did you run ParseData.py first?" .format(filename))
    sys.exit



En,Ra,Dec,L,B,ti = sp.loadtxt(filename,unpack = True,skiprows=1)



p.title("GRB{0} above {1}MeV".format(name,mev))
p.xlabel('Time (s)')
p.ylabel('Energy (MeV)')

p.yscale('log')

p.scatter(ti, En, s=0.3, marker='.')
p.savefig(output)
