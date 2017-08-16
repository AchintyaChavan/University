'''
Created on 13 Aug. 2017

@author: AC
'''

import math
      
class Query:
    
    def __init__(self, n1, a1, n2, a2):
        
        self.name1 = n1
        self.address1 = a1
        self.name2 = n2
        self.address2 = a2
        
    def __repr__(self):
        
        return "%s, %s, %s, %s\n" % (self.name1, self.address1,
                                     self.name2, self.address2)
        


class Node:
    
    def __init__(self, road, addrNo, j1, j2, length, nLots):
        
        self.name = road
        self.addrNo = addrNo
        self.j1 = j1
        self.j2 = j2
        self.roadLength = length
        self.plotNum = nLots
        self.cost1 = 2*self.roadLength/self.plotNum*math.ceil(self.addrNo/2.)-1
        self.cost2 = self.roadLength - self.cost1
        self.start = 0
        self.end = 0      
    
    def __repr__(self):
        
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s \n" % (
                                         self.name, self.addrNo, 
                                         self.j1, self.j2, 
                                         self.roadLength, self.plotNum, 
                                         self.cost1, self.cost2,
                                         self.start, self.end)
        
    def update(self, name, addrNo, type):
        
        if name == self.name and addrNo == self.addrNo:
            
            if type == 's':
                
                self.start = 1
                
            elif type == 'e':
                
                self.end