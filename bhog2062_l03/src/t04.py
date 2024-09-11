
"""
-------------------------------------------------------
[Lab 3, Task 4]
-------------------------------------------------------
Author:  Gurshan bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from utilities import priority_queue_test

fh = open('foods.txt', 'r')

print(priority_queue_test(fh))

fh.close()
