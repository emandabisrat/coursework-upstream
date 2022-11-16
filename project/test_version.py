"""
CMSC 14100
Autumn 2022

Test code for Project #1 Version Class
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
import version

MODULE = "version"

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



@pytest.mark.parametrize("lst, check, expected",
                [
                    (["1.0.0","1","1.0","1."],"1.0.0",True),
                    (["1.2","1.0",],"1.1.0",False),
                    (["1.1","1","1."],"1.1.1",True),
                    (["4","4.17","4.17.3",],"4.17.3",True),
                    (["1.2.0","1.1.2",],"1.1.1",False),
                    (["4.17.4","4.16.","4.16","5.","3."],"4.17.3",False),
                ])
def test_version_compatibility(lst, check, expected):
    ver = version.Version(check)
    recreate_base = ("To recreate this test in ipython3 run:\n"
        "import version\n"
        f"ver = version.Version(\"{check}\")\n")
    for version_str in lst:
        recreate_msg = (recreate_base + 
            f"version2 = version.Version(\"{version_str}\")\n"
            "ver.meets_requirement(version2)")
        version2 = version.Version(version_str)
        check_result(ver.meets_requirement(version2),expected, recreate_msg)
    
@pytest.mark.parametrize("a, b, expected",
                [
                    ("1.0.0","1.0.0",0),
                    ("1.0.1","1.0.0",1),
                    ("1.0.1","1.",1),
                    ("1.0.0","1.0.1",-1),
                    ("2.0.0","1.0.1",1),
                    ("1.4.0","1.4.1",-1),
                    ("1.9.3","2.4.1",-1),
                    ("1.9.3","2.",-1),
                    ('2.2.2', '1.9.9', 1) ,
                    ('2.2.2', '1.0.0', 1) ,
                    ('2.2.2', '2.0.1', 1) ,
                    ('2.2.2', '2.0.0', 1) ,
                    ('2.2.2', '9.0.10', -1) ,
                    ('2.2.2', '2.2.0', 1) ,
                    ('2.2.2', '2.2.1', 1) ,
                    ('2.2.2', '2.2.2', 0) ,
                    ('2.2.2', '2.2.3', -1) ,
                    ('2.2.2', '2.2.22', -1) ,
                    ('2.2.2', '222.22222.22222222', -1) ,
                ])
def test_version_exact_compare(a, b, expected):
    recreate_msg = ("To recreate this test in ipython3 run:\n"
    "import version\n"
    f"verA = version.Version(\"{a}\")\n"
    f"verB = version.Version(\"{b}\")\n"
    "verA.compare_version(verB)")
    verA = version.Version(a)
    verB = version.Version(b)
    helpers.check_equals(verA.compare_version(verB), expected, recreate_msg)
    
    
@pytest.mark.parametrize("a, b, expected",
                [
                    ("1.","1.0.1",-1),
                    ("2.","1.0.1",1),
                    ('2', '3.', -1) ,
                    ('2', '2', 0) ,
                    ('2', '1.', 1) ,
                    ('2', '2.0', -1) ,
                    ('2', '2.1', -1) ,
                    ('2', '3.1', -1) ,
                    ('2', '1.9.9', 1) ,
                    ('2', '2.0.1', -1) ,
                    ('2', '2.0.0', -1) ,
                    ('2', '222.22222.22222222', -1) ,
                    ('2.', '2.1', -1) ,
                    ('2.', '1.9.9', 1) ,
                    ('2.2', '2', 1) ,
                    ('2.2', '2.1', 1) ,
                    ('2.2', '2.2', 0) ,
                    ('2.2', '2.2.0', -1) ,
                    ('2.2', '2.2.1', -1) ,
                    ('2.2.2', '2.2.', 1) ,
                    ('2.2.2', '2.3.', -1) ,
                ])
def test_version_partial_compare(a, b, expected):
    recreate_msg = ("To recreate this test in ipython3 run:\n"
    "import version\n"
    f"verA = version.Version(\"{a}\")\n"
    f"verB = version.Version(\"{b}\")\n"
    "verA.compare_version(verB)")
    verA = version.Version(a)
    verB = version.Version(b)
    helpers.check_equals(verA.compare_version(verB), expected, recreate_msg)
    
