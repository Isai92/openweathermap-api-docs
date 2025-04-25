# Section 5: Ensure Compliance  

### Objective: 
Adhere to **OpenWeatherMap’s** licensing terms and **GDPR** requirements.

### Requirements:  
* Access to **OpenWeatherMap** pricing page


## 5.1 GDPR & Data Licensing
### Key requirements:
1. **OpenWeather`s** weather platform is fully GDPR-compliant.
2. Attribution is mandatory for free tier and optional for paid tiers. 
3. You may process data internally and not resell raw API responses.
 
### Attribution implementation:
#### 1. Web example:
```
<footer>  
  <small>  
    Weather data by  
    <a href="https://openweathermap.org/" target="_blank">OpenWeatherMap</a>  
  </small>  
</footer> 
```

#### 2. Mobile (React Native) example:
```
<Text style={styles.footer}>  
  Powered by <Text style={styles.link} onPress={() => Linking.openURL('https://openweathermap.org')}>OpenWeatherMap</Text>  
</Text>
```
