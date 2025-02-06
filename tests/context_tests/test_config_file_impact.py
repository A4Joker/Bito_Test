import unittest
from unittest.mock import patch
from src.config.settings import Config

class TestConfigFileImpact(unittest.TestCase):
    @patch('src.config.settings.config')
    def test_database_url_config(self, mock_config):
        mock_config.return_value = 'postgresql://testdb/test'
        self.assertEqual(Config.get_database_url(), 'postgresql://testdb/test')

    @patch('src.config.settings.config')
    def test_api_key_config(self, mock_config):
        mock_config.return_value = 'test-api-key'
        self.assertEqual(Config.get_api_key(), 'test-api-key')

    @patch('src.config.settings.config')
    def test_cache_ttl_config(self, mock_config):
        mock_config.return_value = 7200
        self.assertEqual(Config.get_cache_ttl(), 7200)

if __name__ == '__main__':
    unittest.main()