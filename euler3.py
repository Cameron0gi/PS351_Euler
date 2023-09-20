#!/usr/bin/env python
# coding: utf-8

# In[1]:


""""The following is a code that generates data for an approximation of a coupled first order
differential equations, thus allowing second order differential equations to be approximated"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from IPython.display import display


# In[2]:


def func1(x,t):
    return(t-(x*x))


# In[12]:


import math

def datagen(n, filename):
    dt=n
    tmax=5*2*np.pi
    x=0
    y=1
    t=0

    while(abs(t-tmax) > (dt/2)):
        with open(f'{filename}', 'a') as f:
            f.write(str(t)+'\n')
            f.write(str(x)+'\n')
            f.write(str(y)+'\n')
        x=x+y
        y=y-x
        t=t+dt
    


# In[13]:


def datapreptime(d):
    i=0
    o1=[]
    while i < len(d):
        o1.append(d[i])
        i=i+3
    
    return(np.concatenate(o1))

def dataprepx(d):
    i=1
    o1=[]
    while i < len(d):
        o1.append(d[i])
        i=i+3
    
    return(np.concatenate(o1))

def dataprepy(d):
    i=2
    o1=[]
    while i < len(d):
        o1.append(d[i])
        i=i+3
    
    return(np.concatenate(o1))


# In[ ]:





# In[44]:


def plotec(data, filename):

    fig1 = plt.figure()
    ax1 = fig1.add_subplot()  
    
    l1, = ax1.plot(datapreptime(data), dataprepx(data))
    l2, = ax1.plot(datapreptime(data), dataprepy(data))
    legend = (ax1.legend([l1, l2], ['x', 'y']))
    
    ax1.set_ylim(-2, 2)
    ax1.set_xlim(0, 5*2*np.pi)
    
  

    plt.xlabel("Time (s)")
    plt.ylabel("x")
    plt.savefig(f"{filename}", format="svg")
    
    plt.show()


# In[54]:


datagen(1, "e3_1.txt")

data=pd.read_csv("e3_1.txt", delimiter='\t', header=None)
data=data.to_numpy()


# In[55]:


plotec(data, "e3_1.svg")

