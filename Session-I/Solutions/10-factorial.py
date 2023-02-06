""" 
# Project: Python Bootcamp - Session I
# File: 10-factorial.py
# Description: In this exercise we will understand/use for loop. Assume input is positive integer.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

Number = int(input('Enter a number: '))

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.
# since 0! and 1 ! is 1 we have initiated fact variable with 1.
# Do assume the input number is a positive integer as factorial for -ve numbers do not exist.

fact = 1
for i in range(2, Number+1):
    fact *= i

# Write your code above this line
# =================================
# Do not change the code below
print(f"Factorial of {Number} is {fact}")


'''
# Alternet ways
# e.g. 6! = 6*5*4*3*2*1 = 720
# Use: Replace below Block of code with the one you wrote - 4 options given.

#1 
if Number < 0:
        fact = 0
    elif Number == 0 or Number == 1:
        fact = 1
    else:
        fact = 1
        while(Number > 1):
            fact *= Number
            Number -= 1
print(f"Factorial of {Number} is {fact}")

# 2
import math
fact = math.factorial(Number)
print(f"Factorial of {Number} is {fact}")

# 3
import numpy
fact = numpy.prod([i for i in range(1,Number+1)])
print(f"Factorial of {Number} is {fact}")

# 4 recursive approach - we will visit this exercise when we learn functions.
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
print(f"Factorial of {Number} is {factorial(Number)}")

'''