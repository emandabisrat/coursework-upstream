"""
CMSC 14100
Autumn 2022

Test code for Homework #4
"""

import os
import sys
from tabnanny import check
from threading import activeCount

import pytest
import test_helpers as helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw4

MODULE = "hw4"

def check_result(actual, expected, recreate_msg):
    """
    Do the work of checking the result when the
    correctness test is equality.
    """
    # We expect a result is not None
    helpers.check_not_none(actual, recreate_msg)
    # We expect a result of the right type
    helpers.check_type(actual, expected, recreate_msg)
    # We expect a result that is the same as expected
    helpers.check_equals(actual, expected, recreate_msg)


@pytest.mark.parametrize("u, v, expected", 
                         [('morning', 'mourning', 11),
                          ('nigh', 'night', 1),
                          ('nightingale', 'night', 6),
                          ('same', 'same', 0),
                          ('hello', 'friend', 11),
                          ('', 'void', 4),
                          ('void', '', 4),
                          ('', '', 0)])
def test_prefix_distance(u, v, expected):
    """
    Checks prefix_distance() with some short to medium lenght strings.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "prefix_distance", u, v)
    actual = hw4.prefix_distance(u, v)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("u, v, expected",
                         [('morning', 'mourning', 5),
                          ('same', 'same', 0),
                          ('hello', 'friend', 11),
                          ('careless', 'hairless', 8),
                          ('suspicion', 'ion', 6),
                          ('', 'void', 4),
                          ('void', '', 4),
                          ('', '', 0)])
def test_suffix_distance(u, v, expected):
    """
    Checks suffix_distance() with some short and medium lenght strings.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "suffix_distance", u, v)
    actual = hw4.suffix_distance(u, v)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("text, width, expected",
                         [("1234 678", 3, 1),
                          ("Alas, poor Yorick!", 4, 1),
                          ("Beyond the black rainbow", 10, 125),
                          ("Crawling in monochromatic hallways",
                           10, 547),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.",
                           20, 10)])
def test_total_badness(text, width, expected):
    """
    Checks total_badness() with some short and medium lenght strings.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "total_badness", text, width)
    actual = hw4.total_badness(text, width)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("text, width, expected",
                         [("1234 678", 3, ["1234", "678"]),
                          ("Alas, poor Yorick!", 4, ["Alas,","poor","Yorick!"]),
                          ("Beyond the black rainbow", 
                           10, ["Beyond the", "black", "rainbow"]),
                          ("Crawling in monochromatic hallways",
                           10, ["Crawling", "in", "monochromatic", "hallways"]),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.",
                           20, ["If you can look into", "the seeds of time,",
                                "and say which grain", "will grow and which",
                                "will not."])])
def test_split_lines(text, width, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "split_lines", text, width)
    actual = hw4.split_lines(text, width)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("text, width, blanks_visible, expected",
                         [("1234 678", 3, False, "1234\n678"),
                          ("Alas, poor Yorick!", 4, False, "Alas,\npoor\nYorick!"),
                          ("Beyond the black rainbow", 
                           10, False, "Beyond the\nblack\nrainbow"),
                          ("Crawling in monochromatic hallways",
                           10, False, "Crawling\nin\nmonochromatic\nhallways"),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.",
                           20, False,
                           "If you can look into\nthe seeds of time,\nand say which grain\nwill grow and which\nwill not."),
                          ("1234 678", 3, True, "1234\n678"),
                          ("Alas, poor Yorick!", 5, True, "Alas,\npoor_\nYorick!"),
                          ("Beyond the black rainbow", 
                           10, True, "Beyond the\nblack_____\nrainbow___"),
                          ("Crawling in monochromatic hallways",
                           10, True, 
                           "Crawling__\nin________\nmonochromatic\nhallways__"),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.",
                           20, True,
                           "If you can look into\nthe seeds of time,__\nand say which grain_\nwill grow and which_\nwill not.___________")])
def test_arrange_lines(text, width, blanks_visible, expected):
    recreate_msg = helpers.gen_recreate_msg(
                        MODULE, "arrange_lines", text, width, blanks_visible)
    actual = hw4.arrange_lines(text, width, blanks_visible)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("text, width, expected",
                         [("1234 678", 3, "1234\n678"),
                          ("Alas, poor Yorick!", 4, "Alas,\npoor\nYorick!"),
                          ("Beyond the black rainbow", 
                           10, "Beyond the\nblack\nrainbow"),
                          ("Crawling in monochromatic hallways",
                           10, "Crawling\nin\nmonochromatic\nhallways"),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.", 20,
                           "If you can look into\nthe seeds of time,\nand say which grain\nwill grow and which\nwill not.")])
def test_arrange_lines_optional(text, width, expected):
    recreate_msg = helpers.gen_recreate_msg(
                        MODULE, "arrange_lines", text, width)
    actual = hw4.arrange_lines(text, width)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("text, min_width, max_width, expected",
                         [("1234 678", 0, 80, 4),
                          ("Alas, poor Yorick!", 0, 80, 10),
                          ("Beyond the black rainbow", 0, 80, 16),
                          ("Crawling in monochromatic hallways", 0, 80, 25),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.",
                           0, 80, 39),
                          ("1234 678", 5, 80, 8),
                          ("Alas, poor Yorick!", 0, 8, 4),
                          ("Beyond the black rainbow", 5, 20, 16),
                          ("Crawling in monochromatic hallways", 0, 20, 12),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.",
                           0, 39, 39)])
def test_optimal_width(text, min_width, max_width, expected):
    recreate_msg = helpers.gen_recreate_msg(
                        MODULE, "optimal_width", text, min_width, max_width)
    actual = hw4.optimal_width(text, min_width, max_width)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("text, expected",
                         [("1234 678", 4),
                          ("Alas, poor Yorick!", 10),
                          ("Beyond the black rainbow", 16),
                          ("Crawling in monochromatic hallways", 25),
                          ("If you can look into the seeds of time, and say which grain will grow and which will not.", 39)])
def test_optimal_width_optional(text, expected):
    recreate_msg = helpers.gen_recreate_msg(
                        MODULE, "optimal_width", text)
    actual = hw4.optimal_width(text)
    check_result(actual, expected, recreate_msg)