"""Configuration classes for the rent-it API."""

import os

class Config:
    """Base configuration class."""
    DEBUG = False
    DEVELOPMENT = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    DEVELOPMENT = False


class TestingConfig(Config):
    """Testing configuration."""
    DEBUG = True
    DEVELOPMENT = True


class MigrationConfig(Config):
    """Migration configuration."""
    DEBUG = False
    TESTING = False