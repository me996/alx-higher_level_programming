#!/usr/bin/python3
"""define an integer addition function"""


def add_integer(a, b=98):
    """
    Add two integers or floats, cast them to integers if needed.

    :param a: The first number (integer or float).
    :param b: The second number (integer or float). Defaults to 98.

    :return: The addition of a and b as an integer.

    :raises TypeError: If a or b is not an integer or float.
    """
    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    # Calculate and return the addition of a and b
    return a + b
