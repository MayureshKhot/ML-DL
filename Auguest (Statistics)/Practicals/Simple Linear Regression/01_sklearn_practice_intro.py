import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\Auguest (Statistics)\Data.csv")

X = dataset.iloc[:, :-1].values
y= dataset.iloc[:,3].values

from sklearn.impute import SimpleImputer #Transformers for missing value imputation.
imputer = SimpleImputer() #By default it uses mean strategy.

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])
# Filled the value with the mean strategy

imputer = SimpleImputer(strategy='median')

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])
# Filled the value with the median strategy.

imputer = SimpleImputer(strategy='most_frequent')

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:,1:3])
# Filled the value with the median strategy.


# Label Encoder: Convert Categorical data into numerical (cities)
from sklearn.preprocessing import LabelEncoder

labelencoder_X = LabelEncoder()
labelencoder_X.fit_transform(X[:,0])
X[:,0] = labelencoder_X.fit_transform(X[:,0])

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.8, test_size=0.2)
# No need to write train_size & test_size both, you can just write one and system will automatically understand the rest

#Records are pulled randomly and everytime we run the progra, it's changing
#This will affect the accuracy of the model

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.8, test_size=0.2, random_state=0)

#===================================================================================
#FEATURE SCALING = Standardization
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Normalization (0 to 1 scale)
from sklearn.preprocessing import Normalizer
sc_X = Normalizer()
X_train = sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)




















