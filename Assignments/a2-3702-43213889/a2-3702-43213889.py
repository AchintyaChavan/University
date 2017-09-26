'''
Created on 9 Sep. 2017

@author: AC
'''
    
# inputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Non Repo\\COMP3701A2Support-master\\COMP3701A2Support-master\\testcases\\3ASV-easy.txt"
# outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\Assignments\\a2-3702-43213889\\3ASV-easy-output.txt"

def asvConfig_Generator(sampleSize, n):
    
    xs = np.array(random.sample(xrange(0,100), sampleSize)) / 100.
    ys = np.array(random.sample(xrange(0,100), sampleSize)) / 100.

#     samples = zip(xs, ys)
    
    r = tester.Tester.MAX_BOOM_LENGTH
    
    th = (n - 2) * 180.

    configurations = []

    for i in range(len(xs)):
        
        temp = []
        temp.append(tuple([xs[i], ys[i]]))

        c = tester.config.ASVConfig(temp)       
       
        for j in range(1, n):    
                        
            theta = random.randrange(-th, th)      
            th = th - theta
            
            theta = np.deg2rad(theta * (1 + tester.Tester.DEFAULT_MAX_ERROR * n))

            (x,y) = c.getPosition(j-1)
            
            c.__add__((x + r * np.cos(theta), y + r * np.sin(theta)))
       
        configurations.append(c)
       
#     for i in range(len(configurations)):
#         
#         print(configurations[i].__str__())
#     print(len(configurations))

    return configurations

def test_configurations(ts, sample):
       
    c3 = ts.getInvalidAreaStates()  #Area constraint
    c4 = ts.getNonConvexStates()    #Convexity and self intersection constraint    
    c5 = ts.getCollidingStates()    #Collision/Intersection constraint   
    c6 = ts.getOutOfBoundsStates()  #Bounds constraint
    
    
    badStates = list(set(c3)|set(c4)|set(c5)|set(c6))     
    idx = [i for i in range(len(sample))]    
    goodStates = list(set(idx) - set(badStates))
    
    validConfigs = [sample[i] for i in goodStates] 
    
#     print(c3)
#     print(c4)
#     print(c5)
#     print(c6)
      
#     print(badStates)
#     print(goodStates)
#     print(validConfigs) 

    return validConfigs 

def make_edges(c1, c2, test):
    
    temp = []
    edgeConfigs = [c1]

    n1 = c1
    n2 = c2

    edgeCreated = False

    j = 0

    if c1 == c2:
        
        return None

    while (edgeCreated == False):
         
        while (test.isValidStep(n1, n2) == False):
             
            temp.append(n2)
            midPt = (np.asanyarray(n1.getASVPositions()) + np.asarray(n2.getASVPositions())) / 2.
            #         n1 = n2        
            n2 = tester.config.ASVConfig([tuple(i) for i in midPt])
             
            if not test.hasEnoughArea(n2) or not test.isConvex(n2) \
            or not test.fitsBounds(n2) or test.hasCollision(n2, test.ps.getObstacles()):
 
                return None
              
            else:
              
                edgeConfigs.append(n2)
                 
        if n1 == c2:
             
#             print("Already created", j)
            edgeConfigs.append(c2)
            edgeCreated = True
             
        else:
                  
            n1 = n2
            n2 = c2  
                      
#             if test.isValidStep(n1, n2):
#                  
#                 if n2 == c2:
#              
# #                     print("Secondly created", j)
#                     edgeConfigs.append(c2)
#                     edgeCreated = True
#                      
#                 else:
#                      
#                     n1 = n2
#                     n2 = temp.pop()

#     import pdb
#     pdb.set_trace()

#     while (edgeCreated == False):
#          
#         if test.isValidStep(n1, n2):
#              
#             if n1 == c2:
#                  
# #                 print("Already created", j)
# #                 edgeConfigs.append(c2)
#                 edgeCreated = True
#                  
#             else:
#                  
#                 n1 = n2
#                 n2 = temp.pop()
#                  
# #                 if test.isValidStep(n1, n2):
# #                      
# #                     if n2 == c2:
# #                          
# #                         print("Already created", j)
# #                         edgeConfigs.append(c2)
# #                         edgeCreated = True
# #                          
# #                     else:
# #                      
# #                         n1 = n2
# #                         n2 = c2
#                         
# #                     print("Finally created", j)
# #                     edgeConfigs.append(n2)
# #                     edgeCreated = True          
#  
#         midPt = (np.asanyarray(n1.getASVPositions()) + np.asarray(n2.getASVPositions())) / 2.
#         temp.append(n2)
# #         n1 = n2        
#         n2 = tester.config.ASVConfig([tuple(i) for i in midPt])
#          
#         if not test.hasEnoughArea(n2) or not test.isConvex(n2) \
#            or not test.fitsBounds(n2) or test.hasCollision(n2, test.ps.getObstacles()):
#              
#                 return None
#              
#         else:
#              
#             edgeConfigs.append(n2)
#         
#         j += 1   

#     print(edgeConfigs[0].getASVPositions())
#     print(edgeConfigs[-1].getASVPositions())
#     print(m.getASVPositions())    
    return edgeConfigs
    
def graph_creation(configs, ind, ts, edgeConfigs):
    
    # Obtain the first ASV coordinate
    c = [c.getASVPositions()[0] for c in configs]
    c = np.array(c)

#     dist = (1.+ts.MAX_BOOM_LENGTH) * (1.* float(ts.ps.asvCount))
    dist = ts.MAX_BOOM_LENGTH# * (3.* float(ts.ps.asvCount))

    tree = spatial.cKDTree(c)
#     NNIDs = tree.query_ball_point(c[0], dist)
    
#     print(ind)
    for i in range(ind, len(c)):
     
        current = configs[i]

        NNIDs = tree.query_ball_point(c[i], dist)
        
#         print(i)
#         print(NNIDs)
        
        for j in NNIDs:
        
            neighbour = configs[j]
                        
            if not (neighbour, current) in edgeConfigs or not (neighbour, current) in edgeConfigs:
                
                edge = make_edges(current, neighbour, ts)
                                        
                if (edge != None):
                    
                    if current == ts.ps.goalState:
                        
                        key = (current, neighbour)
                        
                    elif neighbour == ts.ps.goalState:
                        
                        key = (neighbour, current)
                        
                    else:
                        
                        key = (current, neighbour)
#                     print("Edge created", i)                 
#                     key = (current, neighbour)
                    edgeConfigs[key] = edge
                    
#                     if key[0] == ts.ps.initialState or key[1] == ts.ps.initialState:
#                         
#                         print("start node added")
#                         
                    if key[0] == ts.ps.goalState or key[1] == ts.ps.goalState:
                         
                        pass
#                         print("goal node added")

#         if i == 2:
#              
#             i = ind
      
#                     print('\n')
#                     print(len(edge))
#                     print(current.getASVPositions())
#                     print(neighbour.getASVPositions())
#                     print(edge[0].getASVPositions())
#                     print(edge[-1].getASVPositions())
#                     print('\n')
 
    return edgeConfigs

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", help = "list of roads and info")
    parser.add_argument("outputFile", help = "initial and final locations")
    args = parser.parse_args()
   
    outputFile = os.path.join(os.getcwd(), args.outputFile)

    print(outputFile)

    edgeConfigs = {}
    
    # Initialise problem file
    problem = tester.ProblemSpec.ProblemSpec()
    problem.loadProblem(args.inputFile)

#     problem.saveSolution(outputFile)
    
    # Initialise tester
    ts = tester.Tester()
    ts.ps = problem
    
    vertices = []
    vertices.append(ts.ps.initialState)
    vertices.append(ts.ps.goalState)
    
        
    t1 = time.time()
    
    ind = 0
    
    for i in range(0, 500):
        
        sample = asvConfig_Generator(30, problem.initialState.getASVCount())
        
        ts.ps.setPath(sample)
            
        v = test_configurations(ts, sample)
        
        if len(vertices) == 2:
            
            ind = 0
            
        else:
            
            ind += len(v)
        
        vertices = vertices + v
    
        edgeConfigs = graph_creation(vertices, ind, ts, edgeConfigs)
    
        cost, route = search.AStar_Search(edgeConfigs, ts.ps.initialState, ts.ps.goalState)
        
        if route:
            
#             print(route)
            sys.stdout.write('\nObtained Route\n')
            break
    
    t2 = time.time()
    sys.stdout.write('\nTime taken: ' + str((t2 - t1)) + '  secs\n')
    
    if route:
            
        ts.ps.setPath(route)        
        ts.ps.saveSolution(outputFile)
        
    else:
        
        f3 = open(outputFile, "w")
        f3.write('No solution obtained')
        
    sys.stdout.write('\nOutput file stored as ' + str(outputFile) + '\n')

    return;

if __name__ == "__main__":
    
    import argparse
    import numpy as np
    import os

#     import pip          
#     pip.main(['install', os.path.join(os.getcwd(), "Shapely-1.5.17-cp27-none-win32.whl")])
            
    import re
    import random
    import scipy.spatial as spatial
    import sys
    import time
    
    import search
    import tester
        
    main()