import sqlite3

import mysql.connector


def db_connection():
    data = get_connection()
    connection = mysql.connector.connect(
        host=str(data[1]),
        database=str(data[2]),
        user=str(data[3]),
        password=str(data[4])
    )
    if connection.is_connected():
        return connection


def get_connection():
    con = sqlite3.connect('./config.db')
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM database WHERE id = 2')

    rows = cursorObj.fetchall()

    for row in rows:
        res = list(row)
        return res
