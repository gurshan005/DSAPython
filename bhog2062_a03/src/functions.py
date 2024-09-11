
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

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    toggle = True

    while not source.is_empty():
        if toggle:
            target1.push(source.pop())
        else:
            target2.push(source.pop())
        toggle = not toggle

    return target1, target2

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = []

    while not source.is_empty():
        temp.append(source.pop())
    while len(temp) != 0:
        source.push(temp.pop(0))

    return

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    OPERATORS = "+-*/"

    values = Stack()
    string = string.split()
    for element in string:
        if element not in OPERATORS and not element.isspace():
            values.push(int(element))

        elif element in OPERATORS and not element.isspace():
            x = values.pop()
            y = values.pop()
            if element == "+":
                values.push(y + x)
            elif element == "-":
                values.push(y - x)
            elif element == "*":
                values.push(y * x)
            else:
                values.push(y / x)
    answer = values.pop()
    return answer


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    values_out = []
    for i in opstring:
        if i == "S":
            stack.push(values_in.pop(0))
        else:
            values_out.append(stack.pop())
    if len(values_in) != 0 or not stack.is_empty():
        values_out = None
    return values_out

# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    mirror = MIRRORED.IS_MIRRORED
    stack = Stack()
    n = len(string)
    i = 0
    if m not in string:
        mirror = MIRRORED.NOT_MIRRORED
    while i < n and string[i] != m:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            mirror = MIRRORED.INVALID_CHAR
            i += 1
    i += 1
    while mirror == MIRRORED.IS_MIRRORED and i < n and not stack.is_empty():
        c = stack.pop()

        if string[i] != c:
            mirror = MIRRORED.MISMATCHED
        else:
            i += 1
    if not (i == n) and mirror == MIRRORED.IS_MIRRORED:
        mirror = MIRRORED.TOO_MANY_RIGHT
    elif not stack.is_empty() and mirror == MIRRORED.IS_MIRRORED:
        mirror = MIRRORED.TOO_MANY_LEFT
    return mirror




