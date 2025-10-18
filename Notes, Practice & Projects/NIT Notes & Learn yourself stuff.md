Learn yourself stuff:



1\. anova framework: analysis of variance. SSR=sum of squared regressor, SSE=sum of square error, SST=sum of square total.



\- SSE: sum of errors

\- SSR: From the predicted point to average

\- SST = SSE + SSR



\- Why we need anova?

&nbsp; = To find regression model's accuracy.

\- R^2 = 1-SSR/SST

\- Adjusted R^2

\- Both the of their range is always between 0 to 1.

\- R squared and adjusted r squared is a performance measure of regression model.



\* Type 1 type 2 error comes in classification models

\* R squared and Adjusted R squared comes under regression models.



=====Machine Learning=======

\- Training phase, testing phase, validation phase

\- Model? 

\- Traditional model: input + input == output

\- ML model: Input, output (inputs only) == logic that can generate output to different input.

\- Supervised data:

&nbsp; - regression: Dependent variables are continuous

&nbsp; - classification: Dependent variables are binary.

\- Unsupervised data:

&nbsp; - Clusters: no dependent variable here, just groups.

(historical: Seen data, future data: unseen data)



---

\- Reinforcement learning:



\- Pipeline for ML model:

1\. Gathering data

2\. Preparing that data

3\. choosing a model

4\. Training

5\. Evaluation

6\. Hyperparameter Tuning

7\. Prediction

8\. ML ops

9\. CI/CD Pipeline



===Data preprocessing pipeline===

1\. Sql query to get the raw data or client shared the data or other team shared the data.

2\. We divide the data into X \& y where x is independent var and y is dependent var.

&nbsp;- x is divided into x train and x test

&nbsp;- y is divided into y train and y test

3\. then we train the data using X\_train + Y\_train, then the model will get generated.

4\. How to divide the data?

\- 70-30, 80-20 or 75-25%.



Data analyst: work on structured data

Data engineer: work on unstructured data.



===Spyder App===

\- Used for training ML models.

\- Scikit learn-



\- It is built on top of Data structures required for machine learning. It also include Math, linear algebra and stats.



\- How to import: from sklearn.

\- Impute, is a transformer



\- fit and transform

&nbsp; - Parameter tuning \& Hyperparameter



==14-08-22025==



Regression -->

&nbsp; - Simple linear regression: y=mx+c

&nbsp; - 



Classification -->

Clustering -->



===18-8-2025===

\*\*Bias \& Variace

-trained the data == Bias

-Test the data == Variance



Bias = 94, variance - 34 (High bias and low variance) == Underfitting

Bias = 40, variance = 89 (Low bias and high variance) == Overfitting

Bias = 94 \& Variance = 82 (Low Bias \& Low variance) == Best fit model



This is called the Bias-Variance tradeoff.



\*\*Overfitting and Underfitting\*\*

Overfitting: Training the model with a lot of attributes is called overfitting. Overfit model = Misclassification



\- Technique to reduce overfitting

1\. PCA (Principle Component analysis)

2\. Regularization technique (lasso \& ridge)

3\. ensemble learning

4\. Cross Validation

5\. Drop out the neurons

6\. Business Knowledge





\*\*Underfitting\*\*

\- Training the model with a very few variables/attributes is called underfitting. This also leads to Misclassification.



\*Techniques to reduce underfitting\*

\- By adding more relevant attributes while training the data.





-----

\*\*Stats for ML\*\* in 02\_linear\_regression.py file in August>Practical

-----



---19-8-2025---

Simple linear model/regression COMPLETED



\*\*Multiple linear regression Model 20-08-2025\*\*



Formula: **y = m1x1 + m2x2 + m3x3 + c**



* Backward Elimination
* Recursive Feature Elimination
* P-value
* statsmodels


Linear REgression
- SLR
- MLR
- Regularization
- Gradience Decent, SG, BGD
- Time Series

Non Linear Regression
- Polynomial
- Support Vector machine
- Decision Tree
- Random Forest
- xgboost regression
- lgb  light gradient boost regression
- ann artificial neural network regression

===Overfitting===
- Low bias high variance
- If you build the model with 100 attributes(features) the model will Overfit, so take only relevant features.
- If coefficient of independent variable is very high, also leads to ovrfitting (Regularization)

==Underfitting===
- high bias low variance

==Low bias, Low variance==
- Best fit model.

===Regularization===
- To reduce high coef to low coef & scale down overfitting regularization is used
- Feature selection Techniques:
  1. lasso regression(l1)(powerful, why?)(feature elimination)
     Lasso = Loss + alpha ||w||
                        (Penalty)
  2. ridge regression(l2):
     
     Ridge R = Loss + alpha ||w||^2
                        (Penalty)

  3. elastic net regression(l1+l2)
     - Inherits few concepts from l1 & l2
      
===Gradient Decent===

(read the jupyter notebook: 21_22082025_Gradient_decent)


===== DONE TILL NOW ========
Feature selection technique
1. Business understanding
2. p-value, rfe, backward elimination
3. lasso regularization
4. decision tree
5. pca

Feature engineering
1. eda technique
2. variable identification 
3. missing variable treatment
4. imputation or transformer
5. outlier, univariate, bivariate, multivariate

Feature Scaling
1. Standardization
2. Normalization

ML concepts:
Linear: Simple linear, Multiple linear, gradient descent, batch gradient descent, l1, l2
Non Linear: polynomial reg, support vector reg, knn, decision tree, random forest, etc. (these are remaining).


===26-06-2025===
Support Vector Regressor (used for regressor) (SVM is used for Classification)
- Best Fit line = Hyperplane
- y=wx+b
- One side of the plane (line) is positive and another is negative, and it is called distance between 2 support line also called marginal distance.
- Decision boundry == svr line
- Final equation: -a <y-mx + B < + a
- Difference between the margins should be Maximun, therefore it's called maximum margin difference.

===KNN===
Distance Matrix
- Euclidian distance (we can apply this on most of the algorithms)
  = Shortest distance
- Manhatten distance
  = Farthest distance
- Cosine Distance
  = distance amongst the words, used in NLP, vector, llm

===28th august===
prev: Poly: Increased the degrees of independent variable
SVR: max marginal distance
KNN: distance matrix (euclidance distance & manhatten distance)

today:
=======Decision tree & Random Forest=======
 - Gini index
 - entropy
 - max depth
 - pruning
 - leaf node
 - root node

- How to decide root node, leaf node, purity, etc.

Random Forest:
Group of decision trees is called random forest

Ensemble learning
- Bagging
  - Random Forest
- Boosting

===2-9-2025===
Classification Regression
A) Performace measure of regression: R-squared, Mean absolute error, Mean squared error, RMSE, confusion matrix.

Algorithms:
1. Logistic Reg
2. SVM
3. DT
4. KNN
5. Random Forest
6. xgboost
7. lgbm
8. naive bayes
9. ANN classifiers

===Confusion matrix===

Formula = 
Accuracy = (TP + TN)/Total
Error = (FP + FN)/Total Or 1 - accuracy
Precision
Recall

f1 score = 2*(precision*recall)/precision+recall

- Why to use all these matrix? how does it affect the model?

===Logistic Reg===
- Logistic reg is both classification and regression model
- Sigmoid fuction is applied to deal with the outlier.
- Logistic regression is also called as maxent classifier


===PCA=== 4-9-2025====

PCA( Principal component analysis)
- used for clustering
- minimizes the larger coefficient
- WE can create multiple PCs from PCA

How to find out best PC based on highest eigen vector
---
Logistic Regression in PCA.
- Explained Variance Ratio
- 
