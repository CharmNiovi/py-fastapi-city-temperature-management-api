from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from city import models, schemas


def post_list_city(db: Session, city: schemas.CityBase):
    city = models.City(**city.dict())
    db.add(city)
    db.commit()
    db.refresh(city)
    return city


def get_list_city(db: Session):
    return db.scalars(select(models.City))


def get_detail_city(db: Session, city_pk: int):
    sql = select(models.City).filter(models.City.id == city_pk)
    city = db.scalar(sql)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


def delete_detail_city(db: Session, city_pk: int):
    db.delete(get_detail_city(db, city_pk))
    db.commit()


def update_detail_city(db: Session, city_pk: int, new_city: schemas.CityPatch):
    old_city = get_detail_city(db, city_pk)
    for attr, value in new_city.dict(exclude_unset=True).items():
        setattr(old_city, attr, value)
    db.commit()
    return old_city
