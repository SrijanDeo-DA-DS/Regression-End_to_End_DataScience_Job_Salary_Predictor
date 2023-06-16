path = 'C:/Users/srija/Documents/DS_Job_Salary_Predictor/'


import os
import sys
import pandas as pd
import shutil
from pathlib import Path

os.chdir(path)

from src.exception import CustomException
from src.logger import logging

def Data_validation(path):
    '''
    This function will validate the raw data coming in on 3 basis:
    1. Is the directory empty ?
    2. If directory is not empty, then name of the file matches the expected value?
    3. If name of file is correct, are there exact number of columns as expected and no entire null columns in the data?
    '''
    
    os.chdir(path)
    
    logging.info("Data Validation started")
    try:
        if os.listdir():
            for i in os.listdir():
                if i.startswith('raw') and i.endswith('.csv'):
                    df = pd.read_csv(i)
                    if len(df.columns)==16 and df.isnull().values.all(axis=0).sum()==0:
                        logging.info("Correct data ",i)
                        shutil.copy(i,"C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/good_data")
                    else:
                        logging.info("Incorrect data ",i)
                        shutil.copy(i,"C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/bad_data_archived")
                else:
                    logging.info("Incorrect filename ",i)
                    shutil.copy(i,"C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/bad_data_archived")
        else:
            logging.info("Folder is empty")
    except Exception as e:
        raise CustomException(e,sys)
        
Data_validation('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/raw_data')