'''
Created on 9 Aug. 2017

@author: AC
'''

class Node:
    
    def __init__(self, currentState, parentState, move, vertex):
        
        
        self.current = currentState #Current puzzle node 
        self.parent = parentState #Parent node of current puzzle        
        self.move = move #Records the move specific to node               
        self.vertex = vertex #Vertex number (Source node is 0)