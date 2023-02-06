""" 
# Project: Python Bootcamp - Session I
# File: 5-membership_operators-string.py
# Description: In this exercise we will understand membership operators operated on strings - also use/importance of upper(), lower().
#              Membership operators: in, not in
#              More/different ways to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

states_of_matter = 'Solid, Liquid, Gas'
print(f"\nStates of matter are: {states_of_matter} \n") 
state_of_orange = input('What is the Material State of an Orange: ')  

# Do not change the code above
# =================================
# Write your code below
# No type conversion needed as we are checking small string as part of longer string.

check = state_of_orange in states_of_matter

# Write your code above this line
# =================================
# Do not change the code below
print(f"State of Orange is in '{states_of_matter}': {check}")


'''
# Alternet ways
# An issue one might notice is if you enter State of matter in ALL CAPS or all small letters.
# the membership operator returns False
# we can use .lower() or .upper() to tackle such case sensitive scenarios.

# Use: Replace below Block of code with the one you wrote

check1 = state_of_orange.lower() in states_of_matter.lower()
print(f"State of Orange is in '{states_of_matter}': {check1}")

check2 = state_of_orange.upper() in states_of_matter.upper()
print(f"State of Orange is in '{states_of_matter}': {check1}")

check3 = state_of_orange.capitalize() in states_of_matter
print(f"State of Orange is in '{states_of_matter}': {check1}")
Note: method capitalize() only capitalizes 1st letter in string - use with caution.
'''