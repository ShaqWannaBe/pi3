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

current = data['current']
daily = data['daily']
today = daily[0]

# current weather conditions
temp = int(round(current['temp'],0))
feels_like = (int(round(current['feels_like'])))
condition = current['weather'][0]['description']

# weather conditions for today
today_summary = today['summary']
today_high_temp = int(round(today['temp']['max']))
today_low_temp = int(round(today['temp']['min']))

#print welcome
print('\n*** WELCOME TO THE WEATHER APP ***')
print('* Current weather:')
print('Temp: ' + str(temp) + ' °F')
print('Feels like: ' + str(feels_like) + ' °F')
print('Condition: ' + str(condition))
print("\n* Today's forecast:")
print(str(today_summary))
print(f'High temp: {str(today_high_temp)}')
print(f'Low temp: {str(today_low_temp)}')

