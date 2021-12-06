#!/usr/bin/python3
"""Printing an integer with error using .format()"""
def safe_print_integer(value):
    value = 25

    print("{:d}\n".format(value))
    if (value == True):
        return True
    else:
        return False

try:
    safe_print_integer(value)
except(NameError, TypeError):
    print("Oops!")
else:
    print("Yess!! you did it.")
    
