import random

def generateInput (iterAmt):
	someList = []
	random.seed(a=0)
	for x in range(0, int(iterAmt/2)):
		orderedPair = [random.randint(0, 10), random.randint(0, 10)]
		someList.append(orderedPair)
	for y in range(0, int(iterAmt/2)):
		orderedPair = [random.randint(10, 20), random.randint(10, 20)]
		someList.append(orderedPair)
	return someList
