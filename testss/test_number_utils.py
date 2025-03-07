from case.number_utils import is_prime_list
import unittest


class PrimeListTest(unittest.TestCase):

    def test_give_prime_list(self):
        prime_list = [2, 3, 5, 7]
        self.assertTrue(is_prime_list(prime_list))

    def test_give_mixed_list(self):
        mixed_list = [2, 4, 5, 9]
        self.assertFalse(is_prime_list(mixed_list))

    def test_give_single_prime(self):
        single_prime = [2]
        self.assertTrue(is_prime_list(single_prime))

    def test_give_single_non_prime(self):
        single_non_prime = [4]
        self.assertFalse(is_prime_list(single_non_prime))

    def test_give_one_in_list(self):
        list_with_one = [1, 3, 5]
        self.assertFalse(is_prime_list(list_with_one))

    def test_empty_list(self):
        empty_list = []
        self.assertTrue(is_prime_list(empty_list))
