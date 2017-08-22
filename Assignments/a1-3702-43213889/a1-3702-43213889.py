'''
Created on 13 Aug. 2017

@author:  Achintya Chavan
@Stud.ID: 43213889
@course:  COMP3702

'''
# queryFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\query2.txt"
# environmentFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\test2.txt"
# outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\output2.txt"

# queryFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\query-simple.txt"
# environmentFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\test-simple.txt"
# outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a1-3702-43213889\\output-simple.txt"

import argparse
import pdb
import time
import re

import road
import search

def string_split(string):
    
    for i, c in enumerate(string):
        
        if not c.isdigit():
            
            break
    
    return i

def file_read(filename):
    
    array = []
    
    with open(filename, "r") as f:
        
        array = f.read().split("\n")
    
    return array

def junction_read(array):
    
    junction = {}
    
    for r in array:
        
        temp = r.split(";")

        road = temp[0].strip()
        start = temp[1].strip()
        end = temp[2].strip()        
        length = int(temp[3].strip())
        nLots = int(temp[4].strip())
                
        if start not in junction:

            junction[start] = {end: [road, start, end, length, nLots]}
            
        else:

            junction[start][end] = [road, start, end, length, nLots]
            
        if end not in junction:
            
            junction[end] = {start: [road, start, end, length, nLots]}
            
        else:
            
            junction[end][start] = [road, start, end, length, nLots]

    return junction

def queries_read(array):
    
    queries = []
    
    for q in array:
        
        temp = q.split(";")
        
        start = temp[0].strip()
        end = temp[1].strip()
        
        i1, i2 = string_split(start), string_split(end)
                
        n1 = start[i1:]
        a1 = int(start[:i1])
        
        n2 = end[i2:]
        a2 = int(end[:i2])
        
        queries.append(road.Query(n1, a1, n2, a2))
        
    return queries       
       
def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("environment", help = "list of roads and info")
    parser.add_argument("query", help = "initial and final locations")
    parser.add_argument("output", help = "file to output results")
    args = parser.parse_args()
    
    f1 = file_read(args.environment)
    f2 = file_read(args.query)
    f3 = open(args.output, "w")

#     f1 = file_read(environmentFile)
#     f2 = file_read(queryFile)
#     f3 = open(outputFile, "w")
    
    #String preprocessing done
    t1 = time.time()
    
    junction = junction_read(f1)
    queries = queries_read(f2)
    
    #Search algorithm starts here
    for q in queries:
        
        cost, path = search.uniform_cost_search(junction, q)
        
        if path == None:
        
            f3.write(str('no-path' + '\n'))
            
        else:
            
            f3.write(str(cost) + ' ; ')
                        
            for i in range(len(path) - 1): f3.write(str(path[i]) + ' - ')
            
            f3.write(str(path[i + 1]) + '\n')

    t2 = time.time()
#     f3.write(str(['Time taken: ', float(t2-t1) * 1000., 'ms']))
#     print('Time taken: ', float(t2-t1) * 1000., 'ms')

    return 0;

if __name__ == "__main__":
    
    main()