import os

class Config:
    
    API_BASE_URL = ''
    SECRET_KEY = 'ninjaits'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'jeremy2bjunior@gmail.com'
    MAIL_PASSWORD = 'Juniors2b12'
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_TEST")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oem:Jeremih23@localhost/devsf'
    DEBUG = True
    
config_options = {
    'development':DevConfig,
    'production': ProdConfig,
    'test':TestConfig
}
    