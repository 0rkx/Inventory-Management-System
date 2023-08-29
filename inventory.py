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
    PRODUCT_ID int PRIMARY KEY,
    PRODUCT_NAME varchar(255),
    SUPPLIER varchar(255),
    COST_PRICE int,
    SELLING_PRICE int,
    INVENTORY int,
    UNIQUE (PRODUCT_ID)
);""")


def add_product():
    print("Function Got Called") #remove when testing over
    p_id = int(input("Enter the Product ID of the product:- "))#add if statement to make it 6 digit or else it will return a error
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


def del_product():
    print("Function got Called") #remove when testing over
    p_id = int(input("Enter the Product ID"))
    p_pass = input("What is the password to my SQL?")
    if p_pass == passw:
        cur.execute("Delete from Products where PRODUCT_ID=%s",(p_id,))#add error handling for wrong ID
        print("Sucessful")
        test_connection.commit()
    else:
        print("Wrong Password")

                 

def view_data():
    print("Function got Called") #remove when testing over
    cur.execute("SELECT * FROM Products")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def modify():
    print("Function got Called") #remove when testing over
    id = int(input("""Enter Product ID of the Item you want to Modify:- """))
    print("""
Reply with the Corresponding Number to your Choice
    1:- Product Name
    2:- Product Supplier
    3:- Cost Price
    4:- Selling Price
    5:- Inventory""")
    x = int(input("Enter Your Choice:- "))
    if x == 1:
        new = input("What would you like the new name of the product to be?:- ")
        cur.execute("UPDATE Products SET Product_NAME=%s Where Product_ID = %s",(new,id))
        print("Modification Complete")
    elif x == 2:
        new = input("What is the name of the new Supplier of the Product?:-  ")
        cur.execute("UPDATE Products SET Supplier=%s Where Product_ID = %s",(new,id))
        print("Modification Complete")
    elif x == 3:
        new = input("What is the new cost price of the product? :-  ")
        cur.execute("UPDATE Products SET Cost_Price=%s Where Product_ID = %s",(new,id))
        print("Modification Complete")
    elif x == 4:
        new = input("What would you like the new selling price of the product to be? :- ")
        cur.execute("UPDATE Products SET Selling_Price=%s Where Product_ID = %s",(new,id))
        print("Modification Complete")
    elif x == 5:
        new = int(input("Enter the Additional Inventory Count:- "))
        cur.execute("SELECT INVENTORY from products where PRODUCT_ID=%s",(id,))
        current_inventory = cur.fetchone()[0]

        new_inventory =  current_inventory+ new
        cur.execute("UPDATE Products SET INVENTORY=%s Where Product_ID = %s",(new_inventory,id))
        print("Modification Complete")
    test_connection.commit()


x = (input("""
Welcome to the Inventory Management Software
Reply with 1 to get data on all prodcuts 
Reply with 2 to add a product
Reply with 3 to modify a product
Reply with 4 to delete a product
-->"""))


if x == "1":
    view_data()
elif x=="2":
    add_product()
elif x=="3":
    modify()
elif x=="4":
    del_product()
else:
    print("idk what happened") #stays till testing ends


