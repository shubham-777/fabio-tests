import dbm
from os import name
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database.mysql import get_db
from schemas import pyd_schemas
from crud import continent

router = APIRouter(prefix="/continent", tags=["continent"], responses={404: {"description": "Not found"}})
tags_metadata = [
    {
        "name": "continent",
        "description": "CRUD operations related to **continent**.",
    }
]



#==============================
# continent
#==============================
@router.get("/get_all",response_model=List[pyd_schemas.Continent])
def get_all_continents(db: Session = Depends(get_db)):
    return continent.get_all_continent(db)

@router.post("/add", status_code=status.HTTP_201_CREATED,response_model=pyd_schemas.Continent)
async def add_new_continent(request: pyd_schemas.Continent, db: Session = Depends(get_db)):
    return continent.add_new_continent(request, db)
