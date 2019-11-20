# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:35:07 2019

@author: Sahil
"""
# This is greedy algo for multi objective with pareto representaion
import numpy as np
from itertools import permutations
import matplotlib.pyplot as plt
import pandas as pd

cost = np.array([[478, 480, 440, 455,475,470],
 [660, 655, 675, 670,635,658],
[110, 115, 128, 100,135,140],        
 [745, 782, 769, 765,755,760],
[345, 380, 360, 355,362,375],
[700, 690, 720, 705,712,730]])

time = np.array([[3, 3, 7, 6,4,4],
[9, 7, 6, 8,10,9],
[7, 6, 8, 9,13,7],		    
[6, 6, 5, 7,3,3],
[5, 2, 4, 6,4,3],
[9, 12, 7, 8,8,6]])


a=[]
a1=[]
b1=[]
c=[]
e1=[]

for i in range(len(cost)):
	for j in range (len(cost)):
		for k in range (len(cost)):
			for l in range(len(cost)):
				for m in range(len(cost)):
					for n in range(len(cost)):
						print(i,j,k,l,m,n)
						a=(cost[0,i],cost[1,j],cost[2,k],cost[3,l],cost[4,m],cost[5,n])
						c=(time[0,i],time[1,j],time[2,k],time[3,l],time[4,m],time[5,n])
						#a1.append(a)
						b=(sum(a))
						print(b)
						b1.append(b)
						ll=(max(c))
						print(ll)
						e1.append(ll)
						
print(b1)



#d1=[]


#for i in range(len(cost)):
#	for j in range(len(cost)):
#		for k in range(len(cost)):
#			for l in range(len(cost)):
#				for m in range(len(cost)):
#					for n in range(len(cost)):
#						print(i,j,k,l,m,n)
#						c=(time[0,i],time[1,j],time[2,k],time[3,l],time[4,m],time[5,n])
#						d1.append(c) 
#						l=(max(c))
#						e1.append(l)
niter=len(b1)
scores = np.arange(2*(niter)).reshape((niter),2)						
print(e1)
#print(min(e1))
for i in range (len(b1)):
    print([b1[i],e1[i]])
    scores[i][0]=b1[i]
    scores[i][1]=e1[i]


print("SCORES")
print(unique(scores))
scores=unique(scores)

def unique(a):
    order = np.lexsort(a.T)
    a = a[order]
    diff = np.diff(a, axis=0)
    ui = np.ones(len(a), 'bool')
    ui[1:] = (diff != 0).any(axis=1) 
    return a[ui]

#print("SCORES")
#print(unique(scores))
#scores=unique(scores)
#######################PARETO#######################################

x = b1
y = e1

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