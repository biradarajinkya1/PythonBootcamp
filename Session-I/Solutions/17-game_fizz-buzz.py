""" 
# Project: Python Bootcamp - Session I
# File: 17-game_fizz-buzz.py
# Description: In this exercise we will understand/use confitional statements if, else and nested if setatements and time module.
               Rules of game:
                1. start counting from 1 
                2. everytime a number fully divisible by 3 comes - say fizz
                3. everytime a number fully divisible by 5 comes - say buzz
                4. everytime a number fully divisible by both 3&5 comes - say FizzBuzz
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""
# import time module to give delay at start of every iteration in loop, to see the loop progressing.

import time

number = int(input("Welcome to Fizz-Buzz.\nTill what number should we count? "))

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.

for number in range(1, number):
    time.sleep(0.2)
    if number % 3 == 0 and number % 5 == 0:
		#Divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:
		#Divisible by 3
        print("Fizz")
    elif number % 5 == 0:
		#Divisible by 5
        print("Buzz")
    else:
        print(number)

# Write your code above this line
# =================================
# Do not change the code below
print(f"")


'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote
 
'''