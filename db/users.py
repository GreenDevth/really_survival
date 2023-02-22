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
            party_name text null,
            join_date text null,
            verify integer null default 0 ,
            primary key (id autoincrement )
        )'''.format(tb_name, )
        return self.db.execute(sql_cmd, ())

    def user_count(self):
        return self.db.fetchone('select count(*) from users order by id',())[0]
    def new_player(self, member, steam, join_date):
        return self.db.execute('insert into users(discord_id, steam_id, join_date) values (?,?, ?)',(member, steam, join_date,))

    def player(self, member):
        return self.db.fetchone('select * from users where discord_id=?', (member,))
    def check(self, member):
        return self.db.fetchone('select count(*) from users where discord_id=?',(member,))[0]
    def approved(self, member):
        return self.db.execute('update users set verify=1 where discord_id=?', (member,))
    def update_city(self, city, member):
        return self.db.execute('update users set party_name=? where discord_id=?', (city, member))
    def wallet_update(self, member, amount):
        return self.db.execute('update users set wallet=? where discord_id=?', (amount, member,))
    def wallet(self, member):
        return self.db.fetchone('select wallet from users where discord_id=?', (member,))[0]

    def delete(self, member):
        return self.db.execute('delete from users where discord_id=?', (member,))



class Supporter:
    def __init__(self):
        self.db = SQLite()


    def drop_table(self):
        table_name = "supporter"
        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        tb_name = "supporter"
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null ,
            discord_id text null ,
            steam_id text null ,
            tag_id text null,
            amount text null,
            primary key (id autoincrement )
        )'''.format(tb_name, )
        return self.db.execute(sql_cmd, ())

    def count(self):
        return self.db.fetchone('select count(*) from supporter order by id', ())[0]
    def check(self, member):
        return self.db.fetchone('select count(*) from supporter where discord_id=?',(member,))[0]
    def new(self, member, steam, tag_id, amount):
        return self.db.execute('insert into supporter(discord_id, steam_id, tag_id, amount) VALUES (?,?,?,?)', (member,steam,tag_id,amount))

    def get(self):
        return self.db.fetchall('select * from supporter order by id', ())

    def member(self, steam):
        return self.db.fetchone('select discord_id from supporter where steam_id=?', (steam,))[0]

    def steam_id(self):
        return [item[0] for item in self.db.fetchall('select steam_id from supporter order by id',())]

    def discord_id(self):
        return [item[0] for item in self.db.fetchall('select discord_id from supporter where steam_id is not null ',())]


class PlayerEvent:
    def __init__(self):
        self.db = SQLite()

    def drop_table(self):
        table_name = "player_event"
        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        tb_name = "player_event"
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null ,
            discord_id text null ,
            steam_id text null ,
            event_name text null,
            success integer not null default 0,
            primary key (id autoincrement )
        )'''.format(tb_name, )
        return self.db.execute(sql_cmd, ())


    def check(self, member):
        return self.db.fetchone('select count(*) from player_event where discord_id=?', (member,))[0]
    def new(self, member, steam, name):
        return self.db.execute('insert into player_event(discord_id, steam_id, event_name) VALUES (?,?,?)',(member,steam,name,))
    def event(self, member):
        return self.db.fetchone('select * from player_event where discord_id=?', (member,))