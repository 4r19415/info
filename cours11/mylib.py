from random import random
import numpy as np
import matplotlib.pyplot as plt



def product(m1,m2):
    C1=m1.shape[1] #
    L1=m1.shape[0] #
    C2=m2.shape[1] #
    L2=m2.shape[0] # (nombre de lignes de la matrice 2)
    m3=(np.zeros((L1,C2))) #? (l1 ligne C2 colones)
    if C1==L2:
        for i in range (L1):       # on parcourt m3
            for j in range (C2):   #

                for k in range(C1):
                        m3[i][j]+=m1[i][k]*m2[k][j]
        return(m3)
    else:
        return(0)

def trace (m):
    a=0.0
    L=m.shape[0]
    c=m.shape[1]
    if L==c:
        for i in range(L):
            a+=m[i][i]
        return(a)
    else:
        return(0)

def moyenne(x):
    return sum(x)/len(x)


def produit_scalaire(x,y):
    if len(x)!=len(y):
        return(0)
    else:
        a=0
        for i in range(len(x)):
           a+=x[i]*y[i]
        return(a)

def variance(x):
    l=0.00
    i=0
    m=moyenne(x)
    if len(x)-1<=0:
        return(0)
    else:
        while i < len(x):
            l+=(x[i]-m)**2
            i=i+1
        return(l/i)



def covariance(x,y):
    l=0.00
    i=0
    mx=moyenne(x)
    my=moyenne(y)
    if len(x)-1<=0:
        return(0)
    else:
        while i < len(x):
            l+=(x[i]-mx)*(y[i]-my)
            i=i+1
        return(l/i)


def Matrice_covariance_2D(x,y):
    return(np.array([[covariance(x,x),covariance(x,y)],[covariance(y,x),covariance(y,y)]]))


def linear_parameters(x,y):
    teta_1=0.00
    teta_0=0.00
    teta_1= covariance(x,y)/variance(x)
    teta_0= moyenne(y)-teta_1*moyenne(x)
    return(teta_1,teta_0)

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
