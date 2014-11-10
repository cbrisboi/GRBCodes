#Chad Brisbois
#11/3/2014
#
#
#This script will take ascii data files for Fermi data and parse the data by energy regime
#
#This output another ascii file (much smaller) that can then be plotted using PhotonPlotter.py
#
#
#
#
#Source File must be in form
#En RA DEC L B time (possibly another thing???)

import scipy as sp



datafile="RawPhotons.grb"
output  ="Photons.grb"
space   ='     '

#Importing file for parsing
En, Ra, Dec, L, B, ti, EventClass = sp.loadtxt(datafile, unpack-True, skipprows=3)


#energy limit
mev = 100.0

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
