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

source1 = Queue()
source2 = Queue()

for value in [5, 8, 12, 8]:
    source1.insert(value)

for value in [7, 9, 14]:
    source2.insert(value)

target = Queue()
target.combine(source1, source2)

print("source1 after combine:", list(source1))
print("source2 after combine:", list(source2))
print("target:", list(target))



