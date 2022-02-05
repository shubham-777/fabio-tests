from os import name
from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from database.mysql import get_db
from models import sql_models
from schemas import pyd_schemas
from crud import city

router = APIRouter(prefix="/city", tags=["city"], responses={404: {"description": "Not found"}})
tags_metadata = [
    {
        "name": "city",
        "description": "CRUD operations related to **city**.",
    }
]


#==============================
# city
#==============================
@router.get("/get_all",response_model=List[pyd_schemas.ShowCity])
def get_all_cities(db: Session = Depends(get_db)):
    return city.get_all_cities(db)


@router.post("/add",status_code=status.HTTP_201_CREATED,response_model=pyd_schemas.ShowCity)
def add_new_city(request: pyd_schemas.AddCity, db: Session = Depends(get_db)):
    return city.add_new_city(request, db)

@router.put("/update/{city_name}",response_model=pyd_schemas.ShowCity, status_code=status.HTTP_202_ACCEPTED,)
def update_city(city_name: str,request: pyd_schemas.BaseCity, db: Session = Depends(get_db)):
    return city.update_city(city_name, request, db)