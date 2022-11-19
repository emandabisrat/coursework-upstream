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
    
basic_dep_cases = [
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", False)], 
                                 False),
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", False)], 
                                 False),
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", False),
                                  ("libenglish", "2.0.1", False)], 
                                 False),
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", True)], 
                                 True),
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", False), 
                                  ("libbanana", "1.0.0", False)], 
                                 True),
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", True), 
                                  ("libbanana", "2.0.0", False)], 
                                 True),
                             (("libshoe", "1.2.3"), 
                                 [("libbanana", "1.0.0", False), 
                                  ("libbanana", "2.0.0", True)], 
                                 True)
                         ]

@pytest.mark.parametrize("lib_args, deps_args, fails",
                         basic_dep_cases)
def test_lib_basic_init(lib_args, deps_args, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    lib_name, lib_ver = lib_args
    deps = [library.Library(n,v,t) for (n,v,t) in deps_args]
    deps_str = [f"library.Library('{n}', '{v}', {t})" for (n,v,t) in deps_args]
    recreate += "deps = [" + ",\n        ".join(deps_str) + "]\n"
    recreate += f"lib = library.Library('{lib_name}', '{lib_ver}', dependencies=deps)\n"
    try:
        lib = library.Library(lib_name, lib_ver, dependencies=deps)
        recreate += f"lib.get_dependencies()\n\n\n"
        actual = lib.get_dependencies()
        helpers.check_type(actual, deps, recreate)
        check_result(set(actual), set(deps), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate


@pytest.mark.parametrize("lib_args, deps_args, fails",
                         basic_dep_cases)
def test_lib_basic_add(lib_args, deps_args, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    lib_name, lib_ver = lib_args
    lib = library.Library(lib_name, lib_ver)
    recreate += (f"lib = library.Library('{lib_name}', '{lib_ver}')\n")
    deps = [library.Library(n,v,t) for (n,v,t) in deps_args]
    try:
        for i, (n,v,t) in enumerate(deps_args):
            recreate += f"lib.add_dependency(library.Library('{n}', '{v}', {t}))\n"
            added = lib.add_dependency(deps[i])
            helpers.check_expected_none(added, recreate)
        recreate += f"lib.get_dependencies()\n\n\n"
        actual = lib.get_dependencies()
        helpers.check_type(actual, deps, recreate)
        check_result(set(actual), set(deps), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate


@pytest.mark.parametrize("libs_args, deps_args, depth, expected",
                         [
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0")], 
                                 [], 
                                 0,
                                 []),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0")], 
                                 [[1]], 
                                 0,
                                 [1]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5")], 
                                 [[1,2]], 
                                 0,
                                 [1,2]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5")], 
                                 [[1],
                                  [2]], 
                                 0,
                                 [1]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5")], 
                                 [[1],
                                  [2]], 
                                 1,
                                 [1,2]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3")], 
                                 [[1,3],
                                  [2]], 
                                 0,
                                 [1,3]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3")], 
                                 [[1,3],
                                  [2]], 
                                 1,
                                 [1,2,3]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3")], 
                                 [[1],
                                  [2,3]], 
                                 1,
                                 [1,2,3]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3")], 
                                 [[1],
                                  [2],
                                  [3]], 
                                 2,
                                 [1,2,3]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3")], 
                                 [[1,3],
                                  [2],
                                  [3]], 
                                 2,
                                 [1,2,3]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1,2],
                                  [3],
                                  [4]], 
                                 1,
                                 [1,2,3,4]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("lib2oclock", "2.4.3"),
                               ("libgununu", "7.6.5"),
                               ("libchili", "3.3.3")], 
                                 [[1],
                                  [2],
                                  [3],
                                  [4],
                                  [5],
                                  [6]], 
                                 5,
                                 [1,2,3,4,5,6]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libbenene", "2.4.3"),
                               ("libbanana", "3.3.3")], 
                                 [[1,2],
                                  [3],
                                  [4]], 
                                 1,
                                 [1,2,3,4]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5")], 
                                 [[1,2],
                                  [],
                                  [1]], 
                                 1,
                                 [1,2]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libbenene", "2.4.3"),
                               ("libbanana", "3.3.3"), 
                               ("libgununu", "7.6.5")], 
                                 [[1,2,5],
                                  [3,5],
                                  [4,5],
                                  [5],
                                  [5]], 
                                 1,
                                 [1,2,3,4,5]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libbenene", "2.4.3"),
                               ("libbanana", "3.3.3"), 
                               ("libgununu", "7.6.5")], 
                                 [[1,2],
                                  [3,5],
                                  [4,5],
                                  [5],
                                  [5]], 
                                 1,
                                 [1,2,3,4,5]),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libbenene", "2.4.3"),
                               ("libbanana", "3.3.3"), 
                               ("libgununu", "7.6.5")], 
                                 [[1,2],
                                  [3],
                                  [4],
                                  [5],
                                  [5]], 
                                 2,
                                 [1,2,3,4,5])
                         ])
def test_lib_get_deps_depth(libs_args, deps_args, depth, expected):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    libs = [library.Library(n,v) for (n,v) in libs_args]
    libs_str = [f"library.Library('{n}', '{v}')" for (n,v) in libs_args]
    recreate += "libs = [" + ",\n        ".join(libs_str) + "]\n\n"
    deps0 = [libs[i] for i in expected]
    for i, deps in enumerate(deps_args):
        for d in deps:
            recreate += f"libs[{i}].add_dependency(libs[{d}])\n"
            libs[i].add_dependency(libs[d])
    recreate += f"libs[{0}].get_dependencies({depth})\n\n\n"
    actual = libs[0].get_dependencies(depth)
    helpers.check_type(actual, deps0, recreate)
    check_result(set(libs[0].get_dependencies(depth)), set(deps0), recreate)

@pytest.mark.parametrize("lib_args, deps_args, upd_args, fails",
                         [
                             (("libshoe", "1.2.3"), 
                              [("libbanana", "1.0.0")], 
                              ("libbanana", "1.0.1", False, 0), 
                              False),
                             (("libshoe", "1.2.3"), 
                              [], 
                              ("libbanana", "1.0.1", False, 0), 
                              True),
                             (("libshoe", "1.2.3"), 
                              [("libbanana", "1.0.0")], 
                              ("libbanana", "1.0.0", False, 0), 
                              True),
                             (("libshoe", "1.2.3"), 
                              [("libbanana", "1.0.0")], 
                              ("libbanana", "1.0.1", True, 0), 
                              True),
                             (("libshoe", "1.2.3"), 
                              [("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libbanana", "1.0.0"), 
                               ("libchili", "3.3.3")], 
                              ("libbanana", "1.0.1", False, 2), 
                              False),
                             (("libshoe", "1.2.3"), 
                              [("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libbanana", "1.0.0"), 
                               ("libchili", "3.3.3")], 
                              ("libbanana", "1.0.1", True, 2), 
                              True),
                             (("libshoe", "1.2.3"), 
                              [("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                              ("libbanana", "1.0.1", False, 0), 
                              True)
                         ])
def test_lib_update_deps(lib_args, deps_args, upd_args, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    deps = [library.Library(n,v) for (n,v) in deps_args]
    updated = deps[:]
    deps_str = [f"library.Library('{n}', '{v}')" for (n,v) in deps_args]
    recreate += "deps = [" + ",\n        ".join(deps_str) + "]\n\n"
    lib_name, lib_ver = lib_args
    lib = library.Library(lib_name, lib_ver, dependencies=deps)
    lib_str = f"lib = library.Library('{lib_name}', '{lib_ver}', dependencies=deps)\n"
    recreate += lib_str
    upd_name, upd_ver, upd_testing, upd_idx = upd_args
    upd_dep = library.Library(upd_name, upd_ver, upd_testing)
    upd_str = f"upd = library.Library('{upd_name}', '{upd_ver}', {upd_testing})\n"
    recreate += upd_str
    recreate += "lib.update_dependency(upd_dep)\n\n"
    try:
        actual = lib.update_dependency(upd_dep)
        helpers.check_expected_none(actual, recreate)
        del updated[upd_idx]
        updated.append(upd_dep)
        check_result(set(lib.get_dependencies()), set(updated), recreate)
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        check_result(set(lib.get_dependencies()), set(deps), recreate)
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate

@pytest.mark.parametrize("libs_args, deps_args, fails",
                         [
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0")], 
                              [[1]], 
                              False),
                             ([("libshoe", "1.2.3"), 
                               ("libshoe", "1.0.0")], 
                              [[1]], 
                              True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3")], 
                              [[1],
                               [2],
                               [3],
                               [0]], 
                              True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1,2],
                                  [3],
                                  [4], 
                                  [0]], 
                                 True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1,2],
                                  [3],
                                  [4], 
                                  [1]], 
                                 True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1,2],
                                  [3],
                                  [4], 
                                  [4],
                                  [1]], 
                                 True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1,2],
                                  [3],
                                  [3], 
                                  [0]], 
                                 True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1],
                                  [3],
                                  [3], 
                                  [4],
                                  [0]], 
                                 True),
                             ([("libshoe", "1.2.3"), 
                               ("libbanana", "1.0.0"),
                               ("libbenene", "3.1.5"),
                               ("libvsf", "2.4.3"),
                               ("libchili", "3.3.3")], 
                                 [[1],
                                  [3],
                                  [3], 
                                  [4],
                                  [2]], 
                                 True)
                         ])
def test_lib_check_cycles(libs_args, deps_args, fails):
    recreate = "\n\nTo recreate this test in IPython, run the following:\n\n"
    libs = [library.Library(n,v) for (n,v) in libs_args]
    libs_str = [f"library.Library('{n}', '{v}')" for (n,v) in libs_args]
    recreate += "libs = [" + ",\n        ".join(libs_str) + "]\n\n"
    try:
        for i, deps in enumerate(deps_args):
            for d in deps:
                recreate += f"libs[{i}].add_dependency(libs[{d}])\n"
                libs[i].add_dependency(libs[d])
        recreate = f"\n\n\nThis test expected a LibraryException to be raised.\n{recreate}"
        assert not fails, recreate
    except library.LibraryException as e:
        recreate = (f"\n\n\nThis test should not have failed due to\n"
                    f"    LibraryException: {e}\n{recreate}")
        assert fails, recreate
