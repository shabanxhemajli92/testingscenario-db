import psycopg2

def get_connection():
    connection = psycopg2.connect(
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        database="inventory_db",
    )
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def adding_into_db():
    connection=get_connection()
    cur=connection.cursor()
    cur.execute(
    "INSERT INTO location (warehouse_name, stock)VALUES('Munchen',40000);"
)
    cur.execute(
    "INSERT INTO location ( warehouse_name, stock)VALUES('Oberhausen',4500);"
)
    connection.commit()
    print("adding..")
    cur.execute("SELECT * FROM location;")
    fetch_database=cur.fetchall()
    close_connection(connection)
    return fetch_database

def sorting_db_greaterthan5():
    connection=get_connection()
    cur=connection.cursor()
    cur.execute(
    "SELECT warehouse_name  FROM location WHERE stock > 5;"
)
    fetch_database=cur.fetchall()
    print(fetch_database)
    connection.commit()
    close_connection(connection)
    return fetch_database
#adding_into_db()    
sorting_db_greaterthan5()