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
    new_image = []
    for lst in image:
        for red,green,blue in lst:
            #red = (77 )
            #grey = ((77 * image[lst][red][0]) + (150 * image[lst][green][1]) + (29 * image[lst][blue][2]) / 256)
            grey = int(((77 * red) + (150 * green) + (29 * blue)) / 256)
            #g = int(grey)
            #new = new_image.append(g)
    return image
def find_region_locations(image, loc, radius):
    ### Replace the body of this function with your solution.
    pass

def blackout_region(image, loc, radius):
    ### Replace the body of this function with your solution.
    pass

def blur_image(image, radius):
    ### Replace the body of this function with your solution.
    pass
