#!//usr/bin/python
#-*- coding:utf-8 -*-

def moyenne(v):
    l=0.00
    i=0
    while i < len(v):
        l=l+v[i]
        i=i+1
    return(l/i)

def scalaire(x,y):
    if len(x)!=len(y):
        return(0)
    else:
        a=0
        for i in range(len(x)):
           a+=x[i]+y[i]
        return(a)

a=range(10)
b=range(10)
c=[5,10]
print(scalaire(a,b))
print(moyenne(a))
print(moyenne(b))
print(moyenne(c))
