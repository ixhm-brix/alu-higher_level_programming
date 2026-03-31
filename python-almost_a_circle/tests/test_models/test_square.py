#!/usr/bin/python3
"""Unit tests for models/square.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import io
import sys


class TestSquare_instantiation(unittest.TestCase):
    """Tests for Square instantiation."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_one_arg(self):
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_is_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_id_auto(self):
        s1 = Square(5)
        s2 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_id_given(self):
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_four_args(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_no_args_raises(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_not_int_raises(self):
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero_raises(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative_raises(self):
        with self.assertRaises(ValueError):
            Square(-1)


class TestSquare_size(unittest.TestCase):
    """Tests for Square size getter and setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_get_size(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_set_size(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_size_sets_width_height(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_not_int_raises(self):
        with self.assertRaises(TypeError) as ctx:
            Square(5).size = "9"
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_size_zero_raises(self):
        with self.assertRaises(ValueError):
            s = Square(5)
            s.size = 0

    def test_size_negative_raises(self):
        with self.assertRaises(ValueError):
            s = Square(5)
            s.size = -1

    def test_size_float_raises(self):
        with self.assertRaises(TypeError):
            Square(5).size = 1.5


class TestSquare_x_y(unittest.TestCase):
    """Tests for Square x and y attributes inherited from Rectangle."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_x_getter(self):
        s = Square(5, 3)
        self.assertEqual(s.x, 3)

    def test_y_getter(self):
        s = Square(5, 0, 4)
        self.assertEqual(s.y, 4)

    def test_x_not_int_raises(self):
        with self.assertRaises(TypeError):
            Square(5, "1")

    def test_y_not_int_raises(self):
        with self.assertRaises(TypeError):
            Square(5, 0, "1")

    def test_x_negative_raises(self):
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_negative_raises(self):
        with self.assertRaises(ValueError):
            Square(5, 0, -1)


class TestSquare_str(unittest.TestCase):
    """Tests for Square __str__ method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_basic(self):
        s = Square(5)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_x_y(self):
        s = Square(3, 1, 3)
        self.assertEqual(str(s), "[Square] (1) 1/3 - 3")

    def test_str_given_id(self):
        s = Square(5, 0, 0, 12)
        self.assertEqual(str(s), "[Square] (12) 0/0 - 5")


class TestSquare_display(unittest.TestCase):
    """Tests for Square display method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_display_basic(self):
        s = Square(2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_x(self):
        s = Square(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")


class TestSquare_area(unittest.TestCase):
    """Tests for Square area method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_area_after_size_change(self):
        s = Square(5)
        s.size = 3
        self.assertEqual(s.area(), 9)


class TestSquare_update(unittest.TestCase):
    """Tests for Square update method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_id(self):
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)

    def test_update_size(self):
        s = Square(5)
        s.update(1, 2)
        self.assertEqual(s.size, 2)

    def test_update_x(self):
        s = Square(5)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)

    def test_update_y(self):
        s = Square(5)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs_size(self):
        s = Square(5)
        s.update(size=7)
        self.assertEqual(s.size, 7)

    def test_update_kwargs_id(self):
        s = Square(5)
        s.update(id=89)
        self.assertEqual(s.id, 89)

    def test_update_kwargs_multiple(self):
        s = Square(5)
        s.update(size=7, y=1, id=89)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 89)

    def test_update_args_over_kwargs(self):
        s = Square(5)
        s.update(89, 2, size=10)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)

    def test_update_no_args(self):
        s = Square(5, 0, 0, 1)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")


class TestSquare_to_dictionary(unittest.TestCase):
    """Tests for Square to_dictionary method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary_keys(self):
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('size', d)
        self.assertIn('x', d)
        self.assertIn('y', d)

    def test_to_dictionary_values(self):
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)

    def test_to_dictionary_type(self):
        s = Square(5)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_no_extra_keys(self):
        s = Square(5)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {'id', 'size', 'x', 'y'})

    def test_to_dictionary_update(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
