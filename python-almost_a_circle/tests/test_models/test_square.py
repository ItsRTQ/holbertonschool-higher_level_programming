import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        # Test initializing with valid parameters
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

        # Test initializing with invalid parameters
        with self.assertRaises(ValueError):
            Square(-1, 2, 3, 1)
        with self.assertRaises(TypeError):
            Square("5", 2, 3, 1)

        # Test initializing with invalid types
        with self.assertRaises(TypeError):
            Square(5, "2", 3, 1)
        with self.assertRaises(TypeError):
            Square(5, 2, "3", 1)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, "1")

    def test_update(self):
        square = Square(5, 2, 3, 1)

        # Test updating with valid parameters using *args
        square.update(2, 7, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        # Test updating with valid parameters using **kwargs
        square.update(size=20, x=8, y=9)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

        # Test updating with invalid parameters
        with self.assertRaises(TypeError):
            square.update(2, "7", 4, 5)

        # Test updating with various types of objects and None
        square.update(2, [7], {'key': 'value'}, None)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)  # Default value for invalid size
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        # Test empty call
        square.update()
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 1)
        result = square.to_dictionary()
        expected_result = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
