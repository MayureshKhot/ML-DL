import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\Auguest (Statistics)\Practicals\Polynomial Regression\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y=dataset.iloc[:,2].values

#Play with the degrees and other parameters
from sklearn.svm import SVR
svr_regressor = SVR(kernel='sigmoid', degree=5, gamma: 'scale')
svr_regressor.fit(X,y)
#164079

svr_model_pred = svr_regressor.predict([[6.5]])
print(svr_model_pred)

#knn model
from sklearn.neighbors import KNeighborsRegressor
knn_reg_model = KNeighborsRegressor(n_neighbors=4, weights='uniform') #By default 5 neighbors
knn_reg_model.fit(X, y)

#default 5 neighbors = 168000 for 6.5
#n_neighbors=7, weights='distance' = 232284

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)
