import numpy as np
from sklearn import *


def format_train(array):
    """Normalize and scale a numpy array of training data for classifier"""
    normalized_array = preprocessing.normalize(array)
    scaled_array = preprocessing.scale(normalized_array)
    return scaled_array


def format_label(array, ravel=False):
    """Encode the labels from training data into a 1D numpy array of integers"""
    if ravel is True:
        raveled = np.ravel(array)
        le = preprocessing.LabelEncoder()
        le.fit(raveled)
        encoded = le.transform(raveled)
        return encoded
    else:
        le = preprocessing.LabelEncoder()
        le.fit(array)
        encoded = le.transform(array)
        return encoded


def format_standard(array):
    """Scale the training and test data with scikit-learn's StandardScaler in a numpy array"""
    scaler = preprocessing.StandardScaler()
    scaler.fit(array)
    array = scaler.transform(array)
    return array


class Trip:
    """Input the predicted labels from the SGD Classifier. Get the whole array or return a set of distinct labels from the array"""
    def __init__(self, predictarr):
        self.predictarr = predictarr

    def get_predicted(self):
        return self.predictarr

    def distinct(self):
        distinct_trip = set(self.predictarr)
        return distinct_trip


class Alter(Trip):
    """Inherited class from Trip that makes the distinct labels array a stack. Pop values from the stack or append a value to the stack."""
    def __init__(self, predictarr):
        Trip.__init__(self, predictarr)
        self.stack = set(predictarr)

    def pop(self):
        self.stack.pop()
        return self.stack

    def add(self, value):
        predict_list = list(self.stack)
        appended = predict_list.append(value)
        return appended

    


