import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] == 200:
        print(f"Weather in {weather_data['name']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print(f"Error: {weather_data['message']}")

def Weather():
    api_key ="235292fbdecde4f8f153a461b5786bd0"
    city = input("Enter city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)
Weather()
