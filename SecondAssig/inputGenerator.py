import random

def generateInput (iterAmt):
	someList = []
	for x in range(0, int(iterAmt/2)):
		orderedPair = [random.uniform(0, 5), random.uniform(0, 5)]
		someList.append(orderedPair)
	for y in range(0, int(iterAmt/2)):
		orderedPair = [random.uniform(5, 10), random.uniform(5, 10)]
		someList.append(orderedPair)
	return someList
