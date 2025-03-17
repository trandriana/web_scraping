import pandas as pd
import requests

def weather_forcast(lat, lon, API_key):
    '''
    Filename: weather_forcast.py
    Description: This function extract 5 Day/ 3 Hour weather forcast from the Weather API 'https://openweathermap.org/api'
    Remark: Get an API key from https://openweathermap.org. Save it to the file weather_api_key.env.
    Author: Tsiry Avisoa Randrianasolo
    Syntax: weather_df = weather_forcast(latitude, longitude)
    Input: 
        -- lat, lon: the latitude and longitude of a city in decimal format 
    Output:
        -- weather_df: a pandas DataFrame containing a list of weather parameters ['Time', 'Temperature', 'Sky', 'RainVolume']
                Time: Time of data forecasted
                Temperature: Temperature in Celsius
                Sky: Group of weather parameters (Rain, Snow, Clouds etc.)
                RainVolume: Rain volume for last 3 hours, mm
    '''

    # Get access to the Weather API    
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}&units=metric")
    weather_json = weather.json()

    # Collecting information
    time, temp, rain, sky = [], [], [], []
    for i in range(len(weather_json['list'])):
        time.append(weather_json['list'][i]['dt'])
        temp.append(weather_json['list'][i]['main']['feels_like'])
        sky.append(weather_json['list'][i]['weather'][0]['main'])
        try:
            rain.append(weather_json['list'][i]['rain']['3h'])
        except KeyError:
            rain.append(0)
            
    # Creating the DataFrame
    weather_df = pd.DataFrame(data = list(zip(time, temp, sky, rain)), columns = ['Time', 'Temperature', 'Sky', 'RainVolume'])

    # Set the appropriate Datatypes
    weather_df['Time'] = pd.to_datetime(weather_df['Time'], unit='s')
    
    return weather_df