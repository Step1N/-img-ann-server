import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
)

key = Config.SECRET_KEY
