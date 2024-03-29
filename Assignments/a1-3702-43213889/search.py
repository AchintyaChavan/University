'''
Created on 16 Aug. 2017

@author: AC
'''

import math
import road
import Queue as Q

def address_length(length, plotSize, addrNo):
    
#     print(length/(1.*plotSize))
    L_n = float(length / (1. * plotSize))
    return round(L_n * (2. * math.ceil( addrNo/(2.) ) - 1), 3)

def starting_node(graph, start):
    
    for key in graph.keys():
         
        for subKey in graph[key].keys():
              
            if graph[key][subKey][0] == start:
                  
                a1 = graph[key][subKey][1]
                a2 = graph[key][subKey][2]
                node = graph[key][subKey]  
                              
                return a1, a2, node            
     
    return None, None

def uniform_cost_search(graph, query):
    
    i = 0
    
    currentCost = {} 
    seq = {}
    path = []
    frontier = Q.PriorityQueue()    

    start = query.name1
    a1 = query.address1
    goal = query.name2
    a2 = query.address2

    # Initialise search to the starting node
    j1, j2, node = starting_node(graph, start)
    frontier.put((0, j1, graph[j1]))
    frontier.put((0, j2, graph[j2]))
    currentCost[j1] = address_length(node[3], node[4], a1)
    currentCost[j2] = node[3] - address_length(node[3], node[4], a1)
    
#     print(currentCost)
    
    seq[j1] = road.Sequence(j1, graph[j1][j2][0], None)
    seq[j2] = road.Sequence(j2, graph[j1][j2][0], None)
    
    path.insert(0, goal)

    while bool(frontier) != False:
       
        item = frontier.get()
        name = item[1]
        current = item[2]

        for key in current.keys():
                        
            if current[key][0] == goal and key in currentCost:

                path.insert(0, key)
                
                if key == current[key][1]:
                
                    cost = address_length(current[key][3], current[key][4], a2)
                    
                else:
                    
                    cost = current[key][3] - address_length(current[key][3], 
                                                            current[key][4], a2)
                
                cost += currentCost[key]               

                while seq[key].parent != None:
                    
                    path.insert(0, seq[key].road)          
                    path.insert(0, seq[key].state)               
                    seq[key] = seq[key].parent
                
                path.insert(0, start)

                return cost, path            
            
        for next in current.keys():      
                       
            estimatedCost = currentCost[name] + current[next][3]         
            
            if next not in currentCost or estimatedCost < currentCost[next]:
                 
                currentCost[next] = estimatedCost                
                priority = estimatedCost                          
                 
                frontier.put((priority, next, graph[next]))
                                
                seq[next] = road.Sequence(name, graph[name][next][0], seq[name])

    return None, None