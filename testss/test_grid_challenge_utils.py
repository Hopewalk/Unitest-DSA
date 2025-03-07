from case.grid_challenge import gridChallenge
import unittest


class TestGridChallenge(unittest.TestCase):

    def test_grid_challenge_sorted(self):
        grid = ["abc", "bcd", "efg"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_challenge_unsorted_rows(self):
        grid = ["efg", "bcd", "abc"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_grid_challenge_sorted_columns(self):
        grid = ["abc", "cde", "fgh"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_challenge_unsorted_columns(self):
        grid = ["abc", "bda", "cfe"]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_grid_challenge_empty_grid(self):
        grid = []
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_challenge_single_row(self):
        grid = ["abc"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_challenge_single_column(self):
        grid = ["a", "b", "c"]
        self.assertEqual(gridChallenge(grid), "YES")

    def test_grid_challenge_mixed_case(self):
        grid = ["Abc", "bCd", "Efg"]
        self.assertEqual(gridChallenge(grid), "YES")
