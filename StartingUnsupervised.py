import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mglearn

from scipy import sparse
from sklearn.datasets import load_iris
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import mglearn

#cancer = load_breast_cancer();
#X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=1)
#
#scalar = MinMaxScaler()
#scalar.fit(X_train)
#
#X_train_scaled = scalar.transform(X_train)
#X_test_scaled = scalar.transform(X_test)
#X, _ = make_blobs(n_samples=50, centers=5, random_state=4, cluster_std=2)
## split it into training and test sets
#X_train, X_test = train_test_split(X, random_state=5, test_size=.1)
#
## plot the training and test sets
#fig, axes = plt.subplots(1, 3, figsize=(13, 4))
#axes[0].scatter(X_train[:, 0], X_train[:, 1],
#                c=mglearn.cm2(0), label="Training set", s=60)
#axes[0].scatter(X_test[:, 0], X_test[:, 1], marker='^',
#                c=mglearn.cm2(1), label="Test set", s=60)
#axes[0].legend(loc='upper left')
#axes[0].set_title("Original Data")
#
## scale the data using MinMaxScaler
#scaler = MinMaxScaler()
#scaler.fit(X_train)
#X_train_scaled = scaler.transform(X_train)
#X_test_scaled = scaler.transform(X_test)
#
## visualize the properly scaled data
#axes[1].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
#                c=mglearn.cm2(0), label="Training set", s=60)
#axes[1].scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], marker='^',
#                c=mglearn.cm2(1), label="Test set", s=60)
#axes[1].set_title("Scaled Data")
#
## rescale the test set separately
## so test set min is 0 and test set max is 1
## DO NOT DO THIS! For illustration purposes only.
#test_scaler = MinMaxScaler()
#test_scaler.fit(X_test)
#X_test_scaled_badly = test_scaler.transform(X_test)
#
## visualize wrongly scaled data
#axes[2].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
#                c=mglearn.cm2(0), label="training set", s=60)
#axes[2].scatter(X_test_scaled_badly[:, 0], X_test_scaled_badly[:, 1],
#                marker='^', c=mglearn.cm2(1), label="test set", s=60)
#axes[2].set_title("Improperly Scaled Data")
#
#for ax in axes:
#    ax.set_xlabel("Feature 0")
#    ax.set_ylabel("Feature 1")
#fig.tight_layout()
#
#print(X_train.shape)
#print(X_test.shape)
#print("transformed shape: {}".format(X_train_scaled.shape))
#print("per-feature minimum before scaling:\n {}".format(X_train.min(axis=0)))
#print("per-feature maximum before scaling:\n {}".format(X_train.max(axis=0)))
#print("per-feature minimum after scaling:\n {}".format(
#    X_train_scaled.min(axis=0)))
#print("per-feature maximum after scaling:\n {}".format(
#    X_train_scaled.max(axis=0)))
#print("per-feature minimum after scaling:\n{}".format(X_test_scaled.min(axis=0)))
#print("per-feature maximum after scaling:\n{}".format(X_test_scaled.max(axis=0)))
#
#
#svm = SVC(C=100)
#X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
#                                                    random_state=0)
#
#scaler = MinMaxScaler()
#scaler.fit(X_train)
#X_train_scaled = scaler.transform(X_train)
#X_test_scaled = scaler.transform(X_test)
#
#svm.fit(X_train_scaled, y_train)
#print("Test set accuracy: {:.2f}".format(svm.score(X_test, y_test)))
#print("Scaled test set accuracy: {:.2f}".format(
#    svm.score(X_test_scaled, y_test)))
#
#scaler = StandardScaler()
#scaler.fit(X_train)
#X_train_scaled = scaler.transform(X_train)
#X_test_scaled = scaler.transform(X_test)
#
## learning an SVM on the scaled training data
#svm.fit(X_train_scaled, y_train)
#
## scoring on the scaled test set
#print("SVM test accuracy: {:.2f}".format(svm.score(X_test_scaled, y_test)))

mglearn.plots.plot_pca_illustration()

plt.show();		