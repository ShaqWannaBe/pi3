import os
import json
import requests
from dotenv import load_dotenv

load_dotenv() #loads .env file contents
api_key = os.getenv("API_KEY")

lat = '33.293160'
lon = '-112.037024'
units = 'imperial'      # Use either metric or imperial

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}&exclude=minutely,hourly&appid={api_key}'
res = requests.get(url)
data = res.json()

high_temp = data['daily']['temp']['max']
print(str(high_temp))