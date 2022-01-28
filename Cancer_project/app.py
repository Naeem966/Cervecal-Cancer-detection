# -*- coding: utf-8 -*-
# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np
import joblib

# Load the CLassifier model
filename = "cancer_model.pkl"

model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('main.html')


@app.route('/predict', methods=['GET','POST'])
#Predict Method for Getting data and loding results
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        partners=int(request.form['partners'])
        pregnancies=int(request.form['pregnancies'])
        Smokes=int(request.form['Smokes'])
        Smokes2=int(request.form['Smokes2'])
        Contraceptives=int(request.form['Contraceptives'])
        Contraceptives_years=int(request.form['Contraceptives _years'])
        
        STDs=int(request.form['STDs'])
        STDs_number=int(request.form['STDs_number'])
        condylomatosis=int(request.form['condylomatosis'])
        cervical_condylomatosis=int(request.form['cervical_condylomatosis'])
        perineal_condylomatosis=int(request.form['perineal_condylomatosis'])
        
        syphilis=int(request.form['syphilis'])
       	pelvic_inflammatory=int(request.form['pelvic_inflammatory'])
        genital_herpes=int(request.form['genital_herpes'])
        molluscum_contagiosum=int(request.form['molluscum_contagiosum'])
        AIDS=int(request.form['AIDS'])
        HIV=int(request.form['HIV'])
        Hepatitis_B=int(request.form['Hepatitis_B'])
        HPV=int(request.form['HPV'])
        Dx_Cancer=int(request.form['Dx_Cancer'])
        Dx_HPV=int(request.form['Dx_HPV'])
        
        data = np.array([[age,partners,pregnancies,Smokes,Smokes2,Contraceptives,Contraceptives_years,STDs,STDs_number,condylomatosis,
       cervical_condylomatosis,perineal_condylomatosis,syphilis,
       pelvic_inflammatory, genital_herpes, molluscum_contagiosum,
       AIDS, HIV, Hepatitis_B, HPV, Dx_Cancer, Dx_HPV]])
        
      #predictions
        my_prediction = model.predict(data)
        
       # Rendering
       
        return render_template('result.html', prediction=my_prediction)
    
    ''' def predict():
    if request.method == 'POST':
        age=float(request.form ['age'])
        Numberofsexualpartners=float(request.form ['Number of sexual partners'])
        Numofpregnancies=float(request.form ['Num of pregnancies'])
        Smokes=float( request.form ['Smokes'])
        Smokes1=float(request.form ['Smokes (years)'])
        HormonalContraceptives=float( request.form ['Hormonal Contraceptives'])
        
        HormonalContraceptives= float( request.form ['Hormonal Contraceptives (years)'])
        IUD=float( request.form ['IUD'])
        
        STD1= float( request.form ['STDs:condylomatosis'])
        
        STD2=float( request.form ['STDs:cervical condylomatosis'])
        
        #parametrs. append( request.form ['STDs:vaginal condylomatosis'])
        
        STD3=float( request.form ['STDs:vulvo-perineal condylomatosis'])
        
        STD4=float( request.form ['STDs:syphilis'])
        
        STD5=float( request.form ['STDs:pelvic inflammatory disease'])
        
        STD6=float( request.form ['STDs:genital herpes'])
        
        STD7=float( request.form ['STDs:molluscum contagiosum'])
        
        STD8=float( request.form ['STDs:AIDS'])
        
        STD9=float( request.form ['STDs:HIV'])
        
        STD10=float( request.form ['STDs:Hepatitis B'])
        
        STD11=float( request.form ['STDs:HPV'])
        
        STD12=float( request.form ['STDs:cervical condylomatosis'])
        
        STD13=float( request.form ['STDs: Time since first diagnosis'])
        
        STD14=float( request.form ['STDs: Time since last diagnosis'])
        STD15=float( request.form ['Dx:Cancer'])
        
        pred_args = [age,Numberofsexualpartners,Numofpregnancies, Smokes,Smokes1,HormonalContraceptives,HormonalContraceptives,IUD
                 ,STD1,STD2,STD3,STD4,STD5,STD6,STD7,STD8,STD9,STD10,STD11,STD12,STD13,STD14,STD15]
        mul_reg = open("Cancer_detection_model.pkl" , "rb" )
        ml_model = joblib.load(mul_reg)
        model_predcition = ml_model.predict([pred_args])
        if model_predcition == 1:
            res = 'Affected'
        else:
            res = 'Not affected'
            '''
        
        
if __name__ == '__main__':
	app.run(debug=true)

