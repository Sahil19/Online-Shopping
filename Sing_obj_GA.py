# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:42:26 2019

@author: Sahil
"""

import numpy as np
import random

import timeit

start = timeit.default_timer()

cost = np.array([[478, 480, 440, 455,475,470],
 [660, 655, 675, 670,635,658],
[110, 115, 128, 100,135,140],        
 [745, 782, 769, 765,755,760],
[345, 380, 360, 355,362,375],
[700, 690, 720, 705,712,730]])


array = np.arange(72)
array = np.arange(72).reshape(2,6,6)

chcost=[]
chind=np.arange(6)

gen=[]
val=np.arange(6)
val1=np.arange(6)

ovobj=10000

corrtime=np.arange(6)
corrcost=np.arange(6)
obj=10000
niter=150

for u in range (0,niter):
    #print("##########################################")
    
    
    for j in range(0,6):
        for k in range(0,6):
            array[0][k][j]= cost[j][random.randint(0,5)]
#    print("ITERATION NO " + str(u) + " @@@@@@@@@@@@@@@@")            
#    print(array)
    
    
    my_list=[]
    for z in range(0,6):
        my_list.append(np.sum(array[0][z]))
        
#    print(my_list)
    
#    print("#########random solutions########")
    sm1=my_list.index(min(my_list))
    my_list[sm1]=10000
    sm2=my_list.index(min(my_list))
#    print(sm1,sm2)
#    print("##############################################")
      
    
    #******************************RANDOM CROSSOVER**********************************
    
    for x in range(0,6):
        s=random.randint(0,5)
        t=random.randint(0,5)
        while(t==s):
            t=random.randint(0,5)
#        print(s,t)
        for y in range(0,6):
            array[1][x][y]= array[0][random.choice([s,t])][y]
    
#    print (array)
    
    ellitism=[]
    for m in range(0,6):
        ellitism.append(np.sum(array[1][m]))
#    print("ELLITISM")    
#    print(ellitism)
    
#    print("#########solution indexes with max sum ########")
    mm1=ellitism.index(max(ellitism))
    ellitism[mm1]=0
    mm2=ellitism.index(max(ellitism)) 
#    print(mm1,mm2)
    
    
    array[1][mm1]=array[0][sm1]
    array[1][mm2]=array[0][sm2]
#    
#    print("#####################FINAL SOLUTION############")
#    print(array)
    sol=[]
    for q in range(0,6):
        sol.append(np.sum(array[1][q]))
        
#    print(sol)
    ss=min(sol)
    gen.append(ss)
    if obj>ss:
        obj=ss
        index1=sol.index(obj)
#        print("index1 " + str(index1))
#        print(obj)
#        print(array[1][index1])

        for p in range(0,6):
            val[p]=array[1][index1][p]
#
#        print("val")
#        print(val)

        for z in range(0,6):

            a=val[z]
            indexx = list(cost[z]).index(a)

#            print("index of cost " + str(indexx))
            chind[z]=indexx
#        print(chind)

    
#print(gen)
print(chind)
print(min(gen))

stop = timeit.default_timer()

print('Time: ', stop - start) 
