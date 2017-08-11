'''
Created on 9 Aug. 2017

@author: AC

python "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Practicals\\Prac2.py bfs 12436578_ 12345687_"

'''

import argparse
import sys
import time

from puzzle import Puzzle
import searchsolver as ss

initial = "1348627_5"
final   = "1238_4765"

def main():
       
#     parser = argparse.ArgumentParser()
#     parser.add_argument("solver", help = "search algorithms to use")
#     parser.add_argument("state1", help = "initial state")
#     parser.add_argument("state2", help = "final state")
#     args = parser.parse_args()
    
#     print(list(args.state1), args.state2)
    
#     p1 = ss.parity_check(list(args.state1))
#     p2 = ss.parity_check(list(args.state2))

    p1 = ss.parity_check(list(initial))
    p2 = ss.parity_check(list(final))

    if (p1 + p2) % 2 > 0:
        
        sys.stdout.write('\n' + 'No solution found: Odd parities' + '\n')
        
    else:      

        t1 = time.time()
        
        moves, sequence = ss.breadth_first_search(list(initial), list(final))
         
#         if args.solver == 'bfs':            
#             moves, sequence = ss.breadth_first_search(list(args.state1), list(args.state2))
#         
#         elif args.action == "dfs":
#             moves, sequence = ss.depth_first_search(list(args.state1), list(args.state2))
    
        t2 = time.time()
  
        sys.stdout.write('\n' + 'Minimum moves: ' + str(len(moves)))
         
        sys.stdout.write('\n ' +  '   ' + str(list(initial)))
         
        for i in range(len(sequence)): 
              
            sys.stdout.write('\n' + str(moves[i]) + '-> ' + str(sequence[i]))
 
        sys.stdout.write('\n' 'Time taken (s): ' + str(t2 - t1) + '\n')
    
    return 0;

if __name__ == "__main__":
    main()