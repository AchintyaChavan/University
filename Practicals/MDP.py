'''
Created on 9 Oct. 2017

@author: AC
'''

import numpy as np

P_c = 1/100. * np.array([[3, 2, 2, 1, 2],
                          [3, 2, 2, 1, 2],
                          [3, 2, 2, 1, 2],
                          [3, 2, 2, 1, 2],                                   
                          [3, 2, 2, 1, 2]])

P_s = 1/100. * np.array([[2, 2, 2, 2, 2],
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

    pass

# Reward Function
def R(c, s, d, t):
    
    pc = 0
    lc = 0
    
    ps = 0
    ls = 0
    
    for i in range(1,4):
    
        pc +=  np.min([i, c + d]) * P_c[c + d][i]
        ps +=  np.min([i, s + t]) * P_s[s + t][i]
        
    for j in range(c + d + 1, 4):
        
        lc += (j - c - d) * P_c[c + d][j]
        
    for k in range(s + t + 1, 4):
        
        ls += (k - s - t) * P_s[s + t][k]
    
    return np.float(pc - 0.5 * lc) + np.float(ps - 0.5 * ls)

# Transition Function
def T(c, s, d, t, cs, ss):
    
    Tc = 0
    Ts = 0
    
    #Tc
    if cs > (c + d):
        
        Tc = 0
        
    elif cs == 0:
        
        Tc = sum([P_c[c + d][i] for i in range(c + d, 4)])
    
    else:
        
        Tc = P_c[c + d][c + d - cs]
        
    #sc            
    if ss > (s + t):
        
        Tc = 0
        
    elif ss == 0:
        
        Tc = sum([P_s[s + t][j] for j in range(s + t, 4)])
    
    else:
        
        Tc = P_s[s + t][s + t - ss]
    
    
    return (Tc / 1.) * (Ts / 1.)


def mdp_value_interation(N, V0):
    
    Discount = 0.95
    
    
    return