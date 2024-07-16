import sqlite3

db = sqlite3.connect('football_transfers.sqlite')

cursor = db.cursor()


def get_all(cursor1):
    row = cursor1.execute("SELECT * FROM country")

    for x in row:
        print(*x)


db.close()
