import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

passw = os.getenv("PASSWORD")
db_connection = mysql.connector.connect(host="localhost", user = "root", password = passw )

db_cursor = db_connection.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS inventory_db")


db_cursor.close()

db_connection.close()

db_connection = mysql.connector.connect(host="localhost", user = "root", password = passw, database = "inventory_db")

db_cursor = db_connection.cursor()

db_cursor.execute("""
Create Table if not exists items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(225) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
)""")

def add_item(name, quantity, price):
    db_cursor = db_connection.cursor()
    sql = "INSERT INTO items (name, quantity, price) VALUES (%s,%s,%s) "
    values = (name, quantity, price)
    db_cursor.execite(sql, values)
    
db_cursor.close()

