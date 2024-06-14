#!/usr/bin/python3
"""this is task 0 of
alx interview projects"""

from typing import List


def validUTF8(data):
    """validUTF8
    returns true or false"""
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            if byte >> 7 == 0b0:
                bytes_to_follow = 0
            elif byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                bytes_to_follow = 1
            elif byte >> 4 == 0b1110:
                bytes_to_follow = 2
            elif byte >> 3 == 0b11110:
                bytes_to_follow = 3
            else:
                return False

        else:
            if byte >> 6 == 0b10:
                bytes_to_follow -= 1
            else:
                return False

        if bytes_to_follow < 0:
            return False

    return bytes_to_follow == 0
