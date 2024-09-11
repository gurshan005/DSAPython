"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: Gurshan Bhogal
ID:     169052062
Email:  bhog2062@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""
from Queue_array import Queue


a = Queue()
b = Queue()
for i in range(3):
    a.insert(1)

b.insert(1)
a.remove()
a.remove()

equals = a == b
print("Testing for __eq__:")
print("equals:", equals)