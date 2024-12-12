import os
import urllib.parse

class Config:
    db_user = os.getenv('DATABASE_USER')
    db_password = urllib.parse.quote_plus(os.getenv('DATABASE_PASSWORD') or '')
    db_host = os.getenv('DATABASE_HOST')
    db_port = os.getenv('DATABASE_PORT')
    db_name = os.getenv('DATABASE_NAME')

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False