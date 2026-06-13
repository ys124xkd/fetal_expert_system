from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__)

# Load the model, scaler, features, and accuracy
with open('model.pkl', 'rb') as f:
    model, scaler, features, accuracy = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html', features=features, accuracy=accuracy)

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(request.form[feature]) for feature in features]
    scaled_data = scaler.transform([data])
    prediction = model.predict(scaled_data)
    
    classification = ''
    if prediction == 1:
        classification = 'Normal'
    elif prediction == 2:
        classification = 'Suspect'
    elif prediction == 3:
        classification = 'Pathological'

    return redirect(url_for('result', prediction=classification, accuracy=accuracy, **dict(zip(features, data))))

@app.route('/result')
def result():
    data = {feature: request.args.get(feature) for feature in features}
    prediction = request.args.get('prediction')
    accuracy = request.args.get('accuracy')
    return render_template('result.html', features=features, data=data, prediction=prediction, accuracy=accuracy)

if __name__ == "__main__":
    app.run(debug=True)
