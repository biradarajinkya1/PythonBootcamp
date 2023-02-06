""" 
# Project: Python Bootcamp - Session I
# File: 3-BMI_calculator.py
# Description: In this exercise we will calaulate Body Mass Index - BMI using the mathematical operators we overviewed.
#              For this program use this Formula for BMI: Weight/Height^2 – weight in kg and height in m
#              More ways to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# Do not change the code above
# =================================
#Write your code below

# The inputs taken will be strings so need to convert them in float
height_float = float(height)
weight_float = float(weight)

BMI = weight_float/(height_float**2)

#Write your code above this line
# =================================
# Do not change the code below
print(f"Your BMI is: {BMI}")


'''
# Alternet ways
# Here we have consolidated multiple lines of code into one line.
# Use: Replace below Block of code with the one you wrote

print("Your BMI is: " + str(float(weight)/(float(height)**2)))

'''