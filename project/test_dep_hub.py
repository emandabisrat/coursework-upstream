"""
CMSC 14100
Autumn 2022

Test code for Project #2
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
import hub

MODULE = "project2-Library"

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
    
hub_dep_tests = [
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False)], 
                              [("libbanana", "1.0.0")], 
                              [1],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libenglish", "2.0.1", False)],
                              [("libbanana", "1.0.0"),
                               ("libenglish", "2.0.1")], 
                              [1,2],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "1.")], 
                              [1],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "1.1")], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "3")], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "2.")], 
                              [2],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "2.0")], 
                              [2],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", None)], 
                              [2],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", True)],
                              [("libbanana", None)], 
                              [1],
                              False),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", True),
                               ("libbanana", "2.0.1", True)],
                              [("libbanana", None)], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False)],
                              [("libbanana", "1.")], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "1.")], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "2.0.1", False)],
                              [("libbanana", "2."),("libbanana", "1.")], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", True),
                               ("libenglish", "2.0.1", False)],
                              [("libbanana", "1.0.0"),
                               ("libenglish", "2.0.1")], 
                              [],
                              True),
                             ([("libshoe", "1.2.3", False), 
                               ("libbanana", "1.0.0", False),
                               ("libenglish", "2.0.1", True)],
                              [("libbanana", "1.0.0"),
                               ("libenglish", "2.0.1")], 
                              [],
                              True)
                         ]

@pytest.mark.parametrize("libs_args, deps_args, expected, fails",
                         hub_dep_tests)
def test_hub_add_dep(libs_args, deps_args, expected, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    recreate += "lib_hub = hub.LibraryHub()\n"
    lib_hub = hub.LibraryHub()

    libs = [lib_hub.register_new_library(n,v,t) for (n,v,t) in libs_args]
    deps = [libs[i] for i in expected]
    lib_name, lib_ver, lib_test = libs_args[0]
    lib = libs[0]

    libs_str = [f"lib_hub.register_new_library('{n}', '{v}', {t})" for (n,v,t) in libs_args]
    recreate += "\n".join(libs_str) + "\n\n"
    recreate += f"deps = {deps_args}\n"
    try:
        for dn, dv in deps_args:
            recreate += f"lib_hub.add_dependency('{lib_name}', '{lib_ver}', '{dn}', '{dv}')\n"
            added = lib_hub.add_dependency(lib_name, lib_ver, dn, dv)
            helpers.check_expected_none(added, recreate)
        recreate += f"lib_hub.get_library('{lib_name}', '{lib_ver}').get_dependencies()\n"
        check_result(set(lib.get_dependencies()), set(deps), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate

@pytest.mark.parametrize("libs_args, deps_args, expected, fails",
                         hub_dep_tests)
def test_hub_add_multiple_deps(libs_args, deps_args, expected, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    recreate += "lib_hub = hub.LibraryHub()\n"
    lib_hub = hub.LibraryHub()

    libs = [lib_hub.register_new_library(n,v,t) for (n,v,t) in libs_args]
    deps = [libs[i] for i in expected]
    lib_name, lib_ver, lib_test = libs_args[0]
    lib = libs[0]

    libs_str = [f"lib_hub.register_new_library('{n}', '{v}', {t})" for (n,v,t) in libs_args]
    recreate += "\n".join(libs_str) + "\n\n"
    recreate += f"deps = {deps_args}\n"
    recreate += f"lib_hub.add_dependencies('{lib_name}', '{lib_ver}', deps)\n"
    try:
        added = lib_hub.add_dependencies(lib_name, lib_ver, deps_args)
        helpers.check_expected_none(added, recreate)
        recreate += f"lib_hub.get_library('{lib_name}', '{lib_ver}').get_dependencies()\n"
        check_result(set(lib.get_dependencies()), set(deps), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate

@pytest.mark.parametrize("libs_args, deps_args, expected, fails",
                         hub_dep_tests)
def test_hub_deps_init(libs_args, deps_args, expected, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    recreate += "lib_hub = hub.LibraryHub()\n"
    lib_hub = hub.LibraryHub()

    libs = [lib_hub.register_new_library(n,v,t) for (n,v,t) in libs_args[1:]]
    deps = [libs[i-1] for i in expected]
    lib_name, lib_ver, lib_test = libs_args[0]

    libs_str = [f"lib_hub.register_new_library('{n}', '{v}', {t})" 
                for (n,v,t) in libs_args[1:]]
    recreate += "\n".join(libs_str) + "\n\n"
    recreate += f"deps = {deps_args}\n"
    recreate += f"lib_hub.register_new_library('{lib_name}', '{lib_ver}', dependencies = deps)\n"
    try:
        lib = lib_hub.register_new_library(lib_name, lib_ver,
                                           dependencies=deps_args)
        check_result(set(lib.get_dependencies()), set(deps), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate

@pytest.mark.parametrize("libs_args, init_deps, upd_args, expected, fails",
                         [
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", False)], 
                              [1], 
                              ("libbanana", "1.0.1"), 
                              [2], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", False)], 
                              [1], 
                              ("libbanana", "1."), 
                              [2], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", False),
                               ("libbanana", "2.0.1", False)], 
                              [1], 
                              ("libbanana", "1."), 
                              [2], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", False),
                               ("libbanana", "2.0.1", False)], 
                              [1], 
                              ("libbanana", "2."), 
                              [3], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", True),
                               ("libbanana", "2.0.1", False)], 
                              [3], 
                              ("libbanana", "1"), 
                              [1], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", False),
                               ("libbanana", "2.0.1", False)], 
                              [1], 
                              ("libbanana", None), 
                              [3], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", False)], 
                              [1], 
                              ("libbanana", None), 
                              [2], 
                              False),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", True),
                               ("libbanana", "1.0.1", True)], 
                              [], 
                              ("libbanana", None), 
                              [], 
                              True),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", True)], 
                              [1], 
                              ("libbanana", None), 
                              [], 
                              True),
                             ([("libshoe", "1.2.3", False),
                               ("libbanana", "1.0.0", False),
                               ("libbanana", "1.0.1", True)], 
                              [1], 
                              ("libbanana", "1.0.1"), 
                              [], 
                              True)
                         ])
def test_hub_update_deps(libs_args, init_deps, upd_args, expected, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    recreate += "lib_hub = hub.LibraryHub()\n"
    lib_hub = hub.LibraryHub()

    libs = [lib_hub.register_new_library(n,v,t) for (n,v,t) in libs_args]
    recreate += (f"libs = [" +
                 f"\n        ".join([f"lib_hub.register_new_library('{n}', '{v}', {t})" 
                                     for (n,v,t) in libs_args]) +
                 f"]\n")
    deps_start = [libs[i] for i in init_deps]
    deps_expected = [libs[i] for i in expected]

    lib_name, lib_ver, _ = libs_args[0]
    lib = libs[0]

    recreate += "\n".join([f"libs[0].add_dependency(libs[{i}])" 
                           for i in init_deps]) + "\n"
    for dep in deps_start:
        lib.add_dependency(dep)

    upd_name, upd_ver = upd_args
    recreate += (f"lib_hub.update_dependency('{lib_name}', '{lib_ver}', "
                 f"'{upd_name}', '{upd_ver}')\n\n")
    try:
        updated = lib_hub.update_dependency(lib_name, lib_ver, upd_name, upd_ver)
        helpers.check_expected_none(updated, recreate)
        check_result(set(lib.get_dependencies()), set(deps_expected), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        check_result(set(lib.get_dependencies()), set(deps_start), recreate)
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate
