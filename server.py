from flask import Flask
import os
import requests

# Create a Flask application
app = Flask(__name__)

# Define a route and its associated function
@app.route('/<movies>')
def getMyNonSenseReview(movies):
    queryParameter = {"product": movies, "quantity": 1}
    headerParameter = {"X-Api-Key": '4161bce418794ce98e1dceaa12630395'}
    response = requests.post("https://randommer.io/api/Text/Review", params = queryParameter, headers = headerParameter)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print("Request failed with status code:", response.status_code)
        return "Oups, could't speak"

port = os.environ.get("PORT",5000)
app.run(debug=False, host="0.0.0.0",port=port)