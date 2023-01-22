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
            character_name text null,
            primary key (id autoincrement )
        )'''.format(table_name, )
        return self.db.execute(sql_cmd, ())

    def citizen_count(self, city):
        return self.db.fetchone('select count(?) from town',(city,))[0]

    def new_citizen(self, city, discord_id, ign):
        return self.db.execute('insert into town(city, discord_id, character_name) values (?,?,?)', (city,discord_id, ign,))

    def boss(self):
        return self.db.fetchone('select discord_id from town where boss=1',())

    def citizen(self, member):
        return self.db.fetchone('select count(*) from town where discord_id=?', (member,))[0]



