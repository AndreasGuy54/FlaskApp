import sqlite3
from sqlite3.dbapi2 import connect

connection = sqlite3.connect('flask_app.db', check_same_thread= False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users (
        username, 
        password,
        fav_team
        )VALUES(
            'Bruce',
            'Wayne',
            'Justice League'
        );"""
)

cursor.execute(
    """INSERT INTO users (
        username, 
        password,
        fav_team
        )VALUES(
            'Tony',
            'Stark',
            'Avengers'
        );"""
)

connection.commit()
cursor.close()
connection.close()