""" 
# Project: Python Bootcamp - Session II
# File: 1-functions_basic.py
# Description: In this exercise we will understand/use functions with simple mathematical operations - +, -, *, /.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# user input
num1 = int(input("Enter a number 1 to perfrom mathematical operations: "))
num2 = int(input("Enter a number 1 to perfrom mathematical operations: "))

# Do not change the code above
# =================================
# Write your code below
def add(a, b):
    return a+b
    
def sub(a, b):
    return a-b
    
def mult(a, b):
    return a*b

def div(a, b):
    return a/b

# Write your code above this line
# =================================
# Do not change the code below
 
print(f"addition is {add(num1,num2)}")
print(f"Substraction is {sub(num1,num2)}")
print(f"Multiplication is {mult(num1,num2)}")
print(f"Division is {div(num1,num2)}")



'''
# Alternet ways / elaboration of functions

1. Using one more variable to contain the result of operation and returning that.
def add(a, b):
    c = a + b
    return c
    
'''