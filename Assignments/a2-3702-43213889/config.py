'''
Created on 9 Sep. 2017

@author: AC
'''
class ASV:
    
    def __init__(self, number, initial):
        
        self.length = number
        self.initial = initial
        
    def __repr__(self):
        
        return "%s, %s, %s, %s\n" % (self.length, self.initial)   
                

class Obstacle:
    
    def __init__(self, v1, v2, v3, v4):
        
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        
    def __repr__(self):
        
        return "%s, %s, %s\n" % (self.v1, self.v2, self.v3, self.v4)