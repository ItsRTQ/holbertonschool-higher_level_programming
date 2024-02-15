import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBaseClass(unittest.TestCase):

    def test_base_instance_creation_with_id(self):
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_base_instance_creation_without_id(self):
        base_instance1 = Base()
        base_instance2 = Base()
        self.assertEqual(base_instance1.id, 1)
        self.assertEqual(base_instance2.id, 2)

    def test_to_json_string_with_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_non_empty_list(self):
        data = [{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]')

    def test_from_json_string_with_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_with_valid_string(self):
        json_string = '[{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]'
        result = Base.from_json_string(json_string)
        expected_result = [{"id": 1, "name": "example"}, {"id": 2, "name": "test"}]
        self.assertEqual(result, expected_result)

    def test_save_to_file(self):
        # You might need to mock the open method or use a temporary file for testing file operations.
        # For simplicity, this example does not handle file I/O.
        instances_list = [Rectangle(1, 2), Rectangle(2, 1)]
        Rectangle.save_to_file(instances_list)
        # Add assertions related to file I/O if necessary.

    def test_load_from_file(self):
        # Similar to save_to_file, you might need to mock open method or handle file I/O properly.
        # For simplicity, this example does not handle file I/O.
        instances_list = Base.load_from_file()
        self.assertEqual(instances_list, [])

if __name__ == '__main__':
    unittest.main()
