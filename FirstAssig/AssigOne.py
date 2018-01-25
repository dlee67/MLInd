import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import inputGenerator

from scipy import sparse
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier as Kn

targetValues = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
			  [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]

inputValues = inputGenerator.generateInput(len(targetValues))

print(inputValues)
			  
#def startProg(someData, trainData, testData):
#	X_train, X_test, y_train, y_test = train_test_split(trainData, testData, random_state=0)
#	knn = Kn(n_neighbors=1)
#	knn.fit(X_train, y_train)
#	result = knn.predict(predictThis)
#	if False:
#		pass
#	
#someData = None


