from unittest import TestCase
from functionsizechecker import results


class TestMerge_results(TestCase):
    def test_merge_empty_lists(self):
        self.assertEqual(results.merge_results([], []), [])
        self.assertEqual(results.merge_results([1], []), [1])
        self.assertEqual(results.merge_results([], [1]), [1])
        self.assertEqual(results.merge_results([1], [1]), [2])
        self.assertEqual(results.merge_results([1, 1], [1]), [2, 1])
        self.assertEqual(results.merge_results([1, 1], [1]), [2, 1])
        self.assertEqual(results.merge_results([1], [1, 1]), [2, 1])
        self.assertEqual(
            results.merge_results([1, 2, 0, 7], [1, 1, 4, 5, 1]),
            [2, 3, 4, 12, 1]
        )

