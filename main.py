import requests
import datetime
from config import url

try:
    response = requests.get(url)
    response_json = response.json()
    response_timestamp = datetime.datetime.fromtimestamp(response_json['dt'])
    print(response_json['name'] + ', ' +response_json['sys']['country'])
    print(response_json['main']['temp'])
    print(response_json['weather'][0]['main'])
    print((response_json['weather'][0]['description']))
    print(response_json['main']['pressure'])
    print(response_json['main']['humidity'])
    print(response_timestamp)

except:
    print('An error occurred while fetching weather data.')

