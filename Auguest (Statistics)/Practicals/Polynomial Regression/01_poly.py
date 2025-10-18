import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\Auguest (Statistics)\Practicals\Polynomial Regression\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y=dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred
# Here we predicted the salary of the employees with 6.5 yrs of salary
# But the predictions cannot be made based on single variable (experience)
#Therefore we apply non-linear regression

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=15)#changing this is called hyperparameter tuning or fine tuning
# Definition : PolynomialFeatures(degree=2, *, interaction_only=False, include_bias=True, order="C")
# Here degree=2 is default and means it'll take 2 features while training the model
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)

lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.title('Truth or Bluff Poly regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)


















