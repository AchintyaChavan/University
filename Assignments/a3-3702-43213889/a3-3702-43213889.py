'''
Created on 18 Oct. 2017

@author: AC
'''

# import numpy as np
import os
import MDP


inputfile = "bronze1.txt"

def main():

    filename = os.path.join(os.getcwd(), inputfile)

    problem = MDP.PS.ProblemSpec()
    problem.loadInputFile(filename)
    problem.generate_stateSpace()
    
    S0 = tuple([key for key in problem.getInitialFunds().values()])
    
    MDP.mdp_value_iteration(problem, 0.4, S0)

#     print(problem.venture.__str__())

    return 0

if __name__ == "__main__":
    main()