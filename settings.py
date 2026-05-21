import os


SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
SECRET_KEY = os.getenv('SECRET_KEY', 'super-secret-key-123')
DROPBOX_TOKEN = os.getenv('DROPBOX_TOKEN')