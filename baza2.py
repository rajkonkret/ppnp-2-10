# relacyjna baza danych sql
# sqlite baza w jednym pliku

import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    query = '''
    CREATE TABLE developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    # cursor.execute(query)  # wykonanie query na bazie
    # sql_connection.commit()  # trwałe zapamietanie zmian na bazie
    cursor.executescript(sql_script)  # wykonanie kody z wczytanego skryptu

except sqlite3.Error as e:
    print("Bład podczas podłączania bazy danych", e)
finally:  # wykonuje się zawsze niezależnie czy był błąd czy nie
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
# Bład podczas podłączania bazy danych table developers already exists
