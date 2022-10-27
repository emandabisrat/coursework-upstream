"""
CMSC 14100
Autumn 2022

Test helper functions
"""

import pytest

def gen_recreate_msg(module, function, *params):
    """
    Generate a message to explain how to recreate a test
    in ipython.
    """
    params_str = ", ".join([str(p) for p in params])

    recreate_msg = "To recreate this test in ipython3 run:\n"
    recreate_msg += "  {}.{}({})".format(module, function, params_str)

    return recreate_msg


def check_not_none(actual, recreate_msg=None):
    """
    Generate an error if the actual value is unexpectedly none.
    """

    msg = "The function returned None."
    msg += " Did you forget to replace the placeholder value we provide?"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is not None, msg


def check_expected_none(actual, recreate_msg=None):
    """
    Generate an error if the actual value is not none
    """

    msg = "The function returned a value other than the expected value: None."
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual is None, msg


def check_type(actual, expected, recreate_msg=None):
    """
    Generate an error if the actual value has the wrong type.
    """
    actual_type = type(actual)
    expected_type = type(expected)

    msg = "The function returned a value of the wrong type.\n"
    msg += "  Expected return type: {}.\n".format(expected_type.__name__)
    msg += "  Actual return type: {}.".format(actual_type.__name__)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert isinstance(actual, expected_type), msg


def check_equals(actual, expected, recreate_msg=None):
    """
    Generate an error if the actual and expected values are not
    equal.
    """
    msg = "Actual ({}) and expected ({}) values do not match."
    msg = msg.format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert actual == expected, msg


def check_float_equals(actual, expected, recreate_msg=None):
    """
    Generate an error if the actual and expected values do not
    fall within epsilon of each other.
    """
    msg = "Actual ({}) and expected ({}) values do not match."
    msg = msg.format(actual, expected)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert pytest.approx(expected) == actual, msg


def check_list_unmodified(param_name, before, after, recreate_msg=None):
    """
    Generate an error if a list was modified when modifications
    are disallowed.
    """

    msg = "You modified the contents of {} (this is not allowed).\n"
    msg = msg.format(param_name)
    msg += "  Value before your code: {}\n".format(before)
    msg += "  Value after your code:  {}".format(after)
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    assert before == after, msg


def check_2D_type(check_element_type_fn, actual, error_msg=None):
    """
    Generate an error if actual is not a list of lists.  Or if an
    element has the wrong type.
    """
    assert isinstance(actual, list), error_msg
    for row in actual:
        assert isinstance(row, list)
        for val in row:
            assert check_element_type_fn(val), error_msg


def check_2D_shape(actual, expected, recreate_msg):
    """
    Check that a list of lists has the right shape
    """

    msg = "The actual shape of the result does not match the expected shape\n"
    msg += "  Expected: {} x {}\n"
    msg += "  Actual: {} x {}\n"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    expected_n = len(expected)
    expected_m = len(expected[0])

    actual_n = len(actual)
    actual_m = len(actual[0])

    assert actual_n == expected_n and actual_m == expected_m, \
        msg.format(expected_n, expected_m, actual_n, actual_m)

    msg = "The rows in the actual result should all be of length {}"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    for row in actual:
        assert len(row) == actual_m, msg.format(expected_m)


def check_2D(check_val_fn, actual, expected, recreate_msg=None):
    """
    Generate an error if at least one entry in actual does not match expected.
    """
    check_2D_shape(actual, expected, recreate_msg)

    msg = "Actual and expected values do not match at location ({}, {}).\n"
    msg += "   Expected value: {}\n"
    msg += "   Actual value: {}"
    if recreate_msg is not None:
        msg += "\n" + recreate_msg

    for i, row in enumerate(expected):
        for j, val in enumerate(row):
            if not check_val_fn(val, actual[i][j]):
                assert False, msg.format(i, j, val, actual[i][j])
