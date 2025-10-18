import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\Auguest (Statistics)\Practicals\Polynomial Regression\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y=dataset.iloc[:,2].values

#decision tree

from sklearn.tree import DecisionTreeRegressor
dt_reg_model = DecisionTreeRegressor(criterion='poisson', splitter='random',)
dt_reg_model.fit(X, y)

dt_reg_pred = dt_reg_model.predict([[6.5]])
print(dt_reg_pred)

#Random forest
# Group of decision trees is called Random forest

from sklearn.ensemble import RandomForestRegressor
#rf_reg_model = RandomForestRegressor()
#rf_reg_model.fit(X, y)
#rf_reg_pred = rf_reg_model.predict([[6.5]])
#print(rf_reg_pred)


# if random state is not tuned, it gives random outputs
rf_reg_model = RandomForestRegressor(random_state=1, n_estimators=3)
rf_reg_model.fit(X, y)

rf_reg_pred = rf_reg_model.predict([[6.5]])
print(rf_reg_pred)

# Till now Random forest is the best, based on the output.