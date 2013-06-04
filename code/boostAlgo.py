#!/c/python27/python
import math

weights = []
dataList = []

'''
This method opens the training file, and then
parses each line to a vector, creating a list
of vectors.
'''
def readFile(filename):
	global dataList
	dataList = []
	with open(filename, 'r') as openFile:
		for line in openFile:
			dataList.append(map(int, line.split()))


'''
This method is our weak classifier, essentially:
Return 1 if the word occurs in the email
Else return -1
'''
def classifier(value):
	return 1 if (value == 1) else -1

def classifierNeg(value):
	return 1 if (value == 0) else -1


'''
Since our classifiers are complements of each other,
we want to flip the error and labels if the error is 
higher than 0.5
'''
def errorCheck(probability, label):
	if probability > 0.5:
		probability = 1.0 - probability
		label = -1 * label
	return probabilityTuple


'''
with the global dataset and global weights
'''
def boosting():
	#1. Declare the global dataset and weight, but they have been previously initialized
	global weights
	bestFeature = -1
	bestError = 100.0
	label = 0

	#2. For each feature in a data point
	for i in range(0, len(dataList[0])-1):
		# A. calculate the total error via evaluating each datapoint
		error = calculateError(i)
		# B. If the total error is less than previous best error, then replace the current error with this and the current feature record
		if (error < bestError) :
			bestFeature = i
			bestError = error
			label = 1
		# should have another check here for the inverse
		elif ( 1.0 - error < bestError ) :
			bestFeature = i
			bestError = 1.0 - error
			label = -1
	
	#3. change the weights
	try:
		alpha = 0.5 * math.log( ((1.0-bestError) / bestError) )
	except ValueError:
		print "Alpha calculate crash with value of ", bestError
		exit(1)

	for i in range(0, len(dataList)):
		y = dataList[i][-1]
		tempLab = 0
		if label == 1:
			tempLab = classifier(dataList[i][bestFeature])
		else:
			tempLab = classifierNeg(dataList[i][bestFeature])
		ep = math.exp(-alpha*y*tempLab)
		weights[i] = weights[i] * ep

	#4. get the normalization factor
	sum = 0.0
	for d in weights:
		sum += d

	for d in range(0, len(weights)):
		weights[d] = weights[d] / sum

	return (bestFeature, label, alpha)

'''
this gives the h1 evaluation of the feature
'''
def calculateError (feature) :
	#0. Terms
	totalError = 0.0

	#1. for each email (data element)
	for i in range(0, len(dataList)):
		# if the feature != the label, increment error
		email = dataList[i]
		if classifier(email[feature]) != email[-1]:
			totalError+=weights[i]

	#2. Return it
	return totalError


def calculateLabel(featureVector, learnerList):
	summation = 0
	for boostLearn in learnerList:
		if boostLearn[1] == 1:
			if featureVector[boostLearn[0]] == 1:
				summation += boostLearn[2]
			else:
				summation -= boostLearn[2]
		else:
			if featureVector[boostLearn[0]] == 0:
				summation += boostLearn[2]
			else:
				summation -= boostLearn[2]
	return (summation / math.fabs(summation))

def readDictionary(tupleSet):
	dictionaryList = []
	with open("..\data\hw6dictionary.txt", 'r') as dictFile:
		for line in dictFile:
			dictionaryList.append(line.split()[0])
	for element in tupleSet:
		if element[1] == 1:
			print "Word in not-spam:", dictionaryList[element[0]]
		else:
			print "Word in spam:", dictionaryList[element[0]]

if __name__ == "__main__" :
	fhTuples = []
	boostingSet = [3, 7, 10, 15, 20]
	for boostRound in boostingSet:
		# 0. Which Round is it?
		print "\nNumber of Boosting iterations:", boostRound

		# 1. read in the training file
		readFile("..\data\hw6train.txt")

		# 2. create any persistent structures
		# List of tuples (feature number, h1 or h0 type)
		fhTuples = []

		# global Vector of weights
		global weights
		weights = [1.0/len(dataList)] * len(dataList)
		
		# 3. for t loops:
		for t in range(0, boostRound):
			# A. Run our boost algorithm (returns a tuple for our list and the new weights)
			# B. Add the resulting tuple to our list
			fhTuples.append(boosting())
		#Calcuate training error by calling classifier on all the training data
		errorCount = 0

		for t in dataList:
			currLabel = calculateLabel(t, fhTuples)
			if currLabel != t[-1]:
				errorCount += 1
		print "Training error:", (errorCount / float (len(dataList)) )

		# 4. Read the test file
		readFile("..\data\hw6test.txt")
		
		errorCount = 0

		for t in dataList:
			currLabel = calculateLabel(t, fhTuples)
			if currLabel != t[-1]:
				errorCount += 1
		print "Test error:", (errorCount / float (len(dataList)) )

		if boostRound >= 10:
			readDictionary(fhTuples)

	# 5. Create a variable for the total error and the total number of emails


	# 6. For each email in the test file
		# A. Label it according to our algorithm
		# B. Compare the labels, add to the error count if it fails

	# 7. Spit out the number for t and a fraction of error count / email count for our personal gains
	# 8. load the dictionary into a vector
	# 9. for each tuple in our list
		# A. spit out the element of the vector in that spot

