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
l.append(22)
l.append(33)
l.append(11)
l.append(55)
l.append(44)
l.append(None)

l.reverse_r()

print(l._rear._value, l._front._value, l._front._next._value, l._front._next._next._value,
      l._front._next._next._next._value, l._front._next._next._next._next._value, l._front._next._next._next._next._next._value)