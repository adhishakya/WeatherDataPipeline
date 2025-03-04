import os
from dotenv import load_dotenv

load_dotenv()

url = 'https://api.openweathermap.org/data/2.5/weather?q=Kathmandu&appid='+os.getenv('API_KEY')+'&units=metric'
