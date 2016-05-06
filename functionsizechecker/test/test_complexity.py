from unittest import TestCase
from functionsizechecker.complexity import get_complexity_by_method


class TestGetComplexityByMethod(TestCase):
    def test_empty_string_returns_nothing(self):
        self.assertEqual(get_complexity_by_method(""), {})

    def test_single_function(self):
        self.assertEqual( get_complexity_by_method("""
def foo():
  pass"""),
            {"foo": 1})

    def test_single_method(self):
        self.assertEqual(get_complexity_by_method("""
class Foo(object):
  def bar():
    pass"""),
        {"Foo.bar": 1})

    def test_nested_function(self):
        self.assertEqual(get_complexity_by_method("""
def foo():
  def bar():
    for i in xrange(3):
       if i == 1:
         return i * 3
  return bar()"""),
                         {"foo": 4})

