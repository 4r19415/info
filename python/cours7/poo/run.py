#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-

#class of random data


from simu_data import generate_data
import matplotlib.pyplot as plt

def main():
    x,y = generate_data(1000, var=5)
    plt.scatter(x, y)
    plt.show()

if __name__ == '__main__':
    main()s

