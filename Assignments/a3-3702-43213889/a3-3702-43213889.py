'''
Created on 18 Oct. 2017

@author: AC
'''

import argparse
import os
import MySolver
import Simulator as Sim

inputfile = "bronze1.txt"
outputfile = "output1.txt"

# The default number of simulations to run. 
DEFAULT_NUM_SIMULATIONS = 1

# Whether to re-create the solver for every simulation. 
RECREATE_SOLVER = False;

# Convergence threshold values
DELTA_THRESHOLD = {'bronze': 5e-5,
                   'silver': 5e-3,
                   'gold': 5e-1,
                   'platinum': 5e0}

def main():

    totalProfit = 0
    
    # The number of simulations to run. */
    numSimulations = DEFAULT_NUM_SIMULATIONS; 
    
#     parser = argparse.ArgumentParser()
#     parser.add_argument("inputFile", help = "list of roads and info")
#     parser.add_argument("outputFile", help = "initial and final locations")
#     args = parser.parse_args()
        
            
    filename = os.path.join(os.getcwd(), inputfile)
 
    #Initialise ProblemSpec Class
    problem = Sim.PS.ProblemSpec()
    problem.loadInputFile(filename)
    problem.generate_stateSpace()

    #Designate convergence threshold value according to type    
    epsilon = DELTA_THRESHOLD[problem.venture.getName()]
    
    #Initialise Solver Class
    solver = MySolver.MySolver(problem, epsilon)
        
    #Initialise Simulator Class with ProblemSpec and Solver classes
    simulator = Sim.Simulator()
    simulator.constructor(solver.problem)
    """
    ####Change this to True to display fortnightly results - Default is False
    """
    simulator.setVerbose(True)
    
     #Perform base value iteration
    if RECREATE_SOLVER == False:
        
        print("Solver Initialised")
        solver.doOfflineComputation("value") 
    
    #Run simulator this many times
    for simNo in range(numSimulations):
        
        print("Simulation Run ", simNo + 1)                
        simulator.reset()
        
        if RECREATE_SOLVER == True:
            
            print("Solver Reinitialised")
            solver = Sim.MySolver.MySolver(problem, epsilon)
            solver.doOfflineComputation("value")
                
        print("-----------------------------------------------")
        
        #Perform simulations over the entire fortnight
        for i in range(solver.problem.getNumFortnights()):
                       
            simulator.simulateStep(solver, solver.problem.getNumFortnights() - (i + 1))
        
        totalProfit += simulator.getTotalProfit()
        print("-----------------------------------------------")
        
        
    simulator.saveStep(os.path.join(os.getcwd(), outputfile))
#     print("-----------------------------------------------")
    print("Summary statistics from " + str(numSimulations) + " runs")
    print("Overall profit: " + str(totalProfit))          
    
    return 0

if __name__ == "__main__":
    main()