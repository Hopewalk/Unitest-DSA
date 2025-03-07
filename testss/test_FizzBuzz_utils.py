from case.FizzBuzz import fizzbuzz
import unittest


class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_multiple_of_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")

    def test_fizz_multiple_of_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")

    def test_buzz_multiple_of_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")

    def test_neither_3_nor_5(self):
        self.assertEqual(fizzbuzz(7), 7)
        self.assertEqual(fizzbuzz(22), 22)
