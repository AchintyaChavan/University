'''
Created on 1 Aug. 2017

@author: AC

python "H:\\Documents\\Achintya\\UQ\\Engineering\\5th Year\\Sem 2 2017\\COMP3702\\Practicals\\Prac1_1_Cat.py"

test1 = "H:\\Documents\\Achintya\\pwd_gen.py"
test2 = "H:\\Documents\\Achintya\\test.txt"

'''

import argparse
import sys
import shutil



def cat(filename):
    
    with open(filename, "r") as f:
        
#         print(f.read())
        sys.stdout.write('\n'+ str(f.read()) + '\n')
#         shutil.copyfileobj(f, sys.stdout)

def record(filename):
    
    
    with open(filename, "w") as f:
            
        for line in sys.stdin:
                
            f.write(line)
               


def main():
       
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help = "action to perform: cat or record")
    parser.add_argument("filename", help = "filename")
    args = parser.parse_args()
     
    if args.action == "cat":
        cat(args.filename)
    elif args.action == "record":
        sys.stdout.write('Recording' + '\n')
        record(args.filename)
      
    return 0;

if __name__ == "__main__":
    main()
    