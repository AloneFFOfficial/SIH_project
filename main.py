import sqlite3 as sql

class Database:
    def __init__(self,table_name):
        conn = sql.connect('Data.db')
        cur = conn.cursur()
        data = cur.execute(f'select * from {table_name}')
        self.data = data.fetchall()

    def __str__(self):
        return self.data
    


class query(Database):
    def __init__(self):
        super().__init__()