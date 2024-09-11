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
from Stack_array import Stack

source1 = Stack()
source1._values = [8, 12, 7, 5]
print("source")
for i in source1:
    print(i)

source1.reverse()
print("reversed source")
for i in source1:
    print(i)