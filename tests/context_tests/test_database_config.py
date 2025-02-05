import unittest
from unittest.mock import patch
from src.config.database_config import DatabaseConfig

class TestDatabaseConfig(unittest.TestCase):
    @patch('src.config.database_config.config')
    def test_config_values_from_env(self, mock_config):
        # Setup mock environment variables
        mock_config.side_effect = lambda key, default=None, cast=None: {
            'DB_HOST': 'test-host',
            'DB_PORT': '5433',
            'DB_USERNAME': 'test-user',
            'DB_PASSWORD': 'test-pass'
        }.get(key, default)

        # Initialize config
        db_config = DatabaseConfig()

        # Verify values are loaded from environment
        self.assertEqual(db_config.HOST, 'test-host')
        self.assertEqual(db_config.PORT, 5433)
        self.assertEqual(db_config.USERNAME, 'test-user')
        self.assertEqual(db_config.PASSWORD, 'test-pass')

    def test_connection_string_format(self):
        with patch('src.config.database_config.config') as mock_config:
            mock_config.side_effect = lambda key, default=None, cast=None: {
                'DB_HOST': 'localhost',
                'DB_PORT': '5432',
                'DB_USERNAME': 'admin',
                'DB_PASSWORD': 'pass123'
            }.get(key, default)

            db_config = DatabaseConfig()
            conn_str = db_config.get_connection_string()
            expected = 'postgresql://admin:pass123@localhost:5432/mydb'
            self.assertEqual(conn_str, expected)