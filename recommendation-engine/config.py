import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')