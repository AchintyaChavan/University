'''
Created on 9 Aug. 2017

@author: AC

python "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Practicals\\Prac1_3.py"

'''

import argparse
import sys

from puzzle import Puzzle

initial = "1348627_5"
final = "1238_4765"



def mybfs(initial, final):
    
    sys.stdout.write('\n'+ str(1) + '\n')

def main():
       
#     parser = argparse.ArgumentParser()
#     parser.add_argument("action", help = "action to perform: cat or record")
#     parser.add_argument("state1", help = "initial state")
#     parser.add_argument("state2", help = "final state")
#     args = parser.parse_args()
#      
#     if args.action == "bfs":
#         mybfs(args.state1, args.state2)
#     elif args.action == "dfs":
#         sequence8(args.state1, args.state2)

    a = Puzzle(initial)
    print(a.puzzle,'\n', a.up())
    
        
    return 0;

if __name__ == "__main__":
    main()