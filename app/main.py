from fastapi import FastAPI

import requests

from app.translater import City

api_key = "KEY"
current_weather_url = "https://api.openweathermap.org/data/2.5/weather?&units=metric&"
forecast_weather_url = "http://api.openweathermap.org/data/2.5/forecast?&units=metric&"
air_pollution_url = "http://api.openweathermap.org/data/2.5/air_pollution?"


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "лаба-4"}


@app.get("/current_weather/{city}")
async def get_weather_info(city: str):
    url = current_weather_url + "appid=" + api_key + "&q=" + str(city)
    response = requests.get(url).json()
    weather_info = response

    return weather_info


@app.get("/forecast_weather/{city_name}/{days}")
async def get_future_weather_info(city_name: str, days: int):
    city = City(city_name)
    count = (24 * days) / 3

    url = forecast_weather_url + f"lat={city.get_latitude()}&lon={city.get_longitude()}&cnt={int(count)}&appid={api_key}"

    response = requests.get(url).json()
    weather_info = response

    return weather_info


@app.get("/air_pollution/{city_name}")
async def get_air_pollution(city_name: str):
    city = City(city_name)

    url = air_pollution_url + f"lat={city.get_latitude()}&lon={city.get_longitude()}&appid={api_key}"

    response = requests.get(url).json()
    weather_info = response

    return weather_info
