import mysql.connector as mc
from mysql.connector import Error
from dotenv import load_dotenv
import os
passw = os.getenv("PASSWORD")

def supplierData(cursor):
    try:
        x=input("Enter supplier name: ")
        cursor.execute("SELECT PRODUCT_ID, PRODUCT_NAME, COST_PRICE, SELLING_PRICE, INVENTORY from products where SUPPLIER=%s", (x,))
        for val in cursor:
            print(val)
    except Error as err:
        print(err)

def removeSupplier(cursor,test_connection):
    try:
        supplier=input("Enter supplier name: ")
        cursor.execute("DELETE from products WHERE SUPPLIER=%s", (supplier,))
        test_connection.commit()  # Commit the transaction
        print(f"Supplier {supplier} removed")
    except Error as err:
        print(err)

