from case.staircase import staircase
import unittest


class TestStaircase(unittest.TestCase):

    def test_staircase_1(self):
        result = staircase(1, "#")
        expected_output = "#\n"
        self.assertEqual(result, expected_output)

    def test_staircase_5(self):
        result = staircase(5, "#")
        expected_output = "    #\n   ##\n  ###\n ####\n#####\n"
        self.assertEqual(result, expected_output)

    def test_staircase_3(self):
        result = staircase(3, "#")
        expected_output = "  #\n ##\n###\n"
        self.assertEqual(result, expected_output)

    def test_staircase_30(self):
        result = staircase(30, "#")
        expected_output = "".join(
            [" " * (30 - i) + "#" * i + "\n" for i in range(1, 31)]
        )
        self.assertEqual(result, expected_output)

    def test_staircase_custom_display(self):
        result = staircase(4, "*")
        expected_output = "   *\n  **\n ***\n****\n"
        self.assertEqual(result, expected_output)

    def test_invalid_input_0(self):
        result = staircase(0, "#")
        self.assertEqual(result, "")

    def test_invalid_input_31(self):
        result = staircase(31, "#")
        self.assertEqual(result, "")
