import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# this dataset is about customer purchased the vehicle or not
dataset = pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\September (Stats and ML)\logit classification.csv")

X = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:, -1].values

from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0) #accuracy = 89
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0) #accuracy = 92, always optimized
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=100) #accuracy = 85

#Scale the data=Standardization
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

#Model Accuracy = Confusion matrix

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)#TP, FN, TN, FP

from sklearn.metrics import accuracy_score
ac=accuracy_score(y_test, y_pred)
print(ac)

from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)

# How to check the model is overfit of underfit?
# Check bias

bias = classifier.score(X_train, y_train)
print(bias)

variance = classifier.score(X_test, y_test)
print(variance)

'''
# 1 testing = 25%, bias = 82%, model accuracy = 89%, variance=89
# This is low bias low variance, therefore best fit line

#if overfit = use gridsarch cv, random

Without scaling also the accuracy will remian same i.e. 89

from sklearn.preprocessing import Normalizer
sc=Normalizer()
X_train = sc.fit_transform(X_train)

with normalizer, we will get even less accuracy (68)

How to increase the accuracy?
- change the train test split

Next?
Model testing on unseen data (validation dataset)

'''



















