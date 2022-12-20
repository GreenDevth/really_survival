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

