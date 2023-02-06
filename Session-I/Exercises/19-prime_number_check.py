""" 
# Project: Python Bootcamp - Session I
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




# Write your code above this line
# =================================
# Do not change the code below
print(f"")
