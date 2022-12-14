import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    
class LocalDevelopmentConfig(Config):
    # SQLITE_DB_DIR = os.path.join(basedir)
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, 'database.sqlite3')
    DEBUG = True
    SECRET_KEY =  '20ef228e4e1e46f3b30d199701184814' #Strong,random and should be in the evn
    SECURITY_PASSWORD_HASH = "bcrypt"    
    SECURITY_PASSWORD_SALT = '169a0d404e624756b11be1e1eeca02cc' # Read from ENV in your case
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_DEFAULT_REMEMBER_ME=False
    SECURITY_UNAUTHORIZED_VIEW = None
    WTF_CSRF_ENABLED = False
