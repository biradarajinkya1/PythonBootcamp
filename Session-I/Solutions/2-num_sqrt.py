""" 
# Project: Python Bootcamp - Session I
# File: 2-num_sqrt.py
# Description: This exercise is to understand/use few mathematical operators and f-strings.
#              For this program assume input is a positive integer.
#              More ways to deal with this will be explained in commented code below using math module.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

a = input("a: ")
# Do not change the code above
# =================================
#Write your code below

sqrt_a = int(a) ** 0.5

#Write your code above this line
# =================================
# Do not change the code below
print(f"Square root of {a} is : {sqrt_a} ")


'''
# Alternet ways
# Assuming input is only +ve integer - using math module
# Use: Replace below block of code with the one you wrote

# add below line at the start of file.

import math

# add below line in code section

sqrt_a = math.sqrt(a)

Alternatively you can use below %d, %f operators insted of f strings to limit fraction part to 3 deimals.
print("Square root of %d is %0.3f"%(a ,sqrt_a))

Built in Math functions:
min()
max()
abs()
pow()

Math module:
math.sqrt()
math.ceil()
math.floor()
math.pi
etc
complete reference
https://www.w3schools.com/python/module_math.asp

To list all functions available inside a module/package
>>> import math
>>> dir(math)

'''