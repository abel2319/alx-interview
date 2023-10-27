#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """a method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    nbr = 0

    for i in data:
        binary = bin(i).replace('0b', '').rjust(8, '0')[-8:]
        if nbr == 0:
            if binary.startswith('110'):
                nbr = 1
            if binary.startswith('1110'):
                nbr = 2
            if binary.startswith('11110'):
                nbr = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            nbr -= 1

    if nbr != 0:
        return False

    return True
