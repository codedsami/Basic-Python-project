# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 22:36:43 2022

@author: miskat mahmud,souhib kafi
"""

import matplotlib.pyplot as plt  
import numpy as np 

vrel=float(input('What is the relative speed of rocket? '))
R=float(input('What is the fuel burning rate? '))
mi=float(input('What is the initial mass of the rocket? '))
mf=float(input('What is the final mass of the rocket? '))
N=int(input('What is the number of divisions? '))


xi=0
vi=0


T=-(mf-mi)/R
dt=T/N
dm=-R*dt
xf=vi*dt+xi
vf=vi-vrel*np.log(mf/mi)
t=np.linspace(0,N*dt,N)
m=np.linspace(mi,mf,N)
x=np.linspace(xi,xf,N)
v=np.linspace(vi,vf,N)


# loop with for 
for i in range(0,N-1): 
    m[i+1]=m[i]-R*dt
    v[i+1]=v[i]-vrel*(dm/m[i])
    x[i+1]=x[i]+v[i]*dt


plt.plot(t,m)
plt.title("mass over time")
plt.xlabel("time")
plt.ylabel("mass")
plt.show()

plt.plot(t,v)
plt.title("velocity over time")
plt.xlabel("time")
plt.ylabel("velocity")
plt.show()

plt.plot(t,x)
plt.title("position over time")
plt.xlabel("time")
plt.ylabel("position")
plt.show()

                     
