'''
Created on 18 Oct. 2017

@author: AC
'''

# import numpy as np
import os
import ProblemSpec as PS
import MDP

inputfile = "bronze1.txt"

def main():

    filename = os.path.join(os.getcwd(), inputfile)

    problem = PS.ProblemSpec()
    problem.loadInputFile(filename)

#     print(problem.venture.__str__())

    return 0

if __name__ == "__main__":
    main()