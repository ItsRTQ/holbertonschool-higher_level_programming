import unittest
import io
import unittest.mock
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    def test_rectangle_instance_creation(self):
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        self.assertEqual(rectangle_instance.width, 4)
        self.assertEqual(rectangle_instance.height, 6)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)
        self.assertEqual(rectangle_instance.id, 1)

    def test_rectangle_area_calculation(self):
        rectangle_instance = Rectangle(4, 6)
        self.assertEqual(rectangle_instance.area(), 24)

    def test_rectangle_display(self):
        rectangle_instance = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle_instance.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 4/6"
        self.assertEqual(str(rectangle_instance), expected_output)

    def test_update_method_with_args(self):
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        rectangle_instance.update(2, 8, 10, 4, 5)
        self.assertEqual(rectangle_instance.id, 2)
        self.assertEqual(rectangle_instance.width, 8)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 4)
        self.assertEqual(rectangle_instance.y, 5)

    def test_update_method_with_kwargs(self):
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        rectangle_instance.update(id=2, width=8, height=10, x=4, y=5)
        self.assertEqual(rectangle_instance.id, 2)
        self.assertEqual(rectangle_instance.width, 8)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 4)
        self.assertEqual(rectangle_instance.y, 5)

    def test_to_dictionary_method(self):
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 4, 'height': 6, 'x': 2, 'y': 3}
        self.assertEqual(rectangle_instance.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
