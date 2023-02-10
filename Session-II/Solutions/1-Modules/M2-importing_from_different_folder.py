""" 
# Project: Python Bootcamp - Session II
# File: M2-importing_from_different_folder.py
# Description: In this exercise we will understand and use our own module and import it from different folder.
#              Doing so in the process we will try to understand the role played by __init__.py file.
#              More/different ways/explaination to deal with this will be explained in commented code below.               
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# Different Ways to import a module/submodule  -do not uncomment below, unless mentioned.
# 1. import my_module
# 2. from my_module import *
#      from my_module import first
#      from my_module import second
#      from my_module import first,second
# 3. from my_module.submodule import third
#      from my_module.submodule.third import my_func3

# 1. import module from different folder and call functions from it.
import my_module.first
print(dir())
my_module.first.my_func1()
my_module.first.my_func10()
my_module.second.my_func2()

# 2. import module(s) from different folder and call functions from it.
#####2.1
# from my_module import *
# first.my_func1()
# second.my_func2()
#####2.2
# from my_module import first
# first.my_func1()
#####2.3
# from my_module import second
# first.my_func2()
#####2.4
# from my_module.first import my_func1
# my_func1()
#####2.5
# from my_module import first,second
# print(dir())
# first.my_func1()
# second.my_func2()

# 3. Import Submodule(s) and  Call functions from it
#####3.1
# import my_module.submodule
# my_module.submodule.third.my_func3()
#####3.2
# from my_module import submodule
# submodule.third.my_func3()
#####3.3
# from my_module.submodule import third
# third.my_func3()
#####3.4
from my_module.submodule.third import my_func3
my_func3()
# my_func30()  # add in __init__.py file and import here as well along with my_func3 and then execute.


# Write your code above this line
# =================================
# Do not change the code below

'''
# Alternet ways / elaboration of modules and submodules calling from differner folder.

We can import complete module/submodule, one/multiple files from a module/submodule, required functions from module/submodule.
Refer below explaination for bettet understanding.

# 1. import my_module                      # importing the complete module
# As seen in M1-importing_from_same_folder.py - this will import everything from 'my_module' folder, but there is a catch.
# It will not always work when there are more than 1 files inside the module. 
# 1.1 empty: __init__.py 
#           This scenario will work fine as long as there is only one file in the module with any number of functions.
#           Soon we add more files - other files will not be easily accessible- by just importing it and keeping __init__.py file empty.
# 1.2 properly written : __init__.py
#           For module with multiple files to work - we need to fill __init__.py file with proper details for the calling/importing 
#           file to know the available files and functions inside the files to use. 
#           Refer __init__.py files from module and submodule folders for correct syntax.

# 2. from my_module import *                # importing everything from the module
#      from my_module import first          # importing only 1 file from the module
#      from my_module import second         # importing only 1 file from the module
#      from my_module import first,second   # importing multiple files from the module

# 3. from my_module.submodule import third             # importing only 1 file from the module
#      from my_module.submodule.third import my_func3  # importing only required function from the file from submodule

'''