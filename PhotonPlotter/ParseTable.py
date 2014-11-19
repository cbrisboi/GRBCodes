#Chad Brisbois
#11/4/2014
#
#
#This script will take ascii Table file for LAT GRBs and parse the data
#
#This output another ascii Table file that can then be plotted used in concert
#  with the photon data for plotting purposes
#
#
#Table found at http://www.asdc.asi.it/grblat/
#
#Source File must be in form
#n, GRB, Ra(degrees), Dec(degrees), Error (degrees), z, trigger time, Boresight distance (degrees), source of position
#
#n, Boresight, and source of position is not used
#
#
#
import scipy as sp



datafile="../GRBTable.dat"
output  ="../GRBParams.dat"
space   ='     '

#Importing file for parsing


array = sp.genfromtxt(datafile, delimiter=',', dtype='S3, S8, S16, S16, S16, S8, S16, S20, S16', skiprows=1)


#Load array values into the appropriate file columns
n=[x[0] for x in array]
GRB=[x[1] for x in array]
Ra=[x[2] for x in array]
Dec=[x[3] for x in array]
Err=[x[4] for x in array]
z=[x[5] for x in array]
trigger=[x[6] for x in array]
Bore=[x[7] for x in array]
Source=[x[8] for x in array]

# number of GRBs ~100 or so
length = len(n)
print( "There are {0} GRBs in the list" .format(length) )

DummyRedshift=777.0
#To avoid issues with the ' - ' for no reshift, I replace it with 777, so that it is recognizeable, but still a number
for i in xrange(length):
    if  ( type(z[i]) != float ):
        z[i]=DummyRedshift



#Setup for file writing
file=open(output, 'w')
header   ='# GRB    Trigger Time    Redshift    RA    DEC    Error    \n'
header2  ='#             (s)            z      (deg) (deg)   (deg)    \n'

file.write(header)
file.write(header2)

##########################################################################
#Go through whole Table
#
#Make it look pretty-ish
##########################################################################

for i in xrange(length):
    line=str(GRB[i])+space+str(trigger[i])+space+str(z[i])+space+str(Ra[i])+space+str(Dec[i])+space+str(Err[i])+'\n'
    file.write(line)


file.close()
