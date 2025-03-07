from case.CatandMouse import cat_and_mouse
import unittest


class TestCatAndMouse(unittest.TestCase):

    def test_cat_a_first(self):
        self.assertEqual(cat_and_mouse(2, 5, 4), "Cat A")

    def test_cat_b_first(self):
        self.assertEqual(cat_and_mouse(1, 5, 3), "Cat B")

    def test_both_reach_at_same_time(self):
        self.assertEqual(cat_and_mouse(2, 6, 4), "Mouse C")

    def test_cat_a_closer(self):
        self.assertEqual(cat_and_mouse(1, 7, 3), "Cat A")

    def test_cat_b_closer(self):
        self.assertEqual(cat_and_mouse(5, 2, 4), "Cat B")

    def test_mouse_at_starting_position(self):
        self.assertEqual(cat_and_mouse(4, 5, 4), "Cat A")

    def test_edge_case_cat_b_first(self):
        self.assertEqual(cat_and_mouse(1, 4, 2), "Cat A")
