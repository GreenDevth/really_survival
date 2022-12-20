from db.db_config import SQLite


class Users:
    def __init__(self):
        self.db = SQLite()

    def drop_table(self):
        table_name = "users"
        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        tb_name = "users"
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null ,
            discord_id text null ,
            steam_id text null ,
            wallet integer null default 0,
            nickname text null,
            join_date text null,
            verify integer null default 0 ,
            primary key (id autoincrement )
        )'''.format(tb_name, )
        return self.db.execute(sql_cmd, ())

    def user_count(self):
        return self.db.fetchone('select count(*) from users order by id',())
    def new_player(self, member, steam, join_date):
        return self.db.execute('insert into users(discord_id, steam_id, join_date) values (?,?, ?)',(member, steam, join_date,))

    def player(self, member):
        return self.db.fetchall('select * from users where discord_id=?', (member,))
    def check(self, member):
        return self.db.fetchone('select count(*) from users where discord_id=?',(member,))[0]