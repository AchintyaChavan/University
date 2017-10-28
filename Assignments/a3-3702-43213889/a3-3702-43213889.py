'''
Created on 18 Oct. 2017

@author: AC
'''

# import numpy as np
import os
import Simulator as Sim


inputfile = "bronze1.txt"
outfile = "output1.txt"

def main():

    epsilon = 4e-5   #Convergence Value
    filename = os.path.join(os.getcwd(), inputfile)
 
    #Initialise ProblemSpec Class
    problem = Sim.PS.ProblemSpec()
    problem.loadInputFile(filename)
    problem.generate_stateSpace()

    #Initialise Solver Class
    solver = Sim.MySolver.MySolver(problem, epsilon)
    solver.doOfflineComputation('value')  #Perform base value iteration
    
    #Initialise Simulator Class with ProblemSpec and Solver classes
    simulator = Sim.Simulator()
    simulator.constructor(problem)
    simulator.setVerbose(True)
    simulator.simulateStep(solver, 16)
                
#     S0 = tuple([key for key in problem.getInitialFunds().values()])
        
#     simulator.saveStep(os.path.join(os.getcwd(), outfile))
    
    return 0

if __name__ == "__main__":
    main()