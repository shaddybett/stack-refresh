Why do we need an orm? ORM(object relational mapper) allows us to interact with the database without writing raw SQL
for example instead of SELECT * FROM users WHERE id = 1 you write user = User.query.get(1)
<!-- Advantages -->
1. Write Python instead of SQL
2. Prevents SQL injections
3. Database portability - you can easily switch between PostgreSQL,SQLite,MySQL etc by simply changing 
SQLALCHEMY_DATABASE_URI = "postgresql://..."
4. Relationships are easier - ORMs simplify one-to-many, many-to-many relationships
5. Migrations become easy
Using Flask-Migrate, the ORM knows how your tables are structured.

<!-- CORS -->
CORS allows us interact with the backend from a different specified url and by doing so prevents requests from unknown urls

<!-- JSON -->
Data format used to send data between frontend and backend

404 means endpoint does not exist 
flask blue prints separate routes for cleaner code