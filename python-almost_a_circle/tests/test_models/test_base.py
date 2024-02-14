import unittest
import json
import os
from models.base import Base, Rectangle, Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        # Test when the list of dictionaries is not empty
        input_list = [{'id': 1, 'name': 'Test1'}, {'id': 2, 'name': 'Test2'}]
        result = Base.to_json_string(input_list)
        expected_result = json.dumps(input_list)
        self.assertEqual(result, expected_result)

        # Test when the list of dictionaries is empty
        input_list_empty = []
        result_empty = Base.to_json_string(input_list_empty)
        expected_result_empty = "[]"
        self.assertEqual(result_empty, expected_result_empty)

        # Test when the input is None
        result_none = Base.to_json_string(None)
        expected_result_none = "[]"
        self.assertEqual(result_none, expected_result_none)

    def test_save_to_file(self):
        # Test saving an empty list
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        # Test saving a non-empty list with Rectangle and Square instances
        obj1 = Rectangle(1, 2, 3, 4)
        obj2 = Square(5, 6, 7)
        Base.save_to_file([obj1, obj2])
        with open("Base.json", "r") as file:
            result = file.read()
            expected_result = Base.to_json_string([obj1.to_dictionary(), obj2.to_dictionary()])
            self.assertEqual(result, expected_result)

        # Test saving a non-empty list with various objects
        obj3 = Base(8)
        obj4 = "string"
        obj5 = [1, 2, 3]
        obj6 = {'key': 'value'}
        Base.save_to_file([obj3, obj4, obj5, obj6])
        with open("Base.json", "r") as file:
            result_various = file.read()
            expected_result_various = Base.to_json_string([obj3.to_dictionary()])
            self.assertEqual(result_various, expected_result_various)

        # Clean up, remove the created file
        os.remove("Base.json")

    def test_from_json_string(self):
        # Test when the JSON string is not empty
        json_string = '[{"id": 1, "name": "Test1"}, {"id": 2, "name": "Test2"}]'
        result = Base.from_json_string(json_string)
        expected_result = json.loads(json_string)
        self.assertEqual(result, expected_result)

        # Test when the JSON string is empty
        json_string_empty = ''
        result_empty = Base.from_json_string(json_string_empty)
        expected_result_empty = []
        self.assertEqual(result_empty, expected_result_empty)

        # Test when the input is None
        result_none = Base.from_json_string(None)
        expected_result_none = []
        self.assertEqual(result_none, expected_result_none)

    def test_create(self):
        # Test creating a Rectangle instance
        rectangle_dict = {'id': 1, 'width': 2, 'height': 3}
        result_rectangle = Rectangle.create(**rectangle_dict)
        expected_result_rectangle = Rectangle(2, 3)
        expected_result_rectangle.id = 1
        self.assertEqual(result_rectangle.to_dictionary(), expected_result_rectangle.to_dictionary())

        # Test creating a Square instance
        square_dict = {'id': 2, 'size': 4}
        result_square = Square.create(**square_dict)
        expected_result_square = Square(4)
        expected_result_square.id = 2
        self.assertEqual(result_square.to_dictionary(), expected_result_square.to_dictionary())

        # Test creating a Base instance
        base_dict = {'id': 3}
        result_base = Base.create(**base_dict)
        expected_result_base = Base(3)
        expected_result_base.id = 3
        self.assertEqual(result_base.to_dictionary(), expected_result_base.to_dictionary())

        # Test creating instances with invalid class names
        invalid_dict = {'id': 4, 'length': 5}
        result_invalid = Base.create(**invalid_dict)
        expected_result_invalid = Base(4)
        expected_result_invalid.id = 4
        self.assertEqual(result_invalid.to_dictionary(), expected_result_invalid.to_dictionary())

        # Test creating instances with missing attributes
        missing_dict = {'id': 5}
        result_missing = Square.create(**missing_dict)
        expected_result_missing = Square(1)
        expected_result_missing.id = 5
        self.assertEqual(result_missing.to_dictionary(), expected_result_missing.to_dictionary())

        # Test creating instances with invalid attributes
        invalid_attr_dict = {'id': 6, 'width': "invalid", 'height': 7}
        result_invalid_attr = Rectangle.create(**invalid_attr_dict)
        expected_result_invalid_attr = Rectangle(1, 7)
        expected_result_invalid_attr.id = 6
        self.assertEqual(result_invalid_attr.to_dictionary(), expected_result_invalid_attr.to_dictionary())

        # Test creating instances with negative attributes
        negative_attr_dict = {'id': 7, 'width': -2, 'height': 8}
        result_negative_attr = Rectangle.create(**negative_attr_dict)
        expected_result_negative_attr = Rectangle(1, 8)
        expected_result_negative_attr.id = 7
        self.assertEqual(result_negative_attr.to_dictionary(), expected_result_negative_attr.to_dictionary())

    def test_load_from_file(self):
        # Test loading from a non-existing file
        result_empty = Base.load_from_file()
        expected_result_empty = []
        self.assertEqual(result_empty, expected_result_empty)

        # Test loading from an existing file with Rectangle and Square instances
        obj1 = Rectangle(1, 2, 3, 4)
        obj2 = Square(5, 6, 7)
        Base.save_to_file([obj1, obj2])
        result = Base.load_from_file()
        expected_result = [obj1, obj2]
        self.assertEqual(len(result), len(expected_result))
        for res, exp_res in zip(result, expected_result):
            self.assertEqual(res.to_dictionary(), exp_res.to_dictionary())

        # Test loading from an existing file with various objects
        obj3 = Base(8)
        obj4 = "string"
        obj5 = [1, 2, 3]
        obj6 = {'key': 'value'}
        Base.save_to_file([obj3, obj4, obj5, obj6])
        result_various = Base.load_from_file()
        expected_result_various = [obj3]
        self.assertEqual(len(result_various), len(expected_result_various))
        for res, exp_res in zip(result_various, expected_result_various):
            self.assertEqual(res.to_dictionary(), exp_res.to_dictionary())

        # Clean up, remove the created file
        os.remove("Base.json")


if __name__ == '__main__':
    unittest.main()
