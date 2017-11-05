'''
Created on 28 Oct. 2017

@author: AC
'''

import MDP

class MySolver:
    
    def __init__(self, problem, epsilon):
        
        self.problem = problem
        
        #Allocated Convergence threshold
        self.epsilon = epsilon
        
         #Dictionary of states whose values contain overall V(s)             
        self.valueTable = {key: 0 for key in problem.stateSpace}
        
        #Dictionary of states whose values contain optimal actions/policies     
        self.policyTable = {key: key for key in problem.stateSpace} 
          
    """
     * Performs an exhaustive offline optimisation before simulations
     * @param type Type of solver to use
    """         
    def doOfflineComputation(self, type):
        
        if type == 'value':
            
            cost, action = MDP.mdp_value_iteration(self.problem, self.valueTable,
                                                   self.policyTable, self.epsilon)
            
        elif type == 'policy':
            
            cost, action = MDP.mdp_policy_iteration(self.problem, self.valueTable,
                                                    self.policyTable, self.epsilon)
               
        self.valueTable = cost
        self.policyTable = action
        
    """
     * Performs an online RTDP method on a particular state
     * @param S0 initial state
    """       
    def doOnlineComputation(self, S0):
        
        S0 = tuple(S0)
        
        N = problem.venture.getNumVentures()
        M = problem.venture.getManufacturingFunds()
        E = problem.venture.getAdditionalFunds()
        Gamma = problem.getDiscountFactor()
        Prices = problem.getSalePrices()
        
        cost, action = MDP.MDP_greedy_search(self.problem, self.valueTable, S0,
                                             N, M, E, Gamma, Prices)
        
        self.valueTable[S0] = cost
        self.policyTable[S0] = action
    
    """
     * Allocate additional funding to each venture
     * @param fund is the leftover manufacturing fund after orders are taken into consideration
     * @return additionalFunding that is needed to topup the leftover funds for next fortnight
    """  
    def generateAdditionalFundingAmounts(self, fund):
        
        additionalFunding = self.policyTable[tuple(fund)]
        
        return list(additionalFunding)
            
        