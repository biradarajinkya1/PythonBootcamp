""" 
# Project: Python Bootcamp - Session II
# File: 10-encapsulation_protected_members.py
# Description: In this exercise we will understand and use one of OOPs concepts encapsulation - more
#              specifically Protected members and accessing them.
#              More/different ways/explaination to understand encapsulation is given in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

# Creating a Parent class
class Bank:
    def __init__(self):
 
        # Protected member
        self._amount = 500_000_000
 
# Creating a Child class
class cred(Bank):
    def __init__(self):
 
        # Calling constructor of Bank class (Parent class)

        Bank.__init__(self)
        print("Calling protected member of base class: ", self._amount)
 
        # Modify the protected variable:
        self._amount = 100_000_000
        print("Calling modified protected member outside class: ", self._amount)
 
 
obj1 = cred()
obj2 = Bank()
 
# Calling protected member - Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._amount)
 
# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._amount)

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


# Protected members
# Protected members (in C++ and JAVA) are those members of the class that cannot be accessed outside the class 
# but can be accessed from within the class and its subclasses. 
# To accomplish this in Python, just follow the convention by prefixing the name of the member by a single underscore “_”.

# Although the protected variable can be accessed out of the class as well as in the derived class (modified too in derived class), 
# it is customary(convention not a rule) to not access the protected out the class body.

# Calling protected member - Can be accessed but should not be done due to convention
'''