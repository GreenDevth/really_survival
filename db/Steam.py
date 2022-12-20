from db.Database import MySQL

tb_name = "steam"
class Steam:
    def __init__(self):
        self.db = MySQL()

    def purge(self):
        sql = """TRUNCATE TABLE {}""".format(tb_name,)
        return self.db.execute(sql,())
