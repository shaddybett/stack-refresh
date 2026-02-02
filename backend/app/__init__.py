from flask import Flask
from .config import Config
from .extensions import db, jwt, cors
from .routes.auth import auth_bp
from .routes.contacts import contacts_bp

def create_app(create_app=Config):    # This allows different configs e.g development, Testing, production for example we can do something like create_app(TestingConfig)
    app = Flask(__name__)  # This creates the flask app. __name__ helps Flask locate resources
    app.config.from_object(create_app) # loads settings like SECRET_KEY keeping config out of the code logic

    # Initialize extensions. Extensions are created once and bound to the app later avoiding circular imposrts and making tests easier
    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    # Register Blueprints. Keeps routes modular,Each feature can live in its own blueprint, essential for large apps
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(contacts_bp, url_prefix="/contacts")

    # Return the app. run.py,tests or WSGI servers call this function
    # Flask app is now ready
    return app

# In python , __init__.py tells python that this folder "app" is a python package but in flask it does more than that. In a production grade flask backend, this file is responsible for:
# Creating the flask application
# Loading configuration
# initializing extensions
# Registering blueprints

# Using create_app() allows:
# Multiple app instances
# Isolated test environments
# Better dependency injection
# Easier scaling & maintenance
# This is non negotiable for serious flask projects

# __init__.py is a factory that assembles the application. It does not do work it prepares the system to work