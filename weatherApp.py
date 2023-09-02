
# This app will query a weather API to find data about the weather.
# Then it will notify users of the weather.

import sms
import os
from dotenv import load_dotenv
import requests
import json

# define the phone numbers you'd like to text
phone_numbers = ["15202330667"]


load_dotenv() #loads .env file contents
api_key = os.getenv("API_KEY")

lat = '33.293160'
lon = '-112.037024'
units = 'imperial'      # Use either metric or imperial

url = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units={units}&exclude=minutely,hourly&appid={api_key}'

res = requests.get(url)
data = res.json()

#prints the result of the api call
# print(res)

# define the current and daily weather
current = data['current']
daily = data['daily']
today = daily[0]

# current weather data
temp = int(round(current['temp'],0))
feels_like = (int(round(current['feels_like'])))
condition = current['weather']

# today's weather data
today_summary = today['summary']
today_high_temp = int(round(today['temp']['max']))
today_low_temp = int(round(today['temp']['min']))


#text_message = f'*** WEATHER APP ANNOUNCEMENT ***\nCurrent Temp - {str(temp)} F\nFeels like - {str(feels_like)} F'
text_message = (f"Good morning! {today_summary}. "
                f"The high will be {str(today_high_temp)} degrees and the "
                f"low will be {str(today_low_temp)}. Have an awesome day.")
#text_message = f'Current temp - {str(temp)}'

# sends the message to every number listed above
for number in phone_numbers:
    sms.send_message(number, 'cricket', text_message)