from case.CaesarCipher import caesarCipher
import unittest


class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher_shift_3(self):
        self.assertEqual(caesarCipher("abc xyz", 3), "def abc")

    def test_caesar_cipher_shift_0(self):
        self.assertEqual(caesarCipher("abc xyz", 0), "abc xyz")

    def test_caesar_cipher_uppercase(self):
        self.assertEqual(caesarCipher("ABC XYZ", 3), "DEF ABC")

    def test_caesar_cipher_with_non_alphabetic(self):
        self.assertEqual(caesarCipher("abc 123!", 3), "def 123!")

    def test_caesar_cipher_large_shift(self):
        self.assertEqual(caesarCipher("abc", 29), "def")

    def test_caesar_cipher_empty_string(self):
        self.assertEqual(caesarCipher("", 5), "")

    def test_caesar_cipher_full_rotation(self):
        self.assertEqual(caesarCipher("abc xyz", 26), "abc xyz")
