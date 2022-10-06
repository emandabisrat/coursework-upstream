"""
CMSC 14100
Autumn 2022

Test code for Homework #3
"""

import copy
import os
import sys

import pytest
import test_helpers as helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw3

MODULE = "hw3"

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



@pytest.mark.parametrize("lst1, lst2, expected",
                         [([1, 2, 3], [1, 1, 2], 2),
                          ([1, 2, 3], [1, 2, 3], 0),
                          ([1, 2, 2], [1, 2, 3], -1),
                          ([1, 2, 3], [-1, -2, -3], 12),
                          ([1.5, 2, 3], [1, 1, 2], 2.5)])
def test_compare_sum(lst1, lst2, expected):
    """
    Test the examples provided in the write up as well as some
    additional cases.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "compare_sum", lst1, lst2)
    lst1_orig = copy.deepcopy(lst1)
    lst2_orig = copy.deepcopy(lst2)
    actual = hw3.compare_sum(lst1, lst2)

    # Make sure the lists have not been modified by the function.
    helpers.check_list_unmodified("lst1", lst1_orig, lst1, recreate_msg)
    helpers.check_list_unmodified("lst2", lst2_orig, lst2, recreate_msg)

    # We expect a result is not None
    helpers.check_not_none(actual, recreate_msg)
    # We expect the result to be a Number
    helpers.check_number(actual, recreate_msg)

    # We expect a result that has the same relationship to zero as
    # the expected value.
    if expected < 0:
        msg = "Expected a value less than zero. Got {}".format(actual)
        msg += "\n" + recreate_msg
        assert actual < 0, msg
    elif expected == 0:
        msg = "Expected zero. Got {}".format(actual)
        msg += "\n" + recreate_msg
        assert actual == 0, msg
    else:
        msg = "Expected a value greater than zero. Got {}".format(actual)
        msg += "\n" + recreate_msg
        assert actual > 0, msg


@pytest.mark.parametrize("lst, idx, expected",
                         [([1, 2, 3, 4], 1, 3),    # interior value, right neighbor largest
                          ([5, 1, 4, 3, 7], 1, 5), # interior value, left neighbor largest
                          ([1, 7, 3, 4], 1, 7),    # interior value, idx largest
                          ([7, 7, 7, 4], 1, 7),    # interior value, all values the same
                          ([1, 2, 3, 4], 0, 4),           # first value, left neighbor largest
                          ([10, 2, 3, 4, 7, 8], 0, 10),   # first value, idx largest
                          ([10, 11, 6, 4, 7, 8], 0, 11),  # first value, right neighbor largest
                          ([11, 11, 11, 4, 7, 8], 0, 11), # first value, all values the same
                          ([1, 2, 20, 4], 3, 20),         # last value, left neighbor largest
                          ([10, 2, 3, 4, 7, 27], 5, 27),   # last value, idx largest
                          ([10, 2, 11, 4, 7, 8], 5, 10),  # last value, right neighbor largest
                          ([11, 1, 1, 4, 11, 11], 5, 11), # last value, all values the same
                          ([1], 0, 1), # exactly one value in the list
                          ([1, 2], 0, 2), # exactly two values in the list
                          ([1, 2], 1, 2) # exactly two values in the list
                          ])
def test_largest_of_three(lst, idx, expected):
    """
    Test largest_of_tree
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "largest_of_three", lst, idx)
    lst_orig = copy.deepcopy(lst)
    actual = hw3.largest_of_three(lst, idx)
    # Make sure the list has not been modified by the function.
    helpers.check_list_unmodified("lst", lst_orig, lst, recreate_msg)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("n, expected",
                         [(0, 1),
                          (1, 1),
                          (2, 1),
                          (3, 2),
                          (4, 2),
                          (9, 9),
                          (12, 21),
                          (14, 37),
                          (17, 86),
                          (21, 265)])
def test_seq(n, expected):
    """
    Test the first few elements of the sequence.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "seq", n)
    actual = hw3.seq(n)
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("lst, a, b, expected",
                         [([], 5, 6, []),   # empty list
                          # one a
                          ([10], 10, 12, [12]),
                          # one b
                          ([12], 10, 12, [10]),
                          # a and b are the same value
                          ([1, 2], 1, 1, [1, 2]),
                          # One copy of a and one copy of b at the start of the list
                          ([1, 7, 8, 9, 10, 11], 1, 7, [7, 1, 8, 9, 10, 11]),
                          # One copy of a and one copy of b at the end of the list
                          ([1, 7, 8, 9, 10, 11], 10, 11, [1, 7, 8, 9, 11, 10]),
                          # Neither a nor b appear in the list
                          ([1, 2, 3, 4, 5], 7, 8, [1, 2, 3, 4, 5]),
                          # Multiple copies of a
                          ([1, 2, 1, 3, 1, 5], 1, 7, [7, 2, 7, 3, 7, 5]),
                          # Multiple copies of b
                          ([1, 2, 1, 3, 1, 5], 7, 1, [7, 2, 7, 3, 7, 5]),
                          # All a
                          ([1, 1, 1, 1], 1, 7, [7, 7, 7, 7]),
                          # All b
                          ([1, 1, 1, 1], 7, 1, [7, 7, 7, 7]),
                          # Try some non integer values
                          (["abc", "def", "abc", "xyz"], "def", "abc", ["def", "abc", "def", "xyz"]),
                          (["abc"], "abc", "x", ["x"]),
                          # Try some values that don't have the same type
                          (["abc"], "abc", 3.2, [3.2]),
                          (["abc", "def", "abc", "xyz", "abc"], "abc", 3.2, [3.2, "def", 3.2, "xyz", 3.2])
                          ])
def test_gen_swap(lst, a, b, expected):
    """
    Test gen_swap
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "gen_swap", lst, a, b)
    lst_orig = copy.deepcopy(lst)
    actual = hw3.gen_swap(lst, a, b)

    # Make sure the list has not been modified by the function.
    helpers.check_list_unmodified("lst", lst_orig, lst, recreate_msg)

    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("lst, expected",
                         [([5], hw3.ALL_MATCH),
                          ([10]*101, hw3.ALL_MATCH),
                          ([35]*100, hw3.ALL_MATCH),
                          ([5, 7], hw3.NOT_ANY_MATCH),
                          ([11] + [10]*101, hw3.NOT_ANY_MATCH),
                          ([5, 5, 7], hw3.SOME_MATCH),
                          ([5, 7, 5, 8], hw3.SOME_MATCH),
                          ([5, 7, 5, 8, 5], hw3.SOME_MATCH),
                          ([27, 3, 3, 3, 3, 3, 27], hw3.SOME_MATCH),
                          ([27, 3, 27, 3, 27, 27, 27], hw3.SOME_MATCH)
                          ])
def test_how_many_equal_first(lst, expected):
    """
    Test how_many_equal_first
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "how_many_equal_first", lst)
    lst_orig = copy.deepcopy(lst)
    actual = hw3.how_many_equal_first(lst)
    # Make sure the list has not been modified by the function.
    helpers.check_list_unmodified("lst", lst_orig, lst, recreate_msg)

    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("lst1, lst2, expected",
                         [([1, 2, 3], [4, 5, 6], [1, 4, 2, 5, 3, 6]),
                          ([1, 2, 3], [4, 5, 6, 7, 8], [1, 4, 2, 5, 3, 6, 3, 7, 3, 8]),
                          ([1], [1, 2, 3, 4], [1, 1, 1, 2, 1, 3, 1, 4]),
                          ([5], [1, 2, 3, 4], [5, 1, 5, 2, 5, 3, 5, 4]),
                          ([1, 2, 3, 4], [5], [1, 5, 2, 5, 3, 5, 4, 5]),
                          (["a", "b"], [1, 2], ["a", 1, "b", 2]),
                          (["the end", "the end", "the end"],
                           ["is never"],
                           ["the end", "is never", "the end", "is never", "the end", "is never"])])
def test_intercalate_lists(lst1, lst2, expected):
    """
    Test the examples provided in the write up as well as some
    additional cases.
    """
    recreate_msg = helpers.gen_recreate_msg(MODULE, "intercalate_lists", lst1, lst2)

    lst1_orig = copy.deepcopy(lst1)
    lst2_orig = copy.deepcopy(lst2)

    actual = hw3.intercalate_lists(lst1, lst2)

    # Make sure the lists have not been modified by the function.
    helpers.check_list_unmodified("lst1", lst1_orig, lst1, recreate_msg)
    helpers.check_list_unmodified("lst2", lst2_orig, lst2, recreate_msg)

    check_result(actual, expected, recreate_msg)
