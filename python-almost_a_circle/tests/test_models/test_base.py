#!/usr/bin/python3
"""Unit tests for models/base.py"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Tests for Base class instantiation."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_no_arg(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_two_bases(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_given(self):
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_none(self):
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_float(self):
        b = Base(1.5)
        self.assertEqual(b.id, 1.5)

    def test_id_string(self):
        b = Base("hello")
        self.assertEqual(b.id, "hello")

    def test_nb_objects_not_incremented_when_id_given(self):
        b1 = Base(10)
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_mixed_id_and_auto(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Tests for Base.to_json_string static method."""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_single_dict(self):
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_multiple_dicts(self):
        d = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(d)
        self.assertIsInstance(result, str)
        import json
        self.assertEqual(json.loads(result), d)

    def test_returns_string(self):
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)

    def test_rectangle_dict(self):
        d = [{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]
        result = Base.to_json_string(d)
        self.assertIsInstance(result, str)

    def test_type_is_string(self):
        self.assertEqual(type(Base.to_json_string([{"id": 1}])), str)


class TestBase_from_json_string(unittest.TestCase):
    """Tests for Base.from_json_string static method."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_single_dict(self):
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])

    def test_multiple_dicts(self):
        s = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(s)
        self.assertEqual(result, [{"id": 1}, {"id": 2}])

    def test_returns_list(self):
        self.assertIsInstance(Base.from_json_string('[{"id": 1}]'), list)

    def test_type_is_list(self):
        self.assertEqual(type(Base.from_json_string('[{"id": 1}]')), list)

    def test_roundtrip(self):
        d = [{"id": 1, "width": 10}]
        self.assertEqual(Base.from_json_string(Base.to_json_string(d)), d)


class TestBase_save_to_file(unittest.TestCase):
    """Tests for Base.save_to_file class method."""

    def tearDown(self):
        for f in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertIn("width", f.read())

    def test_save_two_rectangles(self):
        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn("width", content)

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_square(self):
        s = Square(5)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertIn("size", f.read())

    def test_filename(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_overwrite(self):
        Rectangle.save_to_file([Rectangle(10, 10)])
        Rectangle.save_to_file([Rectangle(1, 1)])
        with open("Rectangle.json", "r") as f:
            import json
            data = json.loads(f.read())
        self.assertEqual(data[0]["width"], 1)


class TestBase_create(unittest.TestCase):
    """Tests for Base.create class method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_rectangle(self):
        r = Rectangle.create(**{"id": 1, "width": 3, "height": 5})
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)

    def test_create_square(self):
        s = Square.create(**{"id": 1, "size": 5})
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 5)

    def test_create_rectangle_all_attrs(self):
        d = {"id": 89, "width": 10, "height": 4, "x": 1, "y": 2}
        r = Rectangle.create(**d)
        self.assertEqual(str(r), "[Rectangle] (89) 1/2 - 10/4")

    def test_create_is_not_same_instance(self):
        r1 = Rectangle(3, 5, 1)
        d = r1.to_dictionary()
        r2 = Rectangle.create(**d)
        self.assertIsNot(r1, r2)


class TestBase_load_from_file(unittest.TestCase):
    """Tests for Base.load_from_file class method."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        for f in ["Rectangle.json", "Square.json"]:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_no_file_returns_empty(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

    def test_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        Base._Base__nb_objects = 0
        result = Rectangle.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Rectangle)

    def test_load_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        Base._Base__nb_objects = 0
        result = Square.load_from_file()
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Square)

    def test_load_returns_list(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        Base._Base__nb_objects = 0
        self.assertIsInstance(Rectangle.load_from_file(), list)


if __name__ == "__main__":
    unittest.main()
