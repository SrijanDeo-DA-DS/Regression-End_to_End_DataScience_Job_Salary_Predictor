## End to end Machine Learning Project

* Created a tool that estimates data science salaries (MAE ~ $ 14K) to help data scientists / data analyst / data engineers negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium 
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Random Forest Regressor, Adaboost, Xgboost and many other using GridsearchCV to reach the best model.
* Built a client facing API using flask (CLient/End-User can use Front End UI and/or shared drive location to put theor test data)

## Code and Resources Used
* Python Version: 3.7
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* For Web Framework Requirements: pip install -r requirements.txt
* Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium

## Data Validation
* I used python scripts to validate the raw data sent by client.
* This is done by verifying the name of file and number of columns in the file. More such checks can be added if needed

## Data Logging and Custom Exception handling
* Every step is logged and a separate folder is created for logging. Such process can help identify problems in the code
* Every error is logged in the logger file with a Custom Error Handling exception message

## Web Scraping
Tweaked the web scraper github repo (above) to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

1. Job title
2. Salary Estimate
3. Job Description
4. Rating
5. Company
6. Location
7. Company Headquarters
8. Company Size
9. Company Founded Date
10. Type of Ownership
11. Industry
12. Sector
13. Revenue
14. Competitors

## Data Cleaning 
After scraping the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

* Parsed numeric data out of salary
* Made column for avg salary out min and max salary
* Removed rows without salary
* Parsed rating out of company text
* Cleaned up company state and headquarters
* Transformed founded date into age of company
* Made columns for if different skills were listed in the job description:
    1. Python
    2. R
    3. Excel
    4. AWS
    5. Spark
    6. Column for simplified job title and Seniority

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables.

* Count of Job vs State 
# ![Count of job vs state](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/f3c0c267-c3b0-41e6-97da-325c7b955d3b)
* Job Salary vs Position vs State vs Sector
# ![Job position vs Salary](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/2e86c81f-ccd4-4c8e-a3e6-7b612e464095), ![Job State vs Salary](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/49aa00d3-8897-426d-81c3-3458d51141be), ![Sector vs Salary](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/52c25747-73f8-4d22-8867-9694c50d36dc)
* Job Sector Wordcloud
# ![Sector Wordcloud](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/ab41d42e-d98f-4fa5-98c6-a0676f7cc938)
* Job Salary Correlation , Job Salary Distribution
# ![Salary correlation](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/577b6bf0-be61-4fa9-8de3-32d8bb552308) , ![Salary Distribution](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/25dc4120-c8df-47c9-88af-229cc3df6346)

* California has maximum number of jobs followed by massachusetts and  New York
* Media Sector is paying the maximum compensation
* Job Salary is highly positively correlated to Company Rating and Number of competitors it has

## Model Training
First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

![Model Score](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/b54c58e2-48e6-4be4-89f7-fa76b5382f30)

FInally, I decided to use Random Forest Regressor

## Productionize the model
Coming soon...
## Front End API
![Front-end-2](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/cddc56ae-579f-4305-ad7c-d11454d387b0)
![Front-end-1](https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/assets/88278620/ce5df099-7c75-4176-83b5-6f9ba2baf78e)

