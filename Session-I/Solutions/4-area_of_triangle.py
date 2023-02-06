""" 
# Project: Python Bootcamp - Session I
# File: 4-area_of_triangle.py
# Description: In this exercise we will calaulate area of a triangle using the mathematical operators and priorities we overviewed.
#              For this program use this Formula for Triangle area : Area = (s(s-a)(s-b)(s-c))^0.5
#              More ways to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""
# Three sides of the triangle is a, b and c:  
a = input('Enter first side: ')  
b = input('Enter second side: ')  
c = input('Enter third side: ')

# Do not change the code above
# =================================
# Write your code below
# Type conversion as all the inputs taken will be strings
a_float = float(a)
b_float = float(b)
c_float = float(c)

# calculate the semi-perimeter  
s = (a_float + b_float + c_float) / 2  
  
# calculate the area  
area = (s*(s-a_float)*(s-b_float)*(s-c_float)) ** 0.5

# Write your code above this line
# =================================
# Do not change the code below
print('The area of the triangle is %0.2f' %area)


'''
# Alternet ways
# Other ways to calculate area using different formulas and inputs are given below
# Use: Replace below Block of code with the one you wrote

# Using base and height as input. Formula : Area = 1/2 * base * height
# Type converting while taking input

base = float(input('Enter Base of Triangle: '))
height = float(input('Enter Height of Triangle: '))

area = 1/2 * base * height
print('The area of the triangle is %0.2f' %area)

# Printing without f-string
#  print(f'The area of the triangle is {area}')
'''