import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df_train = pd.read_csv('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/data_preprocess.csv')

from sklearn.model_selection import train_test_split

X = df_train[['Easy_Apply','python_yn','R_yn','spark','aws','excel','age_of_company','num_comp','Job_Title_simp_data_engineer','Job_Title_simp_data_scientist','Job_Seniority_jr','Job_Seniority_manager','Job_Seniority_na','Job_Seniority_senior','job_state_MA','job_state_NY','job_headquarters_MA','job_headquarters_NY']]
y = df_train['avg_salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))

rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,y_pred)

import pickle
# open a file, where you ant to store the data
file = open('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/random_forest_regression_model.pkl', 'wb')

# dump information to that file
pickle.dump(rf, file)