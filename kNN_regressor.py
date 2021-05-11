# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt

df =  pd.read_csv("house_rental_data.csv.txt")
print(df.head(),"\n")
print("Data types are: ",df.dtypes,"\n")
print("Shape  of dataframe is: \n",df.shape,"\n")
print("Columns are: \n",df.columns,"\n")
print("Checking for missing values:\n",df.isnull().sum(),"\n")

del df["Unnamed: 0"]
print("Coumns are: \n",df.columns,"\n")

corr = df.corr()

x = df.iloc[:,0:6].values
y = df.iloc[:,6].values

from sklearn.preprocessing import StandardScaler
x = StandardScaler().fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=20)

rmse = []
for  k in range(1,100):
    NN_model = KNeighborsRegressor(n_neighbors = k)
    NN_model.fit(x_train, y_train)
    y_pred = NN_model.predict(x_test)

    error = sqrt(mean_squared_error(y_test, y_pred))
    print(k, error)
    rmse.append(error)
    
graph = pd.DataFrame(rmse)
graph.plot()

NN_model = KNeighborsRegressor(n_neighbors = 25)
NN_model.fit(x_train, y_train)
y_pred = NN_model.predict(x_test)

#print(y_pred)
print("\n Training Score: ",(NN_model.score(x_train, y_train)*100).round(2))
print("Test Score: ",(NN_model.score(x_test, y_test)*100).round(2))