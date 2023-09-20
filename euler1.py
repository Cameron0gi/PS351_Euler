#!/usr/bin/env python
# coding: utf-8

# In[12]:


""""
The following is a code that generates data for an approximation of a linear equation
tracking the half-life decay of a radioactive sample, and then generates the exact solution 
so that the two can later can be compared
""""
import math

dt=0.01
tmax=10
tau=2.0

#initial coditions
t=0
n=10

while(abs(t-tmax) > (dt/2)):
    with open('outputdt1.txt', 'a') as f:
        f.write(str(t)+'\n')
        f.write(str(n)+'\n')
    n=n-((n*dt)/tau)
    t=t+dt
    
#calclate t using eqn2
t=0
n=10

while(abs(t-tmax) > (dt/2)):
    with open('outputcalc1.txt', 'a') as f:
        f.write(str(t)+'\n')
        f.write(str(n)+'\n')
    n=n*math.exp(-t/tau)
    t=t+dt


    


# In[13]:


dt=0.001
tmax=10
tau=2.0

#initial coditions
t=0
n=10

while(abs(t-tmax) > (dt/2)):
    with open('outputdt2.txt', 'a') as f:
        f.write(str(t)+'\n')
        f.write(str(n)+'\n')
    n=n-((n*dt)/tau)
    t=t+dt

t=0
n=10

while(abs(t-tmax) > (dt/2)):
    with open('outputcalc2.txt', 'a') as f:
        f.write(str(t)+'\n')
        f.write(str(n)+'\n')
    n=n*math.exp(-t/tau)
    t=t+dt


# In[14]:


dt=0.0005
tmax=10
tau=2.0

#initial coditions
t=0
n=10

while(abs(t-tmax) > (dt/2)):
    with open('outputdt3.txt', 'a') as f:
        f.write(str(t)+'\n')
        f.write(str(n)+'\n')
    n=n-((n*dt)/tau)
    t=t+dt
  
t=0
n=10

while(abs(t-tmax) > (dt/2)):
    with open('outputcalc3.txt', 'a') as f:
        f.write(str(t)+'\n')
        f.write(str(n)+'\n')
    n=n*math.exp(-t/tau)
    t=t+dt


# In[ ]:




