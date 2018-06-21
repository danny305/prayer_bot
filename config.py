import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:////prayer_data_table.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = DEBUG
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = MAIL_USERNAME

SECRET_KEY = '\x15\xc7\x0c\x02\x83\xda\x9e`\xf6ct\xaf\xb9\x85\xb3\xd7,&I\x95\x87\x8a\x9f\x1e'