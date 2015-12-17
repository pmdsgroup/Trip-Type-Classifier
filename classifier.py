import pandas as pd
from processing import *
import matplotlib.pyplot as plt
from collections import Counter

train_file = open('train_ml.csv', 'r')
s = pd.read_csv(train_file, nrows=642925)

test_file = open('test_ml.csv', 'r')
d = pd.read_csv(test_file, nrows=642925)


train_data = (pd.DataFrame({'VisitNumber': s['VisitNumber'].apply(float), 'Weekday':  s['Weekday'].apply(float),
              'Upc': s['Upc'].apply(float), 'ScanCount': s['ScanCount'].apply(float), 'DepartmentDescription': s['DepartmentDescription'].apply(float),
               'FinelineNumber': s['FinelineNumber'].apply(float)}))

labels_data = pd.DataFrame({'TripType': s['TripType'].apply(float)})

test_data = pd.DataFrame({'VisitNumber': d['VisitNumber'].apply(float), 'Weekday':  d['Weekday'].apply(float),
              'Upc': d['Upc'].apply(float), 'ScanCount': d['ScanCount'].apply(float), 'DepartmentDescription': d['DepartmentDescription'].apply(float),
               'FinelineNumber': d['FinelineNumber'].apply(float)})

train_array = np.array(train_data)
labels_array = np.array(labels_data)
test_array = np.array(test_data)

Y_train = format_label(labels_array, ravel=True)
X_train = format_standard(train_array)
test_predict = format_standard(test_data)

sgd = linear_model.SGDClassifier(loss="hinge", penalty="l2")
sgd.fit(X_train, Y_train)
count_predict = Counter(sgd.predict(test_predict))

a = Trip(sgd.predict(test_predict))
print(a.distinct())

b = Alter(sgd.predict(test_predict))
print(b.pop())

dict_predict = dict(count_predict)

e = {k: v for k, v in dict_predict.iteritems()}

plt.bar(range(len(e)), e.values(), align='center')
plt.xticks(range(len(e)), e.keys())
plt.xlabel('Trip Types')
plt.ylabel('Frequency')
plt.title('Predicted Frequency of Trip Types by SGD Classifier from Test Set')

plt.show()

test_file.close()
train_file.close()
