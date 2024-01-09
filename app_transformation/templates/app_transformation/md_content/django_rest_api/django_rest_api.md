

# Django REST API Framework


## What is an API?

An API, or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate and interact with each other. It defines the methods and data formats that developers can use to request and exchange information between programs. APIs are essential for enabling the integration of various services and functionalities in modern software development.

Here's a simple example of how an API works using a hypothetical scenario related to your interests as a startup founder and Python Django web developer:

Imagine you are building a weather application using Python Django, and you want to display weather data from a third-party service like OpenWeatherMap on your website. OpenWeatherMap provides an API that allows developers to access weather data programmatically.

In this case, you can make an API request to OpenWeatherMap with specific parameters like the city and country you want weather data for. OpenWeatherMap processes your request and sends back weather information in a structured format, typically in JSON or XML.

Here's an example of how you might make an API request in Python using the `requests` library:

```python
import requests

# API endpoint URL
url = "https://api.openweathermap.org/data/2.5/weather"

# Parameters for the request
params = {
    'q': 'Chennai,IN',  # City and country
    'appid': 'YOUR_API_KEY'  # Replace with your API key
}

# Send the GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Access the weather information
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    # Display the weather information
    print(f"Temperature in Chennai, India: {temperature}°C")
    print(f"Weather description: {weather_description}")
else:
    print("Failed to fetch weather data")

```

In this code example,
 we are using the OpenWeatherMap API to retrieve weather data for Chennai, India. 
 You would need to replace `'YOUR_API_KEY'` with your actual API key obtained from OpenWeatherMap.
