"""
-------------------------------------------------------
[Lab 5, Task 2]
-------------------------------------------------------
Author:  gurshan bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024"
-------------------------------------------------------
"""
# Imports
from functions import gcd

m = int(input("Enter an integer: "))
n = int(input("Enter another integer: "))
ans = gcd(m, n)

print("The greatest common denominator of", m, "and", n, "is", ans)