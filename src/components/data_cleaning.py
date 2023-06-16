import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_train = pd.read_csv('C:/Users/srija/Documents/DS_Job_Salary_Predictor/data/train.csv')

## Let's clean the columns

## Job Title

def title_simplifier(title):
    if 'data scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' or 'analytics' or 'business' or 'intelligence' in title.lower():
        return 'data analyst'
    elif 'machine learning' in title.lower():
        return 'machine learning engg'
    else:
        return 'na'
    
df_train['Job Title simp'] = df_train['Job Title'].apply(title_simplifier)

def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() :
            return 'senior'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower() or 'principal' in title.lower():
        return 'director'
    elif 'jr' in title.lower() or 'jr.' in title.lower() or 'staff' in title.lower():
        return 'jr'
    else:
        return 'na'
    
df_train['Job Seniority'] = df_train['Job Title'].apply(seniority)

## Salary Estimate

df_train['hourly'] = df_train['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df_train['employer_provided'] = df_train['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df_train = df_train[df_train['Salary Estimate'] != '-1']
salary = df_train['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df_train['min_salary'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df_train['max_salary'] = min_hr.apply(lambda x: int(x.split('-')[1]))
df_train['avg_salary'] = (df_train.min_salary+df_train.max_salary)/2

## Company name

df_train['company_name'] = df_train['Company Name'].apply(lambda x: x.split('\n')[0] if '\n' in x else x)

## job description

#python
df_train['python_yn'] = df_train['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
 
#r studio 
df_train['R_yn'] = df_train['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)

#spark 
df_train['spark'] = df_train['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws 
df_train['aws'] = df_train['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df_train['excel'] = df_train['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

## job state and headquarters

df_train['job_state'] = df_train['Location'].apply(lambda i:i.split(',')[-1])
df_train['job_headquarters'] = df_train['Headquarters'].apply(lambda i:i.split(',')[-1])

df_train['job_state']= df_train.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'new jersey' else 'NJ')
df_train['job_state']= df_train.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'michigan' else 'MI')
df_train['job_state']= df_train.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'oregon' else 'OR')
df_train['job_state']= df_train.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'virginia' else 'NJ')
df_train['job_state']= df_train.job_state.apply(lambda x: x.strip() if x.strip().lower() != 'maryland' else 'MD')

df_train.drop(df_train[df_train['job_state']=='United States'].index,inplace=True)

## Sector

df_train.drop(df_train[df_train['Sector']=='-1'].index,inplace=True)

## Founded

df_train['age of company'] = 2023-df_train['Founded']

## Size

df_train.drop(df_train[df_train['Size']=='-1'].index,inplace=True)

## Competitors

df_train['num_comp'] = df_train['Competitors'].apply(lambda x: len(x.split(',')) if x != '-1' else 0)

## Revenue

df_train.drop(df_train[df_train['Revenue']=='-1'].index,inplace=True)

df_train.drop(['S.no','Job Title', 'Salary Estimate', 'Job Description', 'Company Name', 'Location', 'Headquarters',
              'Founded', 'Competitors','hourly', 'employer_provided', 'min_salary', 'max_salary'],axis=1,inplace=True)

