import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import pandas as pd
import mglearn

from scipy import sparse
#I could get a data base of my own from here.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn

iris_dataset = load_iris()

print("Iris target value is: ", iris_dataset['target_names'])
print("Iris target description is: ", iris_dataset['target_names'])

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

#DataFrame is a table of data.
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
print(iris_dataframe)

pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
							marker='o', hist_kwds={'bins': 20}, s=60,
							alpha=.8, cmap=mglearn.cm3)
							
knn = Kn(n_neighbors=1)
myKnn = knn.fit(X_train, y_train)

guess_this = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(guess_this)
print(prediction)
							
#someStuff = pd.DataFrame([[1, 2, 3], [1,2,3], [1,2,3]], columns=["Super Saiyan", "Super Saiyan 2", "Super Saiyan 3"])
#print(someStuff)	

#from sklearn.cross_validation import train_test_split
#from sklearn.linear_model import LogisticRegressionCV
#
#from keras.models import Sequential
#from keras.layers.core import Dense, Activation
#from keras.utils import np_utils

#A numpy array looks like this.
#x = np.array([[1, 2, 3], [4, 5, 6]])
#print("x:\n{}".format(x));

#A demo of scipy in action.
#eye = np.eye(4) #Assigns an identity matrix of 4 by 4 for variable eye.
#print(eye);
#sparse_matrix = sparse.csr_matrix(eye);
#print("\nScipy sparse CSR matrix:\n{}".format(sparse_matrix))
#
#data = np.ones(4)
#print(data)

