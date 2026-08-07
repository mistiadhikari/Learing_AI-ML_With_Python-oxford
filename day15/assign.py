# a school has collected data about student study hours and their final marks your task is to build a ML model to predict  
# the marks of new student based on the number of hours studied.
# given data:
# S.H   marks
# 1     35
# 12    95

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor
data={
    "Hours":[1,2,3,4,5,6,7,8,9,10,11,12],
    "Final_Marks":[35,40,45,50,55,60,65,70,75,80,85,90]
}
df= pd.DataFrame(data)
X= df[["Hours"]]
Y= df["Final_Marks"]
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)
# model= RandomForestRegressor()
model= LinearRegression() 
model.fit(X_train,Y_train)
predictions= model.predict(X_test)
print("Actual:",Y_test.values)
print("predicted:",predictions)
new_student= pd.DataFrame({
    "Hours":[10]
})

print("study hours:",new_student["Hours"].iloc[0])
print("Predicted marks:", predictions[0])