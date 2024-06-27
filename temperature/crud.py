import os

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from city.models import City, Temperature
from time import time
API_KEY = os.environ.get("API_KEY")
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> int | None:
    request = requests.get(
        WEATHER_API_URL,
        params={"key": API_KEY, "q": city}
    )

    if request.status_code != 200:
        print(f"Error: Can't get data from Weather API for {city}.")
        return

    return request.json()['current']['temp_c']


def update_temperatures(db: Session):
    cities = db.scalars(select(City)).fetchall()
    to_insert = []
    for city in cities:
        print(city.name)
        temperature = get_weather(city.name)
        if temperature:
            if city.temperature:
                city.temperature.temperature = temperature
            else:
                to_insert.append(
                    Temperature(
                        temperature=temperature,
                        city=city,
                    )
                )
    db.add_all(to_insert)
    db.commit()


def get_list_temperatures(db: Session, city_pk: int | None):
    sql = select(Temperature)
    if city_pk:
        sql = sql.where(Temperature.city_id == city_pk)
    return db.scalars(sql)
