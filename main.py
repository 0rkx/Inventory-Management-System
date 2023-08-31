#make this the main python program of the code, the one that routes everything through it. 
#this file is the one that will connect to the database
#the functions should be stored in a folder "functions"

import mysql.connector as mc
from dotenv import load_dotenv
import os
import supplier
import Functions.inventory as inventory
load_dotenv()

passw = os.getenv("PASSWORD")
db_connection = mc.connect(host="localhost", user = "root", password = passw )

curs = db_connection.cursor()

curs.execute("CREATE DATABASE IF NOT EXISTS test1")#change database after testing
db_connection.close()

#opening database
test_connection = mc.connect(host="localhost",database="test1",user = "root",password = passw)
cur = test_connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Products(
    PRODUCT_ID int PRIMARY KEY,
    PRODUCT_NAME varchar(255),
    SUPPLIER varchar(255),
    COST_PRICE int,
    SELLING_PRICE int,
    INVENTORY int,
    UNIQUE (PRODUCT_ID)
);""")

print("""Welcome to the Inventory Management Software
Reply with 1 to get data on all prodcuts 
Reply with 2 to add a product
Reply with 3 to modify a product
Reply with 4 to fetch details about a product
Reply with 5 to delete a product
Reply with 6 to view Supplier data
Reply with 7 to remove Supplier
Reply with Q to Quit
""")

while True:
    x = input("-->")

    if x == "1":
        inventory.view_data(cur,test_connection)
    elif x=="2":
        inventory.add_product(cur,test_connection)
        
    elif x=="3":
        inventory.modify(cur,test_connection)
    elif x=="4":
        inventory.fetch(cur,test_connection)
    elif x=="5":
        inventory.del_product(cur,test_connection)
    elif x=="6":
        supplier.supplierData(cur)
    elif x=="7":
        supplier.removeSupplier(cur,test_connection)
    elif x.upper()=="Q":
        break
    else:
        print("idk what happened")