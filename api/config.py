"""
This file holds database configuration.
"""
import os

DEVELOPMENT_DB_NAME = "DevApkCreator.db"
PROD_DB_NAME = "ProdApkCreator.db"

"""
Database base configuration.
"""
class BaseConfig:
    DEBUG = False
    SECRET_KEY = '\xb2\xae\x00\x87\x00\xde\x16L\xa1PD\\\xe7\xcf\x8b\x11'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

"""
Database development configuration.
"""
class DevelopmentConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DEVELOPMENT_DB_NAME)

"""
Database production configuration.
"""
class ProductionConfig(BaseConfig):
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, PROD_DB_NAME)


config = {
    'dev': 'api.config.DevelopmentConfig',
    'prod': 'api.config.ProductionConfig'
}