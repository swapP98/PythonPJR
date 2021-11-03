import mysql.connector

#Connect to MySQL connector.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password")

mycursor = mydb.cursor()


# Create database for products.
mycursor.execute("CREATE DATABASE mypythonPRJ2")
print("mypythonPRJ database created.")
mydb.close()

#Connect to mypythonPRJ database.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mypythonPRJ2")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sample_customer (CustomerID VARCHAR(8), "
                 "FirstName VARCHAR(20), LastName VARCHAR(20), Phone VARCHAR(90), "
                 "City VARCHAR(50), State VARCHAR(50), CustomerName VARCHAR(50), emails VARCHAR(50), PRIMARY KEY(CustomerID))")

print("sample_customer table created!")

mycursor.execute("CREATE TABLE sample_orders (OrderID VARCHAR(8), "
                 "CustomerID VARCHAR(8), OrderDate DATE, ShippedDate DATE, "
                 "PRIMARY KEY(OrderID))")

print("sample_order table created!")

mydb.close()



