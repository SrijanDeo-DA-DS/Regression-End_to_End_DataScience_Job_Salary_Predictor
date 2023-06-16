path = 'C:/Users/srija/Documents/DS_Job_Salary_Predictor/'

import os
import sys
import pandas as pd

os.chdir(path)

from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split

def train_test_splitting(path):
    os.chdir(path)
    logging.info("Train Test split started")
    try:
        for i in os.listdir():
            
            df = pd.read_csv(i)
            df_train, df_test = train_test_split(df,test_size=0.2)
            df_train.to_csv('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/train.csv',index=False)
            df_test.to_csv('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/test.csv',index=False)
            
            logging.info("Train test split completed")

    except Exception as e:
        logging.info("Error in train test split")
        raise CustomException(e,sys)
        
train_test_splitting('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/good_data')