from flask import Flask, request, render_template, jsonify
import joblib
from fraud_detection import LogisticRegression, preprocess_data

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('fraud_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [float(data[f'v{i}']) for i in range(1, 29)]
    features = [float(data['amount']), float(data['time'])] + features
    
    # Preprocess the input data
    preprocessed_data = preprocess_data([features])
    
    # Make prediction
    prediction = model.predict(preprocessed_data[0])
    
    return jsonify({'prediction': 'Fraudulent' if prediction == 1 else 'Not Fraudulent'})

if __name__ == '__main__':
    app.run(debug=True)