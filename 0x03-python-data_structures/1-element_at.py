#!/usr/bin/python3
def element_at(my_list, idx):
    my_list = [1, 2, 3, 4, 5, 6]
    idx = my_list[1]
    for idx in my_list:
        print(idx)
    if idx < 0:
        return None
    if idx > my_list:
        return None
    print("the element at idx {:d} is {}\n".format(idx, element_at(my_list, idx)))
