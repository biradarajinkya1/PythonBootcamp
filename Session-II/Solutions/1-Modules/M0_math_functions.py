""" 
# Project: Python Bootcamp - Session II
# File: math_functions.py
# Description: In this exercise we will understand how to create our own module/package which can be used in other programs
#              via importing.
#              More/different ways/explaination to understand this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

def add(a,b):
    # print(f"Module's Name: {__name__}")
    return a+b
    
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b
    

# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.

# Simplest way to create own module is to write functions 
# without any other peace of code outside functions/ __main__ module call.

'''