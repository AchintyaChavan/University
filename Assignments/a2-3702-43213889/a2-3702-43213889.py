'''
Created on 9 Sep. 2017

@author: AC
'''
    
    
# import pip
#     
# pip.main(['install', "H:\Documents\Achintya\UQ\Engineering\5th Year\Sem 2 2017\COMP3702\Assignments\a2-3702-43213889\Shapely-1.5.17-cp27-cp27m-win32.whl"])
    
import argparse
import numpy as np
import os
import re
import random

# import config
# import ProblemSpec
import tester

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
    
    th = (n - 2) * 180.

    configurations = []

    for i in range(len(xs)):
        
        c = tester.config.ASVConfig([])        
        c.asvPositions.append((xs[i], ys[i]))
            
        for j in range(1, n):    
                        
            theta = random.randrange(-th, th)      
            th = th - theta
            
            theta = np.deg2rad(theta)
            
            (x,y) = c.asvPositions[j - 1]
            
            c.asvPositions.append((x + 0.05 * np.cos(theta), y + 0.05 * np.sin(theta)))
            
        configurations.append(c)
    
#     print(len(configurations))
    
#     print(configurations[0].get_config())
    
#     for i in range(len(configurations)):
#         
#         print(configurations[i].__str__())

    return configurations

def main():

# #     parser = argparse.ArgumentParser()
# #     parser.add_argument("inputFile", help = "list of roads and info")
# #     parser.add_argument("outputFile", help = "initial and final locations")
# #     args = parser.parse_args()
# #      
# #     f1 = file_read(args.inputFile)
# #     
# #     outFile = os.path.join(os.path.dirname(sys.argv[1]), args.outputFile)
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
    
    problem = tester.ProblemSpec.ProblemSpec()
    problem.loadProblem(inputFile)
    problem.saveSolution(outputFile)
    asvConfig_Generator(sampleSize = 20, problem.initialState.getASVCount())
    
    return;

if __name__ == "__main__":
    
    main()