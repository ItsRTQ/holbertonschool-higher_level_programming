#!/usr/bin/python3
import unittest
"""Unittest for max_integer([..])
"""
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunction(unittest.TestCase):

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result, "Should return None for an empty list")

    def test_overflow(self):
        large_integers = [10**18, 2*(10**18), 5*(10**17)]
        result = max_integer(large_integers)
        self.assertEqual(result, 2*(10**18), "Incorrect result for overflow test")

    def test_float_inf(self):
        inf_list = [1, 2, float('inf'), 4, 5]
        result = max_integer(inf_list)
        self.assertEqual(result, float('inf'), "Incorrect result for float('inf') test")

    def test_max_integer(self):
        test_cases = [
            ([1, 2, 3, 4], 4),
            ([-1, -2, -3, -4, -5], -1),
            ([10, 5, 7, 2, 8], 10),
            ([0, 0, 0, 0, 0], 0),
            ([-5, -10, -15, -20], -5),
            ([5], 5),
            ([-5, 0, 5], 5),
            ([-10, 0, 10], 10),
            ([2, 2.5, 3], 3),
            (list(range(1000000)), 999999),
            ([-1], -1),
        ]

        for input_list, expected_result in test_cases:
            with self.subTest(input_list=input_list, expected_result=expected_result):
                result = max_integer(input_list)
                self.assertEqual(result, expected_result, "Incorrect max integer")

if __name__ == '__main__':
    unittest.main()
