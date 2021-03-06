from fileinput import close
from typing import List
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from database.mysql import SessionLocal, get_db
from models import sql_models
from schemas import pyd_schemas
from celery_worker.crud_worker import app
#==============================
# country
#==============================
@app.task(name="celery_tasks.tasks.get_all_countries")
def get_all_countries():
    db = SessionLocal()
    try:
        llst_countries = db.query(sql_models.Country).all()
        return pyd_schemas.ShowCountry.from_orm_list(llst_countries)
    except Exception as e:
        return {"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,"detail":f"{e}"}
    finally:
        db.close()

@app.task(name="celery_tasks.tasks.get_all_countries_for_continent")
def get_all_countries_of_continent(continent_name: str):
    db = SessionLocal()
    try:
        if not continent_name:
            # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="continent_name cannot be empty")
            return {"status_code":status.HTTP_400_BAD_REQUEST, "detail":"continent_name cannot be empty"}
        lobj_continent = db.query(sql_models.Continent).filter(sql_models.Continent.name==continent_name).first()
        if not lobj_continent:
            # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Continent with continent_name: {continent_name} is not present")
            return {"status_code":status.HTTP_404_NOT_FOUND, "detail":f"Continent with continent_name: {continent_name} is not present"}
        llst_country = db.query(sql_models.Country).filter(sql_models.Country.continent_id==lobj_continent.id).all()
        return pyd_schemas.ShowCountry.from_orm_list(llst_country)
    except Exception as e:
        return {"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,"detail":f"{e}"}
    finally:
        db.close()

@app.task(name="celery_tasks.tasks.add_new_country")
def add_new_country(request: pyd_schemas.AddCountry):
    db = SessionLocal()
    try:
        lobj_continent = db.query(sql_models.Continent).filter_by(id=request.continent_id).first()
        lobj_country = db.query(sql_models.Country).filter_by(name=request.name).first()
        if not lobj_continent:
            # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Continent with continent_id: {request.continent_id} doesn't exits.")
            return {"status_code":status.HTTP_404_NOT_FOUND, "detail":f"Continent with continent_id: {request.continent_id} doesn't exits."}
        if lobj_country:
            # raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Country with country_name: {request.name} already exits.")
            return {"status_code":status.HTTP_409_CONFLICT, "detail":f"Country with country_name: {request.name} already exits."}
        lobj_country = sql_models.Country(name=request.name, population=request.population, area=request.area,
        continent_id=request.continent_id, no_of_hospitals=request.no_of_hospitals, no_of_national_parks=request.no_of_national_parks)
        db.add(lobj_country)
        db.commit()
        db.refresh(lobj_country)
        return pyd_schemas.ShowCountry.from_orm(lobj_country)
    except Exception as e:
        return {"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR,"detail":f"{e}"}
    finally:
        db.close()


def delete_a_country(country_name: str, db: Session):
    lobj_country = db.query(sql_models.Country).filter(sql_models.Country.name==country_name)

    if not lobj_country.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Country with name: {country_name} didn't exists")

    lobj_country.delete(synchronize_session=False)
    db.commit()
    return True

