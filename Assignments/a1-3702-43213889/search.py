'''
Created on 16 Aug. 2017

@author: AC
'''

import math
import pdb
import road
import Queue as Q

def address_length(length, plotSize, addrNo):
    
    return 2 * length/plotSize * math.ceil(addrNo / 2.) - 1

def starting_node(graph, start):
    
    for key in graph.keys():
         
        for subKey in graph[key].keys():
              
            if graph[key][subKey][0] == start:
                  
                name = graph[key][subKey][1]
                node = graph[key][subKey]  
                              
                return name, node            
     
    return None, None
            
def adjacent_nodes(node):
    
    k = []
       
    for key in node.keys():
        
        k.append(key)      
    
    return k   
           
def breadth_first_search(graph, query):
    
    i = 0
    
    currentCost = {}    
    path = []
    frontier = Q.PriorityQueue()    
    explored = set()

    start = query.name1
    a1 = query.address1
    goal = query.name2
    a2 = query.address2

    # Initialise search to the starting node
    name, node = starting_node(graph, start)
    frontier.put((0, name, graph[name]))
    currentCost[name] = address_length(node[3], node[4], a1)
    seq = road.Sequence(name, None)
    
#     explored.add(tuple(name))
    
#     print(q)
    
#     print(name, node, q)

    # Add starting address to the front of queue
#     for key, val in graph.iteritems(): 
#             
#         for v in val:    
#                            
#             if v[0] == start:
#                 
#                 node = v[1]            
#                 q[node] = val
#                 currentCost[node] = address_length(int(v[3]), int(v[4]), a1)
#                 explored.add(tuple(node))
# #                 print(key, v, v[3], v[4], a1, v[0], cost)
# #                 break


          
    while bool(frontier) != False:
       
        item = frontier.get()
        name = item[1]
        current = item[2]
        
        
#         pdb.set_trace()
#         print(name, i, current)

        for key in current.keys():
                        
            if current[key][0] == goal and key in currentCost:
                                
#                 print(key, seq, currentCost)
                while seq != None:
                    
                    
                    path.insert(0, seq.state)

                    seq = seq.parent
                
#                 print(currentCost)
                return currentCost, list(set(path))
            
            
        for next in current.keys():      
                       
            estimatedCost = currentCost[name] + current[next][3]         
            
            if next not in currentCost or estimatedCost < currentCost[next]:
                 
                currentCost[next] = estimatedCost                
                priority = estimatedCost                
                 
                
                 
                frontier.put((priority, next, graph[next]))
                seq = road.Sequence(name, seq)
#                 name = next
            

                
                

#           
#         if node[0] == goal:
#               
#             print(node[0], currentCost)
#               
#             return currentCost, q
#           
#         next = adjacent_nodes(graph, name)
#          
#         for n in next:
#               
#             if tuple(n) not in explored:
#                  
#                 print(n, name)
#                   
#                 explored.add(tuple(n))
#                 q[n] = graph[n][name]
#                 name = n
                 
         
           
#         for c in node:
#              
#             if c[0] == goal:
#                  
# #                 print(c[0], cost)
#                 return currentCost, q
#                  
#          
#         adjacent = add_nodes(node)
#    
#         for n in adjacent:
#              
#             print(n, graph[n])
#              
# #             expectedCost = currentCost[node] + graph[n]             
#                                            
#             if tuple(n) not in explored:             
#                                  
#                 explored.add(tuple(n))
#                 q[n] = graph[n]
#                 node = n
   
#                 print(n, graph[n])
        i += 1      
    
    return currentCost, q