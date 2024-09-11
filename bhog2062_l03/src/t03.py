
"""
-------------------------------------------------------
[Lab 3, Task 3]
-------------------------------------------------------
Author:  Gurshan bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
#from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array

source = [1, 2, 5, 4, 8, 6, 7, 3, 9]
target = []
q = Priority_Queue()
array_to_pq(q, source)
#pq_to_array(q, target)
# print(target)
print(q._values)