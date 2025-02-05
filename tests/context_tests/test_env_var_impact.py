import unittest
from unittest.mock import patch
from src.utils.app_utils import Logger, ApplicationConfig

class TestEnvironmentVariableImpact(unittest.TestCase):
    @patch('src.config.env_config.DEBUG', True)
    @patch('src.config.env_config.LOG_LEVEL', 'DEBUG')
    def test_logger_debug_mode(self):
        logger = Logger()
        self.assertTrue(logger.debug_enabled)
        self.assertEqual(logger.level, 'DEBUG')

    @patch('src.config.env_config.APP_ENV', 'production')
    def test_application_config_production(self):
        config = ApplicationConfig()
        self.assertTrue(config.production)
        self.assertEqual(config.get_environment(), 'PROD')
        self.assertEqual(config.get_cache_timeout(), 3600)

    @patch('src.config.env_config.APP_ENV', 'development')
    @patch('src.config.env_config.DEBUG', True)
    def test_application_config_development(self):
        config = ApplicationConfig()
        self.assertFalse(config.production)
        self.assertTrue(config.debug)
        self.assertEqual(config.get_environment(), 'DEV')
        self.assertEqual(config.get_cache_timeout(), 0)