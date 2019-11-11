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
Nodes = 6

#demand and values satisfying demand of each node
demand = [14 , 8, 5, 7, 12, 6]
values = [8, 10, 13, 8, 9, 3]

#capacity of vehicle
capacity = 23

#distance matrix 
from scipy.spatial import distance_matrix
dist = distance_matrix([[0,0],[0,2],[3,2.5],[4,10],[1,3], [5, 11], [1,3]],
                       [[0,0],[0,2],[3,2.5],[4,10],[1,3], [5, 11], [1,3]])

import numpy as np
#incident matrix show the dispruption between arcs (except from depot)
incident = np.random.rand(6,6)

class INPUT:
    def __init__(self):
        #number of nodes:
        self.nodes = 6 
        #demand and values satisfying demand of each node
        self.demand = [14 , 8, 5, 7, 12, 6]
        self.values = [8, 10, 13, 8, 9, 3]
        #capacity of vehicle
        self.capacity = 23
        #nodes locations 
        self.point_pos = [[0,0],[0,2],[3,2.5],[4,10],[1,3], [5, 11], [1,3]]
        #incident matrix show the dispruption between arcs (except from depot)
        self.incident = np.random.rand(6,6)
        
        
        
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
        
        