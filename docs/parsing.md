# Section 3: Parse Responses. 
### Objective: 
Extract weather data from API responses and convert units for practical use.  

### Requirements:  
* Generated OpenWeatherMap API key (see Section 1).
* Basic *Python*, *JavaScript* and *JSON* parsing knowledge. 

### Parameters:
API responses from **section 2** return nested *JSON* objects. The following table shows the location of data of **temperature**, **humidity** and **weather conditions**. 
| Field       | Path                   | Description                                   |
|:-----------:|:----------------------:|-----------------------------------------------|
| Temperature |        main.temp       | Shown in Kelvin.                              |
|  Conditions | weather[0].description | Summary of weather conditions.                |
|   Humidity  |      main.humidity     | Shown in percentage.                          |
|  Wind Speed |       wind.speed       | Shown in meters per second, in metric system. |


## 3.1 Python Parsing Guide :
*The following example summarizes the process of extracting data for Windows/macOS/Linux users with Python installed.*

### Setup: 
1. Install the *requests* library: 
```
  pip install requests  
```

### Step-by-Step Code: 
```
# Import libraries  
import requests  

# Step 1: Fetch data from API  
API_KEY = "API_KEY"  # Replace with your key  
CITY = "London"  
try:  
    response = requests.get(      f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}")  
    data = response.json()  
    # Step 2: Extract and convert Kelvin to Celsius.  
    temp_kelvin = data["main"]["temp"]  
    temp_celsius = round(temp_kelvin - 273.15, 2) # Formula:°C= K-273.15  

    # Step 3: Extract other data  
    humidity = data["main"]["humidity"]  
    conditions = data["weather"][0]["description"].capitalize()  

    # Step 4: Display results  
    print(f"Weather in {CITY}:")  
    print(f"- Temperature: {temp_celsius}°C")  
    print(f"- Humidity: {humidity}%")  
    print(f"- Conditions: {conditions}")  

except Exception as e:  
    print(f"Error: {e}") 
```
#### Expected Output
```
Weather in London:  
- Temperature: 18.50°C  
- Humidity: 65%  
- Conditions: Scattered clouds
```

## 3.2 JavaScript Parsing Guide :
*The following example summarizes the process of extracting data for  Node.js users with basic terminal knowledge.*

### Setup: 
1. Create a project folder.
2. Open **PowerShell** on project folder, initialize *npm* and install *node-fetch*: 
```
npm init -y  
npm install node-fetch
```
### Step-by-Step Code:
```
// Import libraries  
import fetch from 'node-fetch';  

// Step 1: Fetch data from API  
const API_KEY = "API_KEY";  // Replace with your key  
const CITY = "London";  



const fetchWeather = async () => {  
  try {  
    const response = await fetch(    `https://api.openweathermap.org/data/2.5/weather?q=$[CITY]&appid=$[API_KEY]`  
    );  
    const data = await response.json();  

    // Step 2: Extract and convert temperature  
    const tempCelsius = (data.main.temp - 273.15).toFixed(2);  

    // Step 3: Extract other data  
    const humidity = data.main.humidity;  
    const conditions = data.weather[0].description.toUpperCase();  

    // Step 4: Display results  
    console.log(`Weather in ${CITY}:`);  
    console.log(`- Temperature: ${tempCelsius}°C`);  
    console.log(`- Humidity: ${humidity}%`);  
    console.log(`- Conditions: ${conditions}`);  

  } catch (error) {  
    console.error("Error:", error.message);  
  }  
};  

// Run the script  
fetchWeather();
```
#### Expected Output
```
Weather in London:  
- Temperature: 18.50°C  
- Humidity: 65%  
- Conditions: Scattered clouds

```





