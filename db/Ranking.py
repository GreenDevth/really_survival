from db.db_config import Rank

table_name = "rank"

class Ranking:
    def __init__(self):
        self.db = Rank()

    def drop_table(self):
        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format(table_name)
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null ,
            discord_id text null,
            player_rank integer null default 1,
            player_exp integer null default 0,
            primary key (id autoincrement )
        )'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def check(self, member):
        return self.db.fetchone('select count(*) from rank where discord_id=?',(member,))[0]

    def new_rank(self, member):
        return self.db.execute('insert into rank(discord_id) values (?)', (member,))

    def update_exp(self, member, exp):
        return self.db.execute('update rank set player_exp=? where discord_id=?', (exp,member,))

    def update_rank(self, member, rank):
        return self.db.execute('update rank set player_rank=? where discord_id=?', (rank, member,))
    def ranking(self, member):
        return self.db.fetchone('select * from rank where discord_id=?', (member,))