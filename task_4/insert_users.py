from user import User
import sqlite3


def insert_user(user):
    with sqlite3.connect('users.sqlite3') as db:
        cursor = db.cursor()
        cursor.execute(
            """
            INSERT INTO my_users (ful_name, short_name, age)
            VALUES (?, ?, ?)
            """, (user.get_ful_name(), user.get_short_name(), user.get_age())
        )


Zahar = User("Савчин З.С.", "Савчин Захар Сергеевич", 1996, 2, 3)
Vanya = User("Иванов Иван Иванович", "Иванов И.И.", 1990, 4, 28)
Bob = User("Bob Smith Jimovich", "Bob S.J.", 1945, 11, 12)
# insert_user(Zahar)
# insert_user(Vanya)
# insert_user(Bob)


def find_user_by_age(start_age, end_age):
    with sqlite3.connect('users.sqlite3') as db:
        cursor = db.cursor()
        return cursor.execute("""
                       SELECT ful_name, age FROM my_users
                       WHERE age >= (?) and age <= (?)
                       """, (start_age, end_age)
                       ).fetchall()


print(find_user_by_age(20, 40))