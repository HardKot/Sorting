import sqlite3

def searchtype(format):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT type FROM formats WHERE Name=?",(format,))
    type = cursor.fetchone()
    database.close()
    return type

def addformat(name, type):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT name FROM formats WHERE name=?", (name,))
    if cursor.fetchone() == name:
        cursor.execute("UPDATE formats SET type=? WHERE name=?", (type, name))
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

def addstorage(type, storage):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT type FROM storages WHERE type=?",(type,))
    if cursor.fetchone() == type:
        cursor.execute("UPDATE storges SET storage=? WHERE type=?", (storage, type))
    else:
        cursor.execute("INSERT INTO storages VALUES (?,?)", (type, storage))
    database.commit()
    database.close

def takestorage(type):
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT storage FROM storages WHERE type=?", (type,))
    storge = cursor.fetchone()
    database.close()
    return storge[0]

def taketype():
    database = sqlite3.connect('sorting.db')
    cursor = database.cursor()
    cursor.execute("SELECT name FROM types")
    types = cursor.fetchall()
    database.close()
    return types
