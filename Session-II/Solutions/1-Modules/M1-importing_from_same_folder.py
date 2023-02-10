""" 
# Project: Python Bootcamp - Session II
# File: M1-importing_from_same_folder.py
# Description: In this exercise we will understand and use our own module and import it from same folder.
#              Doing so in the process we will try to understand the difference in import, from import and
#              meaning of __name__ listed in dir().
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# 1. Two Ways to import a module  -do not uncomment below, unless mentioned.
# 1.1 import M0_math_functions
# 1.2 from M0_math_functions import *
# 1.3 import understanding_imports

# 1.1 Using import to use module - uncomment below 3 lines to run
# import M0_math_functions
# print(M0_math_functions.add(10,20))
# print(dir(M0_math_functions))

# 1.2. Using from import to use module/part of module - uncomment below 3 lines to run
# from M0_math_functions import *
# print(sub(10,20))
# print(dir()) # no need to mention module name as done in 1.1

# 1.3 Understanding imports - uncomment below 3 lines to run
import understanding_imports
print(dir(understanding_imports))
print(f"Executed file: Module's Name: '{__name__}'")


# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of classes and objects.

# 1.1
# import :  imports an entire code library.
# Use import when you want to use multiple members of the module.
# dir() function returns 'all properties' and 'methods' of the specified object/module, without the values.

# 1.2
# from import : imports a specific member or members of the library.
# Using from import can save us from repeating the module name, when we need to use it in our code many times.

# 1.3
# Value of '__name__' will tell if the module name. 
# This will also help in knowing if the module is executed directly or is being imported in another file.

'''