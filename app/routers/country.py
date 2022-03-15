from dis import show_code
from os import name
from socket import timeout
from typing import List
from urllib import request
from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from sqlalchemy import Interval
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
async def get_all_countries():
    task = country.get_all_countries.delay()
    result = task.wait(timeout=None, interval=0.5)
    return result

@router.get("/get_countries_of/{continent_name}",response_model=List[pyd_schemas.ShowCountry], status_code=status.HTTP_200_OK)
async def get_all_countries_of_continent(continent_name: str, db: Session = Depends(get_db)):
    task = country.get_all_countries_of_continent.delay(continent_name)
    result = task.wait(timeout=None, interval=0.5)
    return result

@router.post("/add")
async def add_new_country(request: pyd_schemas.AddCountry):
    task_id = country.add_new_country.apply_async(args=[request])
    return JSONResponse(status_code=status.HTTP_202_ACCEPTED, content={"task_id": str(task_id)})

@router.delete("/delete/{country_name}", status_code=status.HTTP_202_ACCEPTED)
async def delete_a_country(country_name: str, db: Session = Depends(get_db)):
    if country.delete_a_country(country_name, db):
        return JSONResponse(status_code=status.HTTP_200_OK, content=f"{country_name} deleted successfully")
    else:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=f"Unable to delete Country: {country_name}")


