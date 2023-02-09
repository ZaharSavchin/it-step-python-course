import sqlite3


with sqlite3.connect('materials.sqlite3') as db:
    cursor = db.cursor()
    avg_weight = cursor.execute('SELECT AVG (weight) FROM materials').fetchone()
    print(int(avg_weight[0]))