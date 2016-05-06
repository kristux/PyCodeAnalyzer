from unittest import TestCase

import mock

from functionsizechecker import project
from functionsizechecker.project import Project


class TestProject(TestCase):
    def test_no_files_in_vc(self):
        vc = mock.Mock()
        p = Project(vc)
        self.assertEqual(p.analyze_method_increase(), [])

