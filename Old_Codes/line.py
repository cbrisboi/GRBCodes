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


ti=[]
En=[]

for i in range(len(tti)-1):
	En.append(abs(EEn[i+1]-EEn[i]))
	ti.append(abs(tti[i+1]-tti[i]))
	

p.scatter(ti,En,marker='x')
p.yscale('log')
p.xscale('log')
p.title('Photons under Norris Curve for Energies>')
p.xlim(10**-5,10)
#p.ylim(10**1,10**5)
p.savefig('mysteriousline.ps')
