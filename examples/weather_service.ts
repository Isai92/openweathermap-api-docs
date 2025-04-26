// Replace with API key
const API_KEY = "[API_KEY]"; 

async function getWeather(city, countryCode) {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city},${countryCode}&appid=${API_KEY}`;
    
    try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return await response.json();
    } catch (error) {
        return `Error: ${error.message}`;
    }
}

// Test with London weather
getWeather("London", "GB")
    .then(data => console.log(data))
    .catch(err => console.error(err));
