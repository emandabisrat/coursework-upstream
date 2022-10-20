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
    params = [str(p) if not isinstance(p, str) else f"'{p}'" for p in params]

    params_str = ", ".join(params)

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
