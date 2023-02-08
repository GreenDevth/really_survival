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
        return self.db.execute('insert into event(event_name, team_name, player_id) VALUES (?,?,?)',
                               (event, team, member,))

    def player(self, member):
        return self.db.fetchone('select * from event where player_id=?', (member,))

    def event(self):
        return self.db.fetchall('select * from event order by id', ())


class TeaserEvent:
    def __init__(self):
        self.db = Events()

    def drop_table(self):
        sql = '''DROP TABLE IF EXISTS {}'''.format("teaser")
        return self.db.execute(sql, ())

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS {}(
            id integer not null,
            title text null,
            image_url text null,
            status integer default 1,
            secret_code text null,
            player_id text null,
            success integer null default 0,
            primary key (id autoincrement)
        )'''.format("teaser")
        return self.db.execute(sql, ())

    def new(self, title, image, secret_code):
        return self.db.execute('insert into teaser(title,secret_code,image_url) VALUES (?,?,?)',
                               (title, secret_code, image,))

    def seccess(self, secret_code):
        return self.db.execute('update teaser set success=1 where secret_code=?', (secret_code,))

    def edit(self, teaser_id, member):
        return self.db.execute('update teaser set player_id=?, status=0 where secret_code=?', (member, teaser_id,))

    def get(self, teaser_id):
        return self.db.fetchone('select * from teaser where id=?', (teaser_id,))

    def teaser_list(self):
        return [item[0] for item in self.db.fetchall('select id from teaser where player_id is null or status=1', ())]

    def my_teaser(self, member):
        return self.db.fetchone('select * from teaser where player_id=?', (member,))

    def check(self, member):
        return self.db.fetchone('select count(*) from teaser where player_id=?', (member,))[0]

    def update_list(self, member, teaser_id):
        return self.db.execute('update teaser set player_id=?, status=0 where id=?',(member, teaser_id,))

    def teaser(self, teaser_id):
        return self.db.fetchone('select * from teaser where id=?', (teaser_id,))


