'''
Created on 16 Aug. 2017

@author: AC
'''

import math
import road

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
    priorityQueue = {}
    explored = set()

    start = query.name1
    a1 = query.address1
    goal = query.name2
    a2 = query.address2

    name, node = starting_node(graph, start)
    priorityQueue[name] = graph[name]
    currentCost[name] = address_length(node[3], node[4], a1)
    explored.add(tuple(name))
    
#     print(priorityQueue)
    
#     print(name, node, priorityQueue)

    # Add starting address to the front of queue
#     for key, val in graph.iteritems(): 
#             
#         for v in val:    
#                            
#             if v[0] == start:
#                 
#                 node = v[1]            
#                 priorityQueue[node] = val
#                 currentCost[node] = address_length(int(v[3]), int(v[4]), a1)
#                 explored.add(tuple(node))
# #                 print(key, v, v[3], v[4], a1, v[0], cost)
# #                 break


          
    while bool(priorityQueue) != False:
       
        node = priorityQueue.pop(name)
         
        print(node)

        for key in node.keys():
            
            if node[key][0] == goal:
                
                print(node[key][0], currentCost)               
                return currentCost, priorityQueue
            
            
        for next in node.keys():
            
            estimatedCost = currentCost[name] + node[next][3]
            
            if tuple(next) not in explored or estimatedCost < currentCost[next]:
                
                currentCost[next] = estimatedCost
                
#                 print(estimatedCost)
                
                explored.add(tuple(next))
                
                priorityQueue[next] = graph[next]
                name = next
            

                
                

#           
#         if node[0] == goal:
#               
#             print(node[0], currentCost)
#               
#             return currentCost, priorityQueue
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
#                 priorityQueue[n] = graph[n][name]
#                 name = n
                 
         
           
#         for c in node:
#              
#             if c[0] == goal:
#                  
# #                 print(c[0], cost)
#                 return currentCost, priorityQueue
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
#                 priorityQueue[n] = graph[n]
#                 node = n
   
#                 print(n, graph[n])
        i += 1      
    
    return currentCost, priorityQueue