#In this exercise, I am going to check for the "validity"
#of the data set.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mglearn
from scipy import sparse
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn
from sklearn import preprocessing
from sklearn import utils

#The data set is regarding the boston house price.
bD = load_boston()
#print("Description for the boston data set: ", bD['DESCR'])
#print("keys for boston_dataset", bD.keys())
#print("data for boston_dataset", bD['data'])
#print("target for boston_dataset", bD['target'])

X_train, X_test, y_train, y_test = train_test_split(bD['data'], bD['target'], random_state=0)
print("My X_train is: ", X_train, "and the shape is: ", X_train.shape)
print("My y_train is: ", y_train, "and the shape is: ", y_train.shape)

lab_enc = preprocessing.LabelEncoder()
new_y_train = lab_enc.fit_transform(y_train)


knn = Kn(n_neighbors=1)
#fit() doesn't accept floating points values (which is another way of saying non-discrete,
#which is another way of saying continuous) for the second argument, the values in the
#array has to be categorical (meaning, discrete).
#https://stackoverflow.com/questions/41925157/logisticregression-unknown-label-type-continuous-using-sklearn-in-python
myKnn = knn.fit(X_train, new_y_train)


guess_this = np.array([[0.21, 1, 0.31, 0.21, 0.71, 0.21, 0.11, 0.01, 0.11, 0.21, 0.341, 0.1, 0.11]])
prediction = knn.predict(guess_this)
print(prediction)

bD_dataframe = pd.DataFrame(X_train, columns=bD.feature_names)

plot_this = pd.plotting.scatter_matrix(bD_dataframe, c=y_train, figsize=(15, 15),
							marker='o', hist_kwds={'bins': 20}, s=60,
							alpha=.8, cmap=mglearn.cm3)

#Plot won't show, unless you invoke show() with matplotlib object.							
plt.show()