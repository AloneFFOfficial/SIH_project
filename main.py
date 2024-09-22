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

    
    def add_query(self, query_text):
        try:
            cur.execute(f"insert into {self.table_name} query values ",(query_text))
            print("query added succesfully")
        except exception as e:
            print(f"error occured : {e} ")
    
    
    def view_queries(self):
        try:
        cur.execute("select *from quieries") 
        all_queries= self.cur.fetchall()     
        return all_queries
        except Exception as e:
            print(f"queries not found:{e}")

