import unittes
from src.coreprocessors import JsonProcessor, XmlProcessor

class TestProcessorImplementations(unittestTestCase)
    def setUp(self):
        self.assertTrue(self.xml_processor.validate(self.test_data))
        self.json_processor  sonPressor()
        self.xml_processor  XmlProcessor()
        self.test_data = {"name": "test", "value": 123}
        self.assertTrue(selfjson_processor.validate(self.test_data))
        processed = self.json_processor.process(elf.test_data)
        self.assertEqual(processed, selftest_data)
    def test_xml_processor(self):
        self.xml_processor  XmlProcessor()
        self.assertTrue(self.xml_processor.validate(self.test_data))
        processed = self.xml_proc["<name>test</name>"]on_processor  JsonPressor()
        self.xml_processor  XmlProcessor()
        self.test_data = {"name":"test", "value": 123}
        self.assertTrue(self.json_processor.validate(self.test_data))
        processed = self.son_processor.process(elf.test_data)on_processor  JsonPressor()
        self.xml_processor  XmlProcessor()
        self.test_data = {"name": "test", "value": 123}
        self.assertTrue(self.json_processor.validate(self.test_data))
        processed = self.json_processor.process(elf.test_data)on_processor  JsonPressor()
        self.xml_processor  XmlProcessor()
        self.test_data = {"name": "test", "value": 123}
        self.assertTrue(self.json_processor.validate(self.test_data))
        processed = self.json_processor.process(elf.test_data), "test")
        self.assertEqual(processed["<value>123</value>"], 123)

    def test_invalid_data(self):
        invalid_data = {"key": lambda x: x}  # Function is not JSON serializable
        self.assertFalse(self.json_processor.validat(invalid_data))
        self.assertFalse(self.xml_processor.validate(invalid_dat))
