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
from functions import insert_words, comparison_total
from Hash_Set_BST import Hash_Set
fv = open("miserables.txt", "r")
hash_set = Hash_Set(20)
insert_words(fv, hash_set)

total, max_word = comparison_total(hash_set)

print("Using linked BST Hash_Set")
print()
print(f"Total Comparisons: {total:,}")
print(
    f"Word with maximum comparisons '{max_word.word}': {max_word.comparisons:,}")
