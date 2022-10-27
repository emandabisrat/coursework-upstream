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
BLACK = (0, 0, 0)


def create_greyscale(image):
    ### Replace the body of this function with your solution.
    
    for tup in image:
        for red,green,blue in tup:
            grey = ((77 * image[tup][i][0]) + (150 * image[tup][i][1]) + (29 * image[tup][i][2]))
            #grey = ((77 * i[0]) + (150 * i[1]) + (29 * i[2]))
            g = int(grey)
    return g
def find_region_locations(image, loc, radius):
    ### Replace the body of this function with your solution.
    pass

def blackout_region(image, loc, radius):
    ### Replace the body of this function with your solution.
    pass

def blur_image(image, radius):
    ### Replace the body of this function with your solution.
    pass
