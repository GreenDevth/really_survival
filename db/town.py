from db.db_config import Town

table_name = "town"
class City:
    def __init__(self):
        self.db = Town()

    def drop_table(self):

        sql_cmd = '''DROP TABLE IF EXISTS {}'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def create_table(self):
        sql_cmd = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null ,
            city text null ,
            discord_id text null,
            boss integer null default 0,
            citizen integer null default 1,
            character_name text null default 'not set',
            primary key (id autoincrement )
        )'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def citizen_count(self, city):
        return self.db.fetchone('select count(*) from town where city=?',(city,))[0]

    def new_citizen(self, city, discord_id):
        return self.db.execute('insert into town(city, discord_id) values (?,?)', (city,discord_id,))

    def update_citizen_boss(self, member):
        return self.db.execute('update town set boss=1 where discord_id=?',(member,))

    def update_citizen_ign(self, member, ign):
        return self.db.execute('update town set character_name=? where discord_id=?', (ign, member,))

    def boss(self):
        return self.db.fetchone('select discord_id from town where boss=1',())

    def citizen(self, member):
        return self.db.fetchone('select * from town where discord_id=?', (member,))

    def city(self, member):
        return self.db.fetchone('select count(*) from town where discord_id=?', (member,))[0]



