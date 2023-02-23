from db.db_config import MySQL


class Bank:
    def __init__(self):
        self.db = MySQL()

    def check_member(self, member):
        return self.db.fetchone('select count(*) from bank where discord_id=%s', (member,))[0]

    def bank(self, member):
        return self.db.fetchone('select * from bank where discord_id=%s', (member,))

    def new(self, member, bank_id):
        return self.db.execute('insert into bank(bank_id, discord_id) VALUES (%s,%s)', (bank_id, member,))

    def update(self, member, coin):
        return self.db.execute('update bank set coins=%s where discord_id=%s', (coin, member,))

    def delete(self, member):
        return self.db.execute('delete from bank where discord_id=%s', (member,))

    def coins(self, member):
        return self.db.fetchone('select coins from bank where discord_id=%s', (member,))[0]




def plus_coin(member, coin):
    try:
        old_coin = Bank().bank(member)[3]
        total = coin + old_coin
        Bank().update(member, total)
    except Exception as e:
        print(e)
        return False
    else:
        return True

def minut_coin(member, coin):
    try:
        old_coin = Bank().bank(member)[3]
        total = coin - old_coin
        Bank().update(member, total)
    except Exception as e:
        print(e)
        return False
    else:
        return True
