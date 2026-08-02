
#datacleaning

import pandas as pd
# df= pd.read_csv("day11/datacleaning.csv")
# print(df.head(10))
# print(df.shape)
#print(df.info)
# print(df.describe)

# df["Age"]= df["Age"].fillna(df["Age"].median()) #filling null value in age
# # print(df.isnull().sum())

# df["Gender"]= df["Gender"].fillna("Unknown") #filling unknown value in gender
# missing= df["Customer_ID"].isna()
# df.loc[missing,"Customer_ID"]= [f"CUST{1000+ i}" for i in range(missing.sum())] 

# df["Unit_Price"]=df["Unit_Price"].fillna(df["Age"].median())
# print(df.isnull().sum())
# print(df.to_csv("datacleaned.csv",index= False))
