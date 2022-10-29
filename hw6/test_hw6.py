"""
CMSC 14100
Autumn 2022

Test code for Homework #6
"""

import copy
import json
import os
import sys

import pytest
import test_helpers as helpers

# Handle the fact that the test code may not
# be in the same directory as the solution code
sys.path.insert(0, os.getcwd())

# Don't complain about the position of the import
# pylint: disable=wrong-import-position
import hw6

MODULE = "hw6"

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


@pytest.mark.parametrize("tst",
                         json.load(open("tests/convert_complex_to_simple.json")))
def test_convert_complex_to_simple_event(tst):
    """
    Test the examples provided in the write up as well as some
    additional cases.
    """

    idx = tst["index"]
    
    recreate_msg = "To recreate this test in ipython3, run:\n"
    recreate_msg += "  data = json.load(open('tests/evm-logs.json'))\n"
    recreate_msg += f"  hw6.convert_complex_to_simple_event(data[{idx}])"

    data = json.load(open('tests/evm-logs.json'))
    complex_event = data[idx]
    complex_event_copy = copy.deepcopy(complex_event)
    actual = hw6.convert_complex_to_simple_event(complex_event)

    # Make sure the dict has not been modified by the function.
    helpers.check_unmodified("complex_event", complex_event, complex_event_copy,
                             recreate_msg)
    check_result(actual, tst["expected"], recreate_msg)


@pytest.mark.parametrize("tst",
                         json.load(open("tests/count_user_events.json")))
def test_count_user_events(tst):
    """
    Test count_user_events on various files.
    """

    input_filename = tst["input_filename"]

    recreate_msg = helpers.gen_recreate_msg(MODULE, "count_user_events", input_filename)

    expected = tst["expected"]
    actual = hw6.count_user_events(input_filename)
    check_result(actual, tst["expected"], recreate_msg)


@pytest.mark.parametrize("tst",
                         json.load(open("tests/load_user_data.json")))
def test_load_user_data(tst):
    """
    Test load_user_data on various files.
    """
    input_filename = tst["input_filename"]

    recreate_msg = helpers.gen_recreate_msg(MODULE, "load_user_data", input_filename)

    expected = json.load(open(tst["output_filename"]))
    actual = hw6.load_user_data(input_filename)
    check_result(actual, expected, recreate_msg)
    

@pytest.mark.parametrize("tst",
                         json.load(open("tests/count_variable_views_per_user.json")))
def test_count_variable_views_per_user(tst):
    """
    Test count_variable_views_per_user on various files
    """
    
    orig_data_filename = tst["orig_filename"]
    user_data_filename = tst["user_filename"]

    recreate_msg = "To recreate this test in ipython3, run:\n"
    recreate_msg += f"  user_data = hw6.load_user_data('{orig_data_filename}')\n"
    recreate_msg += "  hw6.count_variable_views_per_user(user_data)"

    user_data = json.load(open(user_data_filename))
    user_data_copy = copy.deepcopy(user_data)

    actual = hw6.count_variable_views_per_user(user_data)

    # Make sure the lists have not been modified by the function.
    helpers.check_unmodified("user_events", user_data, user_data_copy,
                             recreate_msg)

    expected = tst["expected"]
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("tst",
                         json.load(open("tests/most_complex_view_per_user.json")))
def test_most_complex_view_per_user(tst):
    """
    Test most_complex_view_per_user on various files
    """
    
    orig_data_filename = tst["orig_filename"]
    user_data_filename = tst["user_filename"]

    recreate_msg = "To recreate this test in ipython3, run:\n"
    recreate_msg += f"  user_data = hw6.load_user_data('{orig_data_filename}')\n"
    recreate_msg += "  hw6.most_complex_view_per_user(user_data)"

    user_data = json.load(open(user_data_filename))
    user_data_copy = copy.deepcopy(user_data)

    actual = hw6.most_complex_view_per_user(user_data)

    # Make sure the lists have not been modified by the function.
    helpers.check_unmodified("user_data", user_data, user_data_copy,
                             recreate_msg)

    expected = tst["expected"]
    check_result(actual, expected, recreate_msg)


@pytest.mark.parametrize("tst",
                         json.load(open("tests/compute_max_gap.json")))
def test_compute_max_gap(tst):
    """
    Test compute_max_gap on various files
    """
    
    orig_data_filename = tst["orig_filename"]
    user_data_filename = tst["user_filename"]
    user_id = tst["user_id"]
    var_name = tst["var_name"]

    recreate_msg = "To recreate this test in ipython3, run:\n"
    recreate_msg += f"  user_data = hw6.load_user_data('{orig_data_filename}')\n"
    recreate_msg += f"  hw6.compute_max_gap(user_data, '{user_id}', '{var_name}')"

    user_data = json.load(open(user_data_filename))
    user_data_copy = copy.deepcopy(user_data)

    actual = hw6.compute_max_gap(user_data, user_id, var_name)

    # Make sure the lists have not been modified by the function.
    helpers.check_unmodified("user_events", user_data, user_data_copy,
                             recreate_msg)

    expected = tst["expected"]
    check_result(actual, expected, recreate_msg)
