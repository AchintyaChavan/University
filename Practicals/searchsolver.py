'''
Created on 9 Aug. 2017

@author: AC
'''

from tree import Node
from puzzle import Puzzle

def add_adjacentNodes(node):
    
    updatedNodes = [];   
        
    n = Puzzle(node.current)
    
    updatedNodes.append(Node(n.up(), node, "U", node.vertex + 1))
    updatedNodes.append(Node(n.down(), node, "D", node.vertex + 1))
    updatedNodes.append(Node(n.left(), node, "L", node.vertex + 1))
    updatedNodes.append(Node(n.right(), node, "R", node.vertex + 1))
    
    updatedNodes = [adjacent for adjacent in updatedNodes if adjacent.current != None]
                
    return updatedNodes
        

def breadth_first_search(initial, final):
    
    nodes = []
    moves = []
    explored = set()    
    
    nodes.append(Node(initial, None, None, 0)) #no parent node and vertex = 0
    explored.add(tuple(nodes[0].current))
        
    while len(nodes) > 0:

        v = nodes.pop(0) #Dequeue the first node from the list    
        
        if v.current == final:           
   
            while v.vertex != 0:
                
                moves = list(v.move) + moves
                v = v.parent            
            
            return moves, len(nodes);
            
#         nodes.extend(add_childNodes(v, nodes))
        
        adjacent = add_adjacentNodes(v)
           
        for node in adjacent:            
                        
            if tuple(node.current) not in explored:
                
                explored.add(tuple(node.current))
                nodes.append(node)
