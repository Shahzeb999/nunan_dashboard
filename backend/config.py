import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or         'postgresql://postgres:Shahzeb%4012345@localhost:5432/nunam'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
