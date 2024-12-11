class Config:
    DEBUG = True
    SECRET_KEY = 'secret'

class TestConfig(Config):
    TESTING = True  # Enable testing mode
    DEBUG = False   # Disable debug mode for tests