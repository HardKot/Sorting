import sqlite3
from listtype import types

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
    cursor.execute("INSER INTO formats VALUES (?, ?)", (name, type))
    database.commit()
    database.close()

def addtype(name):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execut("INSERT INTO types VALUES (?)",(name))
    database.commit()
    database.close()

def createdatebase():
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("CREAT TABLE types (name)")
    cursor.execute("CREAT TABLE formats (name, type)")
    database.commit()
    database.close()
    for type in types:
        addtype(type)
        for format in types.get(type):
            addformat(format, type)
