import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inputGenerator

from scipy import sparse
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

targetValues = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
			  [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]

inputValues = inputGenerator.generateInput(len(targetValues))
			  
def plotValues(plotThis):
	for counter in range(0, len(plotThis)):
		plt.scatter(plotThis[counter][0], plotThis[counter][1])
	plt.xlabel("x-axis")
	plt.ylabel("y-axis")
	plt.show()

def startProg(predictThis, input, target):
	X_train, X_test, y_train, y_test = train_test_split(input, target, random_state=0)
	knn = Kn(n_neighbors=1)
	knn.fit(X_train, y_train)
	result = knn.predict([predictThis])
	print("predict() returned: ", result)
	
startProg([0, 9], inputValues, targetValues)
startProg([4, 7], inputValues, targetValues)
startProg([11, 19], inputValues, targetValues)
startProg([12, 17], inputValues, targetValues)	
startProg([0, 20], inputValues, targetValues)	

plotValues(inputValues)
