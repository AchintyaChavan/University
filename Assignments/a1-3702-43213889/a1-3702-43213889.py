'''
Created on 13 Aug. 2017

@author:  Achintya Chavan
@Stud.ID: 43213889
@course:  COMP3702

'''
queryFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\query-simple.txt"
environmentFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\test-simple.txt"
outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\output-simple.txt"

import argparse
import pdb

import re
import road
import search

def file_read(filename):
    
    array = []
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
    
    return array

def environment_read(array):
    
    graph = {}
    
    for r in array:
        
        temp = r.split(";")        
        
        length = int(temp[3].strip())
        nLots = int(temp[4].strip())
        
        for i in range(nLots):       
        
            graph[str(i+1) + temp[0].strip()] = road.Node(i + 1, 
                                   temp[1].strip(), temp[2].strip(), 
                                   length, nLots)
        
    return graph

def queries_read(array):
    
    queries = []
    
    for q in array:
        
        temp = q.split(";")
        
        queries.append([temp[0].strip(), temp[1].strip()])
        
    return queries       
       
def main():
    
#     parser = argparse.ArgumentParser()
#     parser.add_argument("environment", help = "list of roads and info")
#     parser.add_argument("query", help = "initial and final locations")
#     parser.add_argument("output", help = "file to output results")
#     args = parser.parse_args()

    f1 = file_read(environmentFile)
    f2 = file_read(queryFile)
    
    graph = environment_read(f1)
    queries = queries_read(f2)
    
    
    
    for q in queries:
        cost, path = search.breadth_first_search(graph, q[0], q[1])
         
        print(cost, path)

    print(graph)

    return 0;

if __name__ == "__main__":
    main()