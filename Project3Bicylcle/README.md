### General Background

The purpose of this project is to build a machine learning model to predict the number of bikes needed at any given time in Washington D.C. for their bikesharing market [kaggle challenge](https://www.kaggle.com/c/bike-sharing-demand/data). This is broken down into exploratory data analysis (EDA), features selection, modeling and evaluating assumptions (in each respective jupyter notebook).

### EDA

Initial analysis demonstrated visible behavioral difference between casual and registered bike users:

![casual_vs_registered](images/user_diff.png)

Initial analysis also demonstrated that temperature fluctuated most bike rental count:

![temp_count](images/temp_count_fluctuation.png)

### Feature Selection

This analysis demonstrated that hour, workingday,  atemp, humidity, month,  and holiday are the most significant factors and should be included in modeling.

### Modeling

Many different combinations of features were used for linear regression, decision tree and random forest modeling. The specific features for each group are as follows:

- noAnalysis: season, holiday, workingday, weather, temp, atemp, humidity, windspeed, month, day, hour
- EDA: hour, atemp, humidity, month, workingday, holiday
- Interact*: mJulHol, mJunWD, mJultemp, mJulHum, 8h, 18h
- EDA + Interact: hour, atemp, humidity, month, workingday, holiday, mJulHol, mJunWD, mJultemp, mJulHum, 8h, 18h
- noAnalysis + EDA + Interact: season, holiday, workingday, weather, temp, atemp, humidity, windspeed, month, day, hour, hour, atemp, humidity, month, workingday, holiday, hour, atemp, humidity, month, workingday, holiday, mJulHol, mJunWD, mJultemp, mJulHum, 8h, 18h

* quick note: an idea of a former Classmate [Julia](https://github.com/julisep), certain months and hours of day that had high peaks in bike rental count were emphasized by placing higher emphasis on them via a sort of one-hot encoding technique. See featEng() function in modeling notebook for better understanding.

The respective $r^2$ and RMSLE score were calculated for quantifying success of each model:

Linear Regression:

![LR](images/linear_regression.png)

Decision Tree:

![DT](images/decision_tree.png)

Random Forest:

![RF](images/random_forest.png)

As can be seen from the graphs above, decision tree had the bet RMSLE but demonstrated possible overfitting. The next best model to use would be random forest with noAnalysis.

### Evaluating Assumptions

This was done to verify the regression model is unbiased. All assumptions were met except normal residual distribution, homoscedasticity and multicolinearity. Despite these last 3 being violated, the first 4 held true, concluding that the model is unbiased.
