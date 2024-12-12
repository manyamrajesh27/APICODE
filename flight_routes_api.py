from flask import Flask, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Predefined flight routes
flight_routes = [
    "OSL-MOL",
    "BCN-MAD",
    "BER-ORY",
    "JFK-BOSTON"
]

@app.route('/api/flight-route', methods=['GET'])
def get_flight_route():
    # Pick a random route
    selected_route = random.choice(flight_routes)
    return jsonify({"route": selected_route})

@app.route('/api/random-date', methods=['GET'])
def get_random_date():
    # Generate a random date more than 6 months ahead
    today = datetime.now()
    start_date = today + timedelta(days=6 * 30)  # Approx 6 months
    end_date = start_date + timedelta(days=5 * 365)  # Up to 5 years ahead
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    formatted_date = random_date.strftime("%m/%d/%Y")
    return jsonify({"random_date": formatted_date})

if __name__ == '__main__':
    # Run the application on localhost at port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)