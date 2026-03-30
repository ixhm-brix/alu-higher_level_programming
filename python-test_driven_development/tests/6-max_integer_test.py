#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_middle(self):
        """Test with max in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative"""
        self.assertEqual(max_integer([-3, 0, 5, -1]), 5)

    def test_duplicates(self):
        """Test with duplicate max values"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_all_same(self):
        """Test with all identical values"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test with float values"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_no_argument(self):
        """Test with no argument (default empty list)"""
        self.assertIsNone(max_integer())

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)

    def test_two_elements(self):
        """Test with exactly two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)


if __name__ == '__main__':
    unittest.main()
