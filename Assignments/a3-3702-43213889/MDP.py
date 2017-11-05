'''
Created on 9 Oct. 2017

@author: AC
'''

import copy
import ProblemSpec as PS

"""
 * Immediate Reward function R(s, a)
 * @param s Current State
 * @param a Action State
 * @oaram M Maximum threshold for total funding 
 * @param P Probability Matrix
 * @returns the immediate reward at (s, a)
 """
def R(s, a, M, P):
    
    FSale = 0
    FPen = 0
    
    #Could start indexing from 1 since i = 0 will result in zero
    for i in range(0, M + 1):  #(1, M+1)
        
        FSale += PS.np.min([i, s + a]) * P[s + a][i]
        
        
    for j in range(s + a, M + 1): #(s+a+1, M+1)
        
        FPen += (j - s - a) * P[s + a][j]
    
#     for i in range(1, 5):
#     
#         pc +=  np.min([i, c + d]) * P_c[c + d][i]
#         ps +=  np.min([i, s + t]) * P_s[s + t][i]
#         
#     for j in range(c + d + 1, 5):
#         
#         lc += (j - c - d) * P_c[c + d][j]
#         
#     for k in range(s + t + 1, 5):
#         
#         ls += (k - s - t) * P_s[s + t][k]
    
    return PS.np.float(0.6 * FSale - 0.25 * FPen)

"""
 * Transition function R(s, a, s')
 * @param s Current State
 * @param a Action State
 * @param sdash Transition (next) state
 * @param P Probability Matrix
 * @oaram M Maximum threshold for total funding 
 * @param P Probability Matrix
 * @returns the immediate reward at (s, a)
 """
def T(s, a, sdash, M, P):
    
    T = 0
    
    if sdash > (s + a):
        
        T = 0
        
    elif sdash == 0:
        
        T = sum([P[s + a][i] for i in range(s + a + 1, M + 1)]) #(s+a+1, M+1)
                
    else:
        
        T = P[s + a][s + a - sdash]
        
#     print(T)
    
#     Tc = 0
#     Ts = 0
    
    #Tc
#     if cs > (c + d):
#         
#         Tc = 0
#         
#     elif cs == 0:
#         
#         Tc = sum([P_c[c + d][i] for i in range(c + d, 4)])
#     
#     else:
#         
# #         print(c, d, cs)
#         Tc = P_c[c + d][c + d - cs]
        
    #sc            
#     if ss > (s + t):
#         
#         Ts = 0
#         
#     elif ss == 0:
#         
#         Ts = sum([P_s[s + t][j] for j in range(s + t, 4)])
#     
#     else:
#         
#         Ts = P_s[s + t][s + t - ss]
    
#     return Tc * 1. * Ts

    return T

"""
 * Returns all actions that a state can legally transition from
 * @param state Current State
 * @param numVentures Number of ventures
 * @oaram M Maximum threshold for total funding 
 * @param E Maximum threshold for additional spending
 * @returns a list of legal actions from state
 """
def valid_actions(state, numVentures, M, E):

    actions = []
    
    if numVentures == 2:
    
        (s1, s2) = state
    
        for a1 in range(0, M):
            
            for a2 in range(0, M - a1):
            
                if (s1 + s2 + a1 + a2) <= M and (a1 + a2) <= E:
                    
                    actions.append(tuple((a1, a2)))
                    
    elif numVentures == 3:
        
        (s1, s2, s3) = state
    
        for a1 in range(0, M):
            
            for a2 in range(0, M - a1):
                
                for a3 in range(0, M - a1 - a2):
            
                    if (s1 + s2 + s3 + a1 + a2 + a3) <= M and (a1 + a2 + a3) <= E:
                        
                        actions.append(tuple((a1, a2, a3)))
        
    return actions

"""
 * Computes the mdp using value iteration
 * @param problem Problem Spec Config 
 * @param epsilon Convergence value
 * @returns the immediate reward at (s, a)
 """
def mdp_value_iteration(problem, valueTable, policyTable, epsilon):
    
#     V = {key: 0 for key in problem.stateSpace}
#     optimalAction = {key: key for key in problem.stateSpace}

    V = valueTable
    optimalAction = policyTable
    
    N = problem.venture.getNumVentures()
    M = problem.venture.getManufacturingFunds()
    E = problem.venture.getAdditionalFunds()
    Gamma = problem.getDiscountFactor()
    Prices = problem.getSalePrices()
    
    Vprev = 5 * epsilon
    counter = 0
        
    while PS.np.abs(sum(V.values()) - Vprev) > epsilon:
        
        Vprev = sum(V.values())
                
        for S in problem.getStateSpace():
            
            cost, action = MDP_greedy_search(problem, V, S, N, M, E, Gamma, Prices)
            
#             actions = valid_actions(S, N, M, E)
#             total = []
#             
#             for A in actions:
#                 
#                 immediate = 0
#                 expected = 0
#                 
#                 for Sdash in problem.getStateSpace():
#                     
#                     expected += Gamma * V[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
#                                                                  problem.probabilities[i + 1]) for i in range(0, N)])
#                     
#                 immediate = sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
#                 
#                 total.append(immediate + expected)
#              
# #             print(total)    
#             id = PS.np.argmax(PS.np.array(total), axis = 0)
            optimalAction[S] = action
            V[S] = cost
             
        counter = counter + 1
#         print(counter, Vprev)
#         print(V)

#     print(counter)
#     print(optimalAction)
#     print(V)
    
    return V, optimalAction

"""
 * Computes the mdp using policy iteration
 * @param problem Problem Spec Config 
 * @param epsilon Convergence value
 * @returns the immediate reward at (s, a)
 """
def mdp_policy_iteration(problem, valueTable, policyTable, epsilon):
    
    V = valueTable
    Qpidash = {}
    
    N = problem.venture.getNumVentures()
    M = problem.venture.getManufacturingFunds()
    E = problem.venture.getAdditionalFunds()
    Gamma = problem.getDiscountFactor()
    Prices = problem.getSalePrices()
  
    policy = policyTable
     
    # Generate a random policy but making sure it is a legal action
    for key in policy.keys():
         
        action = valid_actions(key, N, M, E)
        policy[key] = action[PS.np.random.randint(len(action))]
        
    Vprev = 5 * epsilon #Arbitrarily large value to get inside loop
    counter = 0
    
    while PS.np.abs(sum(V.values()) - Vprev) > epsilon:
        
        Vprev = sum(V.values())
        
        #Estimate Policy Value
        for S in problem.getStateSpace():
            
            expected = 0
            A = policy[S]
            
            for Sdash in problem.getStateSpace():
                    
                expected += V[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
                                                    problem.probabilities[i + 1]) for i in range(0, N)])
            
            immediate = sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
            
            V[S] = immediate + Gamma * expected

        #Improve Policy
        for S in problem.getStateSpace():
                
#             actions = valid_actions(S, N, M, E)
#             total = []
#             
#             for A in actions:
# 
#                 expected = 0
#                 
#                 for Sdash in problem.getStateSpace():
#                     
#                     expected += Gamma * V[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
#                                                                  problem.probabilities[i + 1]) for i in range(0, N)])
#                     
#                 immediate += sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
#                 
#                 total.append(immediate + expected)
# 
#             id = PS.np.argmax(PS.np.array(total), axis = 0)

            cost, action = MDP_greedy_search(problem, V, S, N, M, E, Gamma, Prices)

            Qpidash[S] = cost
            
            #If policy is not optimal then update it to optimal one and take it up
            if Qpidash[S] > V[S]:
                
                policy[S] = action
                V[S] = Qpidash[S]
            
            #Update Policy
#             if policy[S] == actions[id]:
#  
#                 print(S)
#                 pass
#                          
#             elif Qpidash[S] > Qpi:
#                  
#                 policy[S] = actions[id]
        
        counter = counter + 1
                    
    return Qpidash, policy

"""
 * Computes the greedy policy
 * @param problem Problem Spec Config 
 * @param valueTable Value Function lookup table
 * @param S0 current state
 * @returns the immediate reward at (s, a)
 """
def MDP_greedy_search(problem, valueTable, S0, N, M, E, Gamma, Prices):

#     N = problem.venture.getNumVentures()
#     M = problem.venture.getManufacturingFunds()
#     E = problem.venture.getAdditionalFunds()
#     Gamma = problem.getDiscountFactor()
#     Prices = problem.getSalePrices()
    
    S = S0
    
    actions = valid_actions(S0, N, M, E)
    total = []
         
    for A in actions:
             
        immediate = 0
        expected = 0
         
        for Sdash in problem.getStateSpace():
             
            expected += Gamma * valueTable[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
                                                         problem.probabilities[i + 1]) for i in range(0, N)])
             
        immediate = sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
         
        total.append(immediate + expected)        
           
        id = PS.np.argmax(PS.np.array(total), axis = 0)

    return total[id], actions[id]

"""
 * Uses the currently loaded stochastic model to sample new state.
 * @param state The manufacturing funds allocation
 * @param P Probability Matrices
 * @param N Number of ventures
 * @return New state as list of integers
"""
def sampleMatrix(state, P, N):
    
    row = []
    for k in range(N):

        s = state[k]
        prob = P[k + 1][s]
        row.append(sampleIndex(prob))

    return row

"""
 * Returns an index sampled from a list of probabilities
 * @precondition probabilities in prob sum to 1
 * @param prob
 * @return an int with value within [0, row.size() - 1]
"""
def sampleIndex(row):
        
    sum = 0
    r = PS.np.random.rand()  #Return random dist between 0 or 1
    
    for i in range(len(row)):
        
        sum += row[i]
        
        if (sum >= r):
            
            return i
                    
    return -1  #Need to check if this is valid for larger test cases
