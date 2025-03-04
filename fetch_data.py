import requests
import datetime
import logging
from config import url
from db_operations import insert_weather_data

def fetch_weather_data():
    try:
        logging.info("Fetching weather data...")

        response = requests.get(url)
        response.raise_for_status()  

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
        logging.info("Weather data inserted successfully.")

    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP Request failed: {str(e)}", exc_info=True)
        raise  

    except KeyError as e:
        logging.error(f"Missing key in API response: {str(e)}", exc_info=True)
        raise

    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}", exc_info=True)
        raise
