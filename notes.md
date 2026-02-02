<!-- BACKEND -->
The producton grade backend folder structure includes app, migration, test folders and .env, requirements.txt and run.py. One responsibility per file is necessary to prevent circular imports, easier debugging,easy reading of code and easier testing. App contains everything related to the application logic. init.py makes the app folder a python package and contains the application factory. it allows multiple environments(test,dev,prod), required for clean testing and prevents global state bugs


A config file s a plain text file that stores settings, parameters and credentials for an application separate fromthe main source code. this is because secrets must be centralized, config differs per environment and deployment becomes easier

extensions.py contains shared toolds e.g database, JWT,CORS to prevent circular imports and for clean dependency injection

models.py holds databases as python classes for a single source of truth for data and that ORM logic must stay isolated

routes folder contains files each with one domain of the API auth.py for Authentication and contact.py for Contact CRUD this is necessary for scaling(users,payments,orders...) and readability

The test folder is for automated verification of behaviour for catching regressions, safe refactors, required in real teams

A class is a blueprint for creating objects. It defines what attributes and methods the resluting object will have. Instances are specific objects created from a class

<!-- config.py -->
We define a class for all related configs because a class allows for easy inheritance (DevConfig,ProdConfig)
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret") - used by flask internally for sessions,cookies and security
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db" defines where the database lives
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret") is used to sign tokens so if leaked attackers may forge tokens

<!-- __init__.py -->
this is the application factory very important.





<!-- Refresher notes -->
An industry grade backend folder structure entails the app folder,migrations,test and .env,requirements.txt and run.py files. The app folder contains everything the app requires, tests are all the tests needed for the app, migrations for database management ,.env to store the app's credentials that should not be exposed or pushed to github, extensions.txt to lists all packages that have been installed and in use in the app, run.py to execute the app

<!-- Modular and scalable --> modular means breaking down large application into smaller , independent and manageable components while scalable means systems ability to increase workloads, user traffic or data volumes without compromising performance    


<!-- Root folder structure -->
A production grade flask backend should be modular and scalable. 
Modular means the application is broken down into small, independent components making the codebase easier to read, maintain, test and debug.
Scalable means it should be able to handle growing traffic and features without compromising performance or stability.

At the root level, the project contains several folders and files.
The app folder contains core application logic like routes, models, business logic and configurations
The migrations folder contains database migration scripts to handle schema changes and versioning
The test folder contains automated tests that help ensure system reliability and prevent regressions
The project files includes, .env which stores environment specif variables like database URLs and api keys, keeping sensitive data outside the codebase
requirements.txt contains a list of project dependencies to ensure consistent environment setup across machines
run.py serves as the application entry point and is used to start the flask developement server

<!-- App Folder --> 
__init__.py
In python, __init__.py marks a directory as a package. In flask __init__.py does more than that whereby it is responsible for : creating the flask application, loading configurations, initializing extensions, registering blueprints(routes)
In production we do not use app = Flask(__name__) coz it's bad for testing, multiple environments, scalability instead we use the application factory pattern which means creating a function that builds and returns flask app and app is cteated only when needed
