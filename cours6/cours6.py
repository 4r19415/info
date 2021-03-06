#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-

#regression lineaire


from random import random
import numpy as np
import matplotlib.pyplot as plt

ch= raw_input("action = ")

N=50000




    




if ch =='1':

    def linear(x, params=(0,1,5)):
        return(params[1]*x+params[0]+params[2]*np.random.normal(size=len(x)) )

    x = 10*np.random.random(N)
    y=linear(x,(0,100,5))
    plt.scatter(x,y)
    plt.show()



elif ch =='2':

    def linear(x, params=(0,1)):
        """Generate a linear function f(x)=a*x+b+N(0,1)
    
        Args:
        x (numpy.array()) : vector used to generate the output
        params (tuple of size 2) : b=params[0] and a=params[1]
    
        Returns:
        numpy.array()
        """
        return params[1]*x+params[0]+np.random.normal(size=len(x))


    x = 10*np.random.random(50)
    y = linear(x, (1,3))

    def linear_hypothesis(x, params=(0,1)):
        """Linear function f(x)=a*x+b
    
        Args:
        x (numpy.array()) : vector used to generate the output
        params (tuple of size 2) : b=params[0] and a=params[1]
    
        Returns:
        numpy.array()
        """
        a, b = params[1], params[0]
        return b+a*x

    def cost(x, y, func, func_args):
        """Cost function associated with (x,y) couple and function to fit
    
        Args:
        x : feature vector 
        y : explained variable
        func : target function
        func_args : arguments of function
        
        Returns:
        scalar value of cost
        """
        return 1./len(x)*sum(np.square(y-func(x,func_args)))

    def params_search():
        """2d scan for possible values and return best ones
        """
        errors = []
        params = []
        for p0 in np.linspace(0,10):
            for p1 in np.linspace(0,10):
                p = (p0,p1)
                c = cost(x, y, linear_hypothesis, p)
                errors.append(c)
                params.append(p)
        return params[errors.index(min(errors))]

    best = params_search()
    print "Paramètres optimisant les moindres carrés :", best
    plt.scatter(x,y)
    plt.plot(x,best[0]+best[1]*x)
    plt.show()

elif ch == '3':


 


    x = 10*np.random.random(50)
    y = linear(x, (1,3))

    def linear_hypothesis(x, params=(0,1)):
        """Linear function f(x)=a*x+b
    
        Args:
        x (numpy.array()) : vector used to generate the output
        params (tuple of size 2) : b=params[0] and a=params[1]
    
        Returns:
        numpy.array()
        """
        a, b = params[1], params[0]
        return b+a*x

    def cost(x, y, func, func_args):
        """Cost function associated with (x,y) couple and function to fit
    
        Args:
        x : feature vector 
        y : explained variable
        func : target function
        func_args : arguments of function
        
        Returns:
        scalar value of cost
        """
        return 1./len(x)*sum(np.square(y-func(x,func_args)))

    def random_params_search():
        errors = []
        params = []
        #choix arbitraire de recherche entre 0 et 5
        for p in 5*np.random.rand(10,2):
            p = tuple(p) 
            c = cost(x,y, linear, p)
            errors.append(c)
            params.append(p)
        return params[errors.index(min(errors))]

    best = random_params_search()
    print "Paramètres optimisant les moindres carrés :", best
    plt.scatter(x,y)
    plt.plot(x,best[0]+best[1]*x)
    plt.show()

else:
    print("fail")



