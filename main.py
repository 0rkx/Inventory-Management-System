#make this the main python program of the code, the one that routes everything through it. 
#this file is the one that will connect to the database
#the functions should be stored in a folder "functions"
import random
import mysql.connector as mc
from dotenv import load_dotenv
import os
import Functions.supplier as supplier
import Functions.inventory as inventory
import Functions.transaction as transaction
load_dotenv()

passw = input("Please Enter the Password to MYSQL:- ")
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

cur.execute("""CREATE TABLE IF NOT EXISTS `Users` (
	`UserID` INT,
	`UserName` VARCHAR(255),
    `Password` VARCHAR(255),
	`Role` VARCHAR(255),
    `Name` VARCHAR(255),
	PRIMARY KEY (`UserID`));""")

transaction1= transaction.transactions(cur, passw)

def ran_num():
    valid_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random_number = ''.join([str(random.choice(valid_digits)) for i in range(6)])
    return random_number

def table_exists(name):
    cur.execute("Show tables like %s",(name,))
    return cur.fetchone() is not None
                

def create_user():
    name = input("What is your name?:- ")
    username = input("What would you like your Username to be:- ")
    cur.execute("Select * from Users where username=%s ",(username,))
    exis_user = cur.fetchone()
    if exis_user:
        print("Username Already Exists, Please Restart")
        return
    else:   
        password = input("Pease Enter your desired password:- ")
        role = input("What is your role?:- ")
        userid = ran_num()
        cur.execute("Select * from Users where userid=%s",(userid,))
        exis_num = cur.fetchone()
        if exis_num:
            userid = ran_num()
        insert_q = "INSERT INTO Users (USERID,USERNAME,PASSWORD,ROLE,NAME) VALUES (%s,%s,%s,%s,%s)"
        values = (userid,username,password,role,name)
        cur.execute(insert_q,values)
        test_connection.commit()
        print("User Added Sucessfully")

def login():
    user = input("Please Enter your Username:- ")
    password = input('Please Enter your Password:- ')
    table_name = 'Users'
    cur.execute("SELECT * FROM Users WHERE username=%s", (user,))
    exis_user = cur.fetchone()
    if not exis_user:
        print("Username does not exist.")
        return

    real_pass = exis_user[2]
    if password == real_pass:
        print("""
Welcome to the Inventory Management Software
    Reply with 1 to get data on all prodcuts 
    Reply with 2 to add a product
    Reply with 3 to modify a product
    Reply with 4 to fetch details about a product
    Reply with 5 to delete a product
    Reply with 6 to view Supplier data
    Reply with 7 to remove Supplier
    Reply with 8 to switch to Transactions
    Reply with Q to Quit
    """)

        while True:
            x = input("-->")

            if x == "1":
                inventory.view_data(cur,test_connection)
                inventory.checkStock(cur)
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
            elif x=="8":
                transaction_cursor = transaction1.cursor()
                while True:
                    print("""
Welcome to the Inventory Management Software
    Reply with 1 to view transactions 
    Reply with 2 to add a transaction
    Reply with 3 to modify a transaction
    Reply with 4 to fetch details about a transaction
    Reply with 5 to delete a transaction
    Reply with 6 to view transaction data
    Reply with 7 to remove transaction
    Reply with Q to exit Transactions
    """)
                    act=input("-->")
                    if act==1:
                        inventory.view_data(transaction_cursor)
                    elif act=="q".upper():
                        print("""
Welcome to the Inventory Management Software
    Reply with 1 to get data on all prodcuts 
    Reply with 2 to add a product
    Reply with 3 to modify a product
    Reply with 4 to fetch details about a product
    Reply with 5 to delete a product
    Reply with 6 to view Supplier data
    Reply with 7 to remove Supplier
    Reply with 8 to switch to Transactions
    Reply with Q to Quit
    """)
                        break

            elif x.upper()=="Q":
                break
            else:
                print("idk what happened")
    else:
        print("Wrong Password")
        


x = int(input("""
Please Enter 1 to Login
Please Enter 2 to Create a New Account
    -->"""))

if x == 1:
    login()
if x == 2:
    create_user()
