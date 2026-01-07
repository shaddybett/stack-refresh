<!-- BACKEND -->
The producton grade backend folder structure includes app, migration, test folders and .env, requirements.txt and run.py. One responsibility per file is necessary to prevent circular imports, easier debugging,easy reading of code and easier testing. App contains everything related to the application logic. init.py makes the app folder a python package and contains the application factory. it allows multiple environments(test,dev,prod), required for clean testing and prevents global state bugs


A config file s a plain text file that stores settings, parameters and credentials for an application separate fromthe main source code. this is because secrets must be centralized, config differs per environment and deployment becomes easier

extensions.py contains shared toolds e.g database, JWT,CORS to prevent circular imports and for clean dependency injection

models.py holds databases as python classes for a single source of truth for data and that ORM logic must stay isolated

routes folder contains files each with one domain of the API auth.py for Authentication and contact.py for Contact CRUD this is necessary for scaling(users,payments,orders...) and readability

The test folder is for automated verification of behaviour for catching regressions, safe refactors, required in real teams