import sqlite3

with sqlite3.connect('users.sqlite3') as db:
    cursor = db.cursor()
    cursor.execute(
        """
        CREATE TABLE my_users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ful_name TEXT,
        short_name VARCHAR(50),
        age INT)
        """
    )