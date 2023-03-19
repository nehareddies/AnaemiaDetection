from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
print("Loading Model")
model = pickle.load(open('anaemia_detection.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    gender = float(request.form['gender'])
    hemoglobin = float(request.form['hemoglobin'])
    mch = float(request.form['mch'])
    mchc = float(request.form['mchc'])
    mcv = float(request.form['mcv'])

    result = model.predict([[gender,hemoglobin,mch,mchc,mcv]])[0]
    result = "Anaemia Detection Reports show that you are {} likely to be having Anaemia!".format("more" if result else "not")
    return render_template('index.html', result=result)

app.run(port=8080)