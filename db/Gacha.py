from db.db_config import MySQL


class Gacha:
    def __init__(self):
        self.db = MySQL()

    def member_check(self, member):
        return self.db.fetchone('select count(*) from random_event where discord_id = %s', (member,))[0]
    def new(self, member, steam, result):
        return self.db.execute('insert into random_event(discord_id, steam_id, result) VALUES (%s,%s,%s)', (member,steam,result,))
    def get(self, member):
        return self.db.fetchone('select * from random_event where discord_id=%s', (member,))

    def count_1(self):
        return self.db.fetchone('select count(result) from random_event where result=1',())[0]
    def count_2(self):
        return self.db.fetchone('select count(result) from random_event where result=2',())[0]
    def count_3(self):
        return self.db.fetchone('select count(result) from random_event where result=3',())[0]
    def count_4(self):
        return self.db.fetchone('select count(result) from random_event where result=4',())[0]
    def count(self):
        return self.db.fetchone('select count(*) from random_event order by id',())[0]

