'''
Created on 18 Oct. 2017

@author: AC
'''

import argparse
import os
import MySolver
import Simulator as Sim
import time

# inputfile = "bronze1.txt"
# inputfile = "AI A1/platinum_eg1.txt"
# outputfile = "output1.txt"

# The default number of simulations to run. 
DEFAULT_NUM_SIMULATIONS = 1

# Whether to re-create the solver for every simulation. 
RECREATE_SOLVER = False;

# Convergence threshold values
DELTA_THRESHOLD = {'bronze': 5e-5,
                   'silver': 5e-3,
                   'gold': 5e-1,
                   'platinum': 5e-1}

def main():

    totalProfit = 0
    
    # The number of simulations to run. */
    numSimulations = DEFAULT_NUM_SIMULATIONS; 
    
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", help = "list of roads and info")
    parser.add_argument("outputFile", help = "initial and final locations")
    args = parser.parse_args()
                    
    filename = os.path.join(os.getcwd(), inputfile)
    print("Reading from " + str(filename))
 
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
    
    count = 0
    
     #Perform base value iteration
    if RECREATE_SOLVER == False \
        and not (venture == 'diamond'):
        
        print("Solver Initialised")
        print("-----------------------------------------------")
        solver.doOfflineComputation("policy")
#         print(solver.policyTable) 
#         print(solver.valueTable)

    t2 = time.time()
      
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
            
            if (venture == 'diamond'):
                           
                simulator.simulateOnlineStep(solver, solver.problem.getNumFortnights() - (i + 1))
                
            else:
              
                simulator.simulateOfflineStep(solver)
        
#         if simulator.getTotalProfit() >= 25:
#                
#             print(simulator.getTotalProfit())
#             count += 1
        
        totalProfit += simulator.getTotalProfit()
        print("-----------------------------------------------")
        


    simulator.saveStep(os.path.join(os.getcwd(), outputfile))
#     print("-----------------------------------------------")
    print("Summary statistics from " + str(numSimulations) + " runs")
    print("Overall profit: " + str(totalProfit))
    print("Time taken (s): " + str(t2 - t1))          
        
#     print(count)
    
    return 0

if __name__ == "__main__":
    main()