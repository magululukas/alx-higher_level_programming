#!/usr/bin/python3
def add_integer(a, b=98):
    """A function adding two(2) integers."""
    a = "me"
    b = 98
    result = (a + b)
    return result
    print("{:d}\n".format(result))
    print(add_integer(12, 12))
    print("\n")
try:
    add_integer(a, b=98)
except(TypeError, NameError):
    if True:
        print("a must be an integer\n")
    else:
        print("b must be an integer\n")
