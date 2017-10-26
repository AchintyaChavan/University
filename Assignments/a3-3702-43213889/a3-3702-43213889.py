'''
Created on 18 Oct. 2017

@author: AC
'''

# import numpy as np
import os
import MDP


inputfile = "bronze1.txt"
outfile = "output1.txt"

def main():

    filename = os.path.join(os.getcwd(), inputfile)

    problem = MDP.PS.ProblemSpec()
    problem.loadInputFile(filename)
    problem.generate_stateSpace()
    
    S0 = tuple([key for key in problem.getInitialFunds().values()])
        
    cost, action = MDP.mdp_policy_iteration(problem, 4e-5)
    
#     f3 = open(os.path.join(os.getcwd(), outfile), "w")
#   
#     f3.write(str(action))
#      
#     cost, action = MDP.mdp_value_iteration(problem, 4e-5)
#      
#     f3.write(str(action))

#     print(problem.venture.__str__())

    return 0

if __name__ == "__main__":
    main()