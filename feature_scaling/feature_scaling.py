#! /usr/bin/env python

""" quiz materials for feature scaling clustering """

### FYI, the most straightforward implementation might
### throw a divide-by-zero error, if the min and max
### values are the same
### but think about this for a second--that means that every
### data point has the same value for that feature!
### why would you rescale it?  Or even use it at all?


def featureScaling(arr):
    mini = min(arr)
    range = max(arr) - mini

    res = [(x-mini)/(range*1.0) for x in arr]

    return res

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
