from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import sql_models
from schemas import pyd_schemas

def get_all_continent(db: Session):
    llst_continents = db.query(sql_models.Continent).all()
    return llst_continents

def add_new_continent(request: pyd_schemas.Continent, db: Session):
    entry_exists = db.query(sql_models.Continent.id).filter_by(name=request.name).first()
    if entry_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Continent with continent_name:{request.name} already exist")
    lobj_continent = sql_models.Continent(name=request.name, population=request.population, area=request.area)
    db.add(lobj_continent)
    db.commit()
    db.refresh(lobj_continent)
    return lobj_continent
        