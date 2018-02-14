import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inputGenerator

from scipy import sparse
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.model_selection import train_test_split
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler	

targetValues = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
			  [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
inputValues = inputGenerator.generateInput(len(targetValues))
X_train, X_test, y_train, y_test = train_test_split(inputValues, targetValues,
                                                    random_state=1)
scaler = MinMaxScaler()
svm = SVC(C=100)
			  
def plotValues(plotThis):
	for counter in range(0, len(plotThis)):
		plt.scatter(plotThis[counter][0], plotThis[counter][1])
	plt.xlabel("x-axis")
	plt.ylabel("y-axis")
	plt.show()

def plotRegression(inputValues, targetValues):
	svm = LinearSVC(C=1)
	svm.fit(inputValues, targetValues)
	w = svm.coef_[0]
	a = -w[0]/w[1]
	xx = np.linspace(0, 20)
	yy = a * xx - (svm.intercept_[0]) / w[1]
	for counter in range(0, len(inputValues)):
		plt.scatter(inputValues[counter][0], inputValues[counter][1])
	plt.plot(xx, yy)
	plt.show()
	
def startProg(predictThis, input, target):
	knn = Kn(n_neighbors=1)
	knn.fit(input, target)
	result = knn.predict([predictThis])
	print("predict() returned: ", result)

def scaleValues(inputValues):
	scaler.fit(inputValues)
	Scaled_Set = scaler.transform(inputValues)
	return Scaled_Set

