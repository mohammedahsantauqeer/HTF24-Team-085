from flask import Flask, request, jsonify
import requests
from utils import itinerary_generator, recommend_engine, api_integration

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_preferences = data.get('preferences')
    recommendations = recommend_engine.get_recommendations(user_preferences)
    return jsonify(recommendations)

@app.route('/itinerary', methods=['POST'])
def itinerary():
    data = request.json
    destination = data.get('destination')
    itinerary = itinerary_generator.generate_itinerary(destination)
    return jsonify(itinerary)

@app.route('/weather', methods=['GET'])
def weather():
    location = request.args.get('location')
    weather_data = api_integration.get_weather(location)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
