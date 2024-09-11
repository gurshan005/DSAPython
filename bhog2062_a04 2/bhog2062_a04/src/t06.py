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
from Priority_Queue_array import Priority_Queue

a = Priority_Queue()
for i in [1, 6, 3, -22, 89]:
    a.insert(i)

print("Source: ", a._values)
target1, target2 = a.split_key(3)
print("Target1: ", target1._values)
print("target2: ", target2._values)
