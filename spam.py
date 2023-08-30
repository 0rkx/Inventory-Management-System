import mysql.connector as mc
from dotenv import load_dotenv
import os
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

def add_product():
    try:
        print("Function Got Called") #remove when testing over
        p_id = int(input("Enter the Product ID of the product:- "))
        yz = str(p_id)
        if len(yz) ==6:
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
        else:
            print("The Product ID Should be 6 Digits")
    except mc.Error as err:
        print("Database Error", err)

def del_product():
    print("Function got Called") #remove when testing over
    p_id = int(input("Enter the Product ID"))
    p_pass = input("What is the password to my SQL?")
    try:
        if p_pass == passw:
            cur.execute("Delete from Products where PRODUCT_ID=%s",(p_id,))
            if cur.rowcount > 0:
                print("Product Sucessfully Deleted")
            else:
                print("Product not Found with that ID")
            test_connection.commit()
            
        else:
            print("Wrong Password")
            
    except mc.Error as err:
        print("Database Error", err)

                
def view_data():
    try:
        cur.execute("SELECT * FROM Products")
        rows = cur.fetchall()
        print("ID    NAME    SUPPLIER  CP  SP   AMT")
        for row in rows:
            print(row)
    except mc.Error as err:
        print("Database Error", err)
    

def modify():
    try:
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
    except mc.Error as err:
        print("Database Error", err)
    


def fetch():
    try:
        print("Function got called") #remove after testing
        id = int(input("Enter the ID of the product you would like to fetch"))
        cur.execute("SELECT Product_Name from products where PRODUCT_ID=%s",(id,))
        name = cur.fetchone()[0]
        cur.execute("SELECT Supplier from products where PRODUCT_ID=%s",(id,))
        sup = cur.fetchone()[0]
        cur.execute("SELECT Cost_Price from products where PRODUCT_ID=%s",(id,))
        cp = cur.fetchone()[0]
        cur.execute("SELECT Selling_Price from products where PRODUCT_ID=%s",(id,))
        sp = cur.fetchone()[0]
        cur.execute("SELECT Inventory from products where PRODUCT_ID=%s",(id,))
        inventory = cur.fetchone()[0]   
        print(f"Here are the details for the Product ID {id}")
        print(f"Name: {name}")
        print(f"Supplier: {sup}")
        print(f"Inventory: {inventory}")
        print(f"Cost Price: {cp}")
        print(f"Selling Price: {sp}")
    except mc.Error as err:
        print("Database Error", err)
    

print("""Welcome to the Inventory Management Software
Reply with 1 to get data on all prodcuts 
Reply with 2 to add a product
Reply with 3 to modify a product
Reply with 4 to fetch details about a product
Reply with 5 to delete a product
Reply with 6 to Exit
""")

while True:
    x = input("-->")

    if x == "1":
        view_data()
    elif x=="2":
        add_product()
        
    elif x=="3":
        modify()
    elif x=="4":
        fetch()
    elif x=="5":
        del_product()
    elif x=="6":
        break
    else:
        print("idk what happened") #stays till testing ends