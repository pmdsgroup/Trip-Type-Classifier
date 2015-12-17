import pandas as pd
from processing import *
import matplotlib.pyplot as plt
from collections import Counter

train_file = open('train_ml.csv', 'r')
s = pd.read_csv(train_file, nrows=642925)                                         #Read 642,925 rows from the training and test .csv files

test_file = open('test_ml.csv', 'r')
d = pd.read_csv(test_file, nrows=642925)


train_data = (pd.DataFrame({'VisitNumber': s['VisitNumber'].apply(float), 'Weekday':  s['Weekday'].apply(float),      #Create a pandas dataframe with all features as floats(for compatibility to preprocess data and use with SGD Classifier) 
              'Upc': s['Upc'].apply(float), 'ScanCount': s['ScanCount'].apply(float), 'DepartmentDescription': s['DepartmentDescription'].apply(float),
               'FinelineNumber': s['FinelineNumber'].apply(float)}))

labels_data = pd.DataFrame({'TripType': s['TripType'].apply(float)})                                                  #Make a pandas dataframe with just Trip Type labels from the training data

test_data = pd.DataFrame({'VisitNumber': d['VisitNumber'].apply(float), 'Weekday':  d['Weekday'].apply(float),        #Create a pandas dataframe with all features as floats(for compatibility to preprocess data and use with SGD Classifier) 
              'Upc': d['Upc'].apply(float), 'ScanCount': d['ScanCount'].apply(float), 'DepartmentDescription': d['DepartmentDescription'].apply(float),
               'FinelineNumber': d['FinelineNumber'].apply(float)})

train_array = np.array(train_data)                                  #Create numpy arrays out of all created dataframes
labels_array = np.array(labels_data)
test_array = np.array(test_data)

Y_train = format_label(labels_array, ravel=True)                    #Preprocess data from the custom preprocess library
X_train = format_standard(train_array)
test_predict = format_standard(test_data)

sgd = linear_model.SGDClassifier(loss="hinge", penalty="l2")        #Initialize the SGD Classifier from sklearn
sgd.fit(X_train, Y_train)                                           #Fit the classifier with the training data and labels
count_predict = Counter(sgd.predict(test_predict))                  #Count the number of distinct predicted labels from the test data

print(sgd.score(test_predict, Y_train))                             #Print the f1 score of the classifier

a = Trip(sgd.predict(test_predict))                               
print(a.distinct())                                                 #Print a set of distinct predicted labels

b = Alter(sgd.predict(test_predict))
print(b.pop())                                                      #Print the set with a removed value

dict_predict = dict(count_predict)                                  #Convert predicted labels counter to a dictionary

e = {k: v for k, v in dict_predict.iteritems()}                     #Dictionary comprehension

plt.bar(range(len(e)), e.values(), align='center')                  #Plot the frequencies of predicted labels from the test data using matplotlib
plt.xticks(range(len(e)), e.keys())
plt.xlabel('Trip Types')
plt.ylabel('Frequency')
plt.title('Predicted Frequency of Trip Types by SGD Classifier from Test Set')

plt.show()

test_file.close()
train_file.close()
