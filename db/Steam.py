from db.Database import MySQL

tb_name = "steam"


class Steam:
    def __init__(self):
        self.db = MySQL()

    def purge(self):
        sql = """TRUNCATE TABLE {}""".format(tb_name, )
        return self.db.execute(sql, ())

    def check(self, member):
        return self.db.fetchone('select count(*) from steam where discord_id=%s', (member,))[0]

    def new(self, member, steam):
        return self.db.execute('insert into steam(discord_id, steam_id) values (%s,%s)', (member, steam,))

    def get(self, member):
        return self.db.fetchone('select steam_id from steam where discord_id=%s', (member,))[0]


class Pack:
    def __init__(self):
        self.db = MySQL()

    def purge(self):
        sql = """TRUNCATE TABLE {}""".format("pack")
        return self.db.execute(sql, ())

    def get(self, name):
        return self.db.fetchone('select code from pack where name=%s', (name,))


class Perm:
    def __init__(self):
        self.db = MySQL()

    def purge(self):
        sql = """TRUNCATE TABLE {}""".format("permission")
        return self.db.execute(sql, ())

    def check(self, member):
        return self.db.fetchone('select count(*) from permission where discord_id=%s', (member,))[0]

    def new(self, member):
        return self.db.execute('insert into permission(discord_id) VALUES (%s)', (member,))

    def update(self, member):
        return self.db.execute('update permission set perm=0 where discord_id=%s', (member,))
