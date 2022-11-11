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
import hub

MODULE = "hub"

def gen_base(expected_to_work = True):
    error = "" if expected_to_work else "Failure expected."
    return(f"{error}To recreate this test in ipython3 run:\n"
        f"import {MODULE}\nlib_hub = hub.LibraryHub()\n")

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

@pytest.mark.parametrize("versions, name, expected",
                [
                    (["1.0.0","1",],"LibX",False),
                    (["1.0",],"LibX",False),
                    (["1.0.",],"LibX",False),
                    (["0.1.0","1.0.0","1.0.1","1.1.1"],"LibX",True),
                    (["0.1.0","1.0.0","1.0.1","1.1.1","1.0.1"],"LibX",False),
                    (["4.0.0","4.17.0","4.17.3",],"LibY",True),
                    (["1.2.0","1.1.2","1.3."],"LibY",False),
                    (["1.0.0","4.17.4","1.0.1","4.18.0","5.0.0","4.17.6"],"LibX",True),
                ])
def test_reg_lib(versions, name, expected):
    lib_hub = hub.LibraryHub()
    no_errors = False
    recreate_msg = gen_base(expected)
    try:
        for v in versions:
            recreate_msg += f"lib_hub.register_new_library(\"{name}\", \"{v}\", False)\n"
            lib = lib_hub.register_new_library(name, v, False)
            if lib is None and expected is not False:
                helpers.check_not_none(lib, recreate_msg)
        no_errors = True
    except hub.LibraryException:
        no_errors = False
        if expected is True:
            # We thought this should pass
            helpers.check_equals(True, False, recreate_msg)
    helpers.check_equals(no_errors, expected, recreate_msg)
  

@pytest.mark.parametrize("versions, latest",
                [
                    ([("1.0.0", False)], "1.0.0"),
                    ([("1.0.0", False),("1.0.1", False)], "1.0.1"),
                    ([("1.0.0", False),("1.1.0", False),("1.0.1", False)], "1.1.0"),
                    ([("1.0.0", False),("1.1.0", False),("2.0.1", False)], "2.0.1"),
                    ([("1.0.0", False),("1.1.0", False),("2.0.1", False),("2.0.2", False),("2.1.1", False),("2.2.1", False)], "2.2.1"),
                    ([("1.0.0", False),("1.1.0", False),("2.0.1", True)], "1.1.0"),
                ])
def test_find_latest(versions,latest):
    """
    Check that the find latest version works, with ignoring testing
    """
    recreate_msg = gen_base()
    lib_hub = hub.LibraryHub()
    name = "LibX"
    for ver in versions:
        recreate_msg += (
        f"lib_hub.register_new_library(\"{name}\", \"{ver[0]}\",is_testing={ver[1]})\n"
        )
        lib = lib_hub.register_new_library(name, ver[0],is_testing=ver[1])
        helpers.check_not_none(lib)
    recreate_msg += (
        f"latest_lib = lib_hub.find_latest_version(\"{name}\")\n"
        f"latest_lib.meets_version_req(\"{latest}\")"
    )
    latest_lib = lib_hub.find_latest_version(name)
    helpers.check_equals(latest_lib.meets_version_req(latest), True, recreate_msg)

@pytest.mark.parametrize("versions, latest",
                [
                    ([("1.0.0", False),("1.0.1", True)], "1.0.1"),
                    ([("1.0.0", False),("1.1.0", True),("2.0.1", False)], "2.0.1"),
                    ([("1.0.0", False),("1.1.0", False),("2.0.1", False),("2.0.2", False),("2.1.1", False),("2.2.1", True)], "2.2.1"),
                    ([("1.0.0", True),("1.1.0", False),("2.0.1", True)], "2.0.1"),
                ])
def test_find_testing_latest(versions,latest):
    """
    Check that the find latest version works, with ignoring testing
    """
    recreate_msg = gen_base()
    lib_hub = hub.LibraryHub()
    name = "LibX"
    for ver, is_testing in versions:
        recreate_msg += (
        f"lib_hub.register_new_library(\"{name}\", \"{ver}\",is_testing={is_testing})\n"
        )
        lib = lib_hub.register_new_library(name, ver, is_testing)
        helpers.check_not_none(lib)
    recreate_msg += (
        f"latest_lib = lib_hub.find_latest_version(\"{name}\", include_testing=True)\n"
        f"latest_lib.meets_version_req(\"{latest}\")"
    )
    latest_lib = lib_hub.find_latest_version(name, include_testing=True)
    helpers.check_equals(latest_lib.meets_version_req(latest), True, recreate_msg)


@pytest.mark.parametrize("versions, checks",
                [
                    (
                        # Libraries to register
                        [("LibX","1.0.0", False),("LibX","1.0.1", True)],
                        # Check get by name/version
                        [("LibX","1.0.0","1.0.0")]
                    ),
                    (
                        # Libraries to register
                        [("LibX","1.0.0", False),("LibX","1.0.1", False)],
                        # Check get by name/version
                        [("LibX","1.0.1","1.0.1"),("LibX","1.0.","1.0.1"),("LibX","1","1.0.1")]
                    ),
                    (
                        # Libraries to register
                        [("LibX","1.0.0", True),("LibX","1.0.1", True)],
                        # Check get by name/version
                        [("LibX","1.0",None), ("LibX","1.",None),]
                    ),
                    (
                        # Libraries to register
                        [("LibX","1.0.0", False),("LibX","1.0.1", True)],
                        # Check get by name/version
                        [
                            ("LibX","1.0.","1.0.0"),
                            ("LibX","1.","1.0.0"),
                            ("LibX","1.0.1","1.0.1")
                        ]
                    ),
                    (
                        # Libraries to register
                        [
                            ("LibX","1.0.0", False), ("LibX","1.1.1", False),
                            ("LibX","1.0.1", False), ("LibY","2.1.1", False)
                        ],
                        # Check get by name/version
                        [
                            ("LibX","1","1.1.1"),
                            ("LibY","1.",None),
                            ("LibY","2.","2.1.1")
                        ]
                    ),
                    (
                        # Libraries to register
                        [("LibX","0.1.0", True),],
                        # Check get by name/version
                        [("LibX","0","0.1.0"), ("LibX","0.1.0","0.1.0"),]
                    ),
                ])
def test_get_lib(versions, checks):
    """
     versions: [ (name, vers, testing)]
     checks [name, ver_req, expected]
    """
    recreate_msg = gen_base()
    lib_hub = hub.LibraryHub()
    for vname,ver,testing in versions:
        recreate_msg += (
            f"lib_hub.register_new_library(\"{vname}\", \"{ver}\", {testing})\n"
        )
        lib = lib_hub.register_new_library(vname, ver, testing)
        helpers.check_not_none(lib, recreate_msg)
    for vname, ver_req, expected in checks:
        lib_check = lib_hub.get_library(vname, ver_req)
        recreate_msg += (
            f"lib_check = lib_hub.get_library(\"{vname}\", \"{ver_req}\")\n"
        )
        if expected is not None:
            helpers.check_not_none(lib_check, recreate_msg)
            recreate_msg += (
                f"test_compare_lib = hub.Library(\"{vname}\", \"{expected}\")\n"
            )
            test_compare_lib = hub.Library(vname,expected)
            recreate_msg += (
                "lib_check.compare_version(test_compare_lib)==0\n"
            )
            helpers.check_equals(lib_check.compare_version(test_compare_lib), 0, recreate_msg)
        else:
            recreate_msg += (
                "lib_check is None\n"
            )
            helpers.check_equals(lib_check, None, recreate_msg)


