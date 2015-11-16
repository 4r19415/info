#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-

#regression lineaire


from random import random
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(10)

plt.scatter(x, 3*x+2) #/!\ 3*x fonctionne parce que x est un numpy array
plt.show()

