""" 
# Project: Python Bootcamp - Session II
# File: 3-recursion_fibonacci.py
# Description: In this exercise we will understand/use recursive functions with fibonacci operation.
#              Do check if the passed number of terms is valid input or not.
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
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms): # [0,1,2,3,4,5,6,7,8,9]
    val = recursive_fibonacci(i)
    if val>20:
        break
    else: 
        print(val)

# Write your code above this line
# =================================
# Do not change the code below

print(recursive_fibonacci(15))

'''
# Alternet ways / elaboration of factorail recursion

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 1 - control no of terms to 8 
# 2 - number getting calculated - < 20 
# 0 1 (1+0=1) ((1+0)+ (1) = 2) (2+1 = 3) (3+ 2 = 5) (5+3 = 8)   (8 + 5 = 13)
# 0 1    2          3              4         5          6            7 

'''