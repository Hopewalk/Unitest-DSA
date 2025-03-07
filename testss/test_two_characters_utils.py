from case.two_characters import alternate
import unittest


class TestAlternate(unittest.TestCase):

    def test_alternate_with_alternating_characters(self):
        self.assertEqual(alternate("ababab"), 6)

    def test_alternate_with_single_pair(self):
        self.assertEqual(alternate("abab"), 4)

    def test_alternate_no_alternation(self):
        self.assertEqual(alternate("aaaaa"), 0)

    def test_alternate_with_more_than_two_characters(self):
        self.assertEqual(alternate("abac"), 3)

    def test_alternate_with_multiple_pairs(self):
        self.assertEqual(alternate("ababacbc"), 6)

    def test_alternate_empty_string(self):
        self.assertEqual(alternate(""), 0)

    def test_alternate_single_character(self):
        self.assertEqual(alternate("a"), 0)

    def test_alternate_with_non_alternating_pairs(self):
        self.assertEqual(alternate("aabbcc"), 0)
