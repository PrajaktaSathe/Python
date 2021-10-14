import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris


#classifier code

#loading the data
iris_data=load_iris()
#iris_data=pd.read_csv("iris.csv")

#Splitting the data into features and label
x=iris_data["data"]
y=iris_data["target"]

#Splitting data into tarining and test data
x_train, x_test, y_train, y_test=train_test_split(x,y,random_state=0, test_size=0.3)

kclassifier=KNeighborsClassifier(n_neighbors=2)

#fitting training  data into KNN classifier
kclassifier.fit(x_train, y_train)

xn=np.array([[7,3,4,1.5]])

xpred=kclassifier.predict(xn)

print(iris_data["target_names"][xpred])

#The classifier can be changed into a pickle file fr use in other files
#import pickle
#pickle.dump(kclassifier, open("knclassifier.pkl", "wb"))
#model=pickle.load(open("knclassifier.pkl", "rb"))
#xn=np.array([[5,1,4,2]])