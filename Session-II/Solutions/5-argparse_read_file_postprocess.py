""" 
# Project: Python Bootcamp - Session II
# File: 5-argparse_template.py
# Description: In this exercise we will understand and use argparse module for accepting commandline arguments.
#              To explore some meaningful task along with it - we will postprocess passed logfile and push the data in csv 
#              using pandas module.
#              More/different ways/explaination to deal with this will be explained in commented code below.
# Author: Ajinkya Biradar e-mail: ajinkyabiradar@mirafra.com
# Created: 15/01/2023
# Last modified: 15/01/2023
"""

# Do not change the code above
# =================================
# Write your code below

import argparse 
import os
import pandas as pd

def read_file(file_name):
    with open(file_name) as my_file:
        final_list = []
        # print(type(my_file))
        for line in my_file:
            # print(line.split(" "))
            temp = line.strip().split(" ")
            if temp[0] == "Reply":
                final_list.append(temp)
        print(final_list)
        print(dir(pd))
        df = pd.DataFrame(final_list)
        print(df)
        df.to_excel("output.xlsx",index=False)

if __name__ == '__main__':
    def is_valid_file(parser, arg):
        if not os.path.exists(arg):
            parser.error("The file %s does not exist!" % arg)
        else:
            return arg # return file name

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='filename', help='input file', metavar='FILE', type=lambda x: is_valid_file(parser, x), required=True)
    args = parser.parse_args()
    read_file(args.filename)

# Write your code above this line
# =================================
# Do not change the code below


'''
# Alternet/more ways to handle arguments - grouped arguments, mutually exclusive arguments, etc.
# 
# grouping the arguments.
# group1 = parser.add_argument_group('group1', 'group1 description')
# group1.add_argument('foo', help='foo help')
# group2 = parser.add_argument_group('group2', 'group2 description')
# group2.add_argument('--bar', help='bar help')

# Either of the arguments - mutually exclusive arguments.
# group = parser.add_mutually_exclusive_group()
# group.add_argument('-a', action='store_true')
# group.add_argument('-b', action='store_true')

'''