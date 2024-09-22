import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('Data.db')

# Create a cursor object
cur = conn.cursor()
cur.execute('Create table query(sno,query)')
# List of tuples containing data to insert (for example: serial number and query)
data_to_insert = [
    (1, "What is the fee structure?"),
        (2, "How can I apply for a scholarship?"),
            (3, "What documents are needed for admission?")
            ]

            # SQL query to insert multiple records at once
cur.executemany("INSERT INTO query (sno, query) VALUES (?, ?)", data_to_insert)

            # Commit the changes
conn.commit()

            # Close the connection
conn.close()

print("Multiple records inserted successfully!")




