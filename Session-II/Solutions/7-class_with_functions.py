""" 
# Project: Python Bootcamp - Session II
# File: 7-class_with_functions.py
# Description: In this exercise we will understand and use 2 of most used OOPs concepts Class and Object.
#              Here we will create a very simple class with really simple functions doing basic math operations
#              and pass the values as arguments to perform those math opwrations.
#              Do take input from user for values and also try to use __name__ special variable.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# Create a class -Arithmetic with add (), sub(), div(), mul() functions.
# pass the values as arguments and perform the required operations.

class Arithmatic:
    def __init__(self):
        # self.var1 = 0
        # self.var2 = 0
        pass
    
    def add(self, a, b):
        return a+b
    
    def substract(self, a, b):
        return a-b
    
    def divide(self, a, b):
        return a//b
    
    def multiply(self, a, b):
        return a*b

print(dir(Arithmatic))
    
if __name__ == "__main__":
    calc = Arithmatic()
    input_var = input("Enter 2 integers to do mathematical operations saperated by space: ")
    var1 = int(input_var.split(" ")[0])
    var2 = int(input_var.split(" ")[1])
    
    addition = calc.add(var1, var2)
    substraction = calc.substract(var1, var2)
    multiplication = calc.multiply(var1, var2)
    division = calc.divide(var1, var2)
    print(f" Addition is :{addition}\n Substraction is :{substraction}\n Multiplication is :{multiplication}\n Division is :{division}\n")


# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.

# Brief about __name__ as explained in modules program - 
#   Accessing/Printing __name__ variable:.
#       print(__name__)
#   If the python interpreter is running that module (the source file) as the main program, 
#   it sets the special __name__ variable to have a value “__main__”. 
#   If this file is being imported from another module, __name__ will be set to the module’s name. 

'''
    
