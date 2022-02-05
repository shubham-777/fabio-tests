from dis import show_code
from os import name
from typing import List
from urllib import request
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from database.mysql import get_db
from models import sql_models
from schemas import pyd_schemas
from crud import country

router = APIRouter(prefix="/country",tags=["country"], responses={404: {"description": "Not found"}})
tags_metadata = [
    {
        "name": "country",
        "description": "CRUD operations related to **country**."
    }
]


#==============================
# country
#==============================
@router.get("/get_all",response_model=List[pyd_schemas.ShowCountry])
def get_all_countries(db: Session = Depends(get_db)):
    return country.get_all_countries(db)

@router.get("/get_countries_of/{continent_name}",response_model=List[pyd_schemas.ShowCountry], status_code=status.HTTP_200_OK)
def get_all_countries_of_continent(continent_name: str, db: Session = Depends(get_db)):
    return country.get_all_countries_of_continent(continent_name, db)

@router.post("/add",status_code=status.HTTP_201_CREATED,response_model=pyd_schemas.ShowCountry)
def add_new_country(request: pyd_schemas.AddCountry, db: Session = Depends(get_db)):
    return country.add_new_country(request, db)

@router.delete("/delete/{country_name}", status_code=status.HTTP_202_ACCEPTED)
def delete_a_country(country_name: str, db: Session = Depends(get_db)):
    return country.delete_a_country(country_name, db)

