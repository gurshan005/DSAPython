"""
------------------------------------------------------------------------
[CP164]
------------------------------------------------------------------------
Author: Gurshan Bhogal
ID:     169052062
Email:  bhog2062@mylaurier.ca
__updated__ = "2024-01-11"
------------------------------------------------------------------------
"""
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from copy import deepcopy


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()

    while not source.is_empty():
        temp = source.remove()
        if temp < key:
            target1.insert(temp)
        else:
            target2.insert(temp)

    return target1, target2


def queue_combine(source1, source2):
    target = Queue()
    s1_copy = deepcopy(source1)
    s2_copy = deepcopy(source2)
    
    while not s1_copy.is_empty() or not s2_copy.is_empty():
        if not s1_copy.is_empty():
            target.insert(s1_copy.remove())
        if not s2_copy.is_empty():
            target.insert(s2_copy.remove())
    
    return target
