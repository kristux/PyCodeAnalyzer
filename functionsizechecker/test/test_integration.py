import unittest

from functionsizechecker.analyze import analyze_path
from functionsizechecker.cacher import FileCacher


class VC(object):
    def __init__(self):
        self._histories = []

    def iter_file_histories(self, path):
        return self._histories

    def add_file_history(self, path, files):
        self._histories.append((path, len(files) + 1, files))


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.cacher = FileCacher("cached_results")
        self.cacher.clear_cache()

    def test_nothing_in_vc(self):
        self.assertEqual([], analyze_path("//foo/...", VC()))

    def test_single_file_with_two_revisions(self):
        vc = VC()
        files = [
"""
def fubar():
    pass
""",
"""
def fubar():
    for i in xrange(10):
        yield i ** 2
"""
        ]
        vc.add_file_history("//foo/bar.py", files)
        vc.add_file_history("//foo/baz.py", [
"""
class Baz(object):
    def __init__(self):
        self.x = 3
    def get_x(self):
        return self.x
""",
"""
class Baz(object):
    def __init__(self):
        self.x = 3
    def get_x(self):
        if self.x == 3:
            return self.x
        return None
""",
"""
class Baz(object):
    def __init__(self):
        self.x = 3
    def get_x(self):
        if self.x == 3:
            return self.x
        elif self.x > 3:
            return self.x * 2
        else:
            return self.x / 2
"""
])
        self.assertEqual([1, 1], analyze_path("//foo/...", vc, result_cacher=self.cacher))

    def tearDown(self):
        self.cacher.clear_cache()
