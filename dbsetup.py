import psycopg2
connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="inventory_db",)
curr = connection.cursor()
curr.execute(
    "CREATE TABLE IF NOT EXISTS product (id serial NOT NULL PRIMARY KEY,product_name VARCHAR (100) NOT NULL,product_price int);"
)
# curr.execute(
#     "INSERT INTO product (id, product_name, product_price)VALUES('1', 'Tires', 10),('10', 'Discs', 25),('33', 'Breaks', 50),('44', 'Connectors', 2);"
# )
curr.execute(
    "CREATE TABLE IF NOT EXISTS location (id serial NOT NULL PRIMARY KEY,warehouse_name VARCHAR (100) NOT NULL,warehouse_id serial NOT NULL,stock INT);"
)
# curr.execute(
#     "INSERT INTO location (id, warehouse_name, warehouse_id, stock)VALUES(1,'Lipezig',20,2000);"
# )

connection.commit()
connection.close()
print("Updated")