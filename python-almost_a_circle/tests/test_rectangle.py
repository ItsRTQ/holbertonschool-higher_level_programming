import unittest
import io
import unittest.mock
from models.rectangle import Rectangle

class TestRectangleClass(unittest.TestCase):

    def test_rectangle_instance_creation(self):
        # Test with valid int values
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        self.assertEqual(rectangle_instance.width, 4)
        self.assertEqual(rectangle_instance.height, 6)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)
        self.assertEqual(rectangle_instance.id, 1)

        # Test with invalid str values
        with self.assertRaises(TypeError):
            Rectangle("4", "6", "2", "3", "1")

        # Test with invalid tuple values
        with self.assertRaises(TypeError):
            Rectangle((4, 6), (2, 3), 1)

        # Test with invalid dictionary values
        with self.assertRaises(TypeError):
            Rectangle({'width': 4, 'height': 6, 'x': 2, 'y': 3, 'id': 1})

    def test_rectangle_area_calculation(self):
        # Test with valid int values
        rectangle_instance = Rectangle(4, 6)
        self.assertEqual(rectangle_instance.area(), 24)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Rectangle("4", "6").area()

        # Test with None values
        with self.assertRaises(TypeError):
            Rectangle(None, 6).area()

        # Test with method call with no arguments
        with self.assertRaises(TypeError):
            Rectangle().area()

    def test_rectangle_display(self):
        # Test with valid int values
        rectangle_instance = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rectangle_instance.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Rectangle("3", "2").display()

        # Test with None values
        with self.assertRaises(TypeError):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO):
                Rectangle(3, None).display()

        # Test with method call with no arguments
        with self.assertRaises(TypeError):
            Rectangle().display()

    def test_str_representation(self):
        # Test with valid int values
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 4/6"
        self.assertEqual(str(rectangle_instance), expected_output)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            str(Rectangle("4", "6", "2", "3", "1"))

        # Test with None values
        with self.assertRaises(TypeError):
            str(Rectangle(4, None, 2, 3, 1))

        # Test with method call with no arguments
        with self.assertRaises(TypeError):
            Rectangle().__str__()

    def test_update_method_with_args(self):
        # Test with valid int values
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        rectangle_instance.update(2, 8, 10, 4, 5)
        self.assertEqual(rectangle_instance.id, 2)
        self.assertEqual(rectangle_instance.width, 8)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 4)
        self.assertEqual(rectangle_instance.y, 5)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 2, 3, 1).update("2a", "8b", "10c", "4d", "5e")

        # Test with None values
        with self.assertRaises(TypeError):
            Rectangle(4, 6, None, 3, 1).update(2, None, 10, 4, 5)

        # Test with method call with no arguments
        with self.assertRaises(TypeError):
            Rectangle().update()

    def test_update_method_with_kwargs(self):
        # Test with valid int values
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        rectangle_instance.update(id=2, width=8, height=10, x=4, y=5)
        self.assertEqual(rectangle_instance.id, 2)
        self.assertEqual(rectangle_instance.width, 8)
        self.assertEqual(rectangle_instance.height, 10)
        self.assertEqual(rectangle_instance.x, 4)
        self.assertEqual(rectangle_instance.y, 5)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 2, 3, 1).update(id="2a", width="8b", height="10c", x="4d", y="5e")

        # Test with None values
        with self.assertRaises(TypeError):
            Rectangle(4, 6, 2, 3, 1).update(id=None, width=None, height=10, x=4, y=5)

        # Test with method call with no arguments
        with self.assertRaises(TypeError):
            Rectangle().update()

    def test_to_dictionary_method(self):
        # Test with valid int values
        rectangle_instance = Rectangle(4, 6, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 4, 'height': 6, 'x': 2, 'y': 3}
        self.assertDictEqual(rectangle_instance.to_dictionary(), expected_dict)

        # Test with invalid str values (will raise a TypeError)
        with self.assertRaises(TypeError):
            Rectangle("4", "6", "2", "3", "1").to_dictionary()

        # Test with None values
        with self.assertRaises(TypeError):
            Rectangle(None, None, None, None, None).to_dictionary()

        # Test with method call with no arguments
        with self.assertRaises(TypeError):
            Rectangle().to_dictionary()

if __name__ == '__main__':
    unittest.main()
