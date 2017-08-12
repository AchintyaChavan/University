'''
Created on 13 Aug. 2017

@author: AC
'''

class Environment:
    
    def __init__(self, name, j1, j2, length, nLots):
        
        self.name = name
        self.junc1 = j1[1]
        self.junc2 = j2[1]
        self.roadLength = length
        self.plotNum = nLots
        
    def __repr__(self):
        
        return "%s, %s, %s, %s, %s \n" % (self.name, self.junc1, self.junc2,
                                           self.roadLength, self.plotNum)
        
class Query:
    
    def __init__(self, n1, a1, n2, a2):
        
        self.name1 = n1
        self.address1 = a1
        self.name2 = n2
        self.address2 = a2
        
    def __repr__(self):
        
        return "%s, %s, %s, %s\n" % (self.name1, self.address1,
                                     self.name2, self.address2)