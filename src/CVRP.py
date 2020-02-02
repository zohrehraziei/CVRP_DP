# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:09:00 2019

CVRP (DP)

Author: Zohreh Raziei - raziei.z@husky.neu.edu
"""

from scipy.spatial import distance_matrix
import numpy as np
import itertools
import random as rnd
rnd.seed(0)


class  CVRPDP:
    def __init__(self, data):
        self.Nodes  = data.nodes
        self.demand = data.demand
        self.values = data.values
        self.capacity = data.capacity
        self.incident = data.incident
        self.node_pos= data.point_pos
        
    def DP(self):
        self.dist = distance_matrix(self.node_pos,self.node_pos)
        st_itr = itertools.product(range(0,self.capacity+1), range(0,self.Nodes+1))
        self.states = list()
        #fill out the multidim state space
        for pairs in st_itr:
            self.states.append(pairs)
        #size of the state space
        state_len = len(self.states)
        
        #dynamic programming table:
        table = np.pad(np.zeros((state_len, self.Nodes+1)), (0,1), 'constant')
        table[0] = np.array(self.dist[0].tolist()+ [0])

        #DP main Loop:
        for j in range(1, self.Nodes + 1):
            # j for columns - action space (picking the points)
            deliv   = self.demand[j-1]
            val     = self.values[j-1]
            
            for i in range(1, state_len):
                # i for rows - state spaces pairs of remained capacity and prev node
                if deliv > self.states[i][0]: #self.states[i][0]: cap of state i
                    table[i,j] = table[i,j-1]
                else:
                    distt = self.dist[self.states[i][1]][j]
                    if rnd.random() > self.incident[self.states[i][1]-1][j-1]:
                        # consider disruption as a noise
                        
                        distt += 18*rnd.random()
                    table[i,j] = max(table[i,j-1], 
                         table[self.states.index((self.states[i][0] - deliv,self.states[i][1]))][j-1] + val - distt)
         
        nodes_taken = np.zeros(self.Nodes) 
        tot_states = state_len
        print(table[i,j])  
        #finding the answer from the DP table
        
        for i in range(self.Nodes+1 , 0, -1):
            if table[tot_states][i]>0:
                if table[tot_states][i] != table[tot_states][i-1]:
                    nodes_taken[i-1] = 1
                    deliv = self.demand[i-1]
                    tot_states = self.states.index((self.states[tot_states][0] - deliv,self.states[i][1]))
                else:
                    nodes_taken[i-1] = 0
            else:
                tot_states -= 1   
        print(nodes_taken)        
        return nodes_taken
    


