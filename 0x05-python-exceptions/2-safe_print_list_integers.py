#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """A function printing the first integer values only"""
    count = 0
    for p in range(0,x):
        try:
            print("{:d}\n".format(my_list[p]), end="")
            my_int += 1
        except(NameError, ValueError):
            pass
    print()
    return count
