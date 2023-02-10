""" 
# Project: Python Bootcamp - Session II
# File: 6-class_with_variables.py
# Description: In this exercise we will understand and use 2 of most used OOPs concepts Class and Object.
#              Here we will create a very simple class with one or two variables - create their objects and
#              change default values and tehn print them to see them taking effect. 
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# Create Player class with 2 variables name and age - initialize to any value of your choice.
# Create 1 or more objects of the class and change the default value and print them.

class player:
    # class attribute
    name = ""
    age = 0

# create player object player1
player1 = player()
player1.name = "Virat"
player1.age = 10

# create another player object player2
player2 = player()
player2.name = "Rohit"
player2.age = 15

# access attributes
print(f"{player1.name} is {player1.age} years old")
print(f"{player2.name} is {player2.age} years old")

#Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.

# Prime difference between Class and Object is - 
# Object is an instance of a class.
# All data/variables/functions i.e. members of the class can be accessed with the help of objects.
# No memory will be allocated on defining a class, it will only be allocated on instantiation i.e. object createation.

'''