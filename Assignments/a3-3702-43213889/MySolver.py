'''
Created on 28 Oct. 2017

@author: AC
'''

import ProblemSpec as PS
import MDP

class MySolver:
    
    def __init__(self, problem, epsilon):
        
        self.problem = Problem
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
        
        additionalFunding = self.policyTable[fund]
        
        return additionalFunding
        
#         totalManufacturingFunds = sum(manufacturingFunds)
#         
#         totalAdditional = 0
#         for i in range(problem.venture.getNumVentures()):
#             
#             if (totalManufacturingFunds >= self.problem.venture.getManufacturingFunds()) or \
#                 (totalAdditional >= self.problem.venture.getAdditionalFunds()):
#                 
#                 additionalFunding[i] = 0
#                 
#             else:
#                 
#                 additionalFunding = self.policyTable[manufacturingFunds]
            
        