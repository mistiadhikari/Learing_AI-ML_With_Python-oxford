import pandas as pd
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Marks":[35,40,45,50,55,60,65,70,80,90]
}
df= pd.DataFrame(data)
X= df[["Hours"]]
Y= df["Marks"]
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)


model= RandomForestRegressor()
# model= LinearReression() #to decide which algorithm to use to train the model
model.fit(X_train,Y_train)
predictions= model.predict(X_test)
print("Actual:",Y_test.values)
print("predicted:",predictions)


# print("Training Data:")
# print(X_train)


# print("Training Data:")
# print(X_test)



new_student= pd.DataFrame({
    "Hours":[7]
})
print("study hours:",new_student["Hours"].iloc[0])
print("Predicted marks:", predictions[0])
