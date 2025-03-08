import unittest
from case.strub import guess_float, guess_int
from unittest.mock import patch


class TestRandomFunctions(unittest.TestCase):

    @patch("case.strub.randint")
    def test_guess_int(self, mock_randint):
        mock_randint.return_value = 42

        self.assertEqual(guess_int(1, 100), 42)
        mock_randint.assert_called_with(1, 100)

        self.assertEqual(guess_int(-10, 10), 42)
        mock_randint.assert_called_with(-10, 10)

        self.assertEqual(guess_int(0, 1000), 42)
        mock_randint.assert_called_with(0, 1000)

    @patch("case.strub.uniform")
    def test_guess_float(self, mock_uniform):
        mock_uniform.return_value = 3.14159

        self.assertEqual(guess_float(0, 10), 3.14159)
        mock_uniform.assert_called_with(0, 10)

        self.assertEqual(guess_float(-5.5, 5.5), 3.14159)
        mock_uniform.assert_called_with(-5.5, 5.5)

        self.assertEqual(guess_float(1.5, 9.75), 3.14159)
        mock_uniform.assert_called_with(1.5, 9.75)
