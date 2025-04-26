import os
import requests

def get_weather():
    API_KEY = os.getenv("API_KEY")  # Get from environment variables
    CITY = "London"
    COUNTRY_CODE = "GB"  # UK → GB
    
    try:
        # Make API call
        url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY_CODE}&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Parse data
        temp_kelvin = data["main"]["temp"]
        temp_celsius = round(temp_kelvin - 273.15, 1)
        humidity = data["main"]["humidity"]
        conditions = data["weather"][0]["description"].capitalize()
        
        # Print formatted output
        print(f"Weather in {CITY}:")
        print(f"- Temperature: {temp_celsius}°C")
        print(f"- Humidity: {humidity}%")
        print(f"- Conditions: {conditions}")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    get_weather()
