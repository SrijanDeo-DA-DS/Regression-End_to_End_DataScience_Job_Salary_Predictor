from flask import Flask, render_template, request
import jsonify
import requests
import pickle
#import numpy as np
import sklearn
import pandas as pd
#from sklearn.preprocessing import StandardScaler
#from src.pipeline.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
## Route for a home page

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html') 

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        Job_Seniority=request.form['Job Seniority']
        if Job_Seniority == 'na':
            Job_Seniority_na =1
            Job_Seniority_jr =0
            Job_Seniority_senior =0
            Job_Seniority_manager =0
        else:
            Job_Seniority_na = 0
            Job_Seniority_jr =1
            Job_Seniority_senior =0
            Job_Seniority_manager =0
        Job_Title_simp=request.form['Job Title simp']
        if Job_Title_simp == 'data scientist':
            Job_Title_simp_data_scientist =1 
            Job_Title_simp_data_engineer = 0
        else:
            Job_Title_simp_data_scientist = 0
            Job_Title_simp_data_engineer = 1
        job_state=request.form['job_state']
        if job_state == 'MA':
            job_state_MA =1
            job_state_NY =0
        else:
            job_state_MA =0
            job_state_NY = 1
        job_headquarters=request.form['job_headquarters']
        if job_headquarters == 'MA':
            job_headquarters_MA = 1
            job_headquarters_NY = 0
        else:
            job_headquarters_MA = 0
            job_headquarters_NY = 1
        Easy_Apply=int(request.form['Easy_Apply'])
        python_yn=int(request.form['python_yn'])
        R_yn=int(request.form['R_yn'])
        spark=int(request.form['spark'])
        aws=int(request.form['aws'])
        excel=int(request.form['excel'])
        #Rating=int(request.form['Rating']),
        num_comp=int(request.form['num_comp'])
        age_of_company=int(request.form['age_of_company'])
        
        prediction=model.predict([[Easy_Apply,python_yn,R_yn,spark,aws,excel,age_of_company,num_comp,Job_Title_simp_data_engineer,Job_Title_simp_data_scientist,Job_Seniority_jr,Job_Seniority_manager,Job_Seniority_na,Job_Seniority_senior,job_state_MA,job_state_NY,job_headquarters_MA,job_headquarters_NY]])
        output=round(prediction[0],2)
        return render_template('home.html',results = output)


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True, use_reloader=False, port=0000)      
