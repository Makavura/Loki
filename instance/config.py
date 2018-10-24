
import os


class Configuration(object):
    """Configuration Class """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'rikitikitavi')
    CSRF_ENABLED = True


class DevelopmentConfiguration(Configuration):
    """Develepment"""
    DEBUG = True


class TestingConfiguration(Configuration):
    """Tests Configurations"""
    TESTING = True
    DEBUG = True


class ProductionConfiguration(Configuration):
    """Production Deployment"""
    DEBUG = False
    TESTING = False


config_by_name = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
}