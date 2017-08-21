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
                

class Sequence:
    
    def __init__(self, current, road, parent):
        
        self.state = current        
        self.road = road
        self.parent = parent
        
    def __repr__(self):
        
        return "%s, %s, %s\n" % (self.state, self.road, self.parent)