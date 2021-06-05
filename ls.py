# Implementation of the ls command
# Date June 5, 2021
# Author : kobi-ed

import os
import sys

def checkArguments():
    '''Check if the user passed in 
    arguments to the program.
    Returns boolean'''
    if len(sys.argv) > 1:
        return True
    return False

def showAvailableFolder():
    '''Check if passed in argument is a
    valid folder which exists in 
    current path. Returns boolean'''
    # If user passes in arguments
    # check if argument is a folder
    if checkArguments():
        for arg in sys.argv[1:]:
            if os.path.isdir(arg):
                if len(sys.argv[1:]) == 1:
                    print('   '.join(os.listdir(arg)))
                elif len(sys.argv[1:]) > 1:
                    print(arg + '\n' + '  '.join(os.listdir(arg)) + '\n')
    elif checkArguments() == False:
        if os.path.isdir('.'):
            print('  '.join(os.listdir('.')[1:]))
    else:
        print("File or directory not found!")

if __name__ == "__main__":
    showAvailableFolder()
