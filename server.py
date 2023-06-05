from flask import Flask
import requests

# Create a Flask application
app = Flask(__name__)

# Define a route and its associated function
@app.route('/<movie>')
def getMyNonSenseReview(movie):
    queryParameter = {"product": movie, "quantity": 1}
    headerParameter = {"X-Api-Key": '4161bce418794ce98e1dceaa12630395'}
    response = requests.post("https://randommer.io/api/Text/Review", params = queryParameter, headers = headerParameter)
    if response.status_code == 200:
        response_json = response.json()
        return response_json
    else:
        print("Request failed with status code:", response.status_code)
        return "Oups, could't speak"

# Run the application
if __name__ == '__main__':
    app.run()