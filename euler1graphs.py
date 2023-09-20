#!/usr/bin/env python
# coding: utf-8

# In[33]:


"""
The following code is used to read and process data from euler 1, 
by seperating the time and approximation values that were previously 
seperated by newlines into their respective arrays, and then plots them against each other
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)

data=pd.read_csv("outputdt1.txt", delimiter='\t', header=None)
data=data.to_numpy()

datac=pd.read_csv("outputcalc1.txt", delimiter='\t', header=None)
datac=datac.to_numpy()

data2=pd.read_csv("outputdt2.txt", delimiter='\t', header=None)
data2=data2.to_numpy()

datac2=pd.read_csv("outputcalc2.txt", delimiter='\t', header=None)
datac2=datac2.to_numpy()

data3=pd.read_csv("outputdt3.txt", delimiter='\t', header=None)
data3=data3.to_numpy()

datac3=pd.read_csv("outputcalc3.txt", delimiter='\t', header=None)
datac3=datac3.to_numpy()


# In[34]:


time=[]
value=[]
i=0

def datapreptime(d):
    i=0
    o1=[]
    while i < len(d):
        if (i%2)==0 or (i==0):
            o1.append(d[i])
        i=i+1
    
    return(np.concatenate(o1))

def dataprepvalue(d):
    i=0
    o1=[]
    while i < len(d):
        if (i%2)>0:
            o1.append(d[i])
        i=i+1
    
    return(np.concatenate(o1))


# In[41]:


def plotec(data, datac, filename):

    fig1 = plt.figure()
    ax1 = fig1.add_subplot()  
    
    exact, = ax1.plot(datapreptime(data), dataprepvalue(data))           
    calc, = ax1.plot(datapreptime(datac), dataprepvalue(datac))
    ax1.legend([exact, calc], ["Exact Value", "Calculated Value"])
    plt.xticks(range(0, 11))
    plt.yticks(range(0, 11))
    ax1.set_xlim(0, max(dataprepvalue(data)))

    plt.xlabel("Time (s)")
    plt.ylabel("Estimated Radioactive Decay [Bq]")
    plt.savefig(f"{filename}", format="svg")
    
    plt.show()
    


# In[42]:



plotec(data, datac, "time1graph.svg")


# In[37]:



plotec(data2, datac2, "time2graph.svg")


# In[38]:



plotec(data3, datac3, "time3graph.svg")

