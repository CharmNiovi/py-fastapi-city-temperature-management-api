from fastapi import APIRouter
from sqlalchemy.orm import Session

from city import schemas, crud
from dependences import DB_DEPENDENCY

router = APIRouter()


@router.post("/city/", response_model=schemas.CityRead)
async def post_list_city(
        city: schemas.CityBase,
        db: Session = DB_DEPENDENCY
):
    return crud.post_list_city(db, city)


@router.get("/city/", response_model=list[schemas.CityRead])
async def get_list_city(db: Session = DB_DEPENDENCY):
    return crud.get_list_city(db)


@router.get("/city/{city_pk}/", response_model=schemas.CityRead)
async def get_detail_city(city_pk: int, db: Session = DB_DEPENDENCY):
    return crud.get_detail_city(db, city_pk)


@router.delete("/city/{city_pk/", status_code=204)
async def delete_detail_city(city_pk: int, db: Session = DB_DEPENDENCY):
    crud.delete_detail_city(db, city_pk)


@router.patch("/city/{city_pk/", response_model=schemas.CityRead)
async def patch_detail_city(
        city: schemas.CityPatch,
        city_pk: int,
        db: Session = DB_DEPENDENCY
):
    return crud.update_detail_city(db, city_pk, city)
