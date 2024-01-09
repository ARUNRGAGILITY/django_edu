<a href="/">Home</a>&nbsp;&nbsp;/&nbsp;&nbsp;<a href="/tutorials/tutorials_home_page">Tutorials Home</a>
<b>Python Projects</b>
<br>

# Python Projects

Here are some Python Projects to learn and practice

### 1. To-Do List Application
A simple to-do list manager using Python:

```python
# To-Do List Application

tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("Your tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

while True:
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
```

### 2. Weather App Using API
Fetching weather data using an API (e.g., OpenWeatherMap):

```python
# Weather App Using API

import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your API key from OpenWeatherMap
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
    else:
        print("City not found. Please try again.")

city = input("Enter city name: ")
get_weather(city)
```

### 3. Password Generator
Creating a simple password generator:

```python
# Password Generator

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter password length: "))
generated_password = generate_password(length)
print("Generated Password:", generated_password)
```

### 4. URL Shortener Using Flask
Creating a URL shortener using Flask:

```python
# URL Shortener Using Flask

from flask import Flask, redirect, render_template, request
import shortuuid

app = Flask(__name__)

url_mapping = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    original_url = request.form['url']
    short_url = shortuuid.uuid()[:8]  # Shorten the UUID to make the URL shorter
    url_mapping[short_url] = original_url
    return f"Shortened URL: {request.host}/{short_url}"

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url)
    return "URL not found"

if __name__ == '__main__':
    app.run(debug=True)
```

