import pandas as pd
import mysql.connector

customer_data = pd.read_csv('sample_customer.csv')
print(customer_data)

orders_data = pd.read_csv('sample_orders.csv')

#Connect to MySQL connector.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mypythonPRJ2")

mycursor = mydb.cursor()

for row in customer_data.itertuples():
    print( (row.CustomerID, row.FirstName, row.LastName, row.Phone, row.City, row.State, row.CustomerName, row.emails))
    mycursor.execute("INSERT INTO sample_customer (CustomerID, FirstName, LastName, Phone, City, State, CustomerName, emails) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", 
                    (row.CustomerID, row.FirstName, row.LastName, row.Phone, row.City, row.State, row.CustomerName, row.emails))

mydb.commit()


#mycursor.execute("ALTER TABLE sample_orders ADD CONSTRAINT FK_customerID FOREIGN KEY (CustomerID) REFERENCES sample_customer(CustomerID);")
#mycursor.execute("ALTER TABLE sample_orders DROP FOREIGN KEY FK_customerID;")

for row in orders_data.itertuples():
    mycursor.execute("INSERT INTO sample_orders (OrderID, CustomerID, OrderDate, ShippedDate) VALUES (%s,%s,%s,%s)", 
                    (row.OrderID, row.CustomerID, row.OrderDate, row.ShippedDate))

mydb.commit()
mydb.close()

print("successfully imported data!")