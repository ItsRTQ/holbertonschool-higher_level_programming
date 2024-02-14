import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(unittest.TestCase):

    def test_init(self):
        # Test initializing with valid parameters
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

        # Test initializing with invalid parameters
        with self.assertRaises(ValueError):
            Rectangle(-1, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 1)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, 3, "1")

        # Test initializing with invalid types
        with self.assertRaises(TypeError):
            Rectangle("5", 10, 2, 3, 1)
        with self.assertRaises(TypeError):
            Rectangle(5, "10", 2, 3, 1)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "2", 3, 1)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "3", 1)

    def test_update(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)

        # Test updating with valid parameters using *args
        rectangle.update(2, 7, 14, 3, 4)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 14)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

        # Test updating with valid parameters using **kwargs
        rectangle.update(height=20, x=5, y=6)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

        # Test updating with invalid parameters
        with self.assertRaises(TypeError):
            rectangle.update(2, "7", 14, 3, 4)

        # Test updating with various types of objects and None
        rectangle.update(2, [7], {'key': 'value'}, None, 4)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 1)  # Default value for invalid height
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

        # Test empty call
        rectangle.update()
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 1)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)


if __name__ == '__main__':
    unittest.main()
