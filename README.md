# Trip-Type-Classifier

This file contains instructions on how to run the SGD Classifier algorithm (in order) on real Walmart sales data to predict the type of store trip a customer is on based on the purchased items.

All relevant .csv data files are contained in the working directory that contains the code (this folder)

1. Run sqlite_transform.py to clean the raw data from training and test data files and create a SQlite database from them. It is then used to encode two features (Weekday and DepartmentDescription) in the data. Then exports to correctly formatted .csv files for the classifier.

2. Run Classifier.py. This preprocesses (scales, transforms) the training and test data exported from the database and turns them into numpy arrays. It runs the SGD Classifier and prints the f1 score for the run. It creates a matplotlib bar graph that displays the frequencies of predicted labels from the test data.

***preprocessing.py is a custom library that contains functions to preprocess data and the Trip and Alter classes. 
