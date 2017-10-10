'''
Created on 9 Oct. 2017

@author: AC
'''

import numpy as np
import copy

stateSpace = [(0, 0),
              (0, 1),
              (0, 2),
              (0, 3),
              (0, 4),
              (1, 0),
              (1, 1),          
              (1, 2),
              (1, 3),
              (2, 0),
              (2, 1),
              (2, 2),
              (3, 0),
              (3, 1),
              (4, 0)]


P_c = 1/10. * np.array([[3, 2, 2, 1, 2],
                        [3, 2, 2, 1, 2],
                        [3, 2, 2, 1, 2],
                        [3, 2, 2, 1, 2],                                   
                        [3, 2, 2, 1, 2]])

P_s = 1/10. * np.array([[2, 2, 2, 2, 2],
                        [3, 2, 2, 1, 3],
                        [3, 2, 2, 1, 3],
                        [3, 2, 2, 1, 3],                                   
                        [3, 2, 2, 1, 3]])


def test():
    
#     print(np.sum(range(1,4) * 4))
#     print(np.asarray([x for x in range(0,3)]))

#     print(P_s.shape)
#     print(P_s[0][3])
#     print(sum([P_c[2][i] for i in range(2, 4)]))

#     print(valid_actions((2, 2)))
    

    
    pass

# Reward Function
def R(c, s, d, t):
    
    pc = 0
    lc = 0
    
    ps = 0
    ls = 0
    
    for i in range(1, 5):
    
        pc +=  np.min([i, c + d]) * P_c[c + d][i]
        ps +=  np.min([i, s + t]) * P_s[s + t][i]
        
    for j in range(c + d + 1, 5):
        
        lc += (j - c - d) * P_c[c + d][j]
        
    for k in range(s + t + 1, 5):
        
        ls += (k - s - t) * P_s[s + t][k]
    
    return np.float(pc - 0.5 * lc) + np.float(ps - 0.5 * ls)

# Transition Function
def T(c, s, d, t, cs, ss):
    
#     Tc = 0
#     Ts = 0
    
    #Tc
    if cs > (c + d):
        
        Tc = 0
        
    elif cs == 0:
        
        Tc = sum([P_c[c + d][i] for i in range(c + d, 4)])
    
    else:
        
#         print(c, d, cs)
        Tc = P_c[c + d][c + d - cs]
        
    #sc            
    if ss > (s + t):
        
        Ts = 0
        
    elif ss == 0:
        
        Ts = sum([P_s[s + t][j] for j in range(s + t, 4)])
    
    else:
        
        Ts = P_s[s + t][s + t - ss]
    
    return Tc * 1. * Ts

def valid_actions(state):

    (c, s) = state

    actions = []

    for d in range(0, 4):
        
        for t in range(0, 4 - d):
        
            if (c + d + s + t) <= 4:
                
                actions.append(tuple((d, t)))
        
    return actions

'''
Value Iteration: Complexity O = (t * a * s^2)
'''
def mdp_value_interation(N, S0, Discount):
    
    V = {key: 0 for key in stateSpace}
    future  = {key: 0 for key in stateSpace}
    optimalAction = {key: key for key in stateSpace}
 
    for i in range(0, N):
        
        for S in stateSpace:
        
            (c, s) = S
            actions = valid_actions(S)
            total = []
                        
            for a in actions:
                
                (d, t) = a
                expected = 0                
                
                for Sdash in stateSpace:
                                        
                    (sdash, cdash) = Sdash
                    
                    expected += Discount * 1. * T(c, s, d, t, cdash, sdash) * V[Sdash]
                
#                 print(expected, S)   
                total.append(R(c, s, d, t) + expected)
#                 future[S] = expected
                
            id = np.argmax(np.array(total), axis = 0)
            optimalAction[S] = actions[id]
            V[S] = total[id]

#     print(V[S0], future[S0], V[S0]-future[S0])
#     print(optimalAction[S0])

    return V, optimalAction


'''
Policy Iteration: Complexity O = (t * a * s^2)
'''
def mdp_policy_interation(N, S0, Discount):
    
    V = {key: 0 for key in stateSpace}
    QpiDash = {}    
    
    policy = copy.deepcopy(V)
    
    # Generate a random policy but making sure it is a legal action
    for key in policy.keys():
        
        a = valid_actions(key)
        policy[key] = a[np.random.randint(len(a))]
    

    print("Initial policy for " + str(S0) + ": " + str(policy[S0]))

    breakLoop = False
    
    for i in range(0, N):
        
        for S in stateSpace:
            
            (c, s) = S
            (d, t) = policy[S]
            V[S] = R(c, s, d, t) + Discount * 1. * np.sum(np.array(
                                    [T(c, s, d, t, Sdash[0], Sdash[1]) * V[Sdash] 
                                    for Sdash in stateSpace]))
        
        for S in stateSpace:
            
            Qpi = V[S]
            (c, s) = S            
            actions = valid_actions(S)
            total = []
            
            for a in actions:
                
                (d, t) = a
                expected = 0 
                
                for Sdash in stateSpace:
                                        
                    (sdash, cdash) = Sdash
                    
                    expected += Discount * 1. * T(c, s, d, t, cdash, sdash) * V[Sdash]
                    
                total.append(R(c, s, d, t) + expected)   
            
            id = np.argmax(np.array(total), axis = 0)
            QpiDash[S] = total[id]   #Total reward of maximised action
            
            #Check for convergence: pi
            if policy[S] == actions[id] and S == S0:

                print("Policy converged to optimal policy")
                breakLoop = True
                break
                        
            elif QpiDash[S] > Qpi:
                
                policy[S] = actions[id]
                Qpi = QpiDash[S]
        
        if breakLoop:
            
            break
    
    return QpiDash, policy
