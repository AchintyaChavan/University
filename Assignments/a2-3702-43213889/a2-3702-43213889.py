'''
Created on 9 Sep. 2017

@author: AC
'''

import argparse
import os
import numpy as np

import config

inputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Assignments\\a2-3702-43213889\\a2-tools\\a2-tools\\testcases\\3ASV-easy.txt"
outputFile = "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\Assignments\\a2-3702-43213889\\3ASV-easy-output.txt"


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
    
#     f3 = open(os.path.join(os.getcwd(), outputFile), "w")
    
    return;

if __name__ == "__main__":
    
    main()