#https://stackoverflow.com/questions/46511017/plot-hyperplane-linear-svm-python
#The link above seems to demonstrate what I am looking for.
#

import matplotlib.pyplot as plt
import numpy as np
import inputGenerator

from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
from mglearn.plot_helpers import discrete_scatter

targetValues = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0],
			  [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]

inputValues = inputGenerator.generateInput(len(targetValues))

svm = LinearSVC(C=1)
svm.fit(inputValues, targetValues)

for counter in range(0, len(inputValues)):
		plt.scatter(inputValues[counter][0], inputValues[counter][1])

#This entire thing has to do with the SVC,
#and it's more mathematically incorporated
#than I'd thought.
#Thus, if full understanding of 
w = svm.coef_[0]; print("w is:", w)
a = -w[0] / w[1]; print("a is:", a) # This represents slope, but I am still not sure
									# why we have to put a unary minus in there.
xx = np.linspace(0, 20); print("xx is:", xx)
yy = a * xx - (svm.intercept_[0]) / w[1]; print("yy is:", yy) #Don't know why intercept (which
															  #is referred as an independent value, sometimes)
															  # is being divided by the w[1].

plt.plot(xx, yy, c='k')
plt.show()



#Next time I comeback to this concept, I need to go over the SVC as a mathematical study.

print("My coef's are: ", svm.coef_)
print("My intercept is: ", svm.intercept_)
print("My slope should be: ", (svm.coef_[0][0]/svm.coef_[0][1])) 
