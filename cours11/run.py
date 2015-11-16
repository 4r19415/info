#!//home/lui/anaconda/bin/python
#-*- coding:utf-8 -*-

import random
import mylib

ch= raw_input("action (1 = dé) (2 = comptage) = ")

if ch == "1":

    gg=0
    poulet=0

    for i in range(1000000):
        a= random.randint(1,6)
        if a ==1 or a==2 or a==6:
            ok="gagné"
            gg+=1
        else:
            ok="perdu"
            poulet+=1
        #print " a=",a,ok

    print gg, "gagnés pour", poulet, "perdus"

if ch =="2":
    
    def comptage(elements):
        resutl={}
        for i in range (len(elements)):
            if 'A' in elements.count(i):
               result['A']+=1 
            elif 'B' in elements.count(i):
               result['B']+=1
            elif 'S' in elements.count(i):
               result['C']+=1
        return(result)

    test_list = list('AAABBC')
    result = comptage(test_list)

    assert result['A'] == 3
    assert result['B'] == 2
    assert result['C'] == 1
