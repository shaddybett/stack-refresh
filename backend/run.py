from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# When run, __init__.py builds the app. run.py just runs it
# Is the projects entry point necessary for starting project's development server
# app folder contains all core project logic like routes, models, configurations,
# migrations folder contains database migration scripts for versioning and handling schema changes
# tests folder contains automated tests to ensure system reliability
