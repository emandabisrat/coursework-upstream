"""
CMSC 14100, Autumn 2022
Homework #6

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
import json

ENCODINGS = ['x', 'y', 'row', 'column']
OPERATIONS = ['filters', 'transforms', 'models']

### Exercise 1
def count_user_events(filename):
    f = open(filename)
    events = json.load(f)

    for e in events:
        events.append(e['user_id'])
    events = list(set(events))

    d = {}
    for i in events:
        u = "user_id"
        d[u[i]] = d.get([u[i]],0) + 1
    
    #count = 0
    #user_identification = ""
    #for id, cnt in sorted(d.items()):
        


    return d


### Exercise 2
def convert_complex_to_simple_event(complex_event):
    pass


### Exercise 3
def load_user_data(filename):
    pass


### Exercise 4
def count_variable_views_per_user(user_events):
    pass


### Exercise 5
def most_complex_view_per_user(user_events):
    pass


### Exercise 6
def compute_max_gap(user_events, user, variable):
    pass
