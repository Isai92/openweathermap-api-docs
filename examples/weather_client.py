import os
import requests

# Direct API key input for testing. 
API_KEY = "[API_KEY]"  # 🔑 Replace with the API key.

def get_weather(city, country_code):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors. 
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Test with correct country code.
print(get_weather("London", "GB")) 
