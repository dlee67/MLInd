import random
import inputGenerator
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.datasets import make_blobs
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler	

scaler = MinMaxScaler()
SomeList = inputGenerator.generateInput(20)

scaler.fit(SomeList)
TransformedList = scaler.transform(SomeList)

print("My transformed list is: ", TransformedList)