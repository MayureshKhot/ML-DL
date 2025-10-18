import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv(r"D:\NareshIT_PrakashSenapati\My Projects\Data\iris flower dataset-ML\IRIS.csv")

X = data.drop('species', axis=1) #Axis = 1 is compulsory, it says that check in columns
y = data['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, train_size=0.8, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)
