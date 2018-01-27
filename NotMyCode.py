import matplotlib.pyplot as plt
import numpy as np

from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
from mglearn.plot_helpers import discrete_scatter

def plot_linear_svc_regularization():
    X, y = make_blobs(centers=2, random_state=4, n_samples=30)
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    # a carefully hand-designed dataset lol
    y[7] = 0
    y[27] = 0
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

# coef_ represents the vector that is orthogonal to the hyper plane created by the SVM.
# https://stats.stackexchange.com/questions/39243/how-does-one-interpret-svm-feature-weights	
# 
    for ax, C in zip(axes, [1e-2, 10, 1e3]):
        discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)

        svm = LinearSVC(C=C, tol=0.00001, dual=False).fit(X, y)
        w = svm.coef_[0]; print("w is:", w)
        a = -w[0] / w[1]; print("a is:", a) # This represents slope.
        xx = np.linspace(6, 13); print("xx is:", xx)
        yy = a * xx - (svm.intercept_[0]) / w[1]; print("yy is:", yy)
        ax.plot(xx, yy, c='k')
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.set_xticks(())
        ax.set_yticks(())
        ax.set_title("C = %f" % C)
    axes[0].legend(loc="best")


if __name__ == "__main__":
	plot_linear_svc_regularization()
	#LOOK HERE! THIS IS WHERE THE PLOT IS TO BE DISPLAYED.    
	plt.show()
	
	
	