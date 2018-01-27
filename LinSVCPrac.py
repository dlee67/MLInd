import matplotlib.pyplot as plt
import numpy as np
import inputGenerator

from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
from mglearn.plot_helpers import discrete_scatter

targetValues = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
			  [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]

inputValues = inputGenerator.generateInput(len(targetValues))

mySVM = LinearSVC(C=1)
mySVM.fit(inputValues, targetValues)

print(mySVM.coef_)
print(mySVM.intercept_)
