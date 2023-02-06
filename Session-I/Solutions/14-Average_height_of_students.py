""" 
# Project: Python Bootcamp - Session I
# File: 14-Average_height_of_students.py
# Description: In this exercise we will understand/use of for loop.
               Conditions:
               1. Do not use len and sum function to understand how len and sum function work under the hood.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

student_heights = input("Input a list of student heights ").split()
for n in range (0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
print(student_heights)

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.
	
total_height = 0
for height in student_heights:
	total_height += height
print(f"Total height of all students: {total_height}")

number_of_students = 0
for student in student_heights:
	number_of_students += 1
print(f"Total number of students: {number_of_students}")

average_height = round(total_height / number_of_students)

# Write your code above this line
# =================================
# Do not change the code below
print(f"The Average Height of the class is: {average_height}")


'''
# Alternet ways
# 
# Use: Replace below Block of code with the one you wrote

#1 - Merging 2 for loops into one and not using len and sum functions.
total_height = 0
number_of_students = 0
for item in student_heights:
	total_height += item
    number_of_students += 1
print(f"Total height of all students: {total_height}")
print(f"Total number of students: {number_of_students}")

averaege_height = round(total_height / number_of_students)

#2 - Using len and sum function.
total_height = sum(student_heights)
number_of_students = len(student_heights)
averaege_height = round(total_height / number_of_students)
print(average_height)

'''