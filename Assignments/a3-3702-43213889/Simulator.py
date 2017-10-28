'''
Created on 28 Oct. 2017

@author: AC
'''

import ProblemSpec as PS

class Simulator:
    
    def __init__(self):
        
        self.currentFortnight = 1
        self.problem = None
        self.fundsAllocation = []           #Tuple of manufacturing funds for current fortnight
        self.fundsAllocationHistory = []    #List of manufacturing fund tuples
        self.additionalFundsHistory = []    #List of additional fund tuples
        self.customerOrderHistory = []      #List of customer order tuples
        self.totalProfit = 0
        self.venture = None
        self.probabilities = 0
               
    """
     * Constructor
     * @param spec is a problemspec class
    """    
    def constructor(self, problem):
        
        self.problem = problem
        self.venture = problem.getVentureManager()
        self.probabilities = problem.getProbabilities()
        
        self.reset()
        
    def reset(self):
        
        self.currentFortnight = 1
        self.fundsAllocation = self.problem.getInitialFunds()
        self.fundsAllocationHistory = []    #List of manufacturing fund tuples
        self.additionalFundsHistory = []    #List of additional fund tuples
        self.customerOrderHistory = []      #List of customer order tuples
        self.totalProfit = 0
            
    """
     * Simulate a fortnight. A runtime exception is thrown if the additional
     * funds allocation is invalid. If the additional funds allocation is valid,
     * the customer order demand is sampled and the current fortnight is
     * advanced.
     * @param solver
     * @param numFortnightsLeft
     """
    def simulateStep(self, solver, numFortnightsLeft):
         
        self.fundsAllocationHistory.append(self.fundsAllocation)
        
        orders = self.sampleCustomerOrders(self.fundsAllocation)
        
    
    """
     * Uses the currently loaded stochastic model to sample customer order demand.
     * Note that user wants may exceed the amount in the manufacturing fund
     * @param state The manufacturing funds allocation
     * @return Customer orders as list of item quantities
    """
    def sampleCustomerOrders(self, state):
        
        wants = []
        for k in range(self.venture.getNumVentures()):
            
            s = state[k + 1]
            prob = self.probabilities[k + 1][s]
            wants.append(self.sampleIndex(prob))


        return wants
    
    """
     * Returns an index sampled from a list of probabilities
     * @precondition probabilities in prob sum to 1
     * @param prob
     * @return an int with value within [0, prob.size() - 1]
    """
    def sampleIndex(self, row):
        
        sum = 0
        r = PS.np.random.rand()  #Return random dist between 0 or 1
        
        for i in range(len(row)):
            
            sum += row[i]
            
            if (sum >= r):
                
                return i
                    
        return -1  #Need to check if this is valid for larger test cases
        
     