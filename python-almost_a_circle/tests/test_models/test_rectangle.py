#!/usr/bin/python3
"""Unit tests for models/rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import sys


class TestRectangle_instantiation(unittest.TestCase):
    """Tests for Rectangle instantiation."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_two_args(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)

    def test_id_auto(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_id_given(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_default_x_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_five_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_one_arg_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_no_args_raises(self):
        with self.assertRaises(TypeError):
            Rectangle()


class TestRectangle_width(unittest.TestCase):
    """Tests for Rectangle width getter and setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_get_width(self):
        r = Rectangle(5, 2)
        self.assertEqual(r.width, 5)

    def test_set_width(self):
        r = Rectangle(5, 2)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_width_string(self):
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, "2")
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_width_not_int_raises(self):
        with self.assertRaises(TypeError) as ctx:
            Rectangle("10", 2)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_width_float_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(1.5, 2)

    def test_width_none_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(None, 2)

    def test_width_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 2)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_width_negative_raises(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 2)

    def test_width_list_raises(self):
        with self.assertRaises(TypeError):
            Rectangle([1], 2)

    def test_width_dict_raises(self):
        with self.assertRaises(TypeError):
            Rectangle({"w": 1}, 2)


class TestRectangle_height(unittest.TestCase):
    """Tests for Rectangle height getter and setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_get_height(self):
        r = Rectangle(2, 5)
        self.assertEqual(r.height, 5)

    def test_set_height(self):
        r = Rectangle(2, 5)
        r.height = 10
        self.assertEqual(r.height, 10)

    def test_height_not_int_raises(self):
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, "2")
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_height_float_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 1.5)

    def test_height_none_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(2, None)

    def test_height_zero_raises(self):
        with self.assertRaises(ValueError) as ctx:
            Rectangle(2, 0)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_height_negative_raises(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -5)


class TestRectangle_x(unittest.TestCase):
    """Tests for Rectangle x getter and setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_get_x(self):
        r = Rectangle(2, 5, 3)
        self.assertEqual(r.x, 3)

    def test_set_x(self):
        r = Rectangle(2, 5)
        r.x = 4
        self.assertEqual(r.x, 4)

    def test_x_not_int_raises(self):
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, 2, {})
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_x_float_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5, 1.5)

    def test_x_none_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5, None)

    def test_x_negative_raises(self):
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, -1)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_x_zero_ok(self):
        r = Rectangle(2, 5, 0)
        self.assertEqual(r.x, 0)


class TestRectangle_y(unittest.TestCase):
    """Tests for Rectangle y getter and setter."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_get_y(self):
        r = Rectangle(2, 5, 0, 3)
        self.assertEqual(r.y, 3)

    def test_set_y(self):
        r = Rectangle(2, 5)
        r.y = 4
        self.assertEqual(r.y, 4)

    def test_y_not_int_raises(self):
        with self.assertRaises(TypeError) as ctx:
            Rectangle(10, 2, 3, "1")
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_y_float_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5, 0, 1.5)

    def test_y_none_raises(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5, 0, None)

    def test_y_negative_raises(self):
        with self.assertRaises(ValueError) as ctx:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_y_zero_ok(self):
        r = Rectangle(2, 5, 0, 0)
        self.assertEqual(r.y, 0)


class TestRectangle_area(unittest.TestCase):
    """Tests for Rectangle area method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_area_small(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_area_large(self):
        r = Rectangle(999999999, 999999999)
        self.assertEqual(r.area(), 999999999 * 999999999)

    def test_area_after_update(self):
        r = Rectangle(3, 2)
        r.width = 10
        r.height = 10
        self.assertEqual(r.area(), 100)

    def test_area_one_side(self):
        r = Rectangle(1, 5)
        self.assertEqual(r.area(), 5)


class TestRectangle_display(unittest.TestCase):
    """Tests for Rectangle display method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_display_simple(self):
        r = Rectangle(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_with_x(self):
        r = Rectangle(2, 2, 2, 0)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

    def test_display_with_y(self):
        r = Rectangle(2, 2, 0, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n##\n##\n")

    def test_display_with_x_and_y(self):
        r = Rectangle(2, 3, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n  ##\n")


class TestRectangle_str(unittest.TestCase):
    """Tests for Rectangle __str__ method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_str_basic(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_default_x_y(self):
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/0 - 5/5")

    def test_str_all_default(self):
        r = Rectangle(3, 4)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 3/4")


class TestRectangle_update(unittest.TestCase):
    """Tests for Rectangle update method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_update_id(self):
        r = Rectangle(10, 10)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_two_args(self):
        r = Rectangle(10, 10)
        r.update(89, 2)
        self.assertEqual(r.width, 2)

    def test_update_three_args(self):
        r = Rectangle(10, 10)
        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

    def test_update_four_args(self):
        r = Rectangle(10, 10)
        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

    def test_update_five_args(self):
        r = Rectangle(10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)

    def test_update_kwargs_height(self):
        r = Rectangle(10, 10)
        r.update(height=1)
        self.assertEqual(r.height, 1)

    def test_update_kwargs_width_x(self):
        r = Rectangle(10, 10)
        r.update(width=1, x=2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.x, 2)

    def test_update_args_over_kwargs(self):
        r = Rectangle(10, 10)
        r.update(89, 2, height=5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)

    def test_update_no_args(self):
        r = Rectangle(10, 10, 10, 10, 1)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")


class TestRectangle_to_dictionary(unittest.TestCase):
    """Tests for Rectangle to_dictionary method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary_keys(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('width', d)
        self.assertIn('height', d)
        self.assertIn('x', d)
        self.assertIn('y', d)

    def test_to_dictionary_values(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)

    def test_to_dictionary_type(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_update(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))


if __name__ == "__main__":
    unittest.main()
