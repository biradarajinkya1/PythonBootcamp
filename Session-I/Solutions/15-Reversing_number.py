""" 
# Project: Python Bootcamp - Session I
# File: 15-Reversing_number.py
# Description: In this exercise we will understand/use while loops.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

number = int(input("Enter a number to be reversed? "))

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.

reversed_num = 0
while number != 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10


# Write your code above this line
# =================================
# Do not change the code below
print(f"Reversed Number: {reversed_num}")


'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote

#1 Using string slicing
reversed_num = str(num)[::-1])

#2 Using reversed() on string
 reversed_num = "".join(reversed(str(num)))
 
#3 Using reverse on list
num_list = list(str(num))
num_list.reverse()
reversed_num = "".join(num_list)

#4 Using for loop on str
num = str(num)
# num_list = [num[i] for i in range(len(num)-1, -1, -1)]  # short form of below for loop
for i in range(len(num)-1, -1, -1):
    num_list.append(num[i])
reversed_num =  "".join(num_list)
'''