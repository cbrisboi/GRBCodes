# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 15:47:02 2013

@author: Chad
"""

import scipy as sp                          #This brings in scipy - whenever I type sp  in the program I would otherwise need to type scipy
from scipy import integrate
from matplotlib import pyplot as p          #plotting package - the "as p" allows us to just type p instead of pyplot while configuring the plot settings
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


def Dn(z,n):
	#constants                         #units
	c = 2.99792458*10**5               # km/s
	Ho = 2.175*10**-18                 # 67.11(km/s)/Mpc  ---> Hz
	OM = 0.3175
	OL = 0.6825
	dist = lambda red: ((1+red)**n)/(sp.sqrt(OM*((1+red)**3)+OL))
	integ = integrate.quad(dist,float(0),z)
	d=(c/Ho)*integ[0]
	return d
	
def deltas(t,E):
	dt=[]
	dE=[]
	for i in range(len(t)-1):                              ################## FINDING dt and dE's
		dt.append(t[i+1]-t[i])
		dE.append(abs(E[i+1]-E[i]))
		#if dE>25.0*10**3:
			#print i
			#print dt[i],dE[i]
	return dt,dE

seedy=3.0
def pin(seed=1.0):
	#pi=big. ('3.1415926535897932384626433832795028841971')
	seed = sp.pi*seed
	if seed>10.0:
		seed=seed/10.0
	randy=seed*100000000.0-int(seed*100000000.0)
	return randy , seed


def randE(t,E):
	done=[]
	Es=[]
	length=len(E)-1
	while len(Es)!=len(t):
		test=rand.randint(0,length)
		if not(test in done):
			Es.append(E[test])
			done.append(test)
	return Es

def Planck(deltat,scale):                                      ################## SCALE FOR 1,10 AND 100 PLANCK LINES
	c = 2.99792458*10**5               # km/s                    ################## COMPUTING PLANCK LENGTH PARAMTERS
	Mp = 1.2209*(10**22)                       # MeV/c**2	
	redshift=.903           #=0.34                                     ################## REDSHIFT
	Order = 1
	#computing first order stuff
	Qgrav = Mp*(c)
	scale=1.0/scale
	k1 =  1.0/(Qgrav*scale) 
	D1 = 1.37738149628*10**23    #Dn(redshift,Order)
	#print D1
	#file=open('distance.txt','w')
	#file.write(str(D1))
	#file.close()
	pl=1.0/(k1*D1)

	
	return deltat*pl


EEn , tti, ty, = sp.loadtxt('100MEV10DEGEVENTS.txt',unpack = True,skiprows=3)

ttti=[]
EEEn=[]

mev=100.0                                                   ################### SELECT ENERGIES
mevlim=10000000.0

for i in range(len(tti)):
	if EEn[i]>mev:
		if EEn[i]<mevlim:
			EEEn.append(EEn[i])
			ttti.append(tti[i])
En=[]
ti=[]
starttime=tti[0]+1376.0         #955.0                            ################## GRABBING TIMES 0-3s
for i in range(len(ttti)):
	if ((ttti[i]-starttime)>0.0):
		if (ttti[i]-starttime<3.0):    #50.0
			ti.append(ttti[i]-starttime)
			En.append(EEEn[i])


dt,dE=deltas(ti,En)                          ################## FINDING REAL dt AND dE UNDER CURVE

realp=[0.0,0.0,0.0]

for i in range(len(dE)):
	deet=dt[i]
	for j in range(3):
		scale=1.0*10.0**(-1*j)
		if dE[i]>Planck(deet,scale):
			realp[j]+=1.0


coup=[0,0,0,0]

for counting in range(4):                                    ################## COUNTING COUPLES IN DATA
	threshold=0.10/(10**(counting))   #start at 10s
	for i in range(len(dt)):
		if (dt[i])<threshold:
			coup[counting]+=1.0   



pwin=[0.0,0.0,0.0]


stopwatch=time.time()                                        ################## START STOPWATCH
lastyay=1001.0
yay=[0,0,0,0]
nay=[0,0,0,0]
lastcoup=0.0

PHOTONCOUNT=float(len(ti))
#print ti
pwin=[0.0,0.0,0.0]
#print '------REAL TIMES ABOVE------'
iters = 10**8
for it in range(iters):
	
	couple=[0,0,0,0]
	faket=[]
	
	while(len(faket)!=PHOTONCOUNT):                    ################## GENERATE FAKE PHOTONS
		phot=rand.uniform(0.0,6.0)    #18.0
		tim=rand.uniform(0.0,3.0)      #50.0
		#photo=pin(seedy)
		#phot,seedy=photo
		#phot=57.0*phot
		#timery=pin(seedy)
		#tim,seedy=timery
		#print seedy
		#tim=3.0*tim
		if Norris(tim)>phot:
			faket.append(tim)	
	
	faket.sort()                                       ################## SORTING FAKE PHOTONS
		
	fakeE=randE(faket,En)                          ################## PULLING RANDOM ENERGIES - only under curve or from whole energy set?
		
	fakedt , fakedE = deltas(faket,fakeE)              ################## FINDING FAKE dt AND dE's
	
	planck=[0.0,0.0,0.0]	
	for i in range(len(fakedt)):
		fakedeet=fakedt[i]
		for j in range(3):
			scale=1.0*10.0**(-1*j)
			if fakedE[i]>Planck(fakedeet,scale):
				planck[j]+=1.0

	
	for i in range(len(planck)):
		if planck[i]>realp[i]:
			pwin[i]+=1.0
			#print 'Success at ',str(10**i),'th of the Planck Scale'

	
	for counting in range(4):
		threshold=0.10/(10**(counting))


		for i in range(len(fakedt)):
			if fakedt[i]<threshold:
				couple[counting]+=1.0


		if couple[counting]>=coup[counting]:
			yay[counting]+=1.0

	


print coup
#print couple
print yay

print pwin

	
filename='090510MonteCarlofor'+str(mev)+'MeV.txt'################ SETUP FILE
file=open(filename,'w')
file.write('Real Data Couples below 0.1, 0.01, 0.001, 0.0001: '+str(coup)+'\n')
file.write('Couple Successes out of '+str(iters)+': '+str(yay)+'\n')
file.write('Real Pairs above 1,10,100 Planck lines '+str(realp)+'\n')
file.write('Successes above  1,10,100 Planck lines '+str(pwin)+'\n')
file.close()

						
		


	

print time.time()-stopwatch
#p.scatter(dt,dE,marker='x')
#p.yscale('log')
#p.xscale('log')
#p.title('Photons under Norris Curve for Energies>'+str(mev)+'MeV')
#p.xlim(10**-5,10**0)
#p.ylim(10**1,10**5)
