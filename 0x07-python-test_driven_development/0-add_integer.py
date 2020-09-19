#!/usr/bin/python3
"""this module contain one function that add 2 integers and raise exception if not
Functions:def add_integer(a, b=98)
def add_integer(a) -> integer def add_integer(b=98) -> integer
return sum of a+b
"""


def add_integer(a, b=98):
    """Returns the sum of two integer numbers in binary digits.
      Returns:
      binary_sum (str): Binary string of the sum of a and b"""
    if type(a) == str:
        raise TypeError("a must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    if type(b) == str:
        raise TypeError("b must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    if a == "" and b == "":
        raise TypeError("add_integr() missing 1 required positional argument")
    return a+b