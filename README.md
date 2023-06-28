## End to end Machine Learning Project

* Created a tool that estimates data science salaries (MAE ~ $ 14K) to help data scientists / data analyst / data engineers negotiate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium 
* Engineered features from the text of each job description to quantify the value companies put on python, excel, aws, and spark.
* Optimized Random Forest Regressor, Adaboost, Xgboost and many other using GridsearchCV to reach the best model.
* Built a client facing API using flask

## Code and Resources Used
Python Version: 3.7
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle
For Web Framework Requirements: pip install -r requirements.txt
Scraper Github: https://github.com/arapfaik/scraping-glassdoor-selenium
