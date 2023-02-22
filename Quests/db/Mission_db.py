import sqlite3

table_name = "mission"


class mission_config:
    def __init__(self):
        self.conn = sqlite3.connect('./Quests/db/mission.db')
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


class UserMission:
    def __init__(self):
        self.db = mission_config()

    def drop_table(self):
        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format("user_mission")
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            user_id integer not null ,
            discord_id text null ,
            title text null,
            img longtext null,
            exp integer null default 0,
            coin integer null default 0,
            start_date text null ,
            end_date text null ,
            primary key (user_id autoincrement )
        )'''.format("user_mission", )
        return self.db.execute(sql_cmd, ())

    def check(self, member):
        return self.db.fetchone('select count(*) from user_mission where discord_id=?', (member,))[0]

    def new(self, member, title, img, exp, coin, start_date, end_date):
        return self.db.execute(
            'insert into user_mission(discord_id, title, img, exp, coin, start_date, end_date) VALUES (?,?,?,?,?,?,?)',
            (member, title, img, exp, coin, start_date, end_date,))

    def delete(self, member):
        return self.db.execute('delete from user_mission where discord_id=?', (member,))

    def start_date(self, member):
        return self.db.fetchone('select start_date from user_mission where discord_id=?', (member,))[0]

    def end_date(self, member):
        return self.db.fetchone('select end_date from user_mission where discord_id=?', (member,))[0]

    def mission(self,member):
        return self.db.fetchone('select * from user_mission where discord_id=?', (member,))


class Mission:
    def __init__(self):
        self.db = mission_config()

    def drop_table(self):
        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format(table_name)
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            mission_id integer not null ,
            title text null,
            img longtext null,
            amount integer null ,
            exp integer null default 0,
            coin integer null default 0,
            primary key (mission_id autoincrement )
        )'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def new(self, title, img, amount, exp, coin):
        return self.db.execute('insert into mission(title, img, amount, exp, coin) VALUES (?,?,?,?,?)', (title, img, amount, exp, coin,))

    def list_id(self):
        return [item[0] for item in self.db.fetchall('select mission_id from mission where title not null ', ())]

    def get_mission_by_id(self, mission_id):
        return self.db.fetchone('select * from mission where mission_id = ?', (mission_id,))


def reset_mission():
    Mission().drop_table()
    Mission().create_table()


def reset_user_mission():
    UserMission().drop_table()
    UserMission().create_table()
