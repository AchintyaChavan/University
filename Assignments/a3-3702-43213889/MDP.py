'''
Created on 9 Oct. 2017

@author: AC
'''

import copy
import ProblemSpec as PS

"""
 * Immediate Reward function R(s, a)
 * @param state s, action a, max value M, Probability matrix P
 * @returns the immediate reward at (s, a)
 """
def R(s, a, M, P):
    
    FSale = 0
    FPen = 0
    
    for i in range(1, M + 1):
        
        FSale += PS.np.min([i, s + a]) * P[s + a][i]
        
        
    for j in range(s + a + 1, M + 1):
        
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
 * @param state s, action a, max value M, Probability matrix P
 * @returns the immediate reward at (s, a)
 """
def T(s, a, sdash, M, P):
    
    T = 0
    
    if sdash > (s + a):
        
        T = 0
        
    elif sdash == 0:
        
        T = sum([P[s + a][i] for i in range(s + a, M)])
        
    else:
        
        T = P[s + a][s + a - sdash]
        

    
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
 * @param state, number of ventures, maximum threshold M, excess funding E
 * @returns the immediate reward at (s, a)
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
 * @param problem spec config, epsilon - convergence threshold, initial state - S0
 * @returns the immediate reward at (s, a)
 """
def mdp_value_iteration(problem, epsilon, S0):
    
    V = {key: 0 for key in problem.stateSpace}
    optimalAction = {key: key for key in problem.stateSpace}
    
    N = problem.venture.getNumVentures()
    M = problem.venture.getManufacturingFunds()
    E = problem.venture.getAdditionalFunds()
    Gamma = problem.getDiscountFactor()
    Prices = problem.getSalePrices()
    
    Vprev = 5 * epsilon
    counter = 0
    
    while PS.np.abs(V[S0] - Vprev) > epsilon:
        
        Vprev = V[S0]
        
        for S in problem.getStateSpace():
            
            actions = valid_actions(S, N, M, E)
            total = []
            
            for A in actions:
                
                immediate = 0
                expected = 0
                
                for Sdash in problem.getStateSpace():
                    
                    expected += Gamma * V[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
                                                                 problem.probabilities[i + 1]) for i in range(0, N)])
                    
                immediate = sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
                
                total.append(immediate + expected)
             
#             print(total)    
            id = PS.np.argmax(PS.np.array(total), axis = 0)
            optimalAction[S] = actions[id]
            V[S] = total[id]
             
        counter = counter + 1
#         print(counter, Vprev)
#         print(V)

    print(counter)
    print(optimalAction[S0], V[S0])
    
    return V[S0], optimalAction[S0]

'''
# Value Iteration: Complexity O = (t * a * s^2)
# '''
# def mdp_value_interation(N, S0, Discount):
#     
#     V = {key: 0 for key in stateSpace}
#     future  = {key: 0 for key in stateSpace}
#     optimalAction = {key: key for key in stateSpace}
#  
#     for i in range(0, N):
#         
#         for S in stateSpace:
#         
#             (c, s) = S
#             actions = valid_actions(S)
#             total = []
#                         
#             for a in actions:
#                 
#                 (d, t) = a
#                 expected = 0                
#                 
#                 for Sdash in stateSpace:
#                                         
#                     (sdash, cdash) = Sdash
#                     
#                     expected += Discount * 1. * T(c, s, d, t, cdash, sdash) * V[Sdash]
#                 
# #                 print(expected, S)   
#                 total.append(R(c, s, d, t) + expected)
# #                 future[S] = expected
#                 
#             id = np.argmax(np.array(total), axis = 0)
#             optimalAction[S] = actions[id]
#             V[S] = total[id]
# 
# #     print(V[S0], future[S0], V[S0]-future[S0])
# #     print(optimalAction[S0])
# 
#     return V, optimalAction


"""
 * Computes the mdp using policy iteration
 * @param problem spec config, epsilon - convergence threshold, initial state - S0
 * @returns the immediate reward at (s, a)
 """
def mdp_policy_iteration(problem, epsilon, S0):
    
    V = {key: 0 for key in problem.stateSpace}
    optimalAction = {}
    Qpidash = {}
    
    N = problem.venture.getNumVentures()
    M = problem.venture.getManufacturingFunds()
    E = problem.venture.getAdditionalFunds()
    Gamma = problem.getDiscountFactor()
    Prices = problem.getSalePrices()
  
    policy = copy.deepcopy(V)
     
    # Generate a random policy but making sure it is a legal action
    for key in policy.keys():
         
        action = valid_actions(key, N, M, E)
        policy[key] = action[PS.np.random.randint(len(action))]
        
    breakLoop = False
    Vprev = 5 * epsilon
    counter = 0
    
    while PS.np.abs(V[S0] - Vprev) > epsilon:

        Vprev = V[S0]
        
        #Estimate Policy Value
        for S in problem.getStateSpace():
            
            expected = 0
            A = policy[S]
            
            for Sdash in problem.getStateSpace():
                    
                expected += Gamma * V[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
                                                        problem.probabilities[i + 1]) for i in range(0, N)])
            
            immediate = sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
            
            V[S] = expected + immediate

        #Improve Policy
        for S in problem.getStateSpace():
                
            actions = valid_actions(S, N, M, E)
            total = []
            Qpi = V[S]
            
            for A in actions:
                
                immediate = 0
                expected = 0
                
                for Sdash in problem.getStateSpace():
                    
                    expected += Gamma * V[Sdash] * PS.np.prod([T(S[i], A[i], Sdash[i], M, 
                                                                 problem.probabilities[i + 1]) for i in range(0, N)])
                    
                immediate += sum([Prices[i + 1] * R(S[i], A[i], M, problem.probabilities[i + 1]) for i in range(0, N)])
                
                total.append(immediate + expected)
             
#             print(total)    
            id = PS.np.argmax(PS.np.array(total), axis = 0)

            Qpidash[S] = total[id]
            V[S] = Qpidash[S]
            
            #Update Policy
            if policy[S] == actions[id] and S == S0:
 
                print("Policy converged to optimal policy")
                breakLoop = True
                break
                         
            elif Qpidash[S] > Qpi:
                 
                policy[S] = actions[id]
                Qpi = Qpidash[S]
                
        if breakLoop:
             
            break
        
        counter = counter + 1
        
    print(counter)     
    
    print(Qpidash[S0], policy[S0])            
    return Qpidash[S0], policy[S0]
# '''
# Policy Iteration: Complexity O = (t * a * s^2)
# '''
# def mdp_policy_interation(N, S0, Discount):
#     
#     V = {key: 0 for key in stateSpace}
#     QpiDash = {}    
#     
#     policy = copy.deepcopy(V)
#     
#     # Generate a random policy but making sure it is a legal action
#     for key in policy.keys():
#         
#         a = valid_actions(key)
#         policy[key] = a[np.random.randint(len(a))]
#     
# 
#     print("Initial policy for " + str(S0) + ": " + str(policy[S0]))
# 
#     breakLoop = False
#     
#     for i in range(0, N):
#         
#         for S in stateSpace:
#             
#             (c, s) = S
#             (d, t) = policy[S]
#             V[S] = R(c, s, d, t) + Discount * 1. * np.sum(np.array(
#                                     [T(c, s, d, t, Sdash[0], Sdash[1]) * V[Sdash] 
#                                     for Sdash in stateSpace]))
#         
#         for S in stateSpace:
#             
#             Qpi = V[S]
#             (c, s) = S            
#             actions = valid_actions(S)
#             total = []
#             
#             for a in actions:
#                 
#                 (d, t) = a
#                 expected = 0 
#                 
#                 for Sdash in stateSpace:
#                                         
#                     (sdash, cdash) = Sdash
#                     
#                     expected += Discount * 1. * T(c, s, d, t, cdash, sdash) * V[Sdash]
#                     
#                 total.append(R(c, s, d, t) + expected)   
#             
#             id = np.argmax(np.array(total), axis = 0)
#             QpiDash[S] = total[id]   #Total reward of maximised action
#             
#             #Check for convergence: pi
#             if policy[S] == actions[id] and S == S0:
# 
#                 print("Policy converged to optimal policy")
#                 breakLoop = True
#                 break
#                         
#             elif QpiDash[S] > Qpi:
#                 
#                 policy[S] = actions[id]
#                 Qpi = QpiDash[S]
#         
#         if breakLoop:
#             
#             break
#     
#     return QpiDash, policy
