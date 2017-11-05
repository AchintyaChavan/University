'''
Created on 18 Oct. 2017

@author: AC
'''

import argparse
import os
import MySolver
import Simulator as Sim
import time

inputfile = "platinum1.txt"
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
    venture = problem.venture.getName() 
    epsilon = DELTA_THRESHOLD[venture]
    
    #Initialise Solver Class
    solver = MySolver.MySolver(problem, epsilon)
        
    #Initialise Simulator Class with ProblemSpec and Solver classes
    simulator = Sim.Simulator()
    simulator.constructor(solver.problem)
    """
    ####Change this to True to display fortnightly results - Default is False
    """
    simulator.setVerbose(True)
    
    t1 = time.time()
    
     #Perform base value iteration
    if RECREATE_SOLVER == False \
        and not (venture == 'gold' or venture == 'platinum'):
        
        print("Solver Initialised")
        print("-----------------------------------------------")
        solver.doOfflineComputation("value")
#         print(solver.policyTable) 
    
    #Run simulator this many times
    for simNo in range(numSimulations):
        
        print("Simulation Run " + str(simNo + 1))                
        simulator.reset()
        
        if RECREATE_SOLVER == True \
            and not (venture == 'gold' or venture == 'platinum'):
            
            print("Solver Reinitialised")
            solver = MySolver.MySolver(problem, epsilon)
            solver.doOfflineComputation("value")
                
        print("-----------------------------------------------")
        
        #Perform simulations over the entire fortnight
        for i in range(solver.problem.getNumFortnights()):
            
            if (venture == 'gold' or venture == 'platinum'):
                           
                simulator.simulateOnlineStep(solver, solver.problem.getNumFortnights() - (i + 1))
                
            else:
              
                simulator.simulateOfflineStep(solver)
            
        totalProfit += simulator.getTotalProfit()
        print("-----------------------------------------------")
        
    t2 = time.time()

    simulator.saveStep(os.path.join(os.getcwd(), outputfile))
#     print("-----------------------------------------------")
    print("Summary statistics from " + str(numSimulations) + " runs")
    print("Overall profit: " + str(totalProfit))
    print("Time taken (s): " + str(t2 - t1))          
    
    return 0

if __name__ == "__main__":
    main()