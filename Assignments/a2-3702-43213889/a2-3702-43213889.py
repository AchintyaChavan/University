'''
Created on 9 Sep. 2017

@author: AC
'''

import argparse
import re
import os
import numpy as np

import config

inputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a2-3702-43213889\\a2-tools\\a2-tools\\testcases\\3ASV-easy.txt"
outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\Assignments\\a2-3702-43213889\\3ASV-easy-output.txt"

def obstacle_config(array):

    obstacles = {}
    
    num = int(array.pop(0))

    for i in range(num):
        
        s = re.findall("\d+\.\d+", array[i])
        
        v1 = (s[0], s[1])
        v2 = (s[2], s[3])
        v3 = (s[4], s[5])
        v4 = (s[6], s[7])        
        
        obstacles[i] = config.Obstacle(v1, v2, v3, v4)

    return obstacles


def asv_config(array):
    
    
    goal = {};
    asvs = config.ASV(int(array.pop(0)),{})
    
    s = re.findall("\d+\.\d+", array[0])
    g = re.findall("\d+\.\d+", array[1])
    
    for i in range(asvs.length):
        
        asvs.position[i] = (float(s[2*i]), float(s[2*i+1]))
        goal[i] = (float(g[i]), float(g[i+1]))
    
    array.pop()
    
    return asvs, array[(asvs.length - 1):], goal


def file_read(filename):
    
    array = []
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
        
    return array


def main():

#     parser = argparse.ArgumentParser()
#     parser.add_argument("inputFile", help = "list of roads and info")
#     parser.add_argument("outputFile", help = "initial and final locations")
#     args = parser.parse_args()
#      
#     f1 = file_read(args.inputFile)
#     
#     outFile = os.path.join(os.path.dirname(sys.argv[1]), args.outputFile)
#     
#     f2 = open(outFile, "w")

    f1 = file_read(inputFile)
    
#     print(f1)
    
    asvs, array, goal = asv_config(f1)
        
    obstacles = obstacle_config(array)
    
#     print array
    
#     f3 = open(os.path.join(os.getcwd(), outputFile), "w")
    
    return;

if __name__ == "__main__":
    
    main()