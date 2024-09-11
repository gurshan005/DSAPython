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
from Queue_circular import Queue

q = Queue()
a = Queue()


for i in range(8):
    a.insert(1)
    q.insert(1)
a.insert(2)
q.insert(3)
equals = q == a

print("Testing for __eq__:")
print("equals:", equals)