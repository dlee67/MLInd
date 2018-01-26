from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import mglearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
lr = LinearRegression().fit(X_train, y_train)
print("My predicted value: ", lr.predict(X_train))
print("My linear coefficient is: ", lr.coef_)

#plt.scatter(X_train, y_train)
#plt.plot(X_train, lr.predict(X_train))
#plt.xlabel("x-axis")
#plt.ylabel("y-axis")
#plt.show()