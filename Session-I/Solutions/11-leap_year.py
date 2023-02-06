""" 
# Project: Python Bootcamp - Session I
# File: 11-leap_year.py
# Description: In this exercise we will understand/use confitional statements if, else and nested if setatements.
               Conditions:
                1. Any year that is evenly divisible by 4 is a leap year
                2. If evenly divisible by 100 - leap only if evenly divisible by 400 as well.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

year = int(input("Which year do you want to check? "))

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")	


# Write your code above this line
# =================================
# Do not change the code below
print(f"")


'''
# Alternet ways
# Using conditional statements and logical operators.
# Use: Replace below Block of code with the one you wrote

# 1
  if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):   
    print("Given Year is a leap Year");  
  else:  
    print ("Given Year is not a leap Year") 
'''