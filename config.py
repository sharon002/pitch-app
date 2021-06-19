import os

class Config:
    '''
    General configuration parent class
    '''
    
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SECRET_KEY = "12345q"
    MAIL_USERNAME ='sharonjep2016@gmail.com'
    MAIL_PASSWORD ='sharon002'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'


class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'

    DEBUG = True

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'
    DEBUG = True
    
    # SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")

    


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
    # SECRET_KEY = os.environ.get('SECRET_KEY')


    # DATABASE_PASS = os.environ.get('DATABASE_PASS')
    # UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True

    # # emails configuration

    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = os.environ.get('MAIL_PORT')
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    # DEBUG = True

    # @staticmethod
    # def init_app(app):
    #     pass


# class ProdConfig(Config):

#     '''
#     Production configuration child class

#     Args:
#         Config: The parent configuration class with general configuration settings
#     '''
#     SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_SILVER_URL')




# class DevConfig(Config):

#     '''
#     Development configuration child class

#     Args:
#         Config: The parent configuration class with general configuration settings
#     '''
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'



# class TestConfig(Config):

#     '''
#     Test configuration child class

#     Args:
#         Config: The parent configuration class with general configuration settings
#     '''


#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sho:123456@localhost/pitch2'


# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig,
#     'test': TestConfig
# }
