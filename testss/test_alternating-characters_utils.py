from case.alternating_characters import alternatingCharacters
import unittest


class TestAlternatingCharacters(unittest.TestCase):

    def test_alternating(self):
        self.assertEqual(alternatingCharacters("ABABAB"), 0)

    def test_no_alternation(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_mixed_string(self):
        self.assertEqual(alternatingCharacters("AABBAAB"), 3)

    def test_single_character(self):
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_empty_string(self):
        self.assertEqual(alternatingCharacters(""), 0)

    def test_large_input(self):
        self.assertEqual(alternatingCharacters("A" * 1000), 999)
