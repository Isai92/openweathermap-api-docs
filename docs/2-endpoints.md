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




## 2.2 Real-Time hourly forecast data (/forecast)
### Objective: 
Fetch 5-day weather forecast data for any global location using OpenWeatherMap's API.

### Requirements:  
Generated OpenWeatherMap API key (see Section 1).
Latitude and longitude coordinates (Obtain via */weather* endpoint on Section 2.1)
Web browser or API testing tool. 

### Parameters:
The OpenWeatherMap API allows you to fetch forecast data using the **latitude** and **longitude** of a location. These coordinates can be retrieved using the */weather* endpoint in **section 2.1**.

The following table lists the parameters for the */forecast* endpoint, including their type (required/optional) and purpose:
| Parameter | Type     | Description                                                                                               |
|:---------:|:--------:|-----------------------------------------------------------------------------------------------------------|
|    lat    | required | Latitude of the location                                                                                  |
|    lon    | required | Longitude of the location.                                                                                |
|   appid   | required | Generated API key                                                                                         |
|    mode   | optional | Response format: *JSON*, *XML* and *HTML*. Default: *JSON*.                                                       |
|    cnt    | optional | Number of forecast timestamps (1 timestamp = 3 hours). Default numbers of timestamps will be 40 (5 days). |
|   units   | optional | Measurement system: *standard*, *metric* and *imperial*. Default parameter is: *standard*                         |
|    lang   | optional | Language code.                                                                                            |

### API Call examples: 
#### 1. Basic request.
```
https://api.openweathermap.org/data/2.5/forecast?lat=[Latitude]&lon=[Longitude]&appid=[API_KEY]
```
#### 2. Basic Forecast for Tokyo, Japan.
```
https://api.openweathermap.org/data/2.5/forecast?lat=35.6895&lon=139.6917&appid=[API_KEY]
```
#### Response snippet: 
```
{
  "cod": "200",
  "message": 0,
  "cnt": 2,
  "list": [ 
"dt": 1744513200,
      "main": {
        "temp": 285.24,
},  
      "weather": [  
        {  
          "description": "light rain"  
        }  
      ]  
    },  
    // ... 39 more timestamps  
  ]  
}  
```
#### 3. Short Forecast for Paris, France.
```
https://api.openweathermap.org/data/2.5/forecast?lat=48.8534&lon=2.3488&cnt=2&appid=[API_KEY]
```
#### Response snippet: 
```
{  
  "cod": "200",  
  "cnt": 2,  
  "list": [  
    {  
      "dt": 1744513200,  
      "main": {  
        "temp": 285.13,   
      },  
      "weather": [  
        {  
          "description": "overcast clouds"  
        }  
      ]  
    },  
    {  
      "dt": 1744524000,  
      "main": {  
        "temp": 284.39  
      }  
    }  
  ]  
} 
```
### Steps to test: 
1. Open a new browser tab. 
2. Paste one of the API call examples.  
3. Replace **[Latitude]** and **[Longitude]** with coordinates from **Section 2.1**. 
4. Replace **[API_KEY]** with the generated key
5. Press **Enter**. 
