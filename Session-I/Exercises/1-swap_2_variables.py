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

'''
a = int(a) # --> '5' -> 5
b = int(b)

b = a + b # --> b = 8
a = b - a # --> a = 8 - 3 = 5
b = b - a # --> b = 8 - 5 = 3
'''

c = a 
a = b
b = c

#Write your code above this line
# =================================
# Do not change the code below
print("a: " + str(a))
print("b: " + str(b))