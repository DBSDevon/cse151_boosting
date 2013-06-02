weights
'''
with the global dataset and global weights
'''
def boosting():
	#1. Declare the global dataset and weight, but they have been previously initialized
	global weights
	bestFeature = -1
	totalError = 100.0

	#2. For each feature in a data point
	for ( i in range(0, weights.length) ) :
		# A. calculate the total error via evaluating each datapoint
		error = 0.0
		# B. If the total error is less than previous best error, then replace the current error with this and the current feature record
		if (error < totalError) :
			bestFeature = i
			totalError = error
		# should have another check here for the inverse
	#3. Get the error information
	
	#4. change the weights

'''
this gives the h1 evaluation of the feature
'''
def calculateError (feature) :
	#0. Terms
	totalError = 0.0

	#1. for each email (data element)
	for ( email in trainingList ) :
		# if the feature != the label, increment error
		if ( email[feature] != email[-1] ) :
			totalError++
	#2. Divide the total error by the size
	totalError = totalError / float (email.length)

	#3. Return it
	return totalError


if __name__ == "__main__" :
	# 1. read in the training file
	# 2. create any persistent structures
	# List of tuples (feature number, h1 or h0 type)
	# global Vector of weights
	# 3. for t loops:
		# A. Run our boost algorithm (returns a tuple for our list and the new weights)
		# B. Add the resulting tuple to our list
		# C. Replace our current vector of weights with the new vector
	# 4. Read the test file
	# 5. Create a variable for the total error and the total number of emails
	# 6. For each email in the test file
		# A. Label it according to our algorithm
		# B. Compare the labels, add to the error count if it fails

	# 7. Spit out the number for t and a fraction of error count / email count for our personal gains
	# 8. load the dictionary into a vector
	# 9. for each tuple in our list
		# A. spit out the element of the vector in that spot
