# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:05:08 2019

@author: Sahil
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

cost = np.array([[478, 480, 440, 455,475,470],
 [660, 655, 675, 670,635,658],
[110, 115, 128, 100,135,140],        
 [745, 782, 769, 765,755,760],
[345, 380, 360, 355,362,375],
[700, 690, 720, 705,712,730]])

deltime = np.array([[3, 3, 7, 6,4,4],
[9, 7, 6, 8,10,9],
[7, 6, 8, 9,13,7],		    
[6, 6, 5, 7,3,3],
[5, 2, 4, 6,4,3],
[9, 12, 7, 8,8,6]])

array = np.arange(72)
array = np.arange(72).reshape(2,6,6)

chcost=[]
chind=np.arange(6)

gen=[]
val=np.arange(6)
#val1=np.arange(4)

ovobj=10000

ct=0

corrtime=np.arange(6)
#corrcost=np.arange(4)
obj=10000
niter=15


############################
scores = np.arange(2*(niter-2)).reshape((niter-2),2)
#########################
for ol in range(2,niter):
	
	for u in range (1,ol):
	    #print("##########################################")
	    
	    
	    for j in range(0,6):
	        for k in range(0,6):
	            array[0][k][j]= cost[j][random.randint(0,5)]
#	    print("ITERATION NO " + str(u) + " @@@@@@@@@@@@@@@@")            
	    #print(array)
	    
	    
	    my_list=[]
	    for z in range(0,6):
	        my_list.append(np.sum(array[0][z]))
	        
#	    print(my_list)
#	    
#	    print("#########random solutions########")
	    sm1=my_list.index(min(my_list))
	    my_list[sm1]=10000
	    sm2=my_list.index(min(my_list))
#	    print(sm1,sm2)
#	    print("##############################################")
	      
	    
	    #******************************RANDOM CROSSOVER**********************************
	    
	    for x in range(0,6):
	        s=random.randint(0,5)
	        t=random.randint(0,5)
	        while(t==s):
	            t=random.randint(0,5)
	        #print(s,t)
	        for y in range(0,6):
	            array[1][x][y]= array[0][random.choice([s,t])][y]
	    
	   # print (array)
	    
	    ellitism=[]
	    for m in range(0,6):
	        ellitism.append(np.sum(array[1][m]))
	        
	    #print(ellitism)
	    
#	    print("#########solution indexes with max sum ########")
	    mm1=ellitism.index(max(ellitism))
	    ellitism[mm1]=0
	    mm2=ellitism.index(max(ellitism)) 
#	    print(mm1,mm2)
	    
	    
	    array[1][mm1]=array[0][sm1]
	    array[1][mm2]=array[0][sm2]
	    
#	    print("#####################FINAL SOLUTION############")
	    #print(array)
	    sol=[]
	    for q in range(0,6):
	        sol.append(np.sum(array[1][q]))
	        
#	    print(sol)
	    ss=min(sol)
	    gen.append(ss)
	    if obj>ss:
	        obj=ss
	        index1=sol.index(obj)
#	        print("index1 " + str(index1))
#	        print(obj)
#	        print(array[1][index1])
	
	        for p in range(0,6):
	            val[p]=array[1][index1][p]
	        
#	        print("val")
#	        print(val)
	        #check from here
	        #print(val[1])
	        for z in range(0,6):
	            #chind=[]
	            a=val[z]
	            indexx = list(cost[z]).index(a)
	           
#	            print("index of cost " + str(indexx))
	            chind[z]=indexx
#	        print(chind)
	
	    
	#print(gen)
	#print(chind)
	mcost=min(gen)
	#print(mcost)
	
	for w in range(0,6):
	    corrtime[w]=deltime[w][chind[w]]
	#print(corrtime)
	ctime=max(corrtime)
	#print(ctime)
	scores[ct][0]=mcost
	scores[ct][1]=ctime
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
