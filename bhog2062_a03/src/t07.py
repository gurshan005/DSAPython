"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: Gurshan bhogal
ID:     169052062
Email:  bhog2062@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""
from functions import is_mirror_stack

string = input("Enter a string: ")
valid_chars = input("Enter the valid chars: ")
m = input("Enter the mirror pivot: ")

mirror = is_mirror_stack(string, valid_chars, m)
print(mirror.value)
