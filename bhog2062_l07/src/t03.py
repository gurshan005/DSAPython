"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Gurshan Bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024"
-------------------------------------------------------
"""
# Imports
from List_linked import List

l = List()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

even, odd = l.split_alt()
print(even._front._next._value, odd._front._next._value)