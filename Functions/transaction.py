#make  a table transactions
import mysql.connector as mc
from mysql.connector import Error

def transactions(cursor, password):
    try:
        connection = mc.connect(host = "localhost", database="test1", user="root", passwd=password)
        cursor.execute("CREATE TABLE IF NOT EXISTS Transactions(Day int, Quantity int, Sales int, Profit int, Loss int)")
        return connection
    except Error as err:
        print(err)

#daily u record daily(user input) total sales, ie SUNDAY, MONDAY, TUESDAY etc
#using this calculate that day's profit and loss
#remove sale volume from inventory
#check if any inventory is low (<15), if yes 
#mention Product ID + supplier details
