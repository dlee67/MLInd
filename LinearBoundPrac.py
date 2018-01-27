from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inputGenerator

X, y = mglearn.datasets.make_forge()
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
mySVC = LinearSVC()
myReg = LogisticRegression()

#print("LinearSVC() returns: ", LinearSVC())
#print("LogisticRegression() returns: ", LogisticRegression())

#It's magic, let's just put it that way for now.
#for model, ax in zip([LinearSVC(), LogisticRegression()], axes):
#	#print("model is: ", model)
#	#print("ax is: ", ax)
#	clf = model.fit(X, y)
#	mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5,
#                                    ax=ax, alpha=.7)
#	mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
#	ax.set_title("{}".format(clf.__class__.__name__))
#	ax.set_xlabel("Feature 0")
#	ax.set_ylabel("Feature 1")
#axes[0].legend()
#mglearn.plots.plot_linear_svc_regularization()

#cancer = load_breast_cancer()
#X_train, X_test, y_train, y_test = train_test_split(
#	cancer.data, cancer.target, stratify=cancer.target, random_state=0)
#logreg = LogisticRegression().fit(X_train, y_train)
#print("Training set score: {:.3f}".format(logreg.score(X_train, y_train)))
#print("Test set score: {:.3f}".format(logreg.score(X_test, y_test)))



#plt.show()