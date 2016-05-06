from unittest import TestCase

from functionsizechecker import get_functions_that_were_touched
from functionsizechecker.complexity import get_complexity_by_method

SHORT_FUNCTION = """
def {}():
    pass
"""
MEDIUM_FUNCTION = """
def {}():
    for i in xrange(3):
        yield i"""

class TestGetMethodsThatWereTouched(TestCase):
    def test_if_both_files_are_empty_we_return_empty_dict(self):
        self.assertEqual(self._get_files_that_were_touched("", ""), {})

    def test_if_method_foo_increased(self):
        self.assertEqual(self._get_files_that_were_touched(SHORT_FUNCTION.format("foo"), MEDIUM_FUNCTION.format("foo")), {"foo": 1})

    def test_function_was_added(self):
        self.assertEqual(self._get_files_that_were_touched("", MEDIUM_FUNCTION.format("foo")), {"foo": 1})

    def _get_files_that_were_touched(self, old_file, new_file):
        return get_functions_that_were_touched(
            get_complexity_by_method(old_file),
            get_complexity_by_method(new_file))
