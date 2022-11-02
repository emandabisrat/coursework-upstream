"""
CMSC 14100
Autumn 2022

Test code for Homework #5
"""

import json
import os
import sys
import pytest
import test_helpers as helpers
import image_helpers as ih

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw5

MODULE = "hw5"

def check_result(actual, expected, recreate_msg):
    """
    Do the work of checking the result when the
    correctness test is equality.
    """
    # We expect a result is not None
    helpers.check_not_none(actual, recreate_msg)
    # We expect a result of the right type
    helpers.check_type(actual, expected, recreate_msg)
    # We expect a result that is the same value as an expected value
    helpers.check_equals(actual, expected, recreate_msg)

def check_color(t):
    """
    Verify that t has type (int, int, int) and that the values
    all fall between 0 and 255 inclusive
    """
    return (isinstance(t, tuple) and
            len(t) == 3 and
            all(isinstance(v, int) and 0 <= v <= 255 for v in t))

def check_image(actual, expected, recreate_msg):
    """
    Do the work of checking that the actual image (represented using (byte, byte, byte)
    matches the expected image.
    """

    type_error_msg = "Expected a list of list of (int, int, int)\n"
    if recreate_msg is not None:
        type_error_msg += "\n" + recreate_msg
    helpers.check_2D_type(check_color, actual, type_error_msg)

    helpers.check_2D(lambda a, e: pytest.approx(e) == a,
                     actual, expected, recreate_msg)


def check_image_unmodified(param_name, before, after, recreate_msg=None):
    """
    Generate an error if a list was modified when modifications
    are disallowed.
    """

    msg = "You modified the contents of {} (this is not allowed).\n"
    msg = msg.format(param_name)
    msg += "  Value before your code at location ({}, {}): {}\n"
    msg += "  Value after your code at location ({}, {}):  {}"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    for i, row in enumerate(before):
        for j, before_val in enumerate(row):
            assert before_val is after[i][j], \
                msg.format(i, j, before_val, i, j, after[i][j])

def copy_image(img):
    """
    Make a copy of an image
    """
    # do the copy by hand because we don't want to make new color tuples
    return [list(row) for row in img]


@pytest.mark.parametrize("img_filename, expected_filename",
                         [("tests/test1.ppm", "tests/greyscale1.ppm"),
                          ("tests/test2.ppm", "tests/greyscale2.ppm")])
def test_create_greyscale(img_filename, expected_filename):
    """
    Checks create_greyscale for a specific image.
    """
    rmsg = "To recreate this test in ipython3 run:\n"
    rmsg += f"  img = image_helpers.load_image('{img_filename}')\n"
    rmsg += "  hw5.create_greyscale(img)"

    img = ih.load_image(img_filename)
    img_copy = copy_image(img)
    actual = hw5.create_greyscale(img)
    
    check_image_unmodified("img", img, img_copy, rmsg)
    expected = ih.load_image(expected_filename)
    check_image(actual, expected, rmsg)


@pytest.mark.parametrize("tst_dict",
                         json.load(open("tests/find_region_tests.json")))
def test_find_region_locations(tst_dict):
    """
    Checks find_region_locations for a given image, location, and radius
    """
    img_filename = tst_dict["image_filename"]
    loc = tuple(tst_dict["loc"])
    radius = tst_dict["radius"]
    # json does not support tuples.  Convert index pairs into tuples
    expected = [tuple(t) for t in tst_dict["expected"]]

    rmsg = "To recreate this test in ipython3 run:\n"
    rmsg += f"  img = image_helpers.load_image('{img_filename}')\n"
    rmsg += f"  hw5.find_region_locations(img, {loc}, {radius})"

    img = ih.load_image(img_filename)
    img_copy = copy_image(img)
    actual = hw5.find_region_locations(img, loc, radius)
    
    check_image_unmodified("img", img, img_copy, rmsg)

    # We expect a result is not None
    helpers.check_not_none(actual, rmsg)

    # We expect a result of the right type
    # Check that actual is a list
    helpers.check_type(actual, expected, rmsg)

    # Check that the values in the list are tuples of length 2
    for t in actual:
        assert isinstance(t, tuple) and len(t) == 2, \
            rmsg

    # We expect a result that is the same as expected
    helpers.check_equals(set(actual), set(expected), rmsg)



@pytest.mark.parametrize("tst_dict",
                         json.load(open("tests/blackout_tests.json")))
def test_blackout_region(tst_dict):
    """
    Checks create_greyscale for a specific image.
    """
    img_filename = tst_dict["image_filename"]
    expected_filename = tst_dict["expected_filename"]
    loc = tst_dict["loc"]
    radius = tst_dict["radius"]

    rmsg = "To recreate this test in ipython3 run:\n"
    rmsg += f"  img = image_helpers.load_image('{img_filename}')\n"
    rmsg += f"  hw5.blackout_region(img, {loc}, {radius})"

    img = ih.load_image(img_filename)
    actual = hw5.blackout_region(img, loc, radius)
    
    helpers.check_expected_none(actual)
    
    expected = ih.load_image(expected_filename)
    check_image(img, expected, rmsg)

    
@pytest.mark.parametrize("img_filename, expected_filename, radius",
                         [("tests/test1.ppm", "tests/blur1-1.ppm", 0),
                          ("tests/test1.ppm", "tests/blur1-3.ppm", 1),
                          ("tests/test1.ppm", "tests/blur1-5.ppm", 2),                          
                          ("tests/test2.ppm", "tests/blur2-1.ppm", 0),
                          ("tests/test2.ppm", "tests/blur2-3.ppm", 1),
                          ("tests/test2.ppm", "tests/blur2-5.ppm", 2)])
def test_blur_image(img_filename, expected_filename, radius):
    """
    Checks blur_image for a specific image and radius
    """
    rmsg = "To recreate this test in ipython3 run:\n"
    rmsg += f"  img = image_helpers.load_image('{img_filename}')\n"
    rmsg += f"  hw5.blur_image(img, {radius})"

    img = ih.load_image(img_filename)
    img_copy = copy_image(img)
    actual = hw5.blur_image(img, radius)
    
    check_image_unmodified("img", img, img_copy, rmsg)
    expected = ih.load_image(expected_filename)
    check_image(actual, expected, rmsg)
