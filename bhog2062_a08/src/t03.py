"""
-------------------------------------------------------
[assignment 8, Functions]
-------------------------------------------------------
Author:  gurshan bhogal
ID:         169052062
Email:   bhog2062@mylaurier.ca
__updated__ = "2024-07-11"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from functions import fill_bst, letter_table, do_comparisons, comparison_total

DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"


bst2 = BST()


fill_bst(bst2, DATA2)

fv = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)

letter_table(bst2)