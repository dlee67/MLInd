import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import sparse
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn

bD = load_boston()
print("Boston keys", bD.keys())
print("Boston feature names", bD['feature_names'])
print(bD['DESCR'])

X_train, X_test, y_train, y_test = train_test_split(bD['data'], bD['target'], random_state=0)

print(bD['data'][32])
print(pd.DataFrame(X_train, columns=bD.feature_names))