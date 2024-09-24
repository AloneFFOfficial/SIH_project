# Query Storage and CSV Management System

## Project Overview

This project is a **Query Storage and Management System** built using Python. The application stores queries both in memory (as a dictionary) and in a CSV file. It allows users to:

- Add new queries to the system.
- View all stored queries in memory.
- Delete queries from memory and update the CSV file.
- Sync data between memory and a CSV file for long-term storage.

The system makes use of **Pandas** for CSV file management and ensures that queries can be added, viewed, or deleted in a user-friendly manner.

## Features

- **Persistent Query Storage**: Queries are stored in a CSV file to retain data between sessions.
- **In-Memory Query Management**: Queries are loaded into memory for fast access and manipulation.
- **Add New Queries**: Add queries to both the CSV file and the in-memory dictionary.
- **Delete Queries**: Remove queries from memory, and the changes will be reflected in the CSV file.
- **Menu-based Interaction**: A simple command-line interface to interact with the system.

## Folder Structure

```
.
├── queries.csv         # Stores query data in CSV format
├── main.py             # Main application code
├── README.md           # Project documentation (this file)
└── requirements.txt    # Python dependencies
```

## Getting Started

### Prerequisites

- **Python 3.x** is required to run this project.
- **Pandas** library is used for CSV file operations.

Install required packages by running:

```bash
pip install pandas
```

### Running the Project

1. **Clone the repository** or download the project.
2. Open a terminal and navigate to the project directory.
3. Run the following command to start the application:

```bash
python main.py
```

### CSV File

The system uses a CSV file named `queries.csv` to store query data. If the file does not exist, it will be created automatically.

The CSV file has the following structure:

| query_id | query_text         |
|----------|--------------------|
| 1        | How much is the fee for machanical|
| 2        | What is its fee Structure|

### How the Application Works

When you start the application, the following options are provided:

1. **View all queries in memory**: Displays all the queries currently stored in memory.
2. **Add a new query to the CSV**: Allows the user to add a query by specifying its ID and text. The query is stored in both the CSV and memory.
3. **Delete a query from memory**: Deletes a query from memory. The CSV file is updated to reflect the deletion.
4. **Exit the application**: Ends the program.

### Example

```bash
Menu Options:
1. View all queries in memory
2. Add a new query to the CSV
3. Delete a query from memory
4. Exit the application

Enter your choice (1-4): 2
Enter query id: 101
Enter query text: SELECT * FROM employees WHERE salary > 5000;
Query with ID 101 added to CSV.
Query with ID 101 added successfully!
```

## Classes and Methods

### `CSV_DATA` Class

Handles CSV file creation, data retrieval, addition, and updates.

- **`__init__(self, new_file)`**: Initializes the class, creates the file if it does not exist, and loads data into a Pandas DataFrame.
- **`get_data(self)`**: Retrieves the current data from the CSV file.
- **`add_query_to_csv(self, query_id, query_text)`**: Adds a new query to the CSV file.
- **`update_csv(self, updated_data)`**: Updates the CSV file after deleting a query.

### `QueryStorage` Class

Manages queries in memory (dictionary) and allows for adding, viewing, and deleting queries.

- **`__init__(self)`**: Initializes an empty dictionary to store queries.
- **`add_query(self, query_id, query_text)`**: Adds a query to the in-memory dictionary.
- **`add_queries_from_csv(self, csv_queries)`**: Loads queries from a CSV file into memory.
- **`view_queries(self)`**: Displays all queries stored in memory.
- **`delete_query(self, query_id)`**: Deletes a query from memory and updates the CSV file.
- **`get_all_queries(self)`**: Retrieves all queries stored in memory for CSV updates.

## Future Improvements

- Implement user authentication for query management.
- Add support for more query operations like editing queries.
- Build a web interface using Flask or Django for better user experience.

## License

This project is open-source and available under the **MIT License**.

## Contributions

Contributions are welcome! If you find a bug or have suggestions for improvements, feel free to open an issue or submit a pull request.

---

Feel free to modify this `README.md` to suit the specific needs of your project!
