"""
Unit tests for calculator.py
Run with:
    python -m unittest test_calculator.py -v

These tests mirror the test case scenarios listed in
test_case_scenarios.xlsx (TC01-TC08).
"""

import unittest
from calculator import add, subtract, multiply, divide, evaluate_expression


class TestCalculator(unittest.TestCase):

    def test_tc01_addition_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_tc02_subtraction_positive_numbers(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_tc03_multiplication_positive_numbers(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_tc04_division_positive_numbers(self):
        self.assertEqual(divide(20, 4), 5)

    def test_tc05_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_tc06_addition_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_tc07_decimal_numbers(self):
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_tc08_full_expression_from_ui(self):
        self.assertEqual(evaluate_expression("12+8*2"), 28)


if __name__ == "__main__":
    unittest.main()
