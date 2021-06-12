import sqlite3

# this is the database connection and name
connection = sqlite3.connect('flask_app.db', check_same_thread=False)
cursor = connection.cursor()

# create tables with the cursor
cursor.execute(
    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        fav_team VARCHAR(32)
    );"""
)

connection.commit()
cursor.close()
connection.close()