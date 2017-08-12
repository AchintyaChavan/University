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

import road

def file_read(filename):
    
    array = []
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
    
    return array

def environment_read(array):
    
    roads = []
    
    for r in array:
        
        temp = r.split(";")        
        
        roads.append(road.Environment(temp[0].strip(), temp[1].strip(), 
                                      temp[2].strip(), temp[3].strip(), 
                                      temp[4].strip()))    
        
    return roads

def queries_read(array):
    
    queries = []
    
    for q in array:
        
        temp = q.split(";")
        
        queries.append(road.Query(temp[0][1:-1], temp[0][0], 
                                  temp[1][2:], temp[1][1]))
        
    return queries       
       
def main():
    
#     parser = argparse.ArgumentParser()
#     parser.add_argument("environment", help = "list of roads and info")
#     parser.add_argument("query", help = "initial and final locations")
#     parser.add_argument("output", help = "file to output results")
#     args = parser.parse_args()

    f1 = file_read(environmentFile)
    f2 = file_read(queryFile)
    
    roads = environment_read(f1)
    queries = queries_read(f2)
    
    print(repr(roads[0]))
    print(repr(queries[0]))
    return 0;

if __name__ == "__main__":
    main()