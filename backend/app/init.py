from flask import Flask
from .config import Config
from .extensions import db, ma, cors
from .routes.contacts import contacts_bp