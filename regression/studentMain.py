#! /usr/bin/env python

import numpy
import matplotlib
# matplotlib.use('agg')

import matplotlib.pyplot as plt
#from studentRegression import studentReg
from class_vis import prettyPicture, output_image
from sklearn import linear_model

from age_net_worth_data import ages_train, net_worths_train, ages_test, net_worths_test

#from ages_net_worths import ageNetWorthData

#ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

def studentReg(ages_train, net_worths_train):

    reg = linear_model.LinearRegression()
    reg.fit (ages_train, net_worths_train)
    return reg

reg = studentReg(ages_train, net_worths_train)

print "slope: ", reg.coef_
print "intercept: ", reg.intercept_

# ------------------   R-square values ---------------------- #

print "r-squared score test: ", reg.score(ages_test, net_worths_test)
print "r-squared score train: ", reg.score(ages_train, net_worths_train)

# -------------------------- predictions ------------- "

print reg.predict([27])




plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")


plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())




