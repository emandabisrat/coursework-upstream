"""
CMSC 14100, Autumn 2022
Homework #3

Emanda Bisrat

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

def compare_sum(lst1, lst2):
    """
    compare_sum takes two lists and compares the sum of their
    elements. The function should return a value less than zero if the sum of
    the values in lst1 is less than the sum of the values of list2, zero if
    they are the same, and a value greater than zero if the sum of the first
    list is greater than the sum of the second list.

    Note that you may assume the elements of the lists are all of type
    float or int.

    Inputs:
        lst1 (list): a list of numbers
        lst2 (list): a list of numbers

    Returns (int or float):
        n > 0 if lst1 > lst2
        0 if lst1 = lst2
        n < 0 if lst1 < lst2
    """
    ### EXERCISE 1 -- YOUR CODE TO COMPUTE result GOES HERE
    
    #if sum(lst1) > sum(lst2):
    result = sum(lst1) - sum(lst2)
    #elif sum(lst1) == sum(lst2):
        #result = 0
    #else:
        #result = sum(lst2) - sum(lst1)
    


    ### DO NOT REMOVE THE return STATEMENT BELOW
    return result


def largest_of_three(lst, idx):
    """
    Given a list and an index, return the largest value among the
    indexed value, its left neighbor, and its right neighbor.  Treat the list
    as a ring, so the left neighbor of index 0 is the last element in
    the list, and the right neighbor of the last element is the element
    at index 0.

    Inputs:
      lst: a list of numbers
      idx: an index into the list

    Returns: the largest of the value at idx and its left and right
    neighbors.
    """
    # Do not remove the two assertions. The first ensures that the list is not
    # empty.  The second ensures that idx is a legal index.
    assert len(lst) > 0
    assert len(lst) > idx >= 0

    ### EXERCISE 2 -- YOUR CODE TO COMPUTE result GOES HERE
    #for i in lst:
        #result = max(lst[idx], lst[idx + 1], lst[idx-1])
    
    
    for i in lst:
        if idx == 0:
            result = max(lst[idx], lst[idx + 1], lst[(len(lst))- 1])
        elif idx == (len(lst) - 1):
            result = max((lst[len(lst) - 1]), lst[(len(lst) - 1) - 1], lst[0])
        else:
            result = max(lst[idx], lst[idx + 1], lst[idx-1])



 
    ### DO NOT REMOVE THE return STATEMENT BELOW
    return result


def seq(n):
    """
    Consider the sequence S, where S_0 = S_1 = S_2 = 1 and S_n =
    S_{n-2} + S_{n-3}. Given an integer value n as an input, seq
    computes S_n using an iterative (e.g. a loop) approach.

    Inputs:
        n (int): the index of the sequence to compute

    Returns (int): the nth value of the sequence

    """
    # Do not remove the next line.  It helps verify that n is a sensible value
    assert n >= 0

    ### EXERCISE 3 -- YOUR CODE TO COMPUTE result GOES HERE
    result = None

    ### DO NOT REMOVE THE return STATEMENT BELOW
    return result


def gen_swap(lst, a, b):
    """
    Create a new list, in which every occurrences of the value a in
    lst is replaced by b and every occurrence of b is replaced by a.
    all other values remain the same.

    Inputs:
        lst: a list of values
        a: a value
        b: another value

    Returns: a new list of values
    """
    ### EXERCISE 4 -- YOUR CODE TO COMPUTE result GOES HERE
    
    result = []
    for i in lst:
        if i == a:
            result.append(b)
        elif i == b:
            result.append(a)
        else:
            result.append(i)
    ### DO NOT REMOVE THE return STATEMENT BELOW
    return result


# Constants to use for the setting result in the next problem
ALL_MATCH = "all"
SOME_MATCH = "some"
NOT_ANY_MATCH = "not_any"

def how_many_equal_first(lst):
    """
    how_many_equal_first compares the values in rest of the list to
    the first value to determine whether:
      - all the values in the rest of the list equal the first value,
      - at least some of the values in the rest of the equal the first value, or
      - none of the values in the result of the list equal the first value

    Inputs:
        lst: a non-empty list of integers

    Returns: (string)
      -- "all" if all the values in the list are equal to the first one, or if
          the list only contains one element
      -- "some" if at least one value after the first one is equal to the
          first one
      -- "not_any" if none of the values after the first one match the first one

    """
    assert len(lst) > 0

    ### EXERCISE 5 -- YOUR CODE TO COMPUTE result GOES HERE
    result = []
    for i in lst:
        if i == lst[0]:
            result = ALL_MATCH
        elif i != lst[0] or i == lst[0]:
            result = SOME_MATCH
        elif i != lst[0]:
            result = NOT_ANY_MATCH

    ### DO NOT REMOVE THE return STATEMENT BELOW
    return result


def intercalate_lists(lst1, lst2):
    """
    intercalate_list takes in two lists and returns a NEW list that
    alternates the elements of the input lists. For each pair of elements
    between lst1 and lst2 in the same index position, the element from lst1
    should appear first in the new list. If the lists are not of the same
    length, the function should repeat the last element of the shorter list.

    Inputs:
        lst1 (list): a list of elements
        lst2 (list): a list of elements

    Returns (list): a new list with the elements of lst2 inserted
    between the elements of lst1

    """
    # Do not remove the two assertions. They help verify that the lists are not
    # empty
    assert len(lst1) > 0
    assert len(lst2) > 0

    ### EXERCISE 6 -- YOUR CODE TO COMPUTE result GOES HERE
    result = None

    ### DO NOT REMOVE THE return STATEMENT BELOW
    return result
