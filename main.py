import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

passw = os.getenv("PASSWORD")
db_connection = mysql.connector.connect(host="localhost", user = "root", password = passw )

curs = db_connection.cursor()

curs.execute("CREATE DATABASE IF NOT EXISTS test1")


db_connection.close()

test_connection = mysql.connector.connect(host="localhost",database="test1",user = "root",password = passw)
cur = test_connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Products(
    PRODUCT_ID int,
    PRODUCT_NAME varchar(255),
    SUPPLIER varchar(255),
    COST_PRICE int,
    SELLING_PRICE int,
    INVENTORY int);""")


def add_product():
    print("Function Got Called") #remove when testing over
    p_id = int(input("Enter the Product ID of the product:- "))#add if statement to make it 6 digit or else it will return a error
#if this gets a GUI wont it be better just sayin :>
# for future work, make it so that entering the product id will attempt to fetch all the details of the item
    p_name = input("Enter the Name of the Product:- ")
    p_supp = input("Enter the supplier of the product:- ")
    p_cp = int(input("Enter the cost price of the product:- "))
    p_sp = int(input("Enter the Selling price of the product:- "))
    p_inv = int(input("Enter the Number of Items you are ADDING:- "))
    insert_query = """
        INSERT INTO Products (PRODUCT_ID, PRODUCT_NAME, SUPPLIER, COST_PRICE, SELLING_PRICE, INVENTORY)
        VALUES (%s, %s, %s, %s, %s, %s);
    """
    insert_data = (p_id, p_name, p_supp, p_cp, p_sp, p_inv) 
    cur.execute(insert_query, insert_data)
    test_connection.commit() 
    print("Product Added Sucessfully")

def view_data():
    print("Function got Called") #remove when testing over
    cur.execute("SELECT * FROM Products")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    
x = (input("""
Welcome to the Inventory Management Software
Reply with 1 to get data on all prodcuts 
Reply with 2 to add a product
-->"""))


if x == "1":
    view_data()
elif x=="2":
    add_product()
else:
    print("idk what happened") #stays till testing ends


