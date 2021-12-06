#!/usr/bin/python3
"""printing x elements of alist"""
def safe_print_list(my_list=[], x=0):
    my_list = [1, 2, 3, 4, 5, 6]
    print('my_list')
    for x in my_list:
        print("My list contains: {:d} integers\n".format(x))
try:
    safe_print_list(my_list=[], x=0)
except ValueError:
    print("x is assigned wrongly")
else:
    print("known error not detected")
