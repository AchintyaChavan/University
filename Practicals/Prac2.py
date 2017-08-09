'''
Created on 9 Aug. 2017

@author: AC

python "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Practicals\\Prac1_3.py"

'''

import argparse
import sys
import time

from puzzle import Puzzle
import searchsolver

initial = "1348627_5"
final = "1238_4765"

def main():
       
#     parser = argparse.ArgumentParser()
#     parser.add_argument("solver", help = "search algorithms to use")
#     parser.add_argument("state1", help = "initial state")
#     parser.add_argument("state2", help = "final state")
#     args = parser.parse_args()
#
    t1 = time.time()

#     if args.action == "bfs":
#         moves, queries = searchsolver.breadth_first_search(args.state1, args.state2)
#     elif args.action == "dfs":
#         moves, queries = searchsolver.depth_first_search(args.state1, args.state2)    
    
    moves, queries = searchsolver.breadth_first_search(list(initial), list(final))
    
    t2 = time.time()
    
    sys.stdout.write('\n' + str(moves))
    sys.stdout.write('\n' 'Minimum moves: ' + str(len(moves)))
    sys.stdout.write('\n' 'Nodes searched: ' + str(queries))
    sys.stdout.write('\n' 'Time taken (s): ' + str(t2 - t1) + '\n')
    
    return 0;

if __name__ == "__main__":
    main()