"""
CMSC 14100
Autumn 2022

Test code for Homework #2
"""

import os
import sys

import pytest
import test_helpers as helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw2

MODULE = "hw2"

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

@pytest.mark.parametrize("a, x, expected", 
                         [(0, 0, 0),
                          (5, 2, 12),
                          (5, 0, 0),
                          (9, 1, 10),
                          (9, -2, -20),
                          (-11, 2, -20)])
def test_add_one_and_multiply(a, x, expected):
    """
    Do a single test for Exercise 1: add_one_and_multiply
    """                     
    recreate_msg = helpers.gen_recreate_msg(MODULE, "add_one_and_multiply",
                                            a, x)
    actual = hw2.add_one_and_multiply(a, x)
    check_result(actual, expected, recreate_msg)

@pytest.mark.parametrize("a, b, n, expected",
                         [(2, 4, 2, True),
                          (2, 7, 5, True),
                          (1, 10, 4, False),
                          (8, -8, 5, False),
                          (-8, 7, 5, True)])
def test_are_congruent_mod_n(a, b, n, expected):
    """
    Do a single test for Exercise 2: are_congruent_mod_n.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "are_congruent_mod_n",
                                            a, b, n)
    actual = hw2.are_congruent_mod_n(a, b, n)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("amount, principle, time, expected",
                         [(1250.0, 1000.0, 4.0, 6.25),
                          (1000.0, 1000.0, 4.0, 0.0),
                          (1332.0, 750.0, 10.0, 7.76),
                          (1999.5, 1500, 4.5, 7.4)])
def test_find_interest_rate(amount, principle, time, expected):
    """
    Do a single test for Exercise 3: find_interest_rate
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "find_interest_rate",
                                            amount, principle, time)
    actual = hw2.find_interest_rate(amount, principle, time)
    helpers.check_not_none(actual, recreate_msg)
    helpers.check_type(actual, expected, recreate_msg)
    helpers.check_float_equals(actual, expected, recreate_msg)


##### County classification test cases #####

county_classes = \
    [(8500000, 303.0, "urban"),  # NYC: Urban
     (2700000, 228.0, "urban"),  # Chicago: Urban

     ## Population at urban threshold
     # Population density just above urban threshold
     (50000, 49.99, "urban"),
     # Population density at urban threshold
     (50000, 50.0, "urban"),
     # Population density just below urban threshold
     (50000, 50.0009, "other"),

     ## Population below urban threshold
     # Population density above urban threshold
     (49999, 49.5, "other"),
     # population density just below urban threshold
     (49999, 50.0, "other"),

     ## Population meets rural threshold
     # Population density at rural threshold
     (2500, 5, "rural"),
     # Population density above rural threshold
     (2500, 2.0, "other"),
     # Population density below threshold
     (2500, 5.00001, "rural"),

     ## Population meets rural threshold
     # Population density at rural threshold
     (1000, 2, "rural"),
     # Population density above rural threshold
     (1000, 1.5, "other"),
     # Population density below threshold
     (1000, 2.5, "rural"),

     ## Population neither rural nor urban
     # Population density at rural threshold
     (5000, 10, "other"),
     # Population density at below rural threshold
     (5000, 20, "other"),
     # Population density at urban threshold
     (5000, 5, "other"),
     # Population density at above urban threshold
     (5000, 4.99, "other")]


@pytest.mark.parametrize("population, area, label", county_classes)
def test_is_urban_county(population, area, label):
    """
    Do a single test for Exercise 4: is_urban_county
    """
    expected = label.lower() == "urban"
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_urban_county",
                                            population, area)
    actual = hw2.is_urban_county(population, area)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("population, area, label", county_classes)
def test_is_other_county(population, area, label):
    """
    Do a single test for Exercise 5: is_other_county
    """
    expected = label.lower() not in ["urban", "rural"]
    recreate_msg = helpers.gen_recreate_msg(MODULE, "is_other_county",
                                            population, area)
    actual = hw2.is_other_county(population, area)
    check_result(actual, expected, recreate_msg)


# Use a test name that does not have "is_other_county" as a substring
# to simplify grader.py.
@pytest.mark.parametrize("population, area, label", county_classes)
def test_alt_other_county(population, area, label):
    """
    Do a single test for Exercise 6: alt_is_other_county
    """
    expected = label.lower() not in ["urban", "rural"]
    recreate_msg = helpers.gen_recreate_msg(MODULE, "alt_is_other_county",
                                            population, area)
    actual = hw2.alt_is_other_county(population, area)
    check_result(actual, expected, recreate_msg)

@pytest.mark.parametrize("population, area, expected", county_classes)
def test_label_county(population, area, expected):
    """
    Do a single test for Exercise 7: label_county
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "label_county",
                                            population, area)
    actual = hw2.label_county(population, area)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("length, weight, expected",
                         [(10, 33000, 300),   # above weight threshold
                          (20, 33000, 300),
                          (40, 33000, 300),

                          (10, 30000, 75),    # just below weight threshold
                          (20, 30000, 150),   # just below weight threshold
                          (40, 30000, 300),   # just below weight threshold

                          (10, 2500, 75),     # well below weight threshold
                          (20, 2500, 150),
                          (40, 2500, 300)])
def test_compute_fee(length, weight, expected):
    """
    Do a single test for Exercise 8: compute_fee
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "compute_fee",
                                            length, weight)
    actual = hw2.compute_fee(length, weight)
    check_result(actual, expected, recreate_msg)
