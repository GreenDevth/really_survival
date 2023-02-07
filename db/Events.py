from db.db_config import Events

tb_name = "event"
class Event:
    def __init__(self):
        self.db = Events()


    def drop_table(self):
        sql = '''DROP TABLE IF EXISTS {}'''.format(tb_name)
        return self.db.execute(sql, ())

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null,
            event_name text null,
            team_name text null,
            player_id text null,
            primary key (id autoincrement)
        )'''.format(tb_name)
        return self.db.execute(sql, ())

    def check(self, member):
        return self.db.fetchone('select count(*) from event where player_id=?', (member,))[0]

    def recode(self, member, event, team):
        return self.db.execute('insert into event(event_name, team_name, player_id) VALUES (?,?,?)', (event,team,member,))

    def player(self, member):
        return self.db.fetchone('select * from event where player_id=?', (member,))

    def event(self):
        return self.db.fetchall('select * from event order by id', ())