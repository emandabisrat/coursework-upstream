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

from decimal import Subnormal
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

    Output: 
        The prefix distance of u and v (int)
    """
    sum = len(u) + len(v)
    maximum = max(len(u), len(v))
    for i in range(maximum):
        if i < len(u) and i < len(v):
            if u[i] == v[i]:
                sum = sum - 2
            elif u[i] != v[i]:
                break
    total = sum
    return total    





# Exercise 2
def suffix_distance(u, v):
    """
    Computes the suffix distance of u and v. The suffix distance is the total
    number of characters that do not belong to the longest common suffix shared
    by u and v.


    Input:
        u (str): first input string
        v (str): second input string

    Output: 
        The suffix distance of u and v (int)
    """
    u = u[::-1]
    v = v[::-1]
    suffix = prefix_distance(u,v)
    return suffix

    
# Exercise 3
def total_badness(text, width):
    '''
    Inputs a text string and an integer width and returns the total
    baddness of the text which is represented by a value of the sum 
    of the cubes of how many blank spaces are at the end of each line. 

    Inputs:
        text (str): first input 
        width (int): an integer that varies upon the text
    
    Output:
        The total badness of a text(amount blank spaces)
    '''

    split = split_lines(text, width)
    bad = 0
    for i in split[0: len(split) - 1]:
        bad += (abs(width - len(i))) ** 3
    return bad


# Exercise 4
def split_lines(text, width):
   
    '''
    Inputs the text of usage and the width that the lines within the text have
    to be. This will return a list of lines that have a length at most the 
    given width.

    Input:
        text (lst): first input list
        width (int): an integer that varies based upon the text
    
    Output: 
        a list of lines that each have a maximum width of the width input value

    '''
    
    lines = text.split(' ')
    single_line = lines[0]
    new_list = []
    for i in lines[1:]:
        if len(single_line) + len(i) + 1 <= width:
            single_line = single_line + ' ' + i
        else: 
            new_list.append(single_line)
            single_line = i
    new_list.append(single_line)
    return new_list
    


# Exercise 5


def arrange_lines(text, width, blanks_visible):
    '''
    Inputs the given text string, a width, and blanks_visible which is an 
    optional flag. Then the function returns a single string of the given text
    broken into lines that meet the width requirement.

    Inputs:
        text (str): a string of text
        width (int): an integer that varies based upon the text
        blanks_visible: an optional flag
    
    Output:
        A single string of the text with equal width lines. 
    '''
    various_l = split_lines(text, width)
    final = ""
    if not blanks_visible:
        for i in various_l:
            final += i + "\n"
    elif blanks_visible:
        for i in various_l:
            under = i + ('_' * (width - len(i)) + "\n")
            final += under
    final = final.strip()
    return final 

# Exercise 6
def optimal_width(text, min_width, max_width):
    '''
    Inputs are the text, a minimum width, and a maximum width to 
    '''
    bad = []
    for i in range(min_width, max_width + 1):
        bad.append(total_badness(text,i))
    optimal = min(bad)
    index = bad.index(optimal)
    return index + min_width
    
