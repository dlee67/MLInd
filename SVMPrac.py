from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = [[1, 1], [2, 2]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[0, 0]]))
print(clf.predict([[3, 3]]))
plt.contour(X, y)
plt.show()
