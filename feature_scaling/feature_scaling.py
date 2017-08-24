#! /usr/bin/env python

""" feature scaling example """


from sklearn.preprocessing import MinMaxScaler
import numpy
weights = numpy.array([[115.], [140.], [175.]])
scaler = MinMaxScaler()

rescaled_weights = scaler.fit_transform(weights)

print rescaled_weights
