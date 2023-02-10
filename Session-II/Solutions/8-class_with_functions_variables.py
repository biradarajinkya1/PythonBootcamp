""" 
# Project: Python Bootcamp - Session II
# File: 8-class_with_functions_variables.py
# Description: In this exercise we will understand and use 2 of most used OOPs concepts Class and Object.
#              Here we will create a simple class with few functions doing basic math operations and init vairiables.
#              Pass the variables to the class inseted of functions inside the class and then do the math operations on passed variables.
#              Do take input from user for values and also try to use __name__ special variable.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# Implement default constructor and parameterized constructor

class Arithmatic:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    
    def add(self):
        return self.var1 + self.var2
    
    def substract(self):
        return self.var1 - self.var2
    
    def divide(self):
        return self.var1 // self.var2
    
    def multiply(self):
        return self.var1 * self.var2

    
if __name__ == "__main__":
    input_var = input("Enter 2 integers to do mathematical operations saperated by space: ")
    x = int(input_var.split(" ")[0])
    y = int(input_var.split(" ")[1])
    
    calc = Arithmatic(x, y)
    
    addition = calc.add()
    substraction = calc.substract()
    multiplication = calc.multiply()
    division = calc.divide()
    print(f" Addition is :{addition}\n Substraction is :{substraction}\n Multiplication is :{multiplication}\n Division is :{division}\n")


# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.

# When we mention passing values to a class - we use __init__ function inside class to accept the variables passed.
# Do not pass the values to class (syntactically) as we pass values to functions directly -- __init__ function will do the job for a class.
# We will encounter error if we syntactically mention variables while defining the class.
# The variables passed to a class in __init__ can be accessed with self prefix across the class in different functions.

'''
