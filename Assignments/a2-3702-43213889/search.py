'''
Created on 24 Sep. 2017

@author: AC
'''

import Queue as Q

import tester
from scipy.sparse.csgraph import _shortest_path

# def AStar_Search(graph, query):
#     
#     i = 0
#     
#     currentCost = {} 
#     seq = {}
#     path = []
#     frontier = Q.PriorityQueue()    
# 
#     start = query.name1
#     a1 = query.address1
#     goal = query.name2
#     a2 = query.address2
# 
#     # Initialise search to the starting node
#     j1, j2, node = starting_node(graph, start)
#     frontier.put((0, j1, graph[j1]))
#     frontier.put((0, j2, graph[j2]))
#     currentCost[j1] = address_length(node[3], node[4], a1)
#     currentCost[j2] = node[3] - address_length(node[3], node[4], a1)
#     
# #     print(currentCost)
#     
#     seq[j1] = road.Sequence(j1, graph[j1][j2][0], None)
#     seq[j2] = road.Sequence(j2, graph[j1][j2][0], None)
#     
#     path.insert(0, goal)
# 
#     while bool(frontier) != False:
#        
#         item = frontier.get()
#         name = item[1]
#         current = item[2]
# 
#         for key in current.keys():
#                         
#             if current[key][0] == goal and key in currentCost:
# 
#                 path.insert(0, key)
#                 
#                 if key == current[key][1]:
#                 
#                     cost = address_length(current[key][3], current[key][4], a2)
#                     
#                 else:
#                     
#                     cost = current[key][3] - address_length(current[key][3], 
#                                                             current[key][4], a2)
#                 
#                 cost += currentCost[key]               
# 
#                 while seq[key].parent != None:
#                     
#                     path.insert(0, seq[key].road)          
#                     path.insert(0, seq[key].state)               
#                     seq[key] = seq[key].parent
#                 
#                 path.insert(0, start)
# 
#                 return cost, path            
#             
#         for next in current.keys():      
#                        
#             estimatedCost = currentCost[name] + current[next][3]         
#             
#             if next not in currentCost or estimatedCost < currentCost[next]:
#                  
#                 currentCost[next] = estimatedCost                
#                 priority = estimatedCost                          
#                  
#                 frontier.put((priority, next, graph[next]))
#                                 
#                 seq[next] = road.Sequence(name, graph[name][next][0], seq[name])
# 
#     return None, None

def heuristic(goal, next):
    
    return float(next.totalDistance(goal))

def AStar_Search(edges, start, goal):
    
    frontier = Q.PriorityQueue()
    currentCost = {}
    path = {}
    
    adjacent = [m[1] for m in edges.keys() if m[0] == start]

    for next in adjacent:
        
        cfg = (start, next)
        currentCost[cfg] = 0
        path[cfg] = None
        frontier.put((0, cfg, edges[cfg]))

    while not frontier.empty():
     
        element = frontier.get()
        cfg = element[1]    #cfg[0] is current, cfg[1] is destination config
        node = element[2]        
                
        if node != None:
            
#             print(cfg[0].getASVPositions())
#             print(cfg[1].getASVPositions())
            
            if cfg[0] == goal or cfg[1] == goal:
                
#                 print("Soulution found")
                print(path)
                cost = sum(currentCost.values())
                
                route = []
                
                c = cfg
                i = 0
                while path[c] != None:
                
                    route.insert(0, path[c])
                    c = path[c]
                    i += 1
                    print(i)                
                
                return cost, route

            adjacent = [n for n in edges.keys() if (n[0] == cfg[1] and n[1] != cfg[0])]
                      
            
            for next in adjacent:
                
#                 if (next[1], next[0]) not in currentCost:
                
#                 print(next[0].getASVPositions())
#                 print(next[1].getASVPositions())
                
                                     
                estimatedCost = cfg[1].totalDistance(next[1]) + currentCost[cfg]

                if (next not in currentCost \
                    and (next[1], next[0])) not in currentCost \
                    or estimatedCost < currentCost[next]:
                    
#                     print('hello')
                    currentCost[next] = estimatedCost                    
                    priority = estimatedCost + heuristic(goal, next[0])                    
                    frontier.put((priority, next, edges[next]))
                    path[next] = cfg

    return None, None