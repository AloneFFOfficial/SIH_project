import sqlite3 as sql

'''Getting data from the database'''
class Database:
    def __init__(self):
        self.conn = sql.connect('Data.db')
        self.cur = self.conn.cursor()
        data = self.cur.execute('select * from query')
        self.data = data.fetchall()  # Fetch all rows from the 'query' table
        self.conn.close()

    def get_data(self):
        return self.data


'''Creating the query class'''
class QueryStorage:
    def __init__(self):
        '''Creating the dict'''
        self.query_storage = {}

    '''Adding a single query to the dict'''
    def add_query(self, query_id, query_text):
        try:
            if query_id in self.query_storage:
                raise ValueError(f"Query ID {query_id} already exists in memory.")
            self.query_storage[query_id] = query_text  # Store in memory
            print(f"Query with ID {query_id} added successfully!")
        except ValueError as e:
            print(e)

    '''Adding multiple queries from the database'''
    def add_queries_from_db(self, db_queries):
        for query in db_queries:
            query_id, query_text = query  # Unpack each tuple (id, text)
            self.add_query(query_id, query_text)  # Add each query to the dict

    '''Viewing all the queries in the dict'''
    def view_queries(self):
        if not self.query_storage:
            print("No queries available in memory.")
        else:
            for query_id, query_text in self.query_storage.items():
                print(f"ID: {query_id}, Query: {query_text}")

    '''Deleting queries by ID from the dict'''
    def delete_query(self, query_id):
        try:
            if query_id not in self.query_storage:
                raise KeyError(f"Query ID {query_id} does not exist in memory.")
            del self.query_storage[query_id]  # Delete from memory
            print(f"Query with ID {query_id} deleted successfully!")
        except KeyError as e:
            print(e)


if __name__ == "__main__":
    '''Calling the query class'''
    query_system = QueryStorage()

    '''Getting queries from the Database'''
    db = Database()

    '''Fetching and adding queries from the Database to QueryStorage'''
    print("\nFetching queries from the database and adding them to memory:")
    db_queries = db.get_data()

    if not db_queries:
        print("No queries in the database.")
    else:
        query_system.add_queries_from_db(db_queries)

    '''Viewing the queries in memory after adding from the database'''
    print("\nStored Queries in Memory after adding from the Database:")
    query_system.view_queries()

    '''Deleting data from the query dict'''
    query_system.delete_query(2)

    '''Viewing remaining queries in memory after deletion'''
    print("\nStored Queries in Memory after Deletion:")
    query_system.view_queries()

