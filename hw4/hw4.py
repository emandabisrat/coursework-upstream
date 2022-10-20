"""
CMSC 14100, Autumn 2022
Homework #4

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import math

# Exercise 1
def prefix_distance(u, v):
    """
    Computes the prefix distance of u and v. The prefix distance is the total
    number of characters that do not belong to the longest common prefix shared
    by u and v.

    For example, the prefix distance of "morning" and "mourning" is 11, since
    the longest common prefix of the two strings is "mo".

    Input:
        u (str): first input string
        v (str): second input string

    Output: prefix distance of u and v (int)
    """
    ### Replace the body of this function with your solution.
    for i in range(u[i:len(u)], v[i:len(v)]):
        dist = 0
        if u[i:] == v[i:]:
            dist = dist + 1
            return dist
        else:
            return 

# Exercise 2
def suffix_distance(u, v):
    ### Replace the body of this function with your solution.
    pass

# Exercise 3
def total_badness(text, width):
    ### Replace the body of this function with your solution.
    pass

# Exercise 4
def split_lines(text, width):
    ### Replace the body of this function with your solution.
    pass

# Exercise 5
def arrange_lines(text, width, blanks_visible):
    ### Replace the body of this function with your solution.
    pass

# Exercise 6
def optimal_width(text, min_width, max_width):
    ### Replace the body of this function with your solution.
    pass
