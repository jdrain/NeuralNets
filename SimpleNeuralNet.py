import numpy.random

"""
This file contains an implementation of a simple neural network
We need:
a training set
a function
"""

#training set
input = [1, 2, 3, 4, 5, 6]
output = [2, 4, 6, 8, 10, 12]

#simple multiplication function
def f(input, weight):
    return input * weight

#function to test the net
def testFunction(step, iterations, weight):
    for i in range(0, iterations): #number of times we'll adjust the weight
        for j in range(0, input.__len__()):  #run through the training set
            out = f(input[j], weight)
            if (out < output[j]): #if experimental output is less we should increase the weight
                weight = weight + step * (output[j] - out)
            elif (out > output[j]): #if experimental output is more we should decrease the weight
                weight = weight + step * (output[j] - out)
    return weight