"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: Ishan Shah
ID:     169053350
Email:  shah3350@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""
# Imports
from Sorts_array import Sorts

print("Testing gnome_sort(Array-based):")

lst = []
a = input("Enter a value to your list(Enter to stop): ")
while a != "":
    lst.append(int(a))
    a = input("Enter a value to your list(Enter to stop): ")
print(f"Original list: {lst}")
Sorts.gnome_sort(lst)
print(f"Sorted list: {lst}")
