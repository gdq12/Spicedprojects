The purpose of this project it to build a machine learning model to predict the number of bikes needed at any given time in Washington D.C. for their bikesharing market, for the kaggle challenge. 

Currently, have issues with feature engineering. The principle issue is that Scaling the data leads to negative y true values, making it impossible to calculate the root mean square log error (RMSLE).

Must consult and investigate scalar method correctly done and which combination of methodology is best (exp(ypred) or not). 

Will update when resolve this issue.  