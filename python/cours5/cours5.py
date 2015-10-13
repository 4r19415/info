#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-

#regression lineaire


from random import random
import numpy as np
import matplotlib.pyplot as plt

ch= raw_input("action = ")

N=50000


def linear(x, params=(0,1,5)):
    return(params[1]*x+params[0]+params[2]*np.random.normal(size=len(x)) )
    


if ch =='1':
    x=[]
    for i in range(N):
        x.append(10*random())
    plt.scatter(x,x)
    plt.show()

elif ch =='2':
    x=[random()*i for i in range(N)]
    plt.scatter(x,x)
    plt.show()

elif ch =='3':
    x = 10*np.random.random(N)
    plt.scatter(x,x)
    plt.show()

elif ch =='4':
    from random import normalvariate
    y_normal = [normalvariate(0,1) for i in range(10000)]
    plt.hist(y_normal, bins=50, normed=True)
    plt.show()

elif ch =='5':
    x = 10*np.random.random(N)
    y=linear(x,(0,100,5))
    plt.scatter(x,y)
    plt.show()

else:
    print("fail")



