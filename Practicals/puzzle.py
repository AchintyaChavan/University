'''
Created on 9 Aug. 2017

@author: AC
'''

class Puzzle:
    
    def __init__(self, initial):
        
        self.puzzle = list(initial)
                                
    def up(self):
        
        blank = self.puzzle.index('_')
        updated = self.puzzle[:]
        
        if blank not in (0,1,2):                  
            
            temp = updated[blank - 3]            
            updated[blank - 3] = updated[blank]
            updated[blank] = temp
            
            return updated
            
        else:
            
            return None  
    
    def down(self):
        
        blank = self.puzzle.index('_')
        updated = self.puzzle[:]
        
        if blank not in (6,7,8):                  
            
            temp = updated[blank + 3]            
            updated[blank + 3] = updated[blank]
            updated[blank] = temp
            
            return updated
            
        else:
            
            return None
        
    def left(self):
        
        blank = self.puzzle.index('_')
        updated = self.puzzle[:]
        
        if blank not in (0,3,6):                  
            
            temp = updated[blank - 1]            
            updated[blank - 1] = updated[blank]
            updated[blank] = temp
            
            return updated
            
        else:
            
            return None
        
    def right(self):
        
        blank = self.puzzle.index('_')
        updated = self.puzzle[:]
        
        if blank not in (2,5,8):                  
            
            temp = updated[blank + 1]            
            updated[blank + 1] = updated[blank]
            updated[blank] = temp
            
            return updated
            
        else:
            
            return None