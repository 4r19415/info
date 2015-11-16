#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-

#class of random data


from random import random
import numpy as np
s

def generate_data(N=100, params=(0,1), var=1):
    """ Fonction simulant les donnees : on genere une distribution de points au
        voisinage d'une droite avec la fonction lineaire : f(x)=a*x+b+N(0,1)
        (cf la fonction linear de Regression_1.ipynb)
        
        N      : nombre de points pour generer le vecteur x
        params : parametres de la fonction : b=params[0] et a=params[1]
        var    : facteur faisant varier la variance de la fonction normale N(0,1)
    """
    x= 10*np.random.random(N)
    y= params[0] + params[1]*x+var*np.random.normal(size=len(x))
    return x,y
