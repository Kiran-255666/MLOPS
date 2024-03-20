import requests
import json

# The URL where your Flask API is hosted (change to your actual API endpoint)
api_url = "http://localhost:5000/predict"

# Example input data (change this to match the input format expected by your API)
input_data = {
    "X": 5.0  # Example input; replace with actual input expected by your model
}

# Convert the dictionary to a JSON string before sending it as a POST request
input_data_json = json.dumps(input_data)

# Set the content type to application/json
headers = {
    "Content-Type": "application/json"
}

# Send the POST request to the Flask API
response = requests.post(api_url, data=input_data_json, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the prediction from the response
    prediction = response.json()
    print("Prediction:", prediction)
else:
    print("Error:", response.status_code, response.text)

