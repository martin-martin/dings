import os
import sqlite3


def create_table_if_not_exists():
    # Step 1: Connect to the database (or create one if it doesn't exist)
    conn = sqlite3.connect('dinge.db')

    # Step 2: Create a cursor
    cursor = conn.cursor()

    # Step 3: Execute the SQL query to create the table if it doesn't exist
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS dinge (
            text TEXT,
            available INTEGER,
            url TEXT
        )
    '''
    cursor.execute(create_table_query)

    # Step 4: Commit the changes
    conn.commit()

    # Step 5: Close the connection
    conn.close()


def add_tuple_to_database(data_tuple):
    # Step 1: Connect to the database (or create one if it doesn't exist)
    conn = sqlite3.connect('dinge.db')

    # Step 2: Create a cursor
    cursor = conn.cursor()

    # Step 3: Execute the SQL query to insert the data
    # Assuming the table structure has two columns: 'column1' and 'column2'
    insert_query = "INSERT INTO dinge (text, available, url) VALUES (?, ?, ?)"
    cursor.execute(insert_query, data_tuple)

    # Step 4: Commit the changes
    conn.commit()

    # Step 5: Close the connection
    conn.close()


def drop_database(database_file):
    # Close the connection to the database (if it's open)
    conn = sqlite3.connect(database_file)
    conn.close()

    # Check if the file exists before attempting to remove it
    if os.path.exists(database_file):
        try:
            os.remove(database_file)
            print(f"Database '{database_file}' dropped successfully.")
        except OSError as e:
            print(f"Error while dropping the database: {e}")
    else:
        print(f"Database '{database_file}' not found.")



def search_available_item_in_database(db_name, table_name, search_term, only_available=False):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    if only_available:
        available_constraint = " AND available=1"
    else:
        available_constraint = ""
    # Use the LIKE operator to search for the search_term in the 'text' column
    query = f"SELECT * FROM {table_name} WHERE text LIKE '%{search_term}%'{available_constraint};"

    # Execute the query and fetch the results
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the connection
    conn.close()

    return results

