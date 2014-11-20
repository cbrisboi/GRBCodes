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
#Requires WeekPhotons.txt to be in burst directory, ../GRBs/<burstname>
#
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

print sys.argv

#Only one burst and energy
if ( len(sys.argv) > 3):
    print("You can only parse data for One burst at a time")
    sys.exit()

#Only burst name given, use default 100MeV limit
elif ( len(sys.argv) == 2 ):
    lim=100.0
    name=sys.argv[1]

#Everything is good, set it up
else:
    name=sys.argv[1]
    lim=sys.argv[2]



#Everything is good, set it up
burstname=name
mev=lim
burstdir="/home/campus26/cbrisboi/Desktop/GRB_Research/GRBs/"+str(burstname)+"/"



datafile=burstdir+"WeekPhotons.txt"
output  =burstdir+"Photons.grb"
space   ='     '

#Importing file for parsing
En, Ra, Dec, L, B, ti, EventClass = sp.loadtxt(datafile, unpack=True, skiprows=3)



#size of data file, probably huge!
length = len(En)


#import parameters
paramfilename="/home/campus26/cbrisboi/Desktop/GRB_Research/GRBCodes/GRBParams.dat"

array = sp.genfromtxt(paramfilename, skiprows=2, dtype='S8, S16, S16, S10, S16, S16')


#Load array values into the appropriate file columns                                                                           
GRB=[x[0] for x in array]
trig=[x[1] for x in array]
z=[x[2] for x in array]
ra=[x[3] for x in array]
dec=[x[4] for x in array]
err=[x[5] for x in array]


#Find the trigger time
trigger=0.0
search=len(GRB)
for i in range(search):
    if (burstname==GRB[i]):
        trigger = float(trig[i])

if (trigger==0.0):
    print("This GRB is not in the list!! Update it")
    sys.exit()




#Setup for file writing
file=open(output, 'w')
header='#ENERGY(MeV) RA    DEC      L      B      TIME(s)\n'
file.write(header)


##########################################################################
#Go through whole file, is a long file
#
#Check for photons above energy limit, after trigger time
#
#Add other conditions as needed
##########################################################################
trigger=trigger-1000.0
stop=trigger+1000.0
print trigger
print ti[0]

if (ti[0]>stop):
    print("Hey, doofus! You downloaded the wrong weekly file. Way to go.")
    sys.exit()

for i in xrange(length):
    if ( ( trigger<ti[i]<stop ) ):
        if (En[i]>mev):
            line=str(En)+space+str(Ra)+str(Dec)+space+str(L)+space+str(B)+space+str(ti)+'\n'
            file.write(line)
    
    if (ti[i]>stop):
        break

file.close()
