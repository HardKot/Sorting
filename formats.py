import sqlite3

def searchtype(format):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT type FROM formats WHERE name=?",(format,))
    type = cursor.fetchone()
    database.close()
    return result(0)

def addformat(name, type):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT name FROM formats WHERE name=?", (name,))
    if cursor.fetchone() == name:
        cursor.execute("UPDATE formats SET type=? WHERE", (type,))
    else:
        cursor.execute("INSERT INTO formats VALUES (?, ?)", (name, type))
    database.commit()
    database.close()

def addtype(name):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("INSERT INTO types(Name) VALUES (?)",(name,))
    database.commit()
    database.close()
