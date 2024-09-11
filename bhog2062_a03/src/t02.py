"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: Gurshan bhogal
ID:     169052062
Email:  bhog2062@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""

from Stack_array import Stack

def main():
    source = Stack()
    values = [8, 14, 12, 9, 8, 7, 5]
    for value in values[::-1]:  
        source.push(value)
    
    print("Source stack before splitting:", list(source))

    target1, target2 = source.split_alt()

    print("Target1 stack after splitting:", list(target1))
    print("Target2 stack after splitting:", list(target2))
    print("Source stack after splitting (should be empty):", list(source))

if __name__ == "__main__":
    main()