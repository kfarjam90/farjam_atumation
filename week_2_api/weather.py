import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(weather_data):
    if weather_data["cod"] != "404":
        city_name = weather_data["name"]
        weather = weather_data["weather"][0]["description"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        print(f"Weather in {city_name}: {weather}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found.")

def main():
    api_key = '69584b48a5c368794a4f279d6f4611a2'
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
