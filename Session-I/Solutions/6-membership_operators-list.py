""" 
# Project: Python Bootcamp - Session I
# File: 6-membership_operators-list.py
# Description: In this exercise we will understand membership operators operated on lists.
#              Membership operators: in, not in
#              More/different ways to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

List_of_fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Strawberry', 'Raspberry']
print(f"\n Here is list of fruits: {List_of_fruits} \n") 
fruit = input('Enter a fruit of your choice: ') 

# Do not change the code above
# =================================
# Write your code below
# No type conversion needed as we are checking small string as part of longer string.

check = fruit in List_of_fruits

# Write your code above this line
# =================================
# Do not change the code below
print(f"\nFruit of your choice ({fruit}) is there in List of fruits ({List_of_fruits}): {check}")


'''
# Alternet ways
# An issue one might notice is if you enter State of matter in ALL CAPS or all small letters.
# the membership operator returns False
# we can use .lower() or .upper() to tackle such case sensitive scenarios - for lists we need to loop through each element in list.

# Use: Replace below Block of code with the one you wrote

# Use of : not in 
check1 = fruit not in List_of_fruits
print(f"\nFruit of your choice ({fruit}) is there in List of fruits ({List_of_fruits}): {check}")

# Case sensitive check - I: (any of lower(), upper(), capitalize() can be used)
for f in enumerate(List_of_fruits):
    List_of_fruits[index] = f.lower()
check2 = fruit not in List_of_fruits
print(f"\nFruit of your choice ({fruit}) is there in List of fruits ({List_of_fruits}): {check}")
    
# Case sensitive check - II: (any of lower(), upper(), capitalize() can be used)
List_of_fruits_lower = [x.lower() for x in List_of_fruits]
check3 = fruit in List_of_fruits
print(f"\nFruit of your choice ({fruit}) is there in List of fruits ({List_of_fruits}): {check}")
'''