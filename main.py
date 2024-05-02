import pyodbc

def connect_to_sql_server(server: str, database: str, username: str, password: str):
    try:
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return None

def get_database_name(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT DB_NAME()")
        row = cursor.fetchone()
        return row[0]
    except pyodbc.Error as e:
        print(f"Error fetching database name: {e}")
        return None

# Provide your SQL Server credentials
server = 'DESKTOP-5QSJM94\SQLEXPRESS'
database = 'AdventureWorksDW'
username = 'garima'
password = 'Welcome@123'

# Connect to SQL Server
conn = connect_to_sql_server(server, database, username, password)
if conn:
    # Get the database name
    db_name = get_database_name(conn)
    if db_name:
        print(f"Connected to SQL Server. Database name: {db_name}")
    else:
        print("Failed to fetch database name.")
    conn.close()
else:
    print("Failed to connect to SQL Server.")
