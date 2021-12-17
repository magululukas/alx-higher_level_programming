#!/usr/bin/python3
def element_at(my_list, idx):
    """retrieve the element in a list"""
    my_list = [1, 2, 3, 4, 5, 6]
    for x in my_list:
        idx = x[1]
    if idx < 0:
        return None
    if idx > len(x):
        return None
    print("the element at idx {:d} is {:d}\n".format(idx, element_at(my_list, idx)))
