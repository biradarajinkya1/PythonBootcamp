""" 
# Project: Python Bootcamp - Session II
# File: 19-prime_number_check.py
# Description: In this exercise we will understand/use 
                    1. conditional statements if, else and nested if setatements or 
                    2. for else statements and 
                    3. use of flags and break statement.
               Conditions:
                1. Prime number: A positive integer greater than 1 which has no other factors except 1 and the number itself is called a prime number
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

num = int(input("Enter a number to check for prime: "))

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.
# The idea to solve this problem is to iterate through all the numbers starting from 2 to (N/2) using a for loop 
# and for every number check if it divides N. If we find any number that divides, we return false. 
# If we did not find any number between 2 and N/2 which divides N then it means that N is prime and we will return True.


if num > 1:
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

# Write your code above this line
# =================================
# Do not change the code below
print(f"")


'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote
 
#1  Instead of checking till n, we can check till √n because a larger factor of n must be a multiple of a smaller factor 
    that has been already checked. Now let’s see the code for the first optimization method ( i.e. checking till √n )
    
# just add below imoprt at start of the file 
from math import sqrt
 
# this flag maintains status whether the num is prime or not
prime_flag = 0
 
if(num > 1):
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is a not prime number")
    
'''