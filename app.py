from flask import Flask, request, jsonify, render_template, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    # Renders the home.html page when visiting the root URL
    return render_template('home.html')


@app.route('/FAQ1')
def faq1():
    # Renders the h1.html page
    return render_template('h1.html')

@app.route('/FAQ2')
def faq2():
    # Renders the h2.html page
    return render_template('h2.html')

@app.route('/FAQ3')
def faq3():
    # Renders the h3.html page
    return render_template('h3.html')



@app.route('/blog')
def blog():
    # Renders the index.html page where the prediction form is located
    return render_template('blog.html')

@app.route('/index')
def index():
    # Renders the index.html page where the prediction form is located
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Input from frontend
    features = np.array([
        data['age'], data['sex'], data['cp'], data['trestbps'], data['chol'],
        data['fbs'], data['restecg'], data['thalach'], data['exang'],
        data['oldpeak'], data['slope'], data['ca'], data['thal']
    ]).reshape(1, -1)
    
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})  # Respond to frontend

if __name__ == '__main__':
    app.run(debug=True)
