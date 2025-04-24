import unittest
from src.core.processors import JsonProcessor, XmlProcessor

class TestProcessorImplementations(unittest.TestCase):
    def setUp(self):
        self.json_processor = JsonProcessor()
        self.xml_processor = XmlProcessor()
        self.test_data = {"name": "test", "value": 123}

    def test_json_processor(self):
        self.assertTrue(self.json_processor.validate(self.test_data))
        processed = self.json_processor.process(self.test_data)
        self.assertEqual(processed, self.test_data)

    def test_xml_processor(self):
        self.assertTrue(self.xml_processor.validate(self.test_data))
        processed = self.xml_processor.process(self.test_data)
        self.assertEqual(processed["<name>test</name>"], "test")
        self.assertEqual(processed["<value>123</value>"], 123)

    def test_invalid_data(self):
        invalid_data = {"key": lambda x: x}  # Function is not JSON serializable
        self.assertFalse(self.json_processor.validate(invalid_data))
        self.assertFalse(self.xml_processor.validate(invalid_data))