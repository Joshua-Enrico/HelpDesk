import os

SECRET_KEY = 'hello'
MAIL_SERVER = 'SMTP.gmail.com'
MAIL_PORT = '587'
MAIL_USER_SSL = False
MAIL_USER_TLS = True
MAIL_USERNAME = 'joshuaenrico123@gmail.com'
MAIL_PASSWORD = 'yoyogold123321'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://Helpdesk:Helpdesk@localhost/User'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
