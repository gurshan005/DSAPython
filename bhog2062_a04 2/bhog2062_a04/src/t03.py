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
from functions import Queue, queue_combine

source1 = Queue()
source2 = Queue()

for value in [5, 8, 12, 8]:
    source1.insert(value)

for value in [7, 9, 14]:
    source2.insert(value)

target = queue_combine(source1, source2)

print("source1:", list(source1))
print("source2:", list(source2))
print("target:", list(target))



