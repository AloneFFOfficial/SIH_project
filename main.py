import sqlite3 as sql

'''Creating Database Class'''
class Database:
    def __init__(self, table_name):
        self.conn = sql.connect('Data.db')
        self.cur = self.conn.cursor() 
        self.table_name = table_name 

    '''Fetching data from the db'''
    def fetch_all(self):
        self.cur.execute(f'SELECT * FROM {self.table_name}')
        return self.cur.fetchall()

    '''Closing db connection'''
    def close(self):
        self.conn.close()

'''Creating the query class'''
class QueryStorage:
    def __init__(self):
        '''Creating the dict'''
        self.query_storage = {}

    '''Adding all the queries in the dict'''
    def add_query(self, query_id, query_text):
        try:
            if query_id in self.query_storage:
                raise ValueError(f"Query ID {query_id} already exists in memory.")
            self.query_storage[query_id] = query_text  # Store in memory
            print(f"Query with ID {query_id} added successfully!")
        except ValueError as e:
            print(e)

    '''Vieeing all the queries in the dict'''
    def view_queries(self):
        if not self.query_storage:
            print("No queries available in memory.")
        else:
            for query_id, query_text in self.query_storage.items():
                print(f"ID: {query_id}, Query: {query_text}")

    '''Deleting Queries on the basis of its ID from the dict'''
    def delete_query(self, query_id):
        try:
            if query_id not in self.query_storage:
                raise KeyError(f"Query ID {query_id} does not exist in memory.")
            del self.query_storage[query_id]  # Delete from memory
            print(f"Query with ID {query_id} deleted successfully!")
        except KeyError as e:
            print(e)

# Example usage
if __name__ == "__main__":
    '''Calling the query class'''
    query_system = QueryStorage()

    '''Adding data in the dict'''
    query_system.add_query(1, "What is the fee structure?")
    query_system.add_query(2, "How can I apply for a scholarship?")
    query_system.add_query(3, "What documents are needed for admission?")

    '''Viewing queries in the dict'''
    print("\nStored Queries in Memory:")
    query_system.view_queries()

    '''Deleting data from the query dict'''
    query_system.delete_query(2)

    '''This Shows all the queries which were deleted'''
    print("\nStored Queries in Memory after Deletion:")
    query_system.view_queries()

    '''Geting queries from the Database'''
    db = Database("query_table")

    '''showing queries from the Database'''
    print("\nStored Queries in Database:")
    db_queries = db.fetch_all()
    if not db_queries:
        print("No queries in the database.")
    else:
        for query_id, query_text in db_queries:
            print(f"ID: {query_id}, Query: {query_text}")

    '''Closing the Database'''
    db.close()
    
