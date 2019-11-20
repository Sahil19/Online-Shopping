# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 11:24:59 2019

@author: Sahil
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:42:26 2019

@author: Sahil
"""

import numpy as np
import random

import timeit

start = timeit.default_timer()

cost= np.array([[478,715,649,499],
                [749,799,829,829],
                [350,280,300,290],
                [300,250,280,310]])


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
niter=100

for u in range (0,niter):
#    print("##########################################")
    
    
    for j in range(0,4):
        for k in range(0,4):
            array[0][k][j]= cost[j][random.randint(0,3)]
#    print("ITERATION NO " + str(u) + " @@@@@@@@@@@@@@@@")            
#    print(array)
    
    
    my_list=[]
    for z in range(0,4):
        my_list.append(np.sum(array[0][z]))
        
#    print(my_list)
    
#    print("#########random solutions########")
    sm1=my_list.index(min(my_list))
    my_list[sm1]=10000
    sm2=my_list.index(min(my_list))
#    print(sm1,sm2)
#    print("##############################################")
      
    
    #******************************RANDOM CROSSOVER**********************************
    
    for x in range(0,4):
        s=random.randint(0,3)
        t=random.randint(0,3)
        while(t==s):
            t=random.randint(0,3)
#        print(s,t)
        for y in range(0,4):
            array[1][x][y]= array[0][random.choice([s,t])][y]
    
#    print (array)
    
    ellitism=[]
    for m in range(0,4):
        ellitism.append(np.sum(array[1][m]))
#    print("ELLITISM")    
#    print(ellitism)
#    
#    print("#########solution indexes with max sum ########")
    mm1=ellitism.index(max(ellitism))
    ellitism[mm1]=0
    mm2=ellitism.index(max(ellitism)) 
#    print(mm1,mm2)
    
    
    array[1][mm1]=array[0][sm1]
    array[1][mm2]=array[0][sm2]
    
#    print("#####################FINAL SOLUTION############")
#    print(array)
    sol=[]
    for q in range(0,4):
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
 #You need to update index only if overall min value is less
        for p in range(0,4):
            val[p]=array[1][index1][p]

#        print("val")
#        print(val)

        for z in range(0,4):

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


################################GREEDY STARTS HERE############################

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:54:45 2019

@author: Sahil
"""

import numpy as np
#from itertools import permutations
import timeit

start = timeit.default_timer()
cost= np.array([[478,715,649,499],
                [749,799,829,829],
                [350,280,300,290],
                [300,250,280,310]])

a=[]
a1=[]
b1=[]
mcost=1000000

for i in range(len(cost)):
	for j in range(len(cost)):
		for k in range(len(cost)):
			for l in range(len(cost)):
#				print(i,j,k,l)
				a=(cost[0,i],cost[1,j],cost[2,k],cost[3,l])
				a1.append(a)
				b=(sum(a))
				if(b<mcost):
					mcost=b
					mi=i
					mj=j
					mk=k
					ml=l
				b1.append(b)
				
#print(b1)
print(mcost)
print(mi,mj,mk,ml)

stop = timeit.default_timer()

print('Time: ', stop - start) 
