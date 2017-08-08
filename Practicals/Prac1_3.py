'''
Created on 6 Aug. 2017

@author: AC

python "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Practicals\\Prac1_3.py"

'''

import argparse
import sys
import shutil

def direction(x):  
    
    return {
        -3: 'U',
         3: 'D',
        -1: 'L',
         1: 'R'
    }.get(x, 'Impossible');

def action8(initial, final):
    
    i = initial.find('_')
    j = final.find('_')
    
    diff = j - i
    
#     print(i, j, diff)
    sys.stdout.write('\n'+ str(direction(diff)) + '\n')
    
def main():
       
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help = "action to perform: cat or record")
    parser.add_argument("state1", help = "initial state")
    parser.add_argument("state2", help = "final state")
    args = parser.parse_args()
     
    if args.action == "which_action":
        action8(args.state1, args.state2)
    elif args.action == "sequence":
        sequence8(args.state1, args.state2)
        
    return 0;

if __name__ == "__main__":
    main()