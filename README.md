### `README.md`

# Query Storage System

This is a simple Python project that demonstrates how to store, view, and manage query data both in memory and in a SQLite database. It uses two main classes: `Database` to interact with a SQLite database, and `QueryStorage` to manage queries in memory.

## Project Structure

- **Database Class**: This class handles the connection to the SQLite database and retrieves data from a table named `query`.
- **QueryStorage Class**: This class is responsible for storing queries in memory as a dictionary and providing methods to add, view, and delete queries.

## Features

1. **Store Queries from Database to Memory**:
   - Queries are fetched from a SQLite database (`Data.db`) and stored in an in-memory Python dictionary.
   
2. **Add Queries**:
   - You can add individual queries to the dictionary by specifying a `query_id` and `query_text`.

3. **View Queries**:
   - Displays all queries stored in memory.

4. **Delete Queries**:
   - Queries can be deleted by specifying their `query_id`.

## Requirements

- Python 3.x
- SQLite3 (pre-installed with Python)
- SQLite database named `Data.db` with a table called `query`.

### Example Table Structure for the `query` table:

```sql
CREATE TABLE query (
  id INTEGER PRIMARY KEY,
  text TEXT
);
```

### Sample Data for the `query` table:

```sql
INSERT INTO query (id, text) VALUES (1, 'What is the fee structure?');
INSERT INTO query (id, text) VALUES (2, 'How can I apply for a scholarship?');
INSERT INTO query (id, text) VALUES (3, 'What documents are needed for admission?');
```

## How to Run the Program

1. **Setup Database**:
   - Ensure you have a SQLite database named `Data.db` with a table called `query`.
   - Add some sample queries to the table.

2. **Run the Program**:
   - Execute the script in Python.
   - It will automatically fetch queries from the database and store them in memory.

### Example Commands:

1. **Fetching Queries from Database**:
   - The program will fetch all the queries from the database and store them in memory.

2. **Viewing Queries**:
   - After fetching, the queries will be printed in the console.

3. **Deleting a Query**:
   - The script will delete the query with ID `2` and display the remaining queries in memory.

## Example Usage

```bash
python query_storage.py
```

### Output Example:

```plaintext
Fetching queries from the database and adding them to memory:
Query with ID 1 added successfully!
Query with ID 2 added successfully!
Query with ID 3 added successfully!

Stored Queries in Memory after adding from the Database:
ID: 1, Query: What is the fee structure?
ID: 2, Query: How can I apply for a scholarship?
ID: 3, Query: What documents are needed for admission?

Query with ID 2 deleted successfully!

Stored Queries in Memory after Deletion:
ID: 1, Query: What is the fee structure?
ID: 3, Query: What documents are needed for admission?
```

## Customization

- **Add New Queries**: You can modify the script to allow dynamic input from users to add new queries.
- **Modify Database Connection**: You can change the database name or table structure by modifying the `Database` class accordingly.

## License

This project is licensed under the MIT License.
