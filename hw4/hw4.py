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

    Output: prefix distance of u and v (int)
    """
    ### Replace the body of this function with your solution.
    sum = len(u) + len(v)
    large= max(len(u), len(v))
    for i in range(large):
        if i < (len(u) and i < len(v)):
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

    Output: suffix distance of u and v (int)
    """
    u = u[::-1]
    v = v[::-1]
    suffix = prefix_distance(u,v)
    return suffix

    '''overall = max(len(u), len(v)) 
    dist = len(u) + len(v)
    for i in range(overall):
        if i < (len(v) and len(u)):
            if u[-1] == v[-1]:
                dist = dist -2
            elif u[-1] != v[-i]:
                break
    return dist'''

    
# Exercise 3
def total_badness(text, width):
    by_line = text.split('\n')
    curr_bad = 0
    total_bad = 0
    for i in range(len(by_line) - 1): # skips last line 
        one_word = False
        line = by_line[i]
        curr_bad = 0
        total_bad += curr_bad**3

        # Check if current line is a single word longer than width
        if (len(line.split(' ')) == 1) & (len(line) > width): 
            curr_bad = len(line) - width
            total_bad += curr_bad**3
            break # go to next line
            
        for i in range(len(line) - 1, 0, -1): # go through line backwards
            curr_char = line[i]
            next_char = line[i - 1]
            if (curr_char == ' ') & (next_char != ' '):
                curr_bad += 1 
                total_bad += curr_bad**3
                break ## go to next line bc we've hit a word 

            if (curr_char == ' ') & (next_char == ' '):
                curr_bad += 1
        print('current:', curr_bad)
        
        return total_bad
        pass

# Exercise 4
def split_lines(text, width):
   
    '''
    Inputs the text of usage and the width that the lines within the text have to be. 
    This will return a list of lines that have a length at most the given width.

    Input:
        text (lst): first input list
        width (int): an integer that varies based upon the text
    
    Output: a list of lines that each have a maximum width of the width input value

    '''
    
    lines = text.split('\n')
    new_list = []
    for i in range(len(text)):
        line = lines[i]
        if len(line) > width:
            bad = len(line) - width
            new_list.append(bad)
        else: 
            break
    
    x = line.split(' ')
    return x 


# Exercise 5
def arrange_lines(text, width, blanks_visible):
    ### Replace the body of this function with your solution.
    pass

# Exercise 6
def optimal_width(text, min_width, max_width):
    ### Replace the body of this function with your solution.
    pass
