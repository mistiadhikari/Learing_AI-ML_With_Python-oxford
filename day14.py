import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#1.pandas
df = pd.read_csv("day11/datacleaning.csv")
# print(df)
# print(df.columns)

salesdata = df[["Category","Total_Amount"]]
# print(salesdata.head())
# print(salesdata.info())
#cleanin data

df["Category"]= df["Category"].astype("string")
df["Category"]=df["Category"].str.strip()
df["Category"]=df["Category"].str.title()
df["Category"]= df["Category"].replace({"I.T.":"IT","It":"IT","Information Technology":"IT"})
df["Total_Amount"]=pd.to_numeric(df["Total_Amount"],errors='coerce')
df= df.dropna(subset=["Total_Amount","Category"])

print("\nCleaned Category Values:")
print(df["Category"].value_counts())


categorysales = df.groupby("Category")["Total_Amount"].sum()
print("\nSales by category:")
print(categorysales)

#2.Numpy-convert to numpy arrays for further analysis

categories =  categorysales.index.to_numpy()
sales= categorysales.values

#numpy calculations
total_sales= np.sum(sales)
print("Total Sales:",total_sales)
avg_sales= np.average(sales)
print("Average_sales",avg_sales)
highest_sales= np.max(sales)
print("highest_sales",highest_sales)

highest_index=np.argmax(sales)
print("highest_index:",highest_index)
highest_category= categories[highest_index]
print("highest_category:",highest_category)


#3.Matplotlib
plt.bar(categories, sales)
plt.xlabel("Categories")
plt.ylabel("sales")
plt.xticks(rotation= 50)
plt.tight_layout()
plt.title("sales by category")
plt.show()