'''
Created on 9 Oct. 2017

@author: AC
'''

import MDP

def main():
    
    R0 = (0, 0)
    Discount = 0.95
    N = 2
    
    MDP.mdp_value_interation(N, R0, Discount)
#     MDP.test()
    
    return 0

if __name__ == "__main__":
    main()