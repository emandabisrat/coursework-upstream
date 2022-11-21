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
    '''
    
    '''
    with open(filename) as w:
        data = json.load(open(filename))
        dictionary = {}
        for user_event in data:
            dictionary[user_event['user_id']] = dictionary.get(user_event['user_id'], 0) +1
        return dictionary    


### Exercise 2
def convert_complex_to_simple_event(complex_event):
    '''

    '''
    visual_event = complex_event['vis']
    dictionary = {}
    lst = []
    for i in visual_event:
        if i == 'encoding':
            for key in ENCODINGS:
                if key in visual_event['encoding'].keys():
                    dictionary[key] = visual_event['encoding'][key]['field']
                else:
                    dictionary[key] = None
    for value in OPERATIONS:
        if complex_event[value]:
            lst.append(value)
    dictionary['operations'] = lst
    return dictionary

### Exercise 3
def load_user_data(filename):
    with open(filename) as w:
        file = json.load(w)
        list = []
        dictionary = {}
        if len(file) == 0:
            return dictionary
        else:
            user_id = file[0]['user_id']
            for i in file:
                if user_id == i['user_id']:
                    list.append(convert_complex_to_simple_event(i))
                else:
                    dictionary[user_id] = list
                    list = [convert_complex_to_simple_event(i)]
                    user_id = i['user_id']
            dictionary[file[-1]['user_id']] = list
        return dictionary
    


### Exercise 4
def count_variable_views_per_user(user_events):
    '''
    This function dictionary of simple events per user and returns a 
    dictionary with user_id values as keys storing as values 
    dictionaries that map variable names viewed by that user to counts
    of the number of times the user viewed each variable.

    Input:
        user_evbents (dict): dictionary
     PUtput:
        dictionary


    '''
    dictionary = {}
    count = {}
    for key,value in user_events.items():
        val = []
        for a in value:
            b = list(a.val())
            val =  val + list(set(i for i in b if type(i) != list and i != None))
            for v in val:
                if v in count.keys():
                    count[v] = count[v] = 1
                else:
                    count[v] = 1
        dictionary[key] = count
        count
    return dictionary


### Exercise 5
def most_complex_view_per_user(user_events):
    '''
    This function takes a dictionary of simple events per user and returns 
    a dictionary with user_id values as keys storing as values the index of 
    the most complex view in the input list for each user.
    Inputs: 
        user_events (dict) : user simple evnts 
    Putput:
        new dictionary (dict): a dictionary containing user_id as keys and 
        the index
    
    '''

    new_dictionary = {}
    l_idx = 0
    complex = 0
    for key,v in user_events.items():
        d = 0
        for index , w in enumerate(v):
            x = list(w.values())
            y = list(set([i for i in x if type(i) != list and i != None]))
            z = [i for i in x if type(i) == list]
            a = len(y) + len(z[0])
            if a > complex:
                complex = a
                l_idx = index
        new_dictionary[key] = l_idx
        complex = 0
    return new_dictionary


### Exercise 6
def compute_max_gap(user_events, user, variable):
    '''
    This function takes a dictionary of simple events per user (the “user data” 
    returned by load_user_data), a user id, and a variable name, and returns
     an integer representing the maximum gap between views of the variable 
     (see above) for the specified user.

    Inputs:
        user_events(dict) : dictionary of user simple events
        user : user_id string
        variable (str) : string
    Output:
        gap(int) : the maximum between variables of user ids
    '''
    c = 0
    gap = 0
    gap_ex = False
    for i in user_events[user]:
        if variable in i.values():
            gap_ex = True
            if gap < g and gap_ex:
                gap = g
            g = 0
            c = c + 1
        else:
            if gap_ex:
                g = g + 1
            else:
                g = 0
        if c < 2:
            gap = -1
    return gap


