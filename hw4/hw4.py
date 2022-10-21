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
        if i < (len(u) and len(v)):
            if u[i] == v[i]:
                sum = sum - 2
            elif u[i] != v[i]:
                break
    return sum    


        
    '''for i in range(len(u)):
        if u[i] == v[i]:
            dist = dist + 1
        else:
            break'''


    #total = (len(u) - dist) + (len(v) - dist)
    #ustring = len(u) - dist
    #vstring = len(v) - dist   
    #total = ustring + vstring
    return total 



# Exercise 2
def suffix_distance(u, v):
    ### Replace the body of this function with your solution.

    overall = max(len(u), len(v)) 
    dist = len(u) + len(v)
    for i in range(overall):
        if i < (len(v) and len(u)):
            if u[-1] == v[-1]:
                dist = dist -2
            elif u[-1] != v[-i]:
                break
    return dist

    '''sum = 0
    for i in range(len(u)):
        if u[-i] == v[-i]:
            sum = sum + 1
            
        else:
            break

    total = (len(u) - sum) + (len(v) - sum)
    return total'''

# Exercise 3
def total_badness(text, width):
    ### Replace the body of this function with your solution.
    r = text.split('\n')
    curr_bad = 0
    total_bad = 0
    for l in range(len(r) - 1): # skips last line 
        line = r[l]
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
                break ## go to next line bc we've hit a word 1

            if (curr_char == ' ') & (next_char == ' '):
                curr_bad += 1
        print('current:', curr_bad)
        
        
        
    return total_bad


# Exercise 4
def split_lines(text, width):
    ### Replace the body of this function with your solution.
    #for i in range(len(text)):
    #text(len(width))
    #for i in text:
    #for i in range(text([0], [width])):
    #or i in text[width]:
    r = text.split('\n')
    
    for i in range(len(text)):
        line = r[i]
        if len(line) > width:
            bad = len(line) - width
            total_bad += bad**3
            break
    #result = text.splitlines('\n')

    #x = text.split(' ')
    
    #len(width)
    #x = text.split(' ')
    return total_bad 


# Exercise 5
def arrange_lines(text, width, blanks_visible):
    ### Replace the body of this function with your solution.
    pass

# Exercise 6
def optimal_width(text, min_width, max_width):
    ### Replace the body of this function with your solution.
    pass
