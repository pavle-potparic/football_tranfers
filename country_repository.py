import sqlite3

db = sqlite3.connect('football_transfers.sqlite')

cursor = db.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS country (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, code TEXT)")


def get_all(cursor1):
    row = cursor1.execute("SELECT * FROM country")

    for x in row:
        print(*x)


def get_country(cursor1, country_name):
    row = cursor1.execute("SELECT * FROM country WHERE name LIKE '{}'".format(country_name))

    for x in row:
        print(*x)


def insert_country(cursor1, name, code):
    cursor1.execute("INSERT INTO country (name, code) VALUES ('{}', '{}')".format(name, code))


def update_country(cursor1, row, value_list):
    update_query = f"UPDATE country SET {row} = ? WHERE {row} = ?"
    cursor1.execute(update_query, (value_list[1], value_list[0]))


def delete_country(cursor1, name):
    cursor1.execute("DELETE FROM country WHERE name LIKE '{}'".format(name))

    if cursor1.rowcount > 0:
        print("successfully deleted country " + name)
    else:
        print(name + " not exist in db")


db.close()
