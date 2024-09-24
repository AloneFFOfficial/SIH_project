import pandas as pd
import os

'''Created the CSV class'''
class CSV_DATA:
    def __init__(self, new_file):
        self.file = new_file
        try:
            if os.path.exists(new_file):
                self.data = pd.read_csv(new_file)
            else:
                '''It will Create an empty DataFrame if the file does not exist'''
                self.data = pd.DataFrame(columns=['query_id', 'query_text'])
                self.data.to_csv(new_file, index=False)
                print(f"File '{new_file}' created.")
        except Exception as e:
            print(f"Error reading file: {e}")
            self.data = pd.DataFrame(columns=['query_id', 'query_text'])

    def get_data(self):
        return self.data

    '''Add query to the CSV file if it does not exist'''
    def add_query_to_csv(self, query_id, query_text):
        if query_id not in self.data['query_id'].values:
            new_query = {'query_id': query_id, 'query_text': query_text}
            self.data = self.data._append(new_query, ignore_index=True)
            self.data.to_csv(self.file, index=False)
            print(f"Query with ID {query_id} added to CSV.")
        else:
            print(f"Query ID {query_id} already exists in the CSV file.")

    '''Update the CSV file after query deletion'''
    def update_csv(self, updated_data):
        self.data = updated_data
        self.data.to_csv(self.file, index=False)
        print("CSV file updated.")

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
            self.query_storage[query_id] = query_text
            print(f"Query with ID {query_id} added successfully!")
        except ValueError as e:
            print(e)

    '''Adding multiple queries from the CSV_DATA'''
    def add_queries_from_csv(self, csv_queries):
        for index, row in csv_queries.iterrows():
            query_id, query_text = row['query_id'], row['query_text']
            self.add_query(query_id, query_text)

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
            del self.query_storage[query_id]
            print(f"Query with ID {query_id} deleted successfully!")
        except KeyError as e:
            print(e)

    '''Getting all stored queries for CSV update'''
    def get_all_queries(self):
        return pd.DataFrame(list(self.query_storage.items()), columns=['query_id', 'query_text'])


if __name__ == "__main__":
    query_system = QueryStorage()

    '''Getting queries from the CSV_DATA'''
    new_file = "queries.csv"
    csv_data = CSV_DATA(new_file)

    '''Fetching and adding queries from the CSV_DATA to QueryStorage'''
    csv_queries = csv_data.get_data()

    if csv_queries.empty:
        print("No queries in the CSV file.")
    else:
        query_system.add_queries_from_csv(csv_queries)

    '''Main application loop'''
    while True:
        print("\nMenu Options:")
        print("1. View all queries in memory")
        print("2. Add a new query to the CSV")
        print("3. Delete a query from memory")
        print("4. Exit the application")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            print("\nStored Queries in Memory:")
            query_system.view_queries()

        elif choice == '2':
            query_id = int(input("Enter query id: "))
            query_text = input("Enter query text: ")
            csv_data.add_query_to_csv(query_id, query_text)
            query_system.add_query(query_id, query_text)

        elif choice == '3':
            query_delete_id = int(input("Enter query id to be deleted: "))
            query_system.delete_query(query_delete_id)

            '''Updating the CSV after deletion'''
            updated_data = query_system.get_all_queries()
            csv_data.update_csv(updated_data)

        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
