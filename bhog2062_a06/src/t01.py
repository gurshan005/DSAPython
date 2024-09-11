"""
-------------------------------------------------------
[assignment 6, task 1]
-------------------------------------------------------
Author:  gurshan bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024"
-------------------------------------------------------
"""
# Imports
from Queue_linked import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)
q.remove()

print(q._front._value, q._rear._value, q.is_empty())
