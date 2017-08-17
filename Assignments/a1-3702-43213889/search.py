'''
Created on 16 Aug. 2017

@author: AC
'''

import math
import road

def address_length(length, plotSize, addrNo):
    
    return 2 * Length/plotSize * math.ceil(addrNo / 2.) - 1

def adjacent(graph, current):
    
    
    
    return


def breadth_first_search(graph, query):
    
    cost = []
    priorityQueue = {}

    start = query.name1
    a1 = query.address1
    goal = query.name2
    a2 = query.address2

    for key, val in graph.iteritems():
        
        for v in val:
                    
            if v[0] == start:
            
                priorityQueue[v[1]] = val
        
        
    
    print(priorityQueue)
    
    return cost, priorityQueue