# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:47:02 2013

@author: Chad
"""

import scipy as sp                          #This brings in scipy - whenever I type sp  in the program I would otherwise need to type scipy
import time
import random as rand

rand.seed()

def Norris(t):
	A=44   #285
	tau=1.28  #14.74
	ksai=-1.0    #-1.3862943
	if t!=0.0:
		norris = A*sp.exp(ksai*(t/tau+tau/t))
	else:
		norris=0.0
	return norris


	
def deltas(t):
	dt=[]
	bunch=1
	for i in range(len(t)-bunch):                              ################## FINDING dt and dE's
		dt.append(t[i+bunch]-t[i])
	return dt





EEn , tti, ty, = sp.loadtxt('100MEV10DEGEVENTS.txt',unpack = True,skiprows=3)

ttti=[]
EEEn=[]

mev=1000.0                                                   ################### SELECT ENERGIES
mevlim=10000000.0

for i in range(len(tti)):
	if mev<EEn[i]<mevlim:
			EEEn.append(EEn[i])
			ttti.append(tti[i])
En=[]
ti=[]
starttime=tti[0]+1376.0         #955.0                            ################## GRABBING TIMES 0-3s

for i in range(len(ttti)):
	if (0.0<(ttti[i]-starttime)<3.0):
		ti.append(ttti[i]-starttime)
		En.append(EEEn[i])


dt=deltas(ti)                          ################## FINDING REAL dt


coup=[0,0,0,0]

for counting in range(4):                                    ################## COUNTING COUPLES IN DATA
	threshold=0.10/(10**(counting))   #start at 10s
	print threshold
	for i in range(len(dt)):
		if dt[i]<=threshold:
			coup[counting]+=1.0   



stopwatch=time.time()                                        ################## START STOPWATCH
yay=[0,0,0,0]


PHOTONCOUNT=float(len(ti))


# '------REAL TIMES ABOVE------'
iters = 10**7

for it in range(iters):
	rand.seed()
	couple=[0,0,0,0]
	faket=[]
	
	while(len(faket)!=PHOTONCOUNT):                    ################## GENERATE FAKE PHOTONS
		phot=rand.uniform(0.0,6.0)    #18.0
		tim=rand.uniform(0.0,3.0)      #50.0

		if Norris(tim)>phot:
			faket.append(tim)	
	
	faket.sort()                                       ################## SORTING FAKE PHOTONS
		
	fakedt = deltas(faket)              ################## FINDING FAKE dt AND dE's
	


	for counting in range(4):
		threshold=0.10/(10**(counting))


		for i in range(len(fakedt)):
			if fakedt[i]<=threshold:
				couple[counting]+=1.0
		
		#print couple
		if couple[counting]>=coup[counting]:
			yay[counting]+=1.0

	


print coup
#print couple
print yay



	
filename='090510TimeTestfor'+str(mev)+'MeV.txt'################ SETUP FILE
file=open(filename,'w')
file.write('Real Data Couples below 0.1, 0.01, 0.001, 0.0001: '+str(coup)+'\n')
file.write('Couple Successes out of '+str(iters)+': '+str(yay)+'\n')
file.close()

						
		


	

print time.time()-stopwatch

