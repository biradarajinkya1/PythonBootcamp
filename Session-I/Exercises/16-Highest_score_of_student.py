""" 
# Project: Python Bootcamp - Session I
# File: 16-Highest_score_of_student.py
# Description: In this exercise we will understand/use of for loop.
               Conditions:
               1. Do not use max/min function to understand how max / min function work under the hood.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

student_scores = input("Input a list of student scores ").split()
for n in range (0, len(student_scores)):
	student_scores[n] = int(student_scores[n])
print(student_scores)

# Do not change the code above
# =================================
# Write your code below
# Type conversion is done while taking input.




# Write your code above this line
# =================================
# Do not change the code below
print(f"The heigest score in the class is: {heighest_score}")

