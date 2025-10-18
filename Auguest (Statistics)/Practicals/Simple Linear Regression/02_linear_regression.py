import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"D:\NareshIT_PrakashSenapati\Prakash Sir-Notes\Auguest (Statistics)\14th\Salary_Data.csv")
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.8, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)


plt.scatter(x_test, y_test, color='red')
plt.plot(x_train, regressor.predict(x_train),color='blue')
plt.title('Salary vs Experiece')
plt.xlabel('Years of Experience')
plt.ylabel("Salary")
plt.show()

#Something's wrong, fix it. the model should not be getting this much datapoints


m=regressor.coef_
c=regressor.intercept_

(m*12)+c
(m*20)+c

bias = regressor.score(x_train, y_train)
bias

variance = regressor.score(x_test, y_test)
variance

#Stats for ML

dataset.mean()
dataset['Salary'].mean()

dataset.var()

dataset.std()

# Coefficient of Variation(cv)

from scipy.stats import variation #scientific python used for stats
variation(dataset.values) #this will give cv of entire dataframe

variation(dataset['Salary'])

dataset.corr() #this will give correlation of entire dataset
#corr range is -1 to 1

dataset['Salary'].corr(dataset['YearsExperience']) #this will give us correlation between these variables

dataset.skew()

#Standard Error
dataset.sem()

#Z-score for Standardization of data
# z score will convert the data into equal scales like below

import scipy.stats as stats
dataset.apply(stats.zscore)

stats.zscore(dataset['Salary'])

#Degree of Freedom

a=dataset.shape[0]
b=dataset.shape[1]

degree_of_freedom = a-b
print(degree_of_freedom)
#this will give us degree of freedom for entire df

#Sum of Squared Errors #SSR

y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#Sum of squared #SSE

y = y[0:6]
SSE = np.sum((y-y_pred)**2) #Throwing Errors
print(SSE)

#  SST
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

#R-squared
r_squared = 1-SSR/SST
print(r_squared) #85.7, so this is a good model














