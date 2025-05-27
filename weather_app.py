import requests
import numpy as np
import pandas as pd


def get_weather(city: str):
    API_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q' : city,
        'appid' : API_key,
        'units' : 'metric'
    }
    response = requests.get(url, params = params)

    if response.status_code == 200:
        data = response.json()
        print("\nWeather data: ")
        print(data)
    else:
        print(f"\nError: {response.status_code}")
        data = None

    return data


print("------Weather App------")
city = input("\nEnter city name: ")

weather_data = get_weather(city)

if weather_data:
    temp = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']

    data_matrix = np.array([[temp,humidity], [wind_speed, description]])

    df = pd.DataFrame(data_matrix,
                      index = ['Row1', 'Row2'],
                      columns = ['Value1', 'Value2'])
    print('\nTabular weather data: ')
    print(df)
