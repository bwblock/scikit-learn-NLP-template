#! /usr/bin/env python


"""
    Naive Bayes classifier identifies emails by their authors

    Authors and labels:
    Sara has label 0
    Chris has label 1

    Naive Bayes is great for text--it’s faster and generally gives better performance than an SVM.
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

t0 = time()
clf = GaussianNB()
clf.fit(features_train, labels_train)

print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy = accuracy_score(pred, labels_test)

print "accuracy: %s" %("{:.2f}".format(accuracy * 100)),"%"

#########################################################


