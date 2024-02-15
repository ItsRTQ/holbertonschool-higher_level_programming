import unittest
import io
import unittest.mock
from models.square import Square

class TestSquareClass(unittest.TestCase):

    def test_square_instance_creation(self):
        square_instance = Square(5, 2, 3, 1)
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 2)
        self.assertEqual(square_instance.y, 3)
        self.assertEqual(square_instance.id, 1)

    def test_square_area_calculation(self):
        square_instance = Square(5)
        self.assertEqual(square_instance.area(), 25)

    def test_square_display(self):
        square_instance = Square(3)
        expected_output = "###\n###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square_instance.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        square_instance = Square(5, 2, 3, 1)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(square_instance), expected_output)

    def test_update_method_with_args(self):
        square_instance = Square(5, 2, 3, 1)
        square_instance.update(2, 8, 4, 5)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.x, 4)
        self.assertEqual(square_instance.y, 5)

    def test_update_method_with_kwargs(self):
        square_instance = Square(5, 2, 3, 1)
        square_instance.update(id=2, size=8, x=4, y=5)
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 8)
        self.assertEqual(square_instance.x, 4)
        self.assertEqual(square_instance.y, 5)

    def test_to_dictionary_method(self):
        square_instance = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square_instance.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
