'''
Created on 16 Aug. 2017

@author: AC
'''

import math
import road

def address_length(length, plotSize, addrNo):
    
    return 2 * length/plotSize * math.ceil(addrNo / 2.) - 1

def add_nodes(current):
       
    return list([c[1] for c in current] + [c[2] for c in current])


def breadth_first_search(graph, query):
    
    i = 0
    currentCost = {}
    priorityQueue = {}
    explored = set()

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
                currentCost[node] = address_length(int(v[3]), int(v[4]), a1)
                explored.add(tuple(node))
#                 print(key, v, v[3], v[4], a1, v[0], cost)
#                 break
          
    while bool(priorityQueue) != False:
    
#         print(priorityQueue)
    
        current = priorityQueue.pop(node)

        print(node)
        
        for c in current:
            
            if c[0] == goal:
                
#                 print(c[0], cost)
                return currentCost, priorityQueue
                
        
        adjacent = add_nodes(current)
  
        for n in adjacent:
            
            print(node, n, graph[n])
            
#             expectedCost = currentCost[node] + graph[n]             
                                          
            if tuple(n) not in explored:             
                                
                explored.add(tuple(n))
                priorityQueue[n] = graph[n]
                node = n

#                 print(n, graph[n])
        i += 1
    
    
    return currentCost, priorityQueue