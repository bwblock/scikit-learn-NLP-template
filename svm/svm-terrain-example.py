#! /usr/bin/env python


import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl
from time import time
from sklearn import svm
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## SVM #################################
### we handle the import statement and SVC creation for you here
#from sklearn.svm import SVC
#clf = SVC(kernel="rbf")


#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data

#### store your predictions in a list named pred

t0=time()
clf = svm.SVC(kernel="rbf", gamma=500, C=1.0)
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1=time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"


#   Low C parameter makes the decision boundary smooth.

accuracy = accuracy_score(pred, labels_test)

print "accuracy: %s" %("{:.2f}".format(accuracy * 100)),"%"

#def submitAccuracy():
#    return acc


