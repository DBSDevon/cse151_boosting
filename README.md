In this assignment, we will look at the task of spam classiﬁcation using boosting. Our raw data is a set
of emails, which were collected from a liguistics mailing list; the emails are labeled as spam or not spam.
For your beneﬁt, we have already preprocessed the emails to remove stop-words, punctuation, and to do
some preliminary preprocessing that lemmatises the words (for example, that maps words such as include,
includes and included to the same word), and converted them to vectors of features.

Download ﬁles hw6train.txt, hw6test.txt and hw6dictionary.txt from the class website. The ﬁrst
two ﬁles contain your training and test datasets respectively. The third ﬁle is a dictionary and contains a
list of words. Each line in the ﬁles hw6train.txt and hw6test.txt correspond to an email followed a label
which can be 1 or -1. An email is represented by a feature vector of length 1531; a label -1 indicates that
the email is a spam message, and a label 1 indicates that it is not spam. Coordinate i of the feature vector
corresponding to an email is 1 when word i in hw6dictionary.txt is present in the email and 0 otherwise.
Write down the training and test errors of the classiﬁers obtained after t = 3;7;10;15;20 rounds of
boosting. Use the following weak learning procedure. Each weak learner corresponds to a classiﬁer hi;+ or
hi;-, where i is a word in the dictionary and the classiﬁer hi;+ is the rule:
hi;+(x) = 1; if word i occurs in email x
		= -1; otherwise

Similarly, the classiﬁer hi; is the rule:
hi;-(x) = 1; if word i does not occur in email x
		= -1; otherwise
The set of weak learners C is the collection of such classiﬁers for all i, and your weak learning procedure
should select the weak learner which has the highest accuracy in C with respect to the current weighted set
of examples. Based on the dictionary ﬁle, write down the words corresponding to the weak learners chosen
in the ﬁrst 10 rounds of boosting.

[Hint: If your code is correct, you should get a training error of 0.1140 and a test error of 0.09 after two
rounds of boosting.]