from os import name
from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from database.mysql import get_db
from models import sql_models
from schemas import pyd_schemas


#==============================
# city
#==============================
def get_all_cities(db: Session):
    llst_continents = db.query(sql_models.City).all()
    return llst_continents


def add_new_city(request: pyd_schemas.AddCity, db: Session):
    lobj_country = db.query(sql_models.Country).filter_by(id=request.country_id).first()
    lobj_city = db.query(sql_models.City).filter_by(name=request.name).first()
    if not lobj_country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Country with country_id: {request.country_id} doesn't exits.")
    if lobj_city:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"City with city_name: {request.name} already exits.")
    lobj_country = sql_models.City(name=request.name, population=request.population, area=request.area, country_id=request.country_id,
    no_of_roads=request.no_of_roads,no_of_trees=request.no_of_trees)
    db.add(lobj_country)
    db.commit()
    db.refresh(lobj_country)
    return lobj_country

def update_city(city_name: str,request: pyd_schemas.BaseCity, db: Session):
    lobj_city = db.query(sql_models.City).filter(sql_models.City.cty_name == city_name)

    if not lobj_city.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"City with name: {city_name} didn't exists")

    lobj_city.update({sql_models.City.cty_no_of_trees: request.no_of_trees})
    db.commit()
    return lobj_city