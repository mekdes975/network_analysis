import psycopg2
import pandas as pd

def connect_to_postgres(dbname, user, password, host, port):
    """
    Connects to PostgreSQL database and returns the connection and cursor objects.

    Parameters:
    - dbname: Name of the PostgreSQL database
    - user: PostgreSQL username
    - password: PostgreSQL password
    - host: PostgreSQL server host
    - port: PostgreSQL server port

    Returns:
    - connection: PostgreSQL database connection object
    - cursor: PostgreSQL database cursor object
    """
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = connection.cursor()
    return connection, cursor

def create_tables_from_sql_file(connection, cursor, sql_file_path):
    """
    Creates tables in the PostgreSQL database from a .sql file.

    Parameters:
    - connection: PostgreSQL database connection object
    - cursor: PostgreSQL database cursor object
    - sql_file_path: Path to the .sql file containing table creation queries
    """
    with open(sql_file_path, 'r') as sql_file:
        cursor.execute(sql_file.read())
    connection.commit()

def create_database(dbname, user, password, host, port):
    """
    Creates a PostgreSQL database.

    Parameters:
    - dbname: Name of the new database
    - user: PostgreSQL superuser username
    - password: PostgreSQL superuser password
    - host: PostgreSQL server host
    - port: PostgreSQL server port
    """
    connection, cursor = connect_to_postgres("postgres", user, password, host, port)
    cursor.execute(f"CREATE DATABASE {dbname}")
    connection.commit()
    connection.close()

def read_table_to_dataframe(connection, table_name):
    """
    Reads data from a PostgreSQL table and returns a pandas DataFrame.

    Parameters:
    - connection: PostgreSQL database connection object
    - table_name: Name of the table to read

    Returns:
    - df: Pandas DataFrame containing the data from the table
    """
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, connection)
    return df

def insert_data_into_table(connection, cursor, table_name, data):
    """
    Inserts data into a PostgreSQL table.

    Parameters:
    - connection: PostgreSQL database connection object
    - cursor: PostgreSQL database cursor object
    - table_name: Name of the table to insert data into
    - data: Data to be inserted into the table (formatted as a list of dictionaries)
    """
    columns = ', '.join(data[0].keys())
    placeholders = ', '.join(['%({})s'.format(key) for key in data[0]])

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.executemany(query, data)
    connection.commit()

    
def delete_table(connection, cursor, table_name):
    """
    Deletes a PostgreSQL table.

    Parameters:
    - connection: PostgreSQL database connection object
    - cursor: PostgreSQL database cursor object
    - table_name: Name of the table to delete
    """
    query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(query)
    connection.commit()