""" 
# Project: Python Bootcamp - Session II
# File: 2-recursion_factorial.py
# Description: In this exercise we will understand/use recursive functions with simple factorial operation.
#              Do check if the passed value is valid input or not.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# user input
num = input("Enter a number of which factorial is to be found: ")

# Do not change the code above
# =================================
# Write your code below

# Recursive function
def recursive_factorial(n):
  if n == 1:
      return n
  else:
      return n * recursive_factorial(n-1)
 
# check if the input is valid or not
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", num, "=", recursive_factorial(num))

# Write your code above this line
# =================================
# Do not change the code below


'''
# Alternet ways / elaboration of factorail recursion

#5 ! = 5x4x3x2x1 = 24 * 5 = 120
# 5 * ( 4 * (3 * (2 * (1))))
# 5 * ( 4 * (3 * (2)))
# 5 * ( 4 * 6)
# 5 * ( 24)
# 120

'''