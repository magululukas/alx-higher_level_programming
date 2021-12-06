#!/usr/bin/python3
"""Printing an integer with error using .format()"""
def safe_print_integer(value):
    value = "Schools open"

    print("{:d}\n".format(value))
    if (value == NULL):
        return True
    else:
        return False

try:
    safe_print_integer(value)
except(NameError, TypeError):
    print("Oops!")
else:
    print("Yess!! you did it.")
    
