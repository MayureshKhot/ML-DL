import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"D:\\NareshIT_PrakashSenapati\\Prakash Sir-Notes\Auguest (Statistics)\\20th\\Investment.csv")

X=dataset.iloc[:, :-1]
y=dataset.iloc[:, 4]

X = pd.get_dummies(X, dtype=int)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.8, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

m = regressor.coef_
print(m)

c = regressor.intercept_
print(c)

#X = np.append(arr=np.ones((50,1)).astype(int), values=X, axis=1)

X = np.append(arr=np.full((50,1), 42467).astype(int), values=X, axis=1)

import statsmodels.api as sm #needs to install the stats model

X_opt = X[:, [0,1,2,3,4,5]]
#Ordinary Least Squares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

#As per the results, remove the feature with highest value.
X_opt = X[:, [0,1,2,3,5]]
#Ordinary Least Squares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

#Again
X_opt = X[:, [0,1,2,3]]
#Ordinary Least Squares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()

#Again
X_opt = X[:, [0,1,3]]
#Ordinary Least Squares
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()