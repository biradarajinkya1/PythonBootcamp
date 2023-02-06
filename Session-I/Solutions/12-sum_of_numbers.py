""" 
# Project: Python Bootcamp - Session I
# File: 12-sum_of_numbers.py
# Description: In this exercise we will understand/use of for loop and range. Use of range is shown below:
                for number in range(start,end,step)
                    print(number)
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""
import pytictoc
from pytictoc import TicToc

t = TicToc() #create instance of class
t.tic() #Start timer

# num = int(input("Enter number to get addition all numbers from 0 to entered number: "))
num = 1000
# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.

total = 0
for number in range(1, num+1):
	total += number
    
#for(i=0, i>num, i++) {}

# Write your code above this line
# =================================
# Do not change the code below
print(f"Sum of numbers from 0 to {num} is : {total}")
t.toc() #end timer

'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote

#1 - Using sum and range methods
print(f"Sum of even numbers from 0 to {num} is :{sum(range(0, num+1))}")

'''