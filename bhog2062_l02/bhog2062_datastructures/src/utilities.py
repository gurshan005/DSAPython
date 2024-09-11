"""
-------------------------------------------------------
utility functions.
-------------------------------------------------------
Author:  gurshan bhogal
ID:      169052062
Email:   bhog2062@wlu.ca
Section: CP164 B
__updated__ = "2021-01-12"
-------------------------------------------------------
"""


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source:
        stack.push(source.pop())
    
    return None
    
    
    
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():
        target.insert(0,stack.pop())
        
    return None
    
    
    
    
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = () 
    
    assert stack.is_empty()
    
    for item in source:
        stack.push(item)
        assert stack.peek() == item
        
    assert not stack.is_empty()
    
    while not stack.is_empty():
        expected_item = source.pop()
        assert stack.pop()== expected_item
    
    assert stack.is_empty()
    
    