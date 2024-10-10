import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'  # Update with your DB credentials
    SQLALCHEMY_TRACK_MODIFICATIONS = False
