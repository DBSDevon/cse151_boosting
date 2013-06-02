#!/c/python27/python
import math

weights
trainingList = []

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
	for ( i in range(0, weights.length-1) ) :
		# A. calculate the total error via evaluating each datapoint
		error = calculateError(i)
		# B. If the total error is less than previous best error, then replace the current error with this and the current feature record
		if (error < totalError) :
			bestFeature = i
			bestError = error
			label = 1
		# should have another check here for the inverse
		elif ( 1.0 - error < totalError ) :
			bestFeature = i
			bestError = 1.0 - error
			label = -1
	
	#3. change the weights
	alpha = 0.5 * math.log( (1.0-bestError) / bestError )

	for ( i in range(0, weights.length - 1) :
		y = trainingList.at(i)[-1]
		ep = math.exp(-alpha*y*label)
		weights.at(i) = weights.at(i)*ep

	#4. get the normalization factor
	sum = 0.0
	for ( d in weights ) :
		sum += d

	for ( d in weights ) :
		d = d / sum

	return (bestFeature, label, alpha)

'''
this gives the h1 evaluation of the feature
'''
def calculateError (feature) :
	#0. Terms
	totalError = 0.0

	#1. for each email (data element)
	for ( i in range(0, trainingList-1) ) :
		# if the feature != the label, increment error
		email = trainingList.at(i)
		if ( email[feature] != email[-1] ) :
			totalError+=weights.at(i)

	#2. Return it
	return totalError


if __name__ == "__main__" :
	# 1. read in the training file
	# 2. create any persistent structures
	# List of tuples (feature number, h1 or h0 type)
	fhTuples = []

	# global Vector of weights
	global weights
	weights = [1]*1
	
	# 3. for t loops:
	for (t in range(0, 1)) :
		# A. Run our boost algorithm (returns a tuple for our list and the new weights)
		# B. Add the resulting tuple to our list
		fhTuples.add(boosting())

	# 4. Read the test file
	# 5. Create a variable for the total error and the total number of emails
	# 6. For each email in the test file
		# A. Label it according to our algorithm
		# B. Compare the labels, add to the error count if it fails

	# 7. Spit out the number for t and a fraction of error count / email count for our personal gains
	# 8. load the dictionary into a vector
	# 9. for each tuple in our list
		# A. spit out the element of the vector in that spot

