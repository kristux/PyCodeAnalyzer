from unittest import TestCase

import mock

from functionsizechecker import get_function_increase_signature


class TestGet_function_increase_signature(TestCase):
    def assert_function_signature(self, files, functions_touched, expectedSignature):
        self.assertEqual(
            self.get_function_increase_signature(files, functions_touched),
            expectedSignature
        )

    def test_no_file_passed_in_we_return_empty_list(self):
        self.assertEqual(self.get_function_increase_signature([]), [])

    def test_when_single_file_we_return_emtpy_list(self):
        self.assert_function_signature([""], [], [])

    def test_when_we_have_two_files_where_size_increased(self):
        self.assert_function_signature(["", ""], [{"foo": 1}], [1])

    def test_when_we_have_two_files_but_no_function_increase(self):
        self.assert_function_signature(["", ""], [{}], [])

    def test_function_increases_in_size_twice(self):
        self.assert_function_signature(["", "", ""], [{"foo": 1}, {"foo": 1}], [0, 1])

    def test_two_functions_increased_in_size_once(self):
        self.assert_function_signature(["", ""], [{"foo": 1, "bar": 1}], [2])

    def test_all(self):
        self.assert_function_signature(
            ["", "", ""],
            [{"foo": 1, "bar": 1}, {"foo": -1}, {"foo": 1, "baz": 1, "bar": 1}, {"baz": 1}],
            [2]
        )

    def get_function_increase_signature(self, files, functions_touched=()):
        fake_get_functions_touched = mock.Mock(side_effect=functions_touched)
        with mock.patch("functionsizechecker.get_functions_that_were_touched", fake_get_functions_touched):
            return get_function_increase_signature(*files)

