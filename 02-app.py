from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the trained model from file
model = load('finalized_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Extract the value for 'X' from the incoming request
    value_of_x = data['X']
    
    # Make sure X is in the correct shape for prediction
    value_of_x = np.array(value_of_x).reshape(-1, 1)
    
    # Use the loaded model to make a prediction
    prediction = model.predict(value_of_x)
    
    # Prepare and send the response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True, runat='0.0.0.0')

