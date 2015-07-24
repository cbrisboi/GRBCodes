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
    print("GRB{0}, Default: All Photons >100MeV" .format(name))

#Everything is good, set it up
else:
    name=sys.argv[1]
    lim=sys.argv[2]
    print("GRB{0}, All Photons >{1}MeV" .format(name,lim))


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
#z=[x[2] for x in array]
#ra=[x[3] for x in array]
#dec=[x[4] for x in array]
#err=[x[5] for x in array]


#Find the trigger time
MET=0.0
search=len(GRB)
for i in range(search):
    if (burstname==GRB[i]):
        MET = float(trig[i])

if (MET==0.0):
    print("This GRB is not in the list!! Update it")
    sys.exit()




#Setup for file writing
file=open(output, 'w')
header='#ENERGY(MeV)    RA          DEC           L            B           TIME(s)\n'
file.write(header)


##########################################################################
#Go through whole file, is a long file
#
#Check for photons above energy limit, after trigger time
#
#Add other conditions as needed
##########################################################################


#NEED TO ADD T90 functionality to window, need to change everytime for now
window=3.0

trigger=MET-window
stop=MET+window
#print MET
#print stop

if (ti[0]>stop):
    print("You downloaded the wrong weekly file. Way to go.")
    print
    sys.exit()




for i in xrange(length):
    #Find all photons in time window, and above the emergy limit
    if ( ( trigger<ti[i]<stop )and (En[i]>mev) ):
        line=str(En[i])+space+str(Ra[i])+space+str(Dec[i])+space+str(L[i])+space+str(B[i])+space+str(ti[i])+'\n'
        file.write(line)
    #No need to keep going after the time limit
    if (ti[i]>stop):
        break

file.close()
print("GRB{0}: Data Output to: {1}" .format(burstname, output))
