import unittest
import io
import unittest.mock
from models.square import Square

class TestSquareClass(unittest.TestCase):

    def test_square_instance_creation(self):
        # Test with valid int values
        square_instance = Square(5, 2, 3, 1)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.id, 1)

        # Test with invalid str values
        with self.assertRaises(TypeError):
            Square("5", "2", "3", "1")

        # Test with invalid float values
        with self.assertRaises(TypeError):
            Square(5.5, 2, 3, 1)

        # Test with invalid tuple values
        with self.assertRaises(TypeError):
            Square((5, 5), (2, 2), 1)

        # Test with invalid dictionary values
        with self.assertRaises(TypeError):
            Square({'size': 5, 'x': 2, 'y': 3, 'id': 1})

        # Test with invalid list values
        with self.assertRaises(TypeError):
            Square([5, 5], [2, 2], 1)

        # Test with None values
        with self.assertRaises(TypeError):
            Square(None, None, None, None)

    def test_square_area_calculation(self):
        # Test with valid int values
        square_instance = Square(5)
        self.assertEqual(square_instance.area(), 25)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square("5").area()

        # Test with invalid float values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5.5).area()

        # Test with invalid tuple values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square((5, 5)).area()

        # Test with invalid dictionary values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square({'size': 5}).area()

        # Test with invalid list values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square([5, 5]).area()

        # Test with None values
        with self.assertRaises(TypeError):
            Square(None).area()

    def test_square_display(self):
        # Test with valid int values
        square_instance = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square_instance.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Square("3").display()

        # Test with invalid float values (will raise a TypeError)
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Square(3.5).display()

        # Test with invalid tuple values (will raise a TypeError)
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Square((3, 3)).display()

        # Test with invalid dictionary values (will raise a TypeError)
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Square({'size': 3}).display()

        # Test with invalid list values (will raise a TypeError)
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Square([3, 3]).display()

        # Test with None values
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Square(None).display()

    def test_str_representation(self):
        # Test with valid int values
        square_instance = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square_instance), expected_output)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            str(Square("5", "2", "3", "1"))

        # Test with invalid float values (will raise a TypeError)
        with self.assertRaises(TypeError):
            str(Square(5.5, 2, 3, 1))

        # Test with invalid tuple values (will raise a TypeError)
        with self.assertRaises(TypeError):
            str(Square((5, 5), (2, 2), 1))

        # Test with invalid dictionary values (will raise a TypeError)
        with self.assertRaises(TypeError):
            str(Square({'size': 5, 'x': 2, 'y': 3, 'id': 1}))

        # Test with invalid list values (will raise a TypeError)
        with self.assertRaises(TypeError):
            str(Square([5, 5], [2, 2], 1))

        # Test with None values
        with self.assertRaises(TypeError):
            str(Square(None))

    def test_update_method_with_args(self):
        # Test with valid int values
        square_instance = Square(5, 2, 3, 1)
        square_instance.update(2, 8, 4, 5)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.x, 4)
        self.assertEqual(square_instance.y, 5)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update("2a", "8b", "4c", "5d")

        # Test with invalid float values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(2, 8.5, 4, 5)

        # Test with invalid tuple values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update((2, 2), (8, 8), 4, 5)

        # Test with invalid list values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update([2, 2], [8, 8], 4, 5)

        # Test with None values
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(None, None, None, None)

    def test_update_method_with_kwargs(self):
        # Test with valid int values
        square_instance = Square(5, 2, 3, 1)
        square_instance.update(id=2, size=8, x=4, y=5)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.x, 4)
        self.assertEqual(square_instance.y, 5)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(id="2a", size="8b", x="4c", y="5d")

        # Test with invalid float values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(id=2, size=8.5, x=4, y=5)

        # Test with invalid tuple values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(id=(2, 2), size=(8, 8), x=4, y=5)

        # Test with invalid dictionary values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(id={'id': 2}, size={'size': 8}, x=4, y=5)

        # Test with invalid list values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(id=[2, 2], size=[8, 8], x=4, y=5)

        # Test with None values
        with self.assertRaises(TypeError):
            Square(5, 2, 3, 1).update(id=None, size=None, x=None, y=None)

    def test_to_dictionary_method(self):
        # Test with valid int values
        square_instance = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertDictEqual(square_instance.to_dictionary(), expected_dict)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square("5", "2", "3", "1").to_dictionary()

        # Test with invalid float values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square(5.5, 2, 3, 1).to_dictionary()

        # Test with invalid tuple values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square((5, 5), (2, 2), 1).to_dictionary()

        # Test with invalid dictionary values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square({'size': 5, 'x': 2, 'y': 3, 'id': 1}).to_dictionary()

        # Test with invalid list values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Square([5, 5], [2, 2], 1).to_dictionary()

        # Test with None values
        with self.assertRaises(TypeError):
            Square(None, None, None, None).to_dictionary()

if __name__ == '__main__':
    unittest.main()
