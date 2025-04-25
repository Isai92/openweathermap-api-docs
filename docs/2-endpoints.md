# Section 2: Call Core Endpoints
## 2.1 Real-Time Weather Data (/weather)

### Objective: 
Fetch current weather data for any global location using OpenWeatherMap's API.

### Requirements:  
Generated OpenWeatherMap API key (see Section 1).
Web browser or API testing tool. 

### Parameters:
The OpenWeatherMap API allows you to fetch weather data using **city name**, **state code** (U.S. locations only), and **country code**. 

The following table lists the parameters for the /weather endpoint, including their type (required/optional) and purpose:

| Parameter 	|   Type   	|                                          Description                                          	|
|:---------:	|:--------:	|-----------------------------------------------------------------------------------------------	|
|     q     	| required 	| City name, state (US only), and ISO 3166 country code, comma-separated. Example: `q=Paris,FR` 	|
|   appid   	| required 	| Generated API key                                                                             	|
|    mode   	| optional 	| Response format: *JSON*, *XML* and *HTML*. Default: *JSON*.                                           	|
|   units   	| optional 	| Measurement system: *standard*, *metric* and *imperial*. Default parameter is: *standard*.             	|
|    lang   	| optional 	| Language code.                                                                                	|

### API Call examples: 

#### 1. Basic request from Tokyo, Japan. 
```
https://api.openweathermap.org/data/2.5/weather?q=Tokyo,JP&appid=[API_KEY] 
```
#### Response snippet:
```
 },
  "timezone": 32400,
  "id": 1850144,
  "name": "Tokyo",
  "cod": 200
}
```
#### 2. Request from Paris, France, in celsius units. 
```
https://api.openweathermap.org/data/2.5/weather?q=Paris,FR&units=metric&appid=[API_KEY]
```
#### Response snippet: 
```
"main": {
    "temp": 13.47, // Celsius 
}
```

#### 3. Request from Madrid, Spain, in metric units and Spanish. 
```
https://api.openweathermap.org/data/2.5/weather?q=Madrid,ES&units=metric&lang=es&appid=[API_KEY]
```
 
#### Response snippet: 
```
"weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "muy nubloso", // "Very cloudy" in Spanish 
      "icon": "04n"
    }
```

### Steps to test: 
1. Open a **new browser tab**. 
2. Paste one of the API call examples.  
3. Replace **[API_KEY]** with the generated key. 
4. Press **Enter**. 


