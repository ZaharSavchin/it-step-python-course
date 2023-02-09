import sqlite3


def create_table():
    with sqlite3.connect('materials.sqlite3') as table:
        cursor = table.cursor()
        cursor.execute(
            """
            CREATE TABLE materials (
            id INTEGER,
            name VARCHAR(50),
            weight INTEGER,
            about TEXT)
            """
        )


def insert_values(id: int, name: str, weight: int, about: str):
    with sqlite3.connect('materials.sqlite3') as table:
        cursor = table.cursor()
        cursor.execute(
            """
            INSERT INTO materials (id, name, weight, about)
            VALUES (?, ?, ?, ?)
            """, (id, name, weight, about)
        )


# create_table()
#
#
# insert_values(1, 'steel', 25, "('wheels', 4), ('passengers', 5)]")
# insert_values(2, 'cooper', 15, "('color', 'red'), ('price', 55)]")
# insert_values(3, 'wood', 500, "('color', 'grey'), ('price', 450)]")
# insert_values(4, 'plastik', 20, "('color', 'any'), ('price', 50)]")