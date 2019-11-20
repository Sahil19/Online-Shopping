# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:23:36 2019

@author: Sahil
"""


import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

cost = np.array([[478, 715, 649, 499],
[749, 799, 829, 829],
[350, 280, 300, 290],
[300, 250, 280, 310]])

deltime = np.array([[3, 9, 12, 7],
[3, 2, 12, 7],
[2, 2, 4, 3],
[3, 5, 3, 2]])

arr=np.arange(32)    
arr = np.arange(32).reshape(2,4,4)
chtime=np.arange(4)
chin=np.arange(4)
gen1=[]

ovobj1=1000
ovindexx=0
obj1=500
#array = np.arange(32)
#array = np.arange(32).reshape(2,4,4)
#
#chcost=[]
#chind=np.arange(4)
#
#gen=[]
#val=np.arange(4)
val1=np.arange(4)
#
#ovobj=10000
#
#ct=0
#
#corrtime=np.arange(4)
corrcost=np.arange(4)
ct=0
#obj=10000
niter=50
############################
scores = np.arange(2*(niter-2)).reshape((niter-2),2)
#########################
for ol in range(2,niter):
	
	for u in range (1,ol):
	    
	    
	    for j in range(0,4):
	        for k in range(0,4):
	            arr[0][k][j]= deltime[j][random.randint(0,3)]

	    
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

	        for m in range(0,4):
	            val1[m]=arr[1][index2][m]

	        
	        for z in range(0,4):
	            a=val1[z]
	            indexx2=list(deltime[z]).index(a)
	            chin[z]=indexx2

	
	print(gen1)
	print(min(gen1))
	dtime=min(gen1)
	
	for v in range(0,4):
	    corrcost[v]=cost[v][chin[v]]
	#print(corrcost)
	print(sum(corrcost))
	ccost= sum(corrcost)
	scores[ct][0]=ccost
	scores[ct][1]=dtime
	ct=ct+1
	#print("INTERMEDIATE SCORES:")
	#print(scores)
######################################################################################

def unique(a):
    order = np.lexsort(a.T)
    a = a[order]
    diff = np.diff(a, axis=0)
    ui = np.ones(len(a), 'bool')
    ui[1:] = (diff != 0).any(axis=1) 
    return a[ui]

print("SCORES")
print(unique(scores))
scores=unique(scores)
#######################PARETO#######################################

x = scores[:, 0]
y = scores[:, 1]

plt.scatter(x, y)
plt.xlabel('Objective A')
plt.ylabel('Objective B')
plt.show()

def identify_pareto(scores):
    # Count number of items
    population_size = scores.shape[0]
    print("population size")
    print(population_size)
    # Create a NumPy index for scores on the pareto front (zero indexed)
    population_ids = np.arange(population_size)
    # Create a starting list of items on the Pareto front
    # All items start off as being labelled as on the Parteo front
    pareto_front = np.ones(population_size, dtype=bool)
    # Loop through each item. This will then be compared with all other items
    for i in range(population_size):
        # Loop through all other items
        for j in range(population_size):
            # Check if our 'i' pint is dominated by out 'j' point
            if all(scores[j] <= scores[i]) and any(scores[j] < scores[i]):
                # j dominates i. Label 'i' point as not on Pareto front
                print("paretofronti")
                print(pareto_front[i])
                pareto_front[i] = 0
                # Stop further comparisons with 'i' (no more comparisons needed)
                break
    # Return ids of scenarios on pareto front
    print(population_ids[pareto_front])
    return population_ids[pareto_front]

pareto = identify_pareto(scores)
print ('Pareto front index vales')
print ('Points on Pareto front: \n',pareto)

pareto_front = scores[pareto]
print ('\nPareto front scores')
print (pareto_front)

pareto_front_df = pd.DataFrame(pareto_front)
pareto_front_df.sort_values(0, inplace=True)
pareto_front = pareto_front_df.values
x_all = scores[:, 0]
y_all = scores[:, 1]
x_pareto = pareto_front[:, 0]
y_pareto = pareto_front[:, 1]

plt.scatter(x_all, y_all)
plt.plot(x_pareto, y_pareto, color='r')
plt.xlabel('Objective A')
plt.ylabel('Objective B')
plt.show()
