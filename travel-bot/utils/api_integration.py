import requests
import os

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather(location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

