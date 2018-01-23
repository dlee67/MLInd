#In this exercise, I am going to check for the "validity"
#of the data set.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import sparse
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn

#The data set is regarding the boston house price.
bD = load_boston()
#print("Description for the boston data set: ", bD['DESCR'])
#print("keys for boston_dataset", bD.keys())
#print("data for boston_dataset", bD['data'])
#print("target for boston_dataset", bD['target'])

X_train, X_test, y_train, y_test = train_test_split(bD['data'], bD['target'], random_state=0)
bDF = pd.DataFrame(X_train, columns=bD.feature_names)
print(bDF)