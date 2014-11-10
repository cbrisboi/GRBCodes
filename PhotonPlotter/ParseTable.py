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
#
#
#Source File must be in form
#n, GRB, Ra(degrees), Dec(degrees), Error (degrees), z, trigger time, Boresight distance (degrees), source of position
#
#n, Boresight, and source of position is not used
#
#
#
import scipy as sp



datafile="GRBTable.dat"
output  ="GRBTableClean.dat"
space   ='     '

#Importing file for parsing


array = sp.genfromtxt('./GRBTable.dat', delimiter=',', dtype='S3, S7, S16, S16, S16, S8, S16, S20, S16')


n, GRB, Ra, Dec, Err, z, trigger, Bore, source 

for i in xrange(len(array)):

    n.append(int(array[i][0]))
    GRB.append(str(array[i][1]))

    Ra.append(float(array[i][2]))
    Dec.append(float(array[i][3]))


    Err.append(float(array[i][4]))

    if type(array[i][5])==str :
        z.append(DummyRedshift)
    else:
        z.append(float(array[i][5]))
    
    trigger.append(float(array[i][6])



# number of GRBs ~100 or so
length = len(n)
print length

DummyRedshift=777
#To avoid issues with the ' - ' for no reshift, I replace it with 777, so that it is recognizeable, but still a number
for i in xrange(length):
    if  ( float(z[i]) != z[i] ):
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
#Make it look pretty
##########################################################################



for i in xrange(length):
    line=str(GRB[i])+space+str(trigger[i])+space+str(z[i])+space+str(Ra[i])+space+str(Dec[i])+space+str(Err[i])+'\n'
    file.write(line)


file.close()
