from os import name
from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from database.mysql import SessionLocal
from models import sql_models
from schemas import pyd_schemas

crud_route = APIRouter(prefix="/route", responses={404: {"description": "Not found"}})
tags_metadata = [
    {
        "name": "continent",
        "description": "CRUD operations related to **continent**.",
    },
    {
        "name": "country",
        "description": "CRUD operations related to **country**."
    },
    {
        "name": "city",
        "description": "CRUD operations related to **city**.",
    }
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




#==============================
# continent
#==============================
@crud_route.get("/get_continents",response_model=List[pyd_schemas.Continent], tags=["continent"])
def get_all_continents(db: Session = Depends(get_db)):
    llst_continents = db.query(sql_models.Continent).all()
    return llst_continents

@crud_route.post("/add_continent", status_code=status.HTTP_201_CREATED,response_model=pyd_schemas.Continent, tags=["continent"])
async def add_new_continent(request: pyd_schemas.Continent, db: Session = Depends(get_db)):
    lobj_continent = sql_models.Continent(name=request.name, population=request.population, area=request.area)
    db.add(lobj_continent)
    db.commit()
    db.refresh(lobj_continent)
    return lobj_continent



#==============================
# country
#==============================
@crud_route.get("/get_countries", tags=["country"])
def get_all_countries(db: Session = Depends(get_db)):
    llst_continents = db.query(sql_models.Country).all()
    return llst_continents

@crud_route.get("/get_countries{continent_name}", status_code=status.HTTP_200_OK, tags=["country"])
def get_all_countries_of_continent(continent_name: str,response: Response, db: Session = Depends(get_db)):
    if continent_name:
        lobj_country = db.query(sql_models.Country).filter(sql_models.Continent.name==continent_name).first()
        if lobj_country:
            return lobj_country
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"continent_name: {continent_name} is not present")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="continent_name cannot be empty")

@crud_route.post("add_country",status_code=status.HTTP_201_CREATED,response_model=pyd_schemas.Country, tags=["country"])
def add_new_country(request: pyd_schemas.Country, db: Session = Depends(get_db)):
    lobj_continent = db.query(sql_models.Continent).filter(sql_models.Continent.id==request.continent_id)
    if lobj_continent.first():
        lobj_country = sql_models.Country(name=request.name, population=request.population, area=request.area,
        continent_id=request.continent_id, no_of_hospitals=request.no_of_hospitals, no_of_national_parks=request.no_of_national_parks)
        db.add(lobj_country)
        db.commit()
        db.refresh(lobj_country)
        return lobj_country
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Continent with continent_id: {request.continent_id} doesn't exits.")

@crud_route.delete("/country/{country_name}", status_code=status.HTTP_202_ACCEPTED, tags=["country"])
def delete_a_country(country_name: str, db: Session = Depends(get_db)):
    lobj_country = db.query(sql_models.Country).filter(sql_models.Country.name==country_name)

    if not lobj_country.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Country with name: {country_name} didn't exists")

    lobj_country.delete(synchronize_session=False)
    db.commit()
    return {"detail": "success"}



#==============================
# city
#==============================
@crud_route.get("/get_cities", tags=["city"])
def get_all_cities(db: Session = Depends(get_db)):
    llst_continents = db.query(sql_models.City).all()
    return llst_continents

@crud_route.put("/update_city/{city_name}",status_code=status.HTTP_202_ACCEPTED,  tags=["city"])
def update_city(city_name: str,request: pyd_schemas.City, db: Session = Depends(get_db)):
    lobj_city = db.query(sql_models.City).filter(sql_models.City.cty_name == city_name)

    if not lobj_city.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"City with name: {city_name} didn't exists")

    lobj_city.update({sql_models.City.cty_no_of_trees: request.no_of_trees})
    db.commit()
    return "updated"