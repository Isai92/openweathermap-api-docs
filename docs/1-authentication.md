# Section 01: Authentication and Key testing. 
## 1.1 Obtain API Key. 
### Objective: 
Generate and securely store an OpenWeatherMap API key to authenticate requests.

### Requirements:  
* Web browser.
* Valid Email account.

### Steps: 
1. Visit the official website of Open Weather Map API: https://openweathermap.org/
2. Sign in to your account.
    1. If you don't have an account, create one by confirming your email.
3 Select **Open** in the top menu. 
    1. Select **My API keys** from the dropdown menu.
    2. Your active API keys will appear in a table.
4. Enter a unique name for your key (e.g., 'MyTravelApp') in the API Key Name field.
    1. Select **Generate**.
    2. A new key will show up. 

## 1.2 Test New Generated Key
### Objective: 
Verifying working API keys and interpreting responses.

### Requirements: 
* Generated API key.
* Web browser. 

### Steps: 
1. Open a new browser tab. 
2. Test your key with this cURL command:
```
 https://api.openweathermap.org/data/2.5/weather?q=London&appid=[API_KEY] 
```
3. Replace **[API_KEY]** with the **new generated key**.
4. Press **Enter**. 

#### Following table explains the status codes returned during API key verification:
| Code | Message | Result | 
|:---: |---------|--------|
|  200  |{"coord": {"lon": -0.13, "lat": 51.51}, "main": {"temp": 278.53}, "cod": 200}  | Working API Key | 
| 401 | {"cod": 401, "message": "Invalid API key."} | Not working key |  


  

