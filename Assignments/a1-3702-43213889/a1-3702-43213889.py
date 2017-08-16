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

def file_read(filename):
    
    array = []
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
    
    return array

def environment_read(array):
    
    graph = []
    
    for r in array:
        
        temp = r.split(";")        
        
        length = int(temp[3].strip())
        nLots = int(temp[4].strip())
        
        for i in range(nLots):       
        
            graph.append(road.Node(temp[0].strip(), i + 1, 
                                   temp[1].strip(), temp[2].strip(), 
                                   length, nLots))
        
    return graph

def queries_read(array):
    
    queries = []
    
    for q in array:
        
        temp = q.split(";")
        
        start = re.split('(\d+)', temp[0])
        end = re.split('(\d+)', temp[1])
        
        queries.append(road.Query(start[2].strip(), int(start[1]), 
                                  end[2].strip(), int(end[1])))
        
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

#     for q in queries:        
#         for n in graph:
#             
#             n.update(q.name1, q.address1, 's')
#             n.update(q.name2, q.address2, 'e')

    for node in graph: print(repr(node))
    for q in queries: print(repr(q))

    return 0;

if __name__ == "__main__":
    main()