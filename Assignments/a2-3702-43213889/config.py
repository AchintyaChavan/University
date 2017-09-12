'''
Created on 9 Sep. 2017

@author: AC
'''
class ASV:
    
    def __init__(self, number, pos = {}):
        
        self.length = number
        self.position = pos
        
    def __repr__(self):
        
        return "%s, %s\n" % (self.length, self.position)    
    
    def get_pos(self, asvNum):
                   
        return self.position[asvNum]       

class Obstacle:
    
    def __init__(self, v1, v2, v3, v4):
        
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        
    def __repr__(self):
        
        return "%s, %s, %s, %s\n" % (self.v1, self.v2, self.v3, self.v4)
    
class Configuration:
    
    def __init__(self, x, y, angle, number):
                
        self.x = x
        self.y = y
        self.angle = angle
        self.asv = number        