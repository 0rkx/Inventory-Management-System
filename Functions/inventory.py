import mysql.connector as mc
from mysql.connector import Error
from dotenv import load_dotenv
import os
passw = os.getenv("PASSWORD")




def add_product(cur,test_connection):
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

def del_product(cur,test_connection):
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

                
def view_data(cur,test_connection):
    try:
        cur.execute("SELECT * FROM Products")
        rows = cur.fetchall()
        print("ID    NAME    SUPPLIER  CP  SP   AMT")
        for row in rows:
            print(row)
    except mc.Error as err:
        print("Database Error", err)
    

def modify(cur,test_connection):
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
    


def fetch(cur,test_connection):
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
    

 #stays till testing ends