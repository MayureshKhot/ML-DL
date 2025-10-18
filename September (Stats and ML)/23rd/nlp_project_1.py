import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\September (Stats and ML)\23rd\Restaurant_Reviews.tsv", delimiter = '\t', quoting = 3)

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

corpus = []

for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
# Creating bag of words
from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer()
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

#Splitting the dataset into the training set and test set.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

'''
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
'''

# Try applying all algorithms instead of Decision Tree
# Then check all of their accuracy and compare
# Keep the model with minimum 80% accuracy
# If after trying all models, the accuracy is not enough
# You duplicate the dataset 2 times or 3 times- Data augumentation
# We used without stopwords this time, so meaning has changed for a few words
# So try this one time with stopwords.

'''
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()

#Predicting the Test set results
y_pred = rf.predict(X_test)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier()

from sklearn.svm import SVC
model = SVC()
'''
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(C=5, solver='lbfgs', max_iter=500)

model.fit(X_train, y_train)

#Predicting the test set results
y_pred = model.predict(X_test)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

bias = model.score(X,y)
print(bias)

variance = model.score(X_test, y_test)
print(variance)


