from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import matplotlib.pyplot as plt
import mglearn
import numpy as np

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=1)

#Demonstration that those two work pretty much the similar.
#scaler = MinMaxScaler()	
#PCA is super powerful...

scaler = StandardScaler()
scaler.fit(cancer.data)
X_scaled = scaler.transform(cancer.data)
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca = pca.transform(X_scaled)
plt.figure(figsize=(8, 8))

plt.legend(cancer.target_names, loc="best")
mglearn.discrete_scatter(X_pca[:, 0], X_pca[:, 1], cancer.target)
plt.legend(cancer.target_names, loc="best")
plt.gca().set_aspect("equal")
plt.xlabel("First principal component")
plt.ylabel("Second principal component")
plt.show()

#print("Original shape: {}".format(str(X_scaled.shape)))
#print("Reduced shape: {}".format(str(X_pca.shape)))

#print("X train data: ", X_train)
#print("y train data: ", y_train)
#svm = SVC(C=100)
#svm.fit(X_train, y_train)
#print("Test set accuracy: {:.2f}".format(svm.score(X_test, y_test)))

#scaler.fit(X_train)
#X_train_scaled = scaler.transform(X_train)
#X_test_scaled = scaler.transform(X_test)
#print("Scaled X_train is: ", X_train_scaled);
#print("Scaled X_test is: ", X_test_scaled);
#
#svm.fit(X_train_scaled, y_train)
#print("Scaled test set accuracy: {:.2f}".format(svm.score(X_test_scaled, y_test)))
#svm.score(X_test_scaled, y_test)
