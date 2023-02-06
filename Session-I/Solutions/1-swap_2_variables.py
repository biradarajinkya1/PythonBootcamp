""" 
# Project: Python Bootcamp - Session I
# File: 1-swap_2_variables.py
# Description: This exercise is to understand python variables and playing around with them.
#              For this program assume input can be integer, float, string - anything.
#              More ways to deal with variables will be explained in commented code below assuming only int as input.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

a = input("a: ")
b = input("b: ")
# Do not change the code above
# =================================
#Write your code below

c = a
a = b
b = c

#Write your code above this line
# =================================
# Do not change the code below
print("a: " + a)
print("b: " + b)

'''
# Alternet ways
# Assuming input is only integer - using only 2 variables
# Use: Replace below block of code with the one you wrote

# Using + and -
a=5, b=3
a = a+b
b = a-b
a = a-b

# Using EXOR
a ^= b
b ^= a
a ^= b

# Using * and /
a = a * y
y = a / y
x = a / y
'''