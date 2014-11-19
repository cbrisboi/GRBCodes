#Chad Brisbois
#11/3/2014
#
#
#This script will take ascii data files for Fermi data and parse the data by energy regime
#
#This output another ascii file (much smaller) that can then be plotted using PhotonPlotter.py
#
#sys library allows commandline arguments (like which burst we are working on)
#
#
#Source File must be in form
#En RA DEC L B time Event_class(possibly another thing???)
#
#Usage: ParseData.py <burstname> <energy limit>
#
#Default energy limit is 100MeV

import sys
import scipy as sp


#Only one burst and energy
if ( len(sys.argv) > 2):
    print("You can only parse data for One burst at a time")
    sys.exit()

#Only burst name given, use default 100MeV limit
elif ( len(sys.argv == 1) ):
    lim=100.0

#Everything is good, set it up
else:
    name=sys.argv[0]
    lim=sys.argv[1]



#Everything is good, set it up
burstname=name
mev=lim
burstdir="/home/campus26/cbrisboi/Desktop/GRB_Research/GRBs/"+str(burstname)+"/"



datafile=burstdir+"WeekPhotons.txt"
output  ="Photons.grb"
space   ='     '

#Importing file for parsing
En, Ra, Dec, L, B, ti, EventClass = sp.loadtxt(datafile, unpack=True, skipprows=3)



#size of data file, probably huge!
length = len(En)


#Setup for file writing
file=open(output, 'w')
header='#ENERGY(MeV) RA    DEC      L      B      TIME(s)\n'
file.write(header)


##########################################################################
#Go through whole file, could be a long file
#
#Check for photons above energy limit, need time limits, dont know to filter time
#
#Add other conditions as needed
##########################################################################



for i in xrange(length):
    if ( Enr[i]>mev ):
        line=str(En)+space+str(Ra)+str(Dec)+space+str(L)+space+str(ti)+'\n'
        file.write(line)


file.close()
