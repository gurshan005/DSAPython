"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: gurshan Bhogal
ID:     169052062
Email:  bhog2062@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""
# Imports
from BST_linked import BST

bst = BST()

vals = [0, 3, 6, 9, 12]

for value in vals:
    bst.insert(value)

zero, one, two = bst.node_counts()

print(f"# of nodes with no children: {zero}")
print()

print(f"# of nodes with one child: {one}")
print()

print(f"# of nodes with two children: {two}")
print()

print(f"Testing for __contains__ 6: {bst.__contains__(6)}")
print()

print(f"Parent Node for 6: {bst.parent(6)}")
print()

print(f"Parent Node for 6(recursive): {bst.parent_r(6)}")
