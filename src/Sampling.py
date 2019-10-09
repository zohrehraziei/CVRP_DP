# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:09:00 2019

experim - CVRPDP

Author: Zohreh Raziei - zraziei@smu.edu
"""
from __future__ import division
from CVRP import CVRPDP
import matplotlib.pyplot as plt 
import time


#number of nodes:
Nodes = 3

#demand and values satisfying demand of each node
demand = [2, 3, 1]
values = [6, 16, 3]

#capacity of vehicle
capacity = 5

#distance matrix 
from scipy.spatial import distance_matrix
dist = distance_matrix([[0,0], [6,10], [4,8.5], [7,5]],
                       [[0,0], [6,10], [4,8.5], [7,5]])
import numpy as np
#incident matrix show the dispruption between arcs (except from depot)
incident = np.random.rand(3,3)

class INPUT:
    def __init__(self):
        #number of nodes:
        self.nodes = 3
        #demand and values satisfying demand of each node
        self.demand = [2, 3, 1]
        self.values = [6, 16, 3]
        #capacity of vehicle
        self.capacity = 5
        #nodes locations 
        self.point_pos = [[0,0], [6,10], [4,8.5], [7,5]]
        #incident matrix show the dispruption between arcs (except from depot)
        self.incident = np.random.rand(3,3)
        
        
data = INPUT()
ans = CVRPDP(data)
#print(ans.DP())
est_sol = list()
sol = np.zeros(data.nodes) 
## Sequential Sampling
samp_size = 10000
count = 1
t1 = time.clock()
for i in range(1,samp_size+1):
    count += 1
    #print(ans.DP())
    sol = [x + y for x, y in zip(ans.DP(), sol)]
    est_sol1 = [x / count for x in sol]
    est_sol.append(est_sol1)
t2 = time.clock()
plt.xlabel("Number of Scenario")
plt.ylabel("Probability of Demand Satisfaction")
plt.plot(est_sol)
plt.show()
    

print(est_sol1)  
print(t2 - t1) 
        
        