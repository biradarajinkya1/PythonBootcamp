""" 
# Project: Python Bootcamp - Session II
# File: 11-encapsulation_private_members.py
# Description: In this exercise we will understand and use one of OOPs concepts encapsulation - more
#              specifically Private members and accessing them.
#              More/different ways/explaination to understand encapsulation is given in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
print("Calling the sell function before making any changes")
c.sell()

# change the price
# print(f"Max price is {c.__maxprice}")  
# ^ this throws Attribute error as we are trying to access Private variable outside of the class.
print("Calling the sell function after making changes, but outside the class")
c.__maxprice = 1000
c.sell()
# ^ above modification of the Private Variable won't take effect for the same reason of accessing it outside of the class.
# It won't throw any error though.

# Modifying the Private variable using a method/function inside the class
print("Calling the sell function after making changes, outside the class - but using function from same class")
c.setMaxPrice(1000)
c.sell()

print(dir(c))
# The dir() function returns all properties and methods of the specified object, without the values.
# This function will return all the properties and methods, even built-in properties which are default for all object.

print("Calling the sell function after making changes, outside the class - using ")
c._Computer__maxprice = 5000
c.sell()

# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.
# Original Credit - GeekforGeeks and Stack overflow.

# Encapsulation: 
# It describes the idea of wrapping data and the methods that work on data within one unit. 
# This puts restrictions on accessing variables and methods directly and can prevent 
# the accidental modification of data. To prevent accidental change, an object’s variable can only be 
# changed by an object’s method. Those types of variables are known as private variables.


# Private members
# Private members are similar to protected members, the difference is that the class members declared private 
# should neither be accessed outside the class nor by any base class. 
# In Python, there is no existence of Private instance variables that cannot be accessed except inside a class.

# However, to define a private member prefix the member name with double underscore “__”.

# Private attributes are not protected by the Python system. That is by design.
# Private attributes will be masked. The reason is, that there should be no clashes in the inheritance chain. 
# The masking is done by some implicit renaming. Private attributes will have the real name
#             "_<className>__<attributeName>"

# Thats how mangling is done in Python to access Ptivate variables/members.
'''