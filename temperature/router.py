from fastapi import APIRouter
from sqlalchemy.orm import Session

from dependences import DB_DEPENDENCY
from temperature import crud
from temperature import schemas
import asyncio
router = APIRouter()


@router.post("/temperatures/update/", status_code=201)
async def update_temperatures_of_all_cities(db: Session = DB_DEPENDENCY):
    await asyncio.create_task(crud.update_temperatures(db))


@router.get("/temperatures/", response_model=list[schemas.Temperature])
async def get_list_temperatures(city_id: int | None = None, db: Session = DB_DEPENDENCY):
    return crud.get_list_temperatures(db, city_id)
