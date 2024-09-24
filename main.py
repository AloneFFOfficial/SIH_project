import pandas as pd

'''Getting data from the csv'''
class CSV_DATA:
    def __init__(self,new_file):
        try:
            self.data=pd.read_csv(new_file)
        except Exception as e:
            print(f"file not found: {e}")
            self.data=pd.DataFrame(self.data)


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

    '''Adding multiple queries from the CSV_DATA'''
    def add_queries_from_csv(self, csv_queries):
        for query in csv_queries:
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

    '''Getting queries from the csv_data'''
    new_file="queries.csv"
    csv_data=CSV_DATA(new_file)

    '''Fetching and adding queries from the CSV_DATA to QueryStorage'''
    print("\nFetching queries from the CSV_DATA and adding them to memory:")
    csv_queries = csv_data.get_data()

    if not csv_queries:
        print("No queries in the database.")
    else:
        query_system.add_queries_from_csv(csv_queries)

    '''Viewing the queries in memory after adding from the cvs'''
    print("\nStored Queries in Memory after adding from the cvs:")
    query_system.view_queries()

    '''Deleting data from the query dict'''
    query_system.delete_query(2)

    '''Viewing remaining queries in memory after deletion'''
    print("\nStored Queries in Memory after Deletion:")
    query_system.view_queries()