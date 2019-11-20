# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:44:44 2019

@author: Sahil
"""

import numpy as np
import random

cost = np.array([[478, 715, 649, 499],
[749, 799, 829, 829],
[350, 280, 300, 290],
[300, 250, 280, 310]])

deltime = np.array([[3, 9, 12, 7],
[3, 2, 12, 7],
[2, 2, 4, 3],
[3, 5, 3, 2]])

array = np.arange(32)
array = np.arange(32).reshape(2,4,4)
#chcost=np.arange(4)
chcost=[]
chind=np.arange(4)

gen=[]
val=np.arange(4)
val1=np.arange(4)

ovobj=10000

corrtime=np.arange(4)
corrcost=np.arange(4)
obj=10000
niter=50
############################
scores = np.arange(2*niter).reshape(2,niter)
#########################
for u in range (0,niter):
    print("##########################################")
    
    
    for j in range(0,4):
        for k in range(0,4):
            array[0][k][j]= cost[j][random.randint(0,3)]
    print("ITERATION NO " + str(u) + " @@@@@@@@@@@@@@@@")            
    print(array)
    
    
    my_list=[]
    for z in range(0,4):
        my_list.append(np.sum(array[0][z]))
        
    print(my_list)
    
    print("#########random solutions########")
    sm1=my_list.index(min(my_list))
    my_list[sm1]=10000
    sm2=my_list.index(min(my_list))
    print(sm1,sm2)
    print("##############################################")
      
    
    #******************************RANDOM CROSSOVER**********************************
    
    for x in range(0,4):
        s=random.randint(0,3)
        t=random.randint(0,3)
        while(t==s):
            t=random.randint(0,3)
        print(s,t)
        for y in range(0,4):
            array[1][x][y]= array[0][random.choice([s,t])][y]
    
    print (array)
    
    ellitism=[]
    for m in range(0,4):
        ellitism.append(np.sum(array[1][m]))
        
    print(ellitism)
    
    print("#########solution indexes with max sum ########")
    mm1=ellitism.index(max(ellitism))
    ellitism[mm1]=0
    mm2=ellitism.index(max(ellitism)) 
    print(mm1,mm2)
    
    
    array[1][mm1]=array[0][sm1]
    array[1][mm2]=array[0][sm2]
    
    print("#####################FINAL SOLUTION############")
    print(array)
    sol=[]
    for q in range(0,4):
        sol.append(np.sum(array[1][q]))
        
    print(sol)
    ss=min(sol)
    gen.append(ss)
    if obj>ss:
        obj=ss
        index1=sol.index(obj)
        print("index1 " + str(index1))
        print(obj)
        print(array[1][index1])
 #You need to update index only if overall min value is less
        for p in range(0,4):
            val[p]=array[1][index1][p]
        #val=array[1][index1]
        #val=chcost[0]
        print("val")
        print(val)
        #check from here
        #print(val[1])
        for z in range(0,4):
            #chind=[]
            a=val[z]
            indexx = list(cost[z]).index(a)
            #indexx=cost[z].index(a)
            print("index of cost " + str(indexx))
            chind[z]=indexx
        print(chind)
#    if ovobj>obj:
#        ovobj=obj
#        ovindex1=index1
#    print(ovobj,array[1][ovindex1])
#    print("ovindex1")
#    print(ovindex1)
#    chcost=array[1][ovindex1]
#    val=chcost[0]
#    print("val")
#    print(val)
#    chind=[]
    
print(gen)
print(chind)
print(min(gen))

for w in range(0,4):
    corrtime[w]=deltime[w][chind[w]]
print(corrtime)
print(max(corrtime))

######################################################################################
scores = np.arange(2*niter).reshape(2,niter)
print("SCORES")
print(scores)

#######################################################################################

print("*********************************************")
print("********************FOR DELIVERY TIME*******************")
      

    
arr=np.arange(32)    
arr = np.arange(32).reshape(2,4,4)
chtime=np.arange(4)
chin=np.arange(4)
gen1=[]

ovobj1=1000
ovindexx=0
obj1=500

for u in range (0,niter):
    #print("##########################################")
    
    
    for j in range(0,4):
        for k in range(0,4):
            arr[0][k][j]= deltime[j][random.randint(0,3)]
    #print("ITERATION NO " + str(u) + " @@@@@@@@@@@@@@@@")                        
    #print(arr)
    
    
    my_list1=[]
    for z in range(0,4):
        my_list1.append(np.max(arr[0][z]))
        
    #print(my_list1)
    
    #print("#########random solutions########")
    asm1=my_list1.index(min(my_list1))
    my_list1[asm1]=500
    asm2=my_list1.index(min(my_list1))
    #print(asm1,asm2)
    #print("##############################################")
      
    
    #******************************RANDOM CROSSOVER**********************************
    
    for x in range(0,4):
        s=random.randint(0,3)
        t=random.randint(0,3)
        while(t==s):
            t=random.randint(0,3)
        #print(s,t)
        for y in range(0,4):
            arr[1][x][y]= arr[0][random.choice([s,t])][y]
    
    #print (arr)
    
    ellitism1=[]
    for m in range(0,4):
        ellitism1.append(np.max(arr[1][m]))
        
    #print(ellitism1)
    
    #print("#########solution indexes with max delivery time########")
    amm1=ellitism1.index(max(ellitism1))
    ellitism1[amm1]=0
    amm2=ellitism1.index(max(ellitism1))
    #print(ellitism1)
    #print(amm1,amm2)
    
    
    arr[1][amm1]=arr[0][asm1]
    arr[1][amm2]=arr[0][asm2]
    
    #print("#####################FINAL SOLUTION############")
    #print(arr)
    sol1=[]
    for q in range(0,4):
        sol1.append(np.max(arr[1][q]))
        
    #print(sol1)
    ss1=min(sol1)
    gen1.append(ss1)
    if obj1>ss1:
        obj1=ss1
        index2=sol1.index(obj1)
        #print("index2 "+ str(index2))
        #print(obj1)
        #print(arr[1][index2])
        for m in range(0,4):
            val1[m]=arr[1][index2][m]
        #print("val1")
        #print(val1)
        
        for z in range(0,4):
            a=val1[z]
            indexx2=list(deltime[z]).index(a)
            #print("index of delivery time" + str(indexx2))
            chin[z]=indexx2
        #print(chin)
        
        
        
#    if ovobj1>obj1:
#        ovobj1=obj1
#        ovindex4=index2
#    print(ovobj1,arr[1][ovindexx])
#chtime=arr[1][ovindexx]
#for z in range(0,4):
#    val1=chtime[z]
#    indexx2=np.where(deltime[z]==val1)
#    chin.append(indexx2)

print(gen1)
print(chin)
print(min(gen1))

for v in range(0,4):
    corrcost[v]=cost[v][chin[v]]
print(corrcost)
print(sum(corrcost))