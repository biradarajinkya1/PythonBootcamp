""" 
# Project: Python Bootcamp - Session II
# File: 4-arg_kwarg.py
# Description: In this exercise we will understand and use args and kwargs.
#              Args and Kwargs can be used where number of arguments are either variable or not fixed.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

def myFun_arg(*args):
    print(sum(args))
    for arg in args:
        print(f"Argument through *argv :{arg}")

def myFun_kwarg(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value}")
     
myFun_arg(1, 2, 3, 4)
myFun_arg(1, 2, 3)
myFun_arg(1, 2, 3, 4, 10, 20)


myFun_kwarg(first='I', mid='live in', last='Bangalore')
myFun_kwarg(first='I', mid='live in', last='Bangalore', last_1='and Delhi')

#Write your code above this line
# =================================
# Do not change the code below


'''
# Alternet ways / elaboration of arg and kwarg
# Kwargs and Args do the same job with one difference for kwargs that one needs to assign keywords for argument values.

'''