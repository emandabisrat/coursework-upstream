"""
CMSC 14100
Autumn 2022

Test code for Project #1
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
import library

MODULE = "library"

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
    

@pytest.mark.parametrize("a, b, expected",
                [
                    ("1.0.0","1.0.0",0),
                    ("1.0.1","1.0.0",1),
                    ("1.1.1","1.0.0",1),
                    ("1.0.0","1.0.1",-1),
                    ("2.0.0","1.0.1",1),
                    ("1.4.0","1.4.1",-1),
                    ("1.9.3","2.4.1",-1),
                ])
def test_lib_version_compare(a, b, expected):
    recreate_msg = helpers.gen_recreate_msg(MODULE, "gen_compare", a,b,expected)
    n = "name"
    recreate_msg = ("To recreate this test in ipython3 run:\n"
    "import library\n"
    f"libA = library.Library(\"{n}\",\"{a}\")\n"
    f"libB = library.Library(\"{n}\",\"{b}\")\n"
    "libA.compare_version(libB)")
    libA = library.Library(n,a)
    libB = library.Library(n,b)
    helpers.check_equals(libA.compare_version(libB), expected, recreate_msg)
    
@pytest.mark.parametrize("a, b",
                [
                    ("1.1","1.0.0"),
                    ("1.","1.0.0"),
                    ("1.1.1","1.0."),
                ])
def test_lib_compare_or_create_failure(a, b):
    n = "name"
    recreate_msg = ("This is expecting a failure. To recreate this test in ipython3 run:\n"
    "import library\n"
    f"libA = library.Library(\"{n}\",\"{a}\")\n"
    f"libB = library.Library(\"{n}\",\"{b}\")\n"
    "libA.compare_version(libB)")
    try:
        libA = library.Library(n,a)
        libB = library.Library(n,b)
        helpers.check_equals(libA.compare_version(libB), recreate_msg)
        assert False
    except library.LibraryException:
        assert True
    
def test_mismatched_names_failure():
    recreate_msg = ("Expecting failure. To recreate this test in ipython3 run:\n"
    "import library\n"
    "libA = library.Library(\"name1\",\"1.1.1\")\n"
    "libB = library.Library(\"name2\",\"2.0.2\")\n"
    "libA.compare_version(libB)")
    try:
        libA = library.Library("name1","1.1.1")
        libB = library.Library("name2","2.0.2")
        helpers.check_equals(libA.compare_version(libB), recreate_msg)
        assert False
    except library.LibraryException:
        assert True

@pytest.mark.parametrize("lst, check, expected",
                [
                    (["1.0.0","1","1.0","1."],"1.0.0",True),
                    (["1.2","1.0","0.9","2.1.0"],"1.1.0",False),
                    (["1.1","1","1.","1.1.1"],"1.1.1",True),
                    (["4","4.17","4.17.3",],"4.17.3",True),
                    (["1.2.0","1.1.2","1.3.","1.0","2.1."],"1.1.1",False),
                    (["4.17.4","4.16.","4.16","5.","3."],"4.17.3",False),
                ])
def test_lib_version_compatibility(lst, check, expected):
    libName = "libX"
    recreate_base = ("To recreate this test in ipython3 run:\n"
        "import library\n"
        f"lib = library.Library(\"{libName}\",\"{check}\")\n")
    lib = library.Library(libName, check)
    for version_str in lst:
        recreate_msg = (recreate_base + 
            f"lib.meets_version_req(\"{version_str}\")\n")
        meets_req = lib.meets_version_req(version_str)
        check_result(meets_req, expected, recreate_msg)
