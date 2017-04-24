"""
This is the "function" module.

The function module supplies one function, oddNumer().  For example,

>>> oddNumer(5)
True
"""

def oddNumer(x):
    """Returns true.

    >>> oddNumer(6)
    False

    >>> oddNumer(5.3)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer
    """

    import math
    val = str(x)
    if math.floor(x) != x:
        raise ValueError("n must be exact integer")
    return x % 2 == 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()