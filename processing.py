import numpy as np
from sklearn import *

####Somehow think of a way to create a class and inheritance


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

