'''
Created on 9 Sep. 2017

@author: AC
'''
    
inputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Non Repo\\COMP3701A2Support-master\\COMP3701A2Support-master\\testcases\\3ASV-easy.txt"
outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\Assignments\\a2-3702-43213889\\3ASV-easy-output.txt"


def file_read(filename):
    
    array = []
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
        
    return array

def obstacle_config(array):

    obstacles = {}
    
    num = int(array.pop(0))

    for i in range(num):
        
        s = re.findall("\d+\.\d+", array[i])        
        s = [float(i) for i in s]        

#         v1 = (s[0], s[1])
#         v2 = (s[2], s[3])
#         v3 = (s[4], s[5])
#         v4 = (s[6], s[7])

        x = s[0]
        y = s[1]
        w = s[2] - s[0]
        h = s[5] - s[1]
        
        obstacles[i] = config.Obstacle(x, y, w, h)

    return obstacles


def asv_config(array):
    
    goal = {}
    asvs = config.ASVConfig(int(array.pop(0)),{})
    
    s = re.findall("\d+\.\d+", array[0])
    g = re.findall("\d+\.\d+", array[1])
    
    for i in range(asvs.length):
        
        asvs.position[i] = (float(s[2*i]), float(s[2*i+1]))
        goal[i] = (float(g[i]), float(g[i+1]))
    
    array.pop()
    
    return asvs, array[(asvs.length - 1):], goal

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

def NN(nodes, node):

    dist_2 = np.sum((nodes - node)**2, axis = 1)
    dist_2[dist_2 == 0] = 10.0  #Add a large value to self distance  
    
    return np.argmin(dist_2)

def make_edges(c1, c2, test):
    
    edgeConfigs = [c1]

    n1 = c1
    n2 = c2

    edgeCreated = False

    j = 0

    while (edgeCreated == False):
        
        if test.isValidStep(n1, n2):
            
            if n2 == c2:
                
                print("Already created", j)
                edgeCreated = True
                
            else:
                
                n1 = n2
                n2 = c2
                
                if test.isValidStep(n1, n2):
                    
#                     print("Finally created", j)
                    edgeConfigs.append(n2)
                    edgeCreated = True          

        midPt = (np.asanyarray(n1.getASVPositions()) + np.asarray(n2.getASVPositions())) / 2.
        n1 = n2        
        n2 = tester.config.ASVConfig([tuple(i) for i in midPt])
        
        if not test.hasEnoughArea(n2) or not test.isConvex(n2) \
            or not test.fitsBounds(n2) or test.hasCollision(n2, test.ps.getObstacles()):
            
                return None
            
        else:
            
            edgeConfigs.append(n2)
        
        j += 1   

#     print(m.getASVPositions())    
    return edgeConfigs
    
def graph_creation(configs, ts, edgeConfigs):
    
    # Obtain the first ASV coordinate
    c = [c.getASVPositions()[0] for c in configs]
    c = [(float(c[0]), float(c[1])) for c in c]
    c = np.asarray(c)
    
#     print(c)

    for i in range(len(c)):
                
        current = c[i]
        NNId = NN(c, current)    #Get nearest point
        neighbour = configs[NNId]
        
        edge = make_edges(configs[i], neighbour, ts)
        temp = []
        
        if configs[i] in edgeConfigs:
            
            temp.append(edge)
            edgeConfigs[configs[i]].append(temp)
          
        else:
          
            temp.append([edge])
            edgeConfigs[configs[i]] = temp
            
            
#             print(len(edgeConfigs[configs[i]]))
#         print(current, neighbour.getASVPositions()[0])
    

#     print(edgeConfigs)
#     pass

    return edgeConfigs

def main():

#     parser = argparse.ArgumentParser()
#     parser.add_argument("inputFile", help = "list of roads and info")
#     parser.add_argument("outputFile", help = "initial and final locations")
#     args = parser.parse_args()
# #      
# #     f1 = file_read(args.inputFile)
# #     
# #     outFile = os.path.join(os.path.realpath(__file__), args.outputFile)
# #     
# #     f2 = open(outFile, "w")
#     f1 = file_read(inputFile)
#     
# #     print(f1)
#     
#     asvs, array, goal = asv_config(f1)
#     
# #     print(asvs)
#         
#     obstacles = obstacle_config(array)
#      
#     asvConfig_Generator(20, asvs.length)
#     
# #     print array
#     
# #     f3 = open(os.path.join(os.getcwd(), outputFile), "w")
    edgeConfigs = {}
    
    # Initialise problem file
    problem = tester.ProblemSpec.ProblemSpec()
    problem.loadProblem(inputFile)

#     problem.saveSolution(outputFile)
    
    # Initialise tester
    ts = tester.Tester()
    ts.ps = problem
    
    vertices = []
    vertices.append(ts.ps.initialState)
    vertices.append(ts.ps.goalState)
    
    for i in range(1,100):
        
        sample = asvConfig_Generator(100, problem.initialState.getASVCount())
        
        ts.ps.setPath(sample)
            
        v = test_configurations(ts, sample)
        
        vertices = vertices + v
    
        edgeConfigs = graph_creation(vertices, ts, edgeConfigs)
    
        cost, route = search.AStar_Search(edgeConfigs, ts.ps.initialState, ts.ps.goalState)
        
        if (i % 2 == 0):
            
            print (i, cost, route)

    return;

if __name__ == "__main__":
    
    import argparse
    import numpy as np
    import os

#     import pip          
#     pip.main(['install', os.path.join(os.getcwd(), "Shapely-1.5.17-cp27-none-win32.whl")])
            
    import re
    import random
    import scipy
    
    import search
    import tester
        
    main()