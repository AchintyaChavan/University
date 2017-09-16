'''
Created on 9 Sep. 2017

@author: AC
'''
from shapely import geometry

class ASVConfig:
    
    def __init__(self, number, pos = {}):
        
        self.length = number
        self.position = pos
        
    def __repr__(self):
        
        return "%s, %s\n" % (self.length, self.position)    
    
    def get_pos(self, asvNum):
                   
        return self.position[asvNum]
    
    def get_config(self):
        
        return self.position.values()

class Obstacle:
    
    def __init__(self, v1, v2, v3, v4):
        
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.polygon = geometry.Polygon([list(v1),
                                         list(v2),
                                         list(v3),
                                         list(v4)])
                
    def __repr__(self):
        
        return "%s, %s, %s, %s\n %s\n" % (self.v1, self.v2, self.v3, self.v4, self.polygon) 
        