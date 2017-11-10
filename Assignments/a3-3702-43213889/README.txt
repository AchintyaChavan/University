%%% Readme %%%

Following assignment is done on the Python 2.7 programming language
Ensure the compiler is of Version 2.7. If the environment has both Python 
2 and 3 then rename the Python 3 executable ('python.exe') in C drive to 
'python3.exe' thus ensuring the Python 2.7 interpreter is used instead.

Compilation Code
python a3-3702-[ID]>.py  <inputFileName> <outputFileName>

Input files should be copied into the working folder as the script will
automatically read these files within the working directory 
(no need to have directory path for input files).

Similarly the output file will be automatically stored in the working
directory of the script file.

Example
If the current working directory is set to U:\\COMP3702\\Ass3 then 

python a3-3702-[ID].py input1.txt output1.txt

will read the file "input1.txt" from the folder U:\\COMP3702\\Ass3 and save the
solutions in output1.txt which will be stored in U:\\COMP3702\\Ass3 aswell. 



PARAMETERS THAT CAN BE ALTERED in a3-3702-[ID].py script (main file)
Line 18: Number of simulations to run (default value is 1)
Line 62: Set verbose to False to block printing of fortnightly results (default is True)
		 Useful if the number of simulations is big and need to stop printing everytime.