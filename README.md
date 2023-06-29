## End to end Machine Learning Project

* Created a tool that estimates data science salaries (MAE ~ $ 14K) to help data scientists / data analyst / data engineers negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium 
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Random Forest Regressor, Adaboost, Xgboost and many other using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used
* Python Version: 3.7
* Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
* For Web Framework Requirements: pip install -r requirements.txt
* Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium

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
![alt text]([https://github.com/SrijanDeo-DA-DS/DataScience_Job_Salary_Predictor/blob/main/resources/Count%20of%20job%20vs%20state.png]
