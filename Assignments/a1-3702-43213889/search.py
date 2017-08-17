'''
Created on 16 Aug. 2017

@author: AC
'''

import math
import road

def address_length(length, plotSize, addrNo):
    
    return 2 * Length/plotSize * math.ceil(addrNo / 2.) - 1

def add_nodes(current):
       
    return list([c[2] for c in current])


def breadth_first_search(graph, query):
    
    cost = []
    priorityQueue = {}

    start = query.name1
    a1 = query.address1
    goal = query.name2
    a2 = query.address2

    # Add starting address to the front of queue
    for key, val in graph.iteritems():    
            
        for v in val:     
                           
            if v[0] == start:
                
                node = v[1]            
                priorityQueue[node] = val     
            
    while bool(priorityQueue) != False:
    
#         print(priorityQueue)
    
        current = priorityQueue.pop(node)
        
        print(node)
        
        for c in current:
            
            if c[0] == goal:
                
                print(c[0])
                return cost, priorityQueue
                
        
        adjacent = add_nodes(current)
  
        for n in adjacent:
            
            if n not in priorityQueue:
                
                priorityQueue[n] = graph[n]
                node = n
    
    
    return cost, priorityQueue