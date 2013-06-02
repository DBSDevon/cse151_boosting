#!/c/python27/python

trainingList = []

def boosting():
	yield
'''
This method opens the training file, and then
parses each line to a vector, creating a list
of vectors.
'''
def readFile(filename):
	with open(filename, 'r') as openFile:
		for line in openFile:
			global trainingList
			trainingList.append(map(int, line.split()))


'''
This method is our weak classifier, essentially:
Return 1 if the word occurs in the email
Else return -1
'''
def classifier(value):
	return 1 if (value == 1) else -1

'''
Since our classifiers are complements of each other,
we want to flip the error and labels if the error is 
higher than 0.5
'''
def errorCheck(probabilityTuple):
	if probabilityTuple[0] > 0.5:
		probabilityTuple[0] = 1.0 - probabilityTuple[0]
		probabilityTuple[1] = -1
	return probabilityTuple
