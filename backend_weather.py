import os
import requests
from dotenv import load_dotenv

load_dotenv()


def retrieving_weather_data_api(location):
    api_key = os.getenv("API_KEY")
    url_weather = (f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}'
                   f'?unitGroup=metric&include=days%2Chours&key={api_key}&contentType=json')
    result = requests.get(url_weather)  # this is the request itself
    if result.status_code == 200:
        weather_data = result.json()  # getting just the 'json' data from the api
        filtered_data = filter_weather_variables(weather_data)
        return filtered_data
    else:
        return False


def filter_weather_variables(weather_data):
    days_list = []
    for day in weather_data['days'][:7]:
        day_dict = {"humidity": day['humidity'],
                    "tempmax": day['tempmax'],
                    "tempmin": day['tempmin'],
                    "datetime": day['datetime']}
        days_list.append(day_dict)
    return days_list
