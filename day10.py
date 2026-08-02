# import pandas as pd
# # marks = pd.Series([80,75,90,85,95])
# # print(marks)

# # series = pd.Series([100,200,300,400,500])
# # print(series)

# # student = {
# #     "Name":
# #     ["ram","sita","hari","gita","siya","piya","uma"],
# #     "Age": [20,21,22,20,8,23,44],
# #     "Math": [80,90,75,95,55,90,75]
# # }
# # df= pd.DataFrame(student)
# # print(df)
# # print(df.head()) #first  row of data
# # print(df.tail()) #last  row of data
# # print(df[['Name','Age']]) #values of name and age
# # print(df.loc[0]) #index of 0 is printed Ram
# # print(df.loc[1:3]) #slicing 
# # print(df.iloc[1:3])
# # print(df.describe())

# employe={
#     "Name":["hari","ram","sita","manish","bibek","mayank","siya","ritika","amisha","kishan"],
#     "Department":["Developer","Designer","QA","Finance","DevOops","Developer","UI/UX","Networking","Networking","QA"],
#     "Salary":[40000,20000,4500,6700, None ,23000,14000,22000,24000,45000]
# }
# df= pd.DataFrame(employe)
# # print(df)
# # print(df.shape)
# # print(df.columns)
# # print(df.dtypes)
# # print(df.head())
# # print(df.tail())
# # print(df.isnull().sum())
# # print(df.info()) #checks the data is empty or not
# # print(df.describe()) #prints stats value
# # print(df.fillna(None, inplace=True)) data cleaning
# df= df.dropna() #removes none value row
# print(df)



import pandas as pd
