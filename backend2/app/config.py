import os

class Config:
    SECRET_KEY = os.getenv("secret_key","dev-secret")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    