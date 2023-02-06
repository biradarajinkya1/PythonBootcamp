""" 
# Project: Python Bootcamp - Session I
# File: 8-math_tables.py
# Description: In this exercise we will understand/use bitwise operators to create 7's table.
#              Bitwise operators: &, |, ^, ~, <<, >>
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

print("Printing 7's table: \n") 

# Do not change the code above
# =================================
# Write your code below
# No type conversion needed as we are checking small string as part of longer string.

table = []
for n in range(1,11):
    table.append((n<<3)-n)
    

# Write your code above this line
# =================================
# Do not change the code below
print(f"7's table in List : {table}")


'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote
# Logic:
creating 7 
1<<3 - 1 --> 8-1=7   -->  1000 - 1  --> 0111
2<<3 - 2 --> 16-2=14 --> 10000 - 10 --> 1110
3<<3 - 3 --> 24-3=21 --> 11000 - 11 --> 10101
   |
   |
so final formula is (n<<3)-n for 7 

Similarly if you wish to create a table for 11 
1<<3 + 1*3 --> 8+3=11  -->  1000 + 11   --> 1011
2<<3 + 2*3 --> 16+6=22 --> 10000 + 110  --> 10110
3<<3 + 3*3 --> 24+9=33 --> 11000 + 1001 --> 100001
   |
   |
so final formula is (n<<3)+3n for 11

# Alternate way:

# print(f"7 x {n} = {(n<<3)-n}") # for 7's table
# print(f"7 x {n} = {(n<<3)+(3*n)}") # for 11's table

Note: We have not taken any input here as for each number the formula will change if we are sticking to bitwise operators, 
      with mathematical operators it will quite straight forward.
'''