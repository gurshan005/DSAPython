"""
-------------------------------------------------------
[assignment 6, task 2]
-------------------------------------------------------
Author:  gurshan bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024"
-------------------------------------------------------
"""
from Priority_Queue_linked import Priority_Queue

pq = Priority_Queue()

pq.insert('a')
pq.insert('b')
pq.insert('c')

print(pq._front._value, pq._count)
