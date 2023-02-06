""" 
# Project: Python Bootcamp - Session I
# File: 7-register_read_update_write.py
# Description: In this exercise we will understand use of bitwise operatos while writing a register and things to keep in mind.
#              More/different ways to deal with this will be explained in commented code below.
#              Instruction: Update the registe value by changing 17th and 29th bit to 1.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 23/11/2022
# Last modified: 24/11/2022
"""

print('Lets try to write a register:') 
Reg_red_val = 0x00F0023F
print(f"Current value of a certain CPU register is: {Reg_red_val}")
# Do not change the code above
# =================================
# Write your code below

# write value - change 17th and 29th bit to 1 
((Reg_red_val ^ 1 <<17) | Reg_red_val)
((Reg_red_val ^ 1 <<29) | Reg_red_val)

# Write your code above this line
# =================================
# Do not change the code below
print(f"Updated Value after writing 17th and 29th bit to 1 is: {Reg_red_val}")


'''
# Alternet ways
# Use: Replace below Block of code with the one you wrote
# Suggestion: Do check the 17th and 19th bit before isolating and updating to 1.

# 0x00F0023F --> 0000 0000 1111 0000 0000 0010 0011 1111
#                  ^              ^
#check             &1
#update          0000 0000 0000 0010 0000 0000 0000 0000

read
update : check --> update  
write

'''