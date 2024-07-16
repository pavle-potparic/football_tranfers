import sqlite3
from country_repository import get_all

main_menu = {1: 'Country', 2: 'Club', 3: 'Player', 0: 'Exit'}

country_menu = {1: 'GET ALL COUNTRIES', 2: 'GET COUNTRY BY NAME', 3: 'INSERT COUNTRY',
                4: 'UPDATE COUNTRY', 5: 'DELETE COUNTRY', 0: 'EXIT'}

commands = []

db = sqlite3.connect('football_transfers.sqlite')
cursor = db.cursor()
cursor.execute("INSERT INTO country VALUES (1, 'Srbija', 'Srb')")
cursor.execute("INSERT INTO country VALUES (2, 'Francuska', 'Fra')")
cursor.execute("INSERT INTO country VALUES (3, 'Hrvatska', 'Hrv')")

dict_level = 0

while True:
    if dict_level == 0:
        for key, val in main_menu.items():
            print(str(key) + ':', val)

        question = int(input('Choose the option: '))

        if question == 1:
            while True:
                for key, val in country_menu.items():
                    print(str(key) + ':', val)

                question = int(input('Choose the option: '))

                if question == 0:
                    break

                elif question == 1 or question == 2:
                    print()
                    get_all(cursor)
                    print()

                elif question == 3:
                    input_base = list(input('Enter the values: ').split(' '))
                    commands = [country_menu[3], input_base]

                elif question == 4:
                    input_base = list(input('Enter the values: ').split(' '))
                    commands = [country_menu[4], input_base]

                elif question == 5:
                    input_base = input('Enter the value: ')
                    commands = [country_menu[5], input_base]

        elif question == 0:
            print()
            print(commands)
            print('*****************************')
            print()
            print('CLOSING THE APP')
            break
