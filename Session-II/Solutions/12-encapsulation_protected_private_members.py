""" 
# Project: Python Bootcamp - Session II
# File: 12-encapsulation_protected_private_members.py
# Description: In this exercise we will understand and use 2 of most used OOPs concepts class and encapsulation - 
#              vatiables with prefixed single/double underscore - Protected and Private variables.
#              Here we will create a simple class with __init__ function - declare some variables(prefixed with _/__) in the same 
#              and try to change the variable default value in another function in same class.
#              Also create a child class and try to change Protected and Private member values and observe.
#              More/different ways/explaination to deal with this will be explained in commented code below. 
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

class Car:
    def __init__(self):
        self.color = "red"
        self._speed = 70
        self.__brand = "bmw"
        
    def func2(self):
        self._speed = 90
        print(f"Value of Protected _speed variable after change - inside Car class' method: {self._speed}")

# Creating Object of class Car
car1 = Car()

print(f"Original Car class{dir(car1)}")
# print("\n")
print(f"\nValue of Protected _speed variable before change - Car class: {car1._speed}")
car1.func2()
# Modifying Protected _speed variable outside class
car1._speed = 100
print(f"Value of Protected _speed variable after change - outside Car class: {car1._speed}\n")

# Modifying Private __brand variable outside class 
car1.__brand = "abcd"
print(f"After tring to modify Private __brand variable of Car class{dir(car1)}")
# If we observe output of Dir - above change has created a new variable with "__brand" as name.
# also if we observe the output of Prints of below variables it will make it clear that original __brand variable is still intact.
print(f"\nValue of Private '__brand' variable after change: {car1.__brand}")
print(f"Value of Original Private '_Car__brand' variable: {car1._Car__brand}\n")



class ExtendedCar(Car):
    def __init__(self):
        # Calling constructor of Car class (Parent class)
        Car.__init__(self)
        # Modifying the Variables
        self.color = "green"
        self._speed = 80
        self.__brand = "audi"
        
extended_car = ExtendedCar()
print(f"\nOriginal extended_car class{dir(extended_car)}")

print(f"\nValue of Original Private '_Car__brand' variable - ExtendedCar class: {extended_car._Car__brand}")
print(f"Value of Original Private '_ExtendedCar__brand' variable - ExtendedCar class: {extended_car._ExtendedCar__brand}")



# Write your code above this line
# =================================
# Do not change the code below


'''
# Alternet ways / elaboration of classes and objects.
# Without Calling constructor of Car class (Parent class) we will get Attribute error.
#        Car.__init__(self)
#
'''