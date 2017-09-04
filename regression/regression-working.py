#! /usr/bin/env python

import numpy as np
import matplotlib
# matplotlib.use('agg')


import matplotlib.pyplot as plt

#from studentRegression import studentReg
from class_vis import prettyPicture, output_image
from sklearn import linear_model

import numpy as np
data = np.genfromtxt('data-working-wl.csv',delimiter=',')

#x_data = [[x[0]] for x in data if x[2] == 0]
#y_data = [[x[1]] for x in data if x[2] == 0]

x_data = [[x[0]] for x in data]
y_data = [[x[1]] for x in data]

def studentReg(x_train, y_train):

    reg = linear_model.LinearRegression()
    reg.fit (x_train, y_train)
    return reg

reg = studentReg(x_data, y_data)

print "slope: ", reg.coef_
print "intercept: ", reg.intercept_

# ------------------   R-square values ---------------------- #

print "r-squared score test: ", reg.score(x_data, y_data)
#print "r-squared score train: ", reg.score(ages_train, net_worths_train)

# -------------------------- predictions ------------- "




plt.clf()
plt.scatter(x_data, y_data, color="b", label="train data")

plt.legend(loc=2)
plt.xlabel("x_data")
plt.ylabel("y_data")


plt.savefig("working.png")
output_image("working.png", "png", open("working.png", "rb").read())




