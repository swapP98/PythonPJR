import pandas as pd
import matplotlib.pyplot as plt

# Loading the order data
df = pd.read_csv("orderdata.csv")

#Cleaning the data 
df[["oYY", "oMM", "oDD"]] = df["OrderDate"].str.split("-", expand=True)
print(df)

#Grouping by moonth and year
df2 = df.groupby(["oMM","oYY"])["Quantity"].sum()
print(df2)

#plotting the Quantity bar chart
plt.figure()
ax = df2.plot.bar(rot=0)
plt.xlabel("Months")
plt.ylabel("Quantity")
plt.title("Quantity bar chart")
plt.show()

#Sales calcualtion
df["sales"] = df["Quantity"]*df["Price"]
print(df)

df3 = df.groupby(["oMM","oYY"])["sales"].sum()

#Plotting sales chart
plt.figure()
print(df3)
df3.plot(rot=0)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Sales chart")
plt.show()
