""" 
# Project: Python Bootcamp - Session II
# File: 9-inheritance_basic.py
# Description: In this exercise we will understand and use one of OOPs concepts inheritance.
#              Here we will create 2/3 classes - 1 parent and 1/2 child --> where child class will inherit the properties of parent class.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# Parent/Base class
class Animal:

    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

# Child/Derived class
class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# child class
class Snake(Animal):

    def hiss(self):
        print("I am snake. I make Hiss sound, when messed around!!")

# Create object of the Dog class and calling members of the base & derived class
dog1 = Dog()
dog1.eat()
dog1.sleep()
dog1.bark()

# Create object of Snake class and calling members of Parent and Child class
snake1 = Snake()
snake.eat()
snake.sleep()
snake.hiss()


# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.

# Inheritance - to understand this by analogy - 
# All children of humanbeings inherit some innet features from parents like - hair, skintone, nose, lips, property etc.
# Same way Inheritance works - child class interits properties of parent class.
# Here syntactically we mention Parent class name as an argument while defining child class.

'''