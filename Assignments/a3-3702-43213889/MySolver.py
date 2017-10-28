'''
Created on 28 Oct. 2017

@author: AC
'''

import MDP

class MySolver:
    
    def __init__(self, problem, epsilon):
        
        self.problem = problem
        self.epsilon = epsilon       #Convergence threshold
        self.valueTable = {}         #Dictionary of states whose values contain overall V(s)
        self.policyTable = {}        #Dictionary of states whose values contain optimal action
            
    def doOfflineComputation(self, type):
        
        if type == 'value':
            
            cost, action = MDP.mdp_value_iteration(self.problem, self.epsilon)
            
        elif type == 'policy':
            
            cost, action = MDP.mdp_policy_iteration(self.problem, self.epsilon)
               
        self.valueTable = cost
        self.policyTable = action
    
    def doOnlineComputation(self, initialState, fortnightsLeft):
        
        pass
    
    """
     * Allocate additional funding to each venture
     * @param fund is the leftover manufacturing fund after orders are taken into consideration
     * @return additionalFunding that is needed to topup the leftover funds for next fortnight
    """  
    def generateAdditionalFundingAmounts(self, fund):
        
        additionalFunding = self.policyTable[tuple(fund)]
        
        return list(additionalFunding)
            
        