#Generation of sample dataset

import pandas as pd
import random

customers =  pd.read_csv("customers.csv")

customers = customers.drop(columns=['Street'])

customers["CustomerName"] = customers["FirstName"] + " " +  customers["LastName"]

email_providers = ["@gmailx.com", "@outloox.com", "@yahoox.com", "@banana.com", "@macrosoft.com"]

symbols  = ["_","."]

customers["emails"] = customers["FirstName"] + random.Random().choice(symbols) + customers["LastName"] + random.Random().choice(email_providers)
customers["emails"] = customers["emails"].str.lower()

print(customers.head(100))
customers.iloc[0:100].to_csv("sample_customer.csv", index=False)

## ORDERS

orders = pd.read_csv("orderdata.csv")
orders = orders.drop(columns=['ManagerID','Quantity','Price','Freight'])
print(orders)

orders.to_csv("sample_orders.csv", index=False)
mergeTB = customers.join(orders.set_index('CustomerID'), on='CustomerID')
mergeTB.to_csv("merge.csv", index=False)
print(mergeTB)



