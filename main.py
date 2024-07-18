import sqlite3
from country_repository import get_all, get_country, insert_country, delete_country, update_country

main_menu = {1: 'Country', 2: 'Club', 3: 'Player', 0: 'Exit'}

country_menu = {1: 'GET ALL COUNTRIES', 2: 'GET COUNTRY BY NAME', 3: 'INSERT COUNTRY',
                4: 'UPDATE COUNTRY', 5: 'DELETE COUNTRY', 0: 'EXIT'}

db = sqlite3.connect('football_transfers.sqlite')
cursor = db.cursor()
cursor.execute("INSERT INTO country (name, code) VALUES ('Srbija', 'Srb')")
cursor.execute("INSERT INTO country (name, code) VALUES ('Francuska', 'Fra')")
cursor.execute("INSERT INTO country (name, code) VALUES ('Hrvatska', 'Hrv')")
cursor.execute("INSERT INTO country (name, code) VALUES ('Engleska', 'Eng')")

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

                elif question == 1:
                    print()
                    get_all(cursor)
                    print()

                elif question == 2:
                    print()
                    name = input('Enter the country name: ')
                    print()
                    get_country(cursor, name)
                    print()

                elif question == 3:
                    input_base = list(input('Enter the country name and the country code: ').split(' '))
                    insert_country(cursor, input_base[0], input_base[1])

                elif question == 4:
                    name_or_code = input('Do you want to change name or code: ')
                    input_base = list(input('Enter the original value for country and then new one: ').split(' '))
                    update_country(cursor, name_or_code, input_base)

                elif question == 5:
                    input_base = input('Enter the name of the country you want to delete: ')
                    delete_country(cursor, input_base)

        elif question == 0:
            print()
            print('*****************************')
            print()
            print('CLOSING THE APP')
            break

db.commit()
db.close()
