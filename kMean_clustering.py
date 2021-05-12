# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

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

wcss = []
for i in range(1, 15):
    k_means = KMeans(n_clusters = i, init = "k-means++", random_state = 1)
    k_means.fit_predict(x)
    #k_means.inertia_ : wcss score
    wcss.append(k_means.inertia_)
    print("i:",i,"wcss:", k_means.inertia_)

plt.plot(range(1, 15), wcss)
plt.title("Elbow Method")
plt.xlabel("No. of clusters")
plt.ylabel("WCSS Score")
plt.show()

k_means = KMeans(n_clusters = 5, init = "k-means++", random_state = 1)
print(k_means.fit_predict(x))