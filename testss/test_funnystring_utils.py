from case.funnystring import funnyString
import unittest


class TestFunnyString(unittest.TestCase):

    def test_funny_string(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny_string(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_single_character(self):
        self.assertEqual(funnyString("a"), "Funny")

    def test_empty_string(self):
        self.assertEqual(funnyString(""), "Funny")

    def test_palindrome_string(self):
        self.assertEqual(funnyString("abcdcba"), "Funny")

    def test_not_funny_multiple_character(self):
        self.assertEqual(funnyString("abcdefg"), "Not Funny")
