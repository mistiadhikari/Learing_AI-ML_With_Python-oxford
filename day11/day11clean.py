import pandas as pd

df=pd.read_csv("datacleaned.csv")
print(df.info)
df["Amount"]=df["Quantity"]* df["Unit_Price"]
print(df["Quantity"],["Unit_Price"],["Amount"].head(10))
# print(df.head(23))
print(df.isnull().sum())
