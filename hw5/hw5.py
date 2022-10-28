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
            grey = (((77 * red) + (150 * green) + (29 * blue))//256)
            new_image.append((grey, grey, grey))
    return new_image
def find_region_locations(image, loc, radius):
    ### Replace the body of this function with your solution.
    lst = []
    for i, x in enumerate(image):
        for j, item in enumerate(x):
            k = loc[0]
            l = loc[1]
            if radius >= abs(i - k) and radius >= abs(j - l):
                lst.append((i,j))
    return lst
    
def blackout_region(image, loc, radius):
    ### Replace the body of this function with your solution.
    for i, x in enumerate(image):
        for j, item in enumerate(x):
            k = loc[0]
            l = loc[1]
            if (radius >= abs(i - k) and radius >= abs(j - l)):
                image[i][j] == BLACK
                image.append((image[i][j]))
    return image

def blur_image(image, radius):
    ### Replace the body of this function with your solution.
    new_image = []
    for i in image:
        for x in i:
            red_sum = red_sum + x[0]
            blue_sum = blue_sum + x[1]
            green_sum = green_sum + x[2]
            
    red_avg = red_sum/len(red_sum)
    blue_avg = blue_sum/len(blue_sum)
    green_avg = green_sum/len(green_sum)
    new_image.append(red_avg, blue_avg, green_avg)
    return new_image