import asyncio
import os

import aiohttp
from sqlalchemy import select
from sqlalchemy.orm import Session

from city.models import City, Temperature
from time import time
API_KEY = os.environ.get("API_KEY")
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


async def get_weather(city: str, session) -> int | None:
    async with session.get(WEATHER_API_URL, params={"key": API_KEY, "q": city}) as response:
        if response.status != 200:
            print(f"Error: Can't get data from Weather API for {city}.")
            return

        response = await response.json()
        return response['current']['temp_c']


async def update_temperatures(db: Session):
    cities = db.scalars(select(City)).fetchall()
    to_insert = []
    async with aiohttp.ClientSession() as session:
        temperatures = await asyncio.gather(*[get_weather(city.name, session) for city in cities])

    temperature_iter = iter(temperatures)
    for city in cities:
        temperature = next(temperature_iter)
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
