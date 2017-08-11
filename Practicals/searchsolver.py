'''
Created on 9 Aug. 2017

@author: AC
'''

from tree import Node
from puzzle import Puzzle

def parity_check(state):
    
    parity = 0;
    
    temp = state[:]
    temp.remove('_')
    
    for i in range(len(temp)):  
                      
        for j in range(i):
            
            if int(temp[j]) > int(temp[i]):
                                
                parity = parity + 1                                
    
    return (parity % 2)

def add_adjacentNodes(node):
    
    updatedNodes = [];   
        
    n = Puzzle(node.current)
    
    updatedNodes.append(Node(n.up(), node, "U", 
                             node.vertex + 1, node.treeDepth + 1))
    updatedNodes.append(Node(n.down(), node, "D", 
                             node.vertex + 1, node.treeDepth + 1))
    updatedNodes.append(Node(n.left(), node, "L", 
                             node.vertex + 1, node.treeDepth + 1))
    updatedNodes.append(Node(n.right(), node, "R", 
                             node.vertex + 1, node.treeDepth + 1))
    
    updatedNodes = [adjacent for adjacent in updatedNodes if adjacent.current != None]
                
    return updatedNodes
        

def breadth_first_search(initial, final):
    
    nodes = []
    moves = []
    sequence = []
    explored = set()    
    
    nodes.append(Node(initial, None, None, 0, 0)) #no parent node and vertex = 0
    explored.add(tuple(nodes[0].current))
        
    while len(nodes) > 0:

        v = nodes.pop(0) #Dequeue the first node from the list    
        
        if v.current == final:           
   
            while v.vertex != 0:
                
                moves = list(v.move) + moves
                sequence.insert(0, v.current)
                v = v.parent            
            
            return moves, sequence;
            
#         nodes.extend(add_childNodes(v, nodes))
        
        adjacent = add_adjacentNodes(v)
           
        for node in adjacent:            
                        
            if tuple(node.current) not in explored:
                
                explored.add(tuple(node.current))
                nodes.append(node)     #insert child at bottom of queue          
    
    return None, None #will output NULL if no solution is found

def depth_first_search(initial, final, treeDepth = 10):
    
    nodes = []
    moves = []
    sequence = []
    explored = set()    
    
    nodes.append(Node(initial, None, None, 0, 0)) #no parent node and vertex = 0
    explored.add(tuple(nodes[0].current))
        
    while len(nodes) > 0:

        v = nodes.pop(0) #Dequeue the first node from the list    
        
        if v.current == final:           
   
            while v.vertex != 0:
                
                moves = list(v.move) + moves
                sequence.insert(0, v.current)
                v = v.parent            
            
            return moves, sequence;
            
#         nodes.extend(add_childNodes(v, nodes))
        
        if v.treeDepth < treeDepth:
        
            adjacent = add_adjacentNodes(v)          
               
            for node in adjacent:            
                            
                if tuple(node.current) not in explored:
                    
                    explored.add(tuple(node.current))
                    nodes.insert(0, node)  #insert child at top of stack                
    
    return None, None #will output NULL if no solution is found