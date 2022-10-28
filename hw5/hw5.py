"""
CMSC 14100, Autumn 2022
Homework #5

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

# A constant for the color black
# #from pickle import TUPLE
# from tkinter.tix import COLUMN


BLACK = (0, 0, 0)


def create_greyscale(image):
    '''
    A function that takes an image and returns a new greyscale version of the 
    image. This will happen by using the equation to change every RGB value in 
    every tuple inside the image.

    Input: 
        image (list(lists(tuples))) : only input string

    Output: 
        new_image(lst) : a list of lists of tuples
    '''
    new_image = []
    for lst1 in image:
        lst = []
        for red,green,blue in lst1:
            grey = (((77 * red) + (150 * green) + (29 * blue))//256)
            lst.append((grey, grey, grey))
        new_image.append(lst)
    return new_image
def find_region_locations(image, loc, radius):
    '''
    A function that takes an image, location (i,j), and radius and returns a new 
    list of locations in a specified region. 

    Inputs:
        image (list) : A list of list of tuples
        loc (i,j) : a location in terms of a list
        radius (int) : an integer

    Output:
        region_locations (lst) : a list of tuples of locations
    '''
    lst = []
    for i, x in enumerate(image):
        for j, item in enumerate(x):
            k = loc[0]
            l = loc[1]
            if radius >= abs(i - k) and radius >= abs(j - l):
                lst.append((i,j))
    return lst
    
def blackout_region(image, loc, radius):
    '''
    A fucntion that takes an image, location, and radius and returns blacked
    out pixels in the region of the specified radius by replacing the pixels 
    with black pixels.

    Inputs:
        image (list) : A list of list of tuples
        loc (i,j) : a location in terms of a list
        radius (int) : an integer
    
    Output:
        None : the image is only modified
    '''
    for i, x in enumerate(image):
        for j, item in enumerate(x):
            k = loc[0]
            l = loc[1]
            if (radius >= abs(i - k) and radius >= abs(j - l)):
                image[i][j] = (BLACK)


def blur_image(image, radius):
    '''
    A function that takes an image and a radius for an image and then computes 
    a new image in which each pixel is a blurred version. The region is 
    determined by the radius. 

    Input: 
        image(lst) : a list of lists of tuples
        radius(int) : an integer
    
    Output:
        new_image(lst): a lst of lists of tuples
    '''
    loc = ()
    x,y = loc
    region = find_region_locations(image, loc, radius)
    new_image = []
    count = 0
    for i in region:
        lst = []
        for tup in i:
            red_sum = red_sum + tup[0]
            blue_sum = blue_sum + tup[1]
            green_sum = green_sum + tup[2]
            count = count + 1
        lst.append((red_sum/count, blue_sum/count, green_sum/count))
    new_image.append(lst)
    return new_image