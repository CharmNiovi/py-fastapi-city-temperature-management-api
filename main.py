from fastapi import FastAPI

from city.router import router as city_router
from database import Base, engine
from temperature.router import router as temperature_router

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(city_router)
app.include_router(temperature_router)
