#!//usr/bin/python
#-*- coding:utf-8 -*-


euler = 1


if (euler == 1):
    f=0
    for i in range(1000):
        if (((i % 5)==0) or ((i % 3)==0)):
            f=f+i
    print  f


