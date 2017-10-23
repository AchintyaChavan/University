'''
Created on 18 Oct. 2017

@author: AC
'''

# import numpy as np
import os
import ProblemSpec as PS
import MDP

constraints = {'bronze': [3, 3], 'silver': [5, 4],
               'gold': [6, 4], 'platinum': [8, 5]}

# stateSpace = {}
# stateSpace['bronze'] = [(0,0),
#                         (0,1),
#                         (0,2),
#                         (0,3),
#                         (1,0),
#                         (1,1),
#                         (1,2),
#                         (2,0),
#                         (2,1),             
#                         (3,0)]
# 
# stateSpace['silver'] = [(0,0),
#                         (0,1),
#                         (0,2),
#                         (0,3),
#                         (1,0),
#                         (1,1),
#                         (1,2),
#                         (2,0),
#                         (2,1),             
#                         (3,0)]
# 
# P_c = 1/10. * np.array([[3, 2, 2, 1, 2],
#                         [3, 2, 2, 1, 2],
#                         [3, 2, 2, 1, 2],
#                         [3, 2, 2, 1, 2],                                   
#                         [3, 2, 2, 1, 2]])
# 
# P_s = 1/10. * np.array([[2, 2, 2, 2, 2],
#                         [3, 2, 2, 1, 3],
#                         [3, 2, 2, 1, 3],
#                         [3, 2, 2, 1, 3],                                   
#                         [3, 2, 2, 1, 3]])


inputfile = "bronze1.txt"

def file_read(filename):
    
    cfg = MDP.VenctureConfig()
    array = []    
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
    
    print(array)
    
    cfg.type = array[0]
    cfg.total = constraints[cfg.type][0]
    cfg.extra = constraints[cfg.type][1]
    cfg.discount = float(array[1])
    cfg.timestamps = int(array[2])
    cfg.states = stateSpace[cfg.type]

    arr3 = array[3].split(' ')
    arr4 = array[4].split(' ')
    
    for i in range(len(arr3)):

        cfg.price[i + 1] = int(arr3[i])
        cfg.cost[i + 1] = int(arr4[i])
        cfg.ventures += 1

    i = 5
    for j in range(cfg.ventures):
        
        mat = []
        
        for k in range(cfg.total + 1):
            
            row = [float(r) for r in array[i + k].split(' ')]
            mat.append(row)
    
        cfg.matrices[j + 1] = np.array(mat)
        
        i = i + k

#     print(cfg.__str__())

    return cfg

def main():

    filename = os.path.join(os.getcwd(), inputfile)
    
#     cfg = file_read(filename)

    problem = PS.ProblemSpec()
    problem.loadInputFile(filename)

#     print(problem.venture.__str__())

    return 0

if __name__ == "__main__":
    main()