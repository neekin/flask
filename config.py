import os

basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/movie?charset=utf8'
# app.config['SECRT_KEY'] = 'a random string'
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = True ##mysql配置
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    
    @staticmethod
    def init_app(app):
        pass
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  \
             'sqlite:///' + os.path.join (basedir,'data-dev.sqlite3')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  \
             'sqlite:///' + os.path.join (basedir,'data-test.sqlite3')

class ProductionConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  \
             'sqlite:///' + os.path.join (basedir,'data.sqlite3')
                 
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}                 