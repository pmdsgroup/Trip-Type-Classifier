import numpy as np
from sklearn import *


def format_train(array):
    normalized_array = preprocessing.normalize(array)
    scaled_array = preprocessing.scale(normalized_array)
    return scaled_array


def format_label(array, ravel=False):
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
    scaler = preprocessing.StandardScaler()
    scaler.fit(array)
    array = scaler.transform(array)
    return array


class Trip:

    def __init__(self, predictarr):
        self.predictarr = predictarr

    def get_predicted(self):
        return self.predictarr

    def distinct(self):
        distinct_trip = set(self.predictarr)
        return distinct_trip


class Alter(Trip):

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

    


