import requests

# Define the base URL for the OpenWeatherMap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Specify the city for which you want to retrieve weather data
city_name = "Tokyo"

# Your unique API key (replace 'YOUR_API_KEY' with your actual API key)
api_key = "YOUR_API_KEY"

# Define the parameters for the API request
params = {
    'q': city_name,
    'appid': api_key,
    'units': 'metric',  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    'lang': 'ja'        # Language parameter set to Japanese
}

# Send a GET request to the API with the specified parameters
response = requests.get(BASE_URL, params=params)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    data = response.json()

    # Extract and print specific weather details
    print(f"City: {data['name']}")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print(f"Error: Failed to retrieve data. Status code: {response.status_code}")
