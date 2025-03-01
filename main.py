import requests
import datetime
from config import url
from db_operations import insert_weather_data

try:
    response = requests.get(url)
    response_json = response.json()
    response_timestamp = datetime.datetime.fromtimestamp(response_json['dt']).strftime('%Y-%m-%d %H:%M:%S')

    data = (
        response_json['name']+', '+response_json['sys']['country'],
        response_json['main']['temp'],
        response_json['weather'][0]['main'],
        response_json['weather'][0]['description'],
        response_json['main']['pressure'],
        response_json['main']['humidity'],
        response_timestamp,
    )
    
    insert_weather_data(data)

except:
    print("An error occurred while fetching weather data.")

