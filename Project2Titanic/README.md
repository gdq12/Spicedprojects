The purpose of this project was to attempt to build a valid machine learning model to be able with the highest capacity determine the survival rate of Titanic passengers provided by the [Kaggle Titanic Challenge](https://www.kaggle.com/c/titanic). 

Since the outcome is binary (survived/not survived) Logistic Regression was initially employed for model building. Also used Decision Tree and Random Forest in an attempt to improve model accuracy. 

Feature engineering and Hyperparameter Optimization were used in an attempt to build the best possible model. 

For this present analysis, a particular emphasis was placed on custom building functions that automate Receiver Operating Characteristic (ROC) curve along with Precision-Recall curve production for several machine learning model at a time. Therefore, machine learning model assessment is based primarily on what these graphs reveal. 

The following ROC and precision-recall curves show the various models attempted for the most part correctly predicted passenger survival rate: 

![curves](https://github.com/spicedacademy/allspice-arrays-code/blob/gloria/Project2Titanic/ROCrf.png) 
