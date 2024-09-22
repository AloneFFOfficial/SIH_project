
# Query Storage System

This project implements a query storage system that can handle queries in memory (using a dictionary) and fetch queries from an SQLite database. The project is divided into two main classes:

- `QueryStorage`: Manages in-memory storage using a dictionary.
- `Database`: Reads data from an SQLite database.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Classes](#classes)
  - [QueryStorage](#querystorage-class)
  - [Database](#database-class)
- [Example Usage](#example-usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AloneFFOfficial/SIH_project.git
   ```

2. **Install SQLite3**:
   If you don't have SQLite installed, follow the [SQLite installation guide](https://www.sqlite.org/download.html) based on your operating system.

## Usage

- The `QueryStorage` class allows you to store, view, and delete queries in memory using a Python dictionary.
- The `Database` class interacts with an SQLite database and fetches all data from a specified table.

## Classes

### QueryStorage Class

**Methods**:

1. `add_query(query_id, query_text)`:
   - Adds a query to the in-memory dictionary.
   - Throws an error if the query ID already exists.

2. `view_queries()`:
   - Displays all stored queries from the in-memory dictionary.

3. `delete_query(query_id)`:
   - Deletes a query by its ID from the in-memory dictionary.
   - Throws an error if the query ID does not exist.

### Database Class

**Methods**:

1. `fetch_all()`:
   - Fetches all data from the specified table in the SQLite database.

2. `close()`:
   - Closes the database connection.

## Example Usage

```python
# Example usage of QueryStorage class
query_system = QueryStorage()

# Adding queries to in-memory storage
query_system.add_query(1, "What is the fee structure?")
query_system.add_query(2, "How can I apply for a scholarship?")
query_system.add_query(3, "What documents are needed for admission?")

# Viewing all queries
query_system.view_queries()

# Deleting a query
query_system.delete_query(2)

# Viewing queries after deletion
query_system.view_queries()

# Example usage of Database class
db = Database("query_table")

# Fetching all queries from the database
db_queries = db.fetch_all()
for query_id, query_text in db_queries:
    print(f"ID: {query_id}, Query: {query_text}")

# Closing the database connection
db.close()
```

## Contributing

Contributions are welcome! If you have any ideas to improve the system or find any bugs, feel free to open an issue or a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
