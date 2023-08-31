"""

This app will query a weather API to find data about the weather.
Then it will notify users of the weather.

"""

import sms
import os
from dotenv import load_dotenv
import requests
import json
from colorama import Fore as FORE


phone_numbers = ("15202330667")


load_dotenv() #loads .env file contents
api_key = os.getenv("API_KEY")

lat = '33.293160'
lon = '-112.037024'
units = 'imperial'      # Use either metric or imperial

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}&exclude=minutely,hourly&appid={api_key}'

res = requests.get(url)
data = res.json()

#prints the result of the api call
# print(f'{FORE.RED}{res}{FORE.RESET}')

#round the current temp and turn it into an integer
temp = int(round(data['current']['temp'],0))
feels_like = (int(round(data['current']['feels_like'])))
condition = data['current']['weather']

#print welcome
print('\n*** WELCOME TO THE WEATHER APP ***')
print('* Current Temp: ' + str(temp) + ' °F')
print('* Feels like: ' + str(feels_like) + ' °F')


text_message = f'*** WEATHER APP ANNOUNCEMENT ***\nCurrent Temp: {str(temp)} °F\nFeels like: {str(feels_like)} °F'

for number in phone_numbers:
    sms.send_message(number, 'cricket', text_message)