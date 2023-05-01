import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Heart Disease Prediction Model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = [ "BMI", "smoking","AlcoholDrinking","Stroke", "PhysicalHealth", "MentalHealth",
                       "DiffWalking", "Sex", "Age", "Race", "Diabetic", "PhysicalActivity",
                        "GenHealth", "SleepTime", "Asthma", "KidneyDisease", "SkinCancer"]
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
        
    if output == 1:
        res_val = "** Heart Disease **"
    else:
        res_val = "No Heart Disease "
        

    return render_template('index.html', prediction_text='Patient has {}'.format(res_val))

if __name__ == "__main__":
    app.run()
