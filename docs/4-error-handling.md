# Section 4: Handle Errors. 
### Objective: 
Diagnose and resolve common API errors.

### Requirements:  
* Basic understanding of *HTTP* status codes.  
* Access to API key **[Section 1]**

## 4.1 Authentication Errors (HTTP 401)
### Causes: 
* Invalid or missing API key.   
* Key not activated. 

### Solutions: 
#### 1. Regenerate Key
Follow **[Section 1]** steps to create a new key. 

## 4.2 City Not Found (HTTP 404)
### Causes: 
* Misspelled city name.
* Incorrect format.

### Solutions:  
#### 1. Incorrect format
Always add **country code** to get the correct city. 

#### 2. Using coordinates
If city names fail, use latitude and longitude from */weather*: 
```
https://api.openweathermap.org/data/2.5/weather?lat=48.85&lon=2.35&appid=[API_KEY]  
```
## 4.3 Rate-Limiting Errors (HTTP 429)
### Causes: 
* Exceeding **free tier** limits (60 calls/minute).
* *Burst* requests from multiple users. 

### Solutions: 
1. Add **Delay** Between Calls: 
Wait 1 second between calls, the following is a *Python* example:
```
import time  

def make_call(url):  
    """Safely handles rate limits with 1.2s buffer"""  
    time.sleep(1.2)  # 60 calls/min = 1 call/sec + 20% buffer  
    return requests.get(url) 
```
2. Cache Responses
 The following is a JavaScript caching example:
```
const cache = {};  
async function getCachedWeather(city) {  
    if (cache[city]) return cache[city];  
    const data = await fetchWeather(city);  
    cache[city] = data;  
    return data;  
} 
```
3. Upgrade Tier
Consider paid plans for higher limits.
