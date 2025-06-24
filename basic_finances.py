#!/usr/bin/env python
# coding: utf-8

# Some Financial Calculations
# ====

# Taken from [here](https://www.analyticsvidhya.com/blog/2021/08/basic-financial-calculations-using-python/)

# In[1]:


import numpy as np
import math


# In[13]:


#Calculate Simple interest
def simple_interest(p, r, t, show=False):
    '''p: float
           Ammount in €#
        r: float
            Interest rate in %
        t: int
            Time in years
    '''
    si=(p*r*t)/100
    a= p+si
    if show:
        print('SIMPLE INTEREST')
        print('Amount: ', p,'€') #in Euros
        print("Rate of Interest (Per Annum)", r,'%') #In %
        print("Time (In Years): ",t,'years')
        print("Final Amount: ", a,'€')
        print("Simple Interest: ", si,'€')
    return si, a


# In[7]:


#compound interest
def compound_interest(p,r,t, show=False):
    a= p*((1+r/100)**t)
    ci= a-p
    if show:
        print ('COMPOUND INTEREST')
        print('Amount: ', p,'€')
        print("Rate of Interest (Per Annum)", r, '%')
        print("Time (In Years): ",t,'years')
        print("Final Amount: ", a,'€')
        print("Compound Interest: ", ci,'€')
    return ci,a


# In[ ]:


# Purchasing power
def pur_power(p,r,t,show=False):
    a= p* ((100/(100+r))**t) # Calculate final amount
    if show:
        print ('PURCHASING POWER')
        print("Initial Amount: ",p)
        print("Annual Inflation Rate: ",r)
        print("Time in years:", t)
        print("Final amount after",t,"years of inflation: ", a)
    return a # Return final amount


# In[ ]:


#compound annual growth rate
def CAGR(p,a,t,show=False):
    t_inv=1/t
    cagr_rate= (((a/p)**t_inv)  -1)*100 #calculate compund annual growth rate
    if show:
        print ('COMPOUND ANUAL GROWTH RATE')
        print("Initial value of money: ",p)
        print('Final value of money: ',a)
        print("Time in years: ", t)
        print("Compound Annual Growth Rate (CAGR): ", cagr_rate)
    return cagr_rate


# In[ ]:


#monthly EMI calculation
def EMI(p,r,n,show=False):
    r_mon=  r/(12*100) #Monthly rate
    emi = p * r_mon * ((1+r_mon)**n)/((1+r_mon)**n - 1)
    if show:
        print("Total Loan Amount: ",p)
        print("Rate of Interest: ",r)
        print("Number of installments: ",n)
        print("EMI for",n,"months: ",emi )
    return emi


# In[11]:


simple_interest(1000, 5, 3, True)
print ('\n')
compound_interest(1000,5,3,True)


# In[ ]:


pur_power(1150,3,2.4)

