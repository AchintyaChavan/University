'''
Created on 9 Oct. 2017

@author: AC
'''

import MDP

def main():
    
    R0 = (0, 0)
    Discount = 0.95
    N = 2
    
    V, action = MDP.mdp_value_interation(N, R0, Discount)
    
    print("Optimal Action for " + str(R0) + ": " + str(action[R0]))
    print("Total reward: " + str(V[R0]))
    
    return 0

if __name__ == "__main__":
    main()