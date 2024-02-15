import unittest
import json
import os
import tempfile
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
        # Use a temporary file for testing file I/O
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name

            # Create instances list with specific ids
            instances_list = [Rectangle(1, 2, id=7), Rectangle(2, 1, id=11)]

            # Save instances to the temporary file
            Rectangle.save_to_file(instances_list)

            # Load instances from the temporary file
            loaded_instances = Rectangle.load_from_file()

            # Check if the loaded instances have the same attributes as the expected instances
            expected_instances = [Rectangle(1, 2, id=7), Rectangle(2, 1, id=11)]
            for loaded_instance, expected_instance in zip(loaded_instances, expected_instances):
                self.assertEqual(vars(loaded_instance), vars(expected_instance))

    def test_load_from_file(self):
        # Use a temporary file for testing file I/O
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name

            # Write a JSON string to the temporary file
            with open(temp_filename, 'w') as file:
                file.write('[{"id": 7, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 11, "width": 2, "height": 1, "x": 0, "y": 0}]')

            # Load instances from the temporary file
            instances_list = Rectangle.load_from_file()

            # Check if the loaded instances have the same attributes as the expected instances
            expected_list = [Rectangle(1, 2, id=7), Rectangle(2, 1, id=11)]
            for loaded_instance, expected_instance in zip(instances_list, expected_list):
                self.assertEqual(vars(loaded_instance), vars(expected_instance))

    # Additional test cases for None as arguments and empty method calls

    def test_base_load_from_file_with_none(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(None)

    def test_base_save_to_file_with_empty_list(self):
        Base.save_to_file([])
        # Check if the file is created and not empty
        self.assertTrue(os.path.exists("Rectangle.json"))
        self.assertNotEqual(os.path.getsize("Rectangle.json"), 0)

if __name__ == '__main__':
    unittest.main()
