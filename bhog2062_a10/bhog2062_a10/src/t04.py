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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque

print("Testing Gnome Sort(Deque linked list):")

lst = Deque()
a = input("Enter a value to your list(Enter to stop): ")
while a != "":
    lst.insert_rear((int(a)))
    a = input("Enter a value to your list(Enter to stop): ")
print(f"Original list:")
for i in lst:
    print(i, end=" ")
print()
Sorts.gnome_sort(lst)
print(f"Sorted list:")
for i in lst:
    print(i, end=" ")
