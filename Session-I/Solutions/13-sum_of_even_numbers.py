""" 
# Project: Python Bootcamp - Session I
# File: 12-sum_of_even_numbers.py
# Description: In this exercise we will understand/use of for loop and range. Use of range is shown below:
                for number in range(start,end,step)
                    print(number)
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

num = int(input("Enter number to get addition all Even numbers from 0 to entered number: "))

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.
# Using step argument of range().

total = 0
for number in range(2, num+1, 2):
	total += number

# Write your code above this line
# =================================
# Do not change the code below
print(f"Sum of even numbers from 0 to {num} is : {total}")


'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote

#1 - Using mathematical operators and comparison operators. 
total1 = 0
for number in range(2, number+1):
	if number%2 == 0:
		total1 += number
print(total1)

#2 - Using sum and range methods
print(f"Sum of even numbers from 0 to {num} is :{sum(range(0, num+1, 2))}")
'''