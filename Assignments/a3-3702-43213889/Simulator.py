'''
Created on 28 Oct. 2017

@author: AC
'''

import MySolver
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
        
        self.verbose = False
               
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
        self.fundsAllocation = self.problem.getInitialFunds().values()
        self.fundsAllocationHistory = []   
        self.additionalFundsHistory = []    
        self.customerOrderHistory = []      
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
        
        profit = 0
        
        # Record manufacturing funds at start of fortnight
        fortnightStartManufacturingFunds = self.fundsAllocation[:]
        self.fundsAllocationHistory.append(self.fundsAllocation)
        
        # Generature customer orders
        orders = self.sampleCustomerOrders(self.fundsAllocation)
        
        prices = self.problem.getSalePrices().values()
        
        for i in range(len(orders)):
            
            # Compute profit from sales
            sold = PS.np.min([orders[i], self.fundsAllocation[i]])
            profit += (sold * prices[i] * 0.6)

            # Compute missed opportunity
            missed = orders[i] - sold
            profit -= (missed * prices[i] * 0.25)

            # Update manufacturing fund levels    
            self.fundsAllocation[i] -= sold
        
        # Add customer orders to history
        self.customerOrderHistory.append(orders)
        
        # Record manufacturing fund levels after customer orders
        afterOrderFunds = self.fundsAllocation[:]

        # Get addition funding amounts
        additionalFunding = solver.generateAdditionalFundingAmounts(afterOrderFunds)
    
        if len(additionalFunding) != self.problem.venture.getNumVentures():
            
            raise Exception("Invalid additional funding list size")
        
        totalAdditional = 0
        totalFunds = 0
        
        # Apply additional funds to manufacturing fund levels
        for i in range(len(additionalFunding)):
            
            totalAdditional += additionalFunding[i]
            self.fundsAllocation[i] += additionalFunding[i]
            totalFunds += self.fundsAllocation[i]
            
        if totalAdditional > self.problem.venture.getAdditionalFunds():
        
            raise Exception("Amount of additional funding is too large.")
        
        if totalFunds > self.problem.venture.getManufacturingFunds():
            
            raise Exception("Maximum manufacturing funds exceeded.")
        
        # Add additional funding amount to history
        self.additionalFundsHistory.append(additionalFunding)
        
        # Update discounted profit
        self.totalProfit += self.problem.getDiscountFactor() ** (self.currentFortnight - 1) * 1. * profit
  
        if self.verbose == True:

            print("Fortnight " + str(self.currentFortnight))
            print("Start manufacturing funds: " + str(fortnightStartManufacturingFunds))
            print("Customer order: " + str(orders))
            print("Funds after customer order: " + str(afterOrderFunds))
            print("Additional funding: " + str(additionalFunding))
            print("Funds after funding: " + str(self.fundsAllocation))
            print("Profit this fortnight: " + str(float(profit)))
            
            if (self.currentFortnight == self.problem.getNumFortnights()):
                
                print("Total discounted profit: " + str(self.totalProfit))
            
    
        self.currentFortnight += 1
    
    """
     * Uses the currently loaded stochastic model to sample customer order demand.
     * Note that user wants may exceed the amount in the manufacturing fund
     * @param state The manufacturing funds allocation
     * @return Customer orders as list of item quantities
    """
    def sampleCustomerOrders(self, state):
        
        wants = []
        for k in range(self.venture.getNumVentures()):

            s = state[k]
            prob = self.probabilities[k + 1][s]
            wants.append(self.sampleIndex(prob))

        return wants
    
    """
     * Returns an index sampled from a list of probabilities
     * @precondition probabilities in prob sum to 1
     * @param prob
     * @return an int with value within [0, row.size() - 1]
    """
    def sampleIndex(self, row):
        
        sum = 0
        r = PS.np.random.rand()  #Return random dist between 0 or 1
        
        for i in range(len(row)):
            
            sum += row[i]
            
            if (sum >= r):
                
                return i
                    
        return -1  #Need to check if this is valid for larger test cases
    
    """
     * Saves the current history and total penalty to file
     * @param filename The path to the text file to save to
     * @throws IOException
    """
    def saveStep(self, filename):
        
        self.problem.saveOutputFile(filename, self.customerOrderHistory, self.additionalFundsHistory)
        
    """
     * Set verbose to true for console output
     * @param verbose
    """
    def setVerbose(self, verbose):
        
        self.verbose = verbose   
    
    """
     * Get funds allocation from history
     * @precondition fortnight < currentFortnight
     * @param fortnight The fortnight to retrieve. Fortnight starts at 1.
     * @return the fundsAllocation for that week.
    """
    def getFundsAllocationAt(self, fortnight):
        
        return self.fundsAllocationHistory[fortnight - 1]
    
    """
     * Get additional funding from history
     * @precondition fortnight < currentFortnight
     * @param fortnight The fortnight to retrieve. Fortnight starts at 1.
     * @return the additional funding for that fortnight.
    """
    def getAdditionalFundingAt(self, fortnight):
        
        return self.additionalFundsHistory[fortnight - 1]
    
    """
     * Get customer orders from history
     * @precondition fortnight < currentFortnight
     * @param fortnight The fortnight to retrieve. Fortnight starts at 1.
     * @return the user request for that fortnight.
    """
    def getCustomerOrderAt(self, fortnight):
        
        return self.customerOrderHistory[fortnight - 1]
    
    """
     * @return the total profit so far
    """ 
    def getTotalProfit(self):
        
        return self.totalProfit
    
    def getCurrentFortnight(self):
        
        return self.currentFortnight
    
    def getFundsAllocation(self):
        
        funds = self.fundsAllocation[:]
        
        return funds
    
    