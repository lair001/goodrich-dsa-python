from typing import Sequence
from unittest.mock import patch
import sys, pytest
import solutions.libs.utils.argv as argv_utils


# A list is just a 1D matrix, after all
def execute_base_parse_matrix_test(args, expectations, parsing_function, starting_index):
    with patch.object(sys, 'argv', args):
        expectations = expectations if isinstance(expectations[0], list) else [expectations]
        current_index = starting_index
        for expected_values in expectations:
            matrix, current_index = parsing_function(current_index)
            assert_matrices_are_equal(expected_values, matrix, 0)
        assert current_index is len(args)


def assert_matrices_are_equal(expected, actual, start):
    if isinstance(expected, Sequence) and not isinstance(expected, str):
        if start == len(expected):
            return
        else:
            assert_matrices_are_equal(expected[start], actual[start], 0)
            assert_matrices_are_equal(expected, actual, start + 1)
    else:
        assert expected is actual


def execute_parse_list_test(args, expected_values):
    execute_base_parse_matrix_test(args, expected_values, argv_utils.parse_list, 1)


def execute_parse_list_test_with_starting_index(args, expected_values, starting_index):
    execute_base_parse_matrix_test(args, expected_values, argv_utils.parse_list, starting_index)


def execute_parse_int_list_test(args, expected_values):
    execute_base_parse_matrix_test(args, expected_values, argv_utils.parse_int_list, 1)


def execute_parse_int_matrix_test(args, expected_values):
    execute_base_parse_matrix_test(args, expected_values, argv_utils.parse_int_matrix, 1)


def test_parse_list_with_square_brackets():
    args = ["path", "[", "1", "2", "3", "]"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_french_braces():
    args = ["path", "{", "1", "2", "3", "}"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_parenthesis():
    args = ["path", "(", "1", "2", "3", ")"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_angular_brackets():
    args = ["path", "<", "1", "2", "3", ">"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_multiple_lists():
    args = ["path", "[", "1", "2", "3", "]", "[", "4", "5", "6", "]"]
    expectations = [["1", "2", "3"], ["4", "5", "6"]]
    execute_parse_list_test(args, expectations)


def test_parse_list_with_commas():
    args = ["path", "[", "1", ",", "2", ",", "3", "]"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_list_as_single_arg_and_elements_separated_by_commas():
    args = ["path", "[1,2,3]"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_list_as_single_arg_and_elements_separated_by_spaces():
    args = ["path", "[1 2 3]"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_list_with_list_as_single_arg_and_elements_separated_by_by_commas_and_spaces():
    args = ["path", "[ 1 , 2 , 3 ]"]
    expected_values = ["1", "2", "3"]
    execute_parse_list_test(args, expected_values)


def test_parse_int_list():
    args = ["path", "[", "1", "2", "3", "]"]
    expected_values = [1, 2, 3]
    execute_parse_int_list_test(args, expected_values)


def test_parse_int_list_with_a_non_integer_in_list():
    args = ["path", "[", "1", "a", "3", "]"]
    with patch.object(sys, 'argv', args):
        with pytest.raises(ValueError) as ve:
            argv_utils.parse_int_list(1)
        assert "invalid literal for int() with base 10" in str(ve)


def test_parse_2d_int_matrix():
    args = ["path", "[", "[", "1", "2", "]", "[", "3", "4", "]", "]"]
    expected_values = [[[1, 2], [3, 4]]]
    execute_parse_int_matrix_test(args, expected_values)


def test_parse_3d_int_matrix():
    args = ["path", "[", "[", "[", "1", "2", "]", "]", "[", "[", "3", "4", "]", "]", "]"]
    expected_values = [[[[1, 2]], [[3, 4]]]]
    execute_parse_int_matrix_test(args, expected_values)


def test_parse_multiple_int_matrices():
    args = ["path", "[", "[", "1", "2", "]", "[", "3", "4", "]", "]",
            "[", "[", "[", "1", "2", "]", "]", "[", "[", "3", "4", "]", "]", "]"]
    expected_values = [[[1, 2], [3, 4]], [[[1, 2]], [[3, 4]]]]
    execute_parse_int_matrix_test(args, expected_values)
