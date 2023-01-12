# -*- coding: utf-8 -*-
"""
Created on Tue May 10 12:53:18 2022

@author: miskat mahmud
"""

import math
import numpy as np
import matplotlib.pyplot as plt

#a
L=float(input('What is the period(L) for f(x)? '))
N=int(input('What is the number of divisions(N) for f(x)? '))

x=np.linspace(-L*3,L*3, N+1)
A=L/2
B=((4*L)/math.pi**2)

#summation
for n in range(0,N-1):
    C=(2*n-1)
    D=np.cos((C*math.pi*x)/L)
    E=B/C**2
    G=E*D
    F=A-G   #G=f(x)
    
    
#plotting    
plt.plot(x,F) 
plt.title("Triangle wave") 
plt.xlabel("Time")
plt.ylabel("Amplitude")      



#b
L=float(input('What is the period(L) for an? '))
n=int(input('What is the term(n) for an? '))
N=1000 #number of divisions

B=2/L
dx=L/N

an=0
for x in range(0,N-1):
    an = an + (x*np.cos((n*math.pi*x)/L)*dx)
    sum_an = B*an
  
print("sum_an",sum_an)    