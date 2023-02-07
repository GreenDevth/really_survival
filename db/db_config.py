import sqlite3
from config import db_connection

class MySQL:
    def __init__(self):
        self.conn = db_connection()
        self.cur = self.conn.cursor()

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()
        return self.cur

    def fetchall(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchall()
        res = list(result)
        return res

    def fetchone(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        res = list(result)
        return res

    def select(self, query, data):
        self.cur.execute(query, data)
        return self.cur

    def __del__(self):
        self.conn.close()

class SQLite:
    def __init__(self):
        self.conn = sqlite3.connect('./db/users.db')
        self.cur = self.conn.cursor()

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()
        return self.cur

    def fetchall(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchall()
        res = list(result)
        return res

    def fetchone(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        res = list(result)
        return res

    def select(self, query, data):
        self.cur.execute(query, data)
        return self.cur

    def __del__(self):
        self.conn.close()

class Town:
    def __init__(self):
        self.conn = sqlite3.connect('./db/city.db')
        self.cur = self.conn.cursor()

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()
        return self.cur

    def fetchall(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchall()
        res = list(result)
        return res

    def fetchone(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        res = list(result)
        return res

    def select(self, query, data):
        self.cur.execute(query, data)
        return self.cur

    def __del__(self):
        self.conn.close()


class Rank:
    def __init__(self):
        self.conn = sqlite3.connect('./db/ranking.db')
        self.cur = self.conn.cursor()

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()
        return self.cur

    def fetchall(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchall()
        res = list(result)
        return res

    def fetchone(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        res = list(result)
        return res

    def select(self, query, data):
        self.cur.execute(query, data)
        return self.cur

    def __del__(self):
        self.conn.close()

class Events:
    def __init__(self):
        self.conn = sqlite3.connect('./db/events.db')
        self.cur = self.conn.cursor()

    def execute(self, query, data):
        self.cur.execute(query, data)
        self.conn.commit()
        return self.cur

    def fetchall(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchall()
        res = list(result)
        return res

    def fetchone(self, query, data):
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        res = list(result)
        return res

    def select(self, query, data):
        self.cur.execute(query, data)
        return self.cur

    def __del__(self):
        self.conn.close()