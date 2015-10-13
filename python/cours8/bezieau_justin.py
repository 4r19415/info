#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-


from random import random
import numpy as np


params=(0,1)

def moyenne(x):
    l=0.00
    i=0
    while i < len(x):
        l=l+x[i]
        i=i+1
    return(l/i)


def produit_scalaire(x,y):
    if len(x)!=len(y):
        return(0)
    else:
        a=0
        for i in range(len(x)):
           a+=x[i]+y[i]
        return(a)

def variance(x):
    l=0.00
    i=0
    if len(x)-1<=0:
        return(0)
    else:
        while i < len(x):
            l=(x[i]-moyenne(x))**2
            i=i+1
        return(l/i)

def covariance(x,y):
    l=0.00
    i=0
    if len(x)-1<=0:
        return(0)
    else:
        while i < len(x):
            l=(x[i]-moyenne(x))*(y[i]-moyenne(y))
            i=i+1
        return(l/i)

def linear_parameters(x,y):
    teta_1=0.00
    teta_2=0.00
    teta_0=0.00
    teta_1= covariance(x,y)/variance(x)
    teta_2= covariance(x,y)/variance(y)
    teta_0= moyenne(y)-teta_1*moyenne(x)
    return(teta_1,teta_2,teta_0)

x= 10*np.random.random(100)
y= params[0] + params[1]*x + np.random.normal(size=len(x))



print "moyenne :",moyenne(x)
print "produit_scalaire :" ,produit_scalaire(x,y)
print "vaiance :", variance(x)
print "covariance :", covariance(x,y)
print "linear_parameters :",linear_parameters(x,y)


    
